# -*- coding: utf-8 -*-
"""Mental-Yi-V2 Model

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/#fileId=https%3A//storage.googleapis.com/kaggle-colab-exported-notebooks/mental-yi-v2-model-f94ad603-0cc9-4575-b48e-00e4a1cae5c5.ipynb%3FX-Goog-Algorithm%3DGOOG4-RSA-SHA256%26X-Goog-Credential%3Dgcp-kaggle-com%2540kaggle-161607.iam.gserviceaccount.com/20240426/auto/storage/goog4_request%26X-Goog-Date%3D20240426T045837Z%26X-Goog-Expires%3D259200%26X-Goog-SignedHeaders%3Dhost%26X-Goog-Signature%3D310324d48a6a8e2157b1165e81988b92ebf9f8392d4e9d236aa880ef5aa99387cd204954edf27298503457f3d7d468e90a0faa96e9ed9858891b65312bbec0ae70afb7df068ed6401ce2e87b62287cb7dbf3699fa2833df3065c38e1907f9b8ce1a973b5c34fd29e62878e734b77a57811245ebf9ff0c10cff1f257d5f29ea1ac8e86c131c59c076e8e4139e08d41e9d67fcdbaab8bb5e1d1d280cf51699e30d5fa637bdb036197ea90b94aaaf5438b6c363cd542d4fe8a493d3fabe2119bb609d450bd71b44f0e64f4aede2fc1ac105eebd178027de0825db540da1c0f27b9aa640495173737216ff297fd107773123c03d349febfe571bedffc2ef4bc32d2e
"""

! pip install -q -U datasets  einops accelerate bitsandbytes peft trl

pip install -q transformers[torch]

from huggingface_hub import login
login('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',  write_permission=True)

from transformers import AutoTokenizer, BitsAndBytesConfig,pipeline,TrainingArguments, Trainer
import torch
from datasets import load_dataset, concatenate_datasets, Dataset
from transformers import AutoModelForCausalLM

compute_dtype = getattr(torch, "float16")

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=compute_dtype,
    bnb_4bit_use_double_quant=True,
)

#model1=AutoModelForCausalLM.from_pretrained("01-ai/Yi-6B-Chat", device_map = "auto", torch_dtype = "auto")
model=AutoModelForCausalLM.from_pretrained("01-ai/Yi-6B-Chat",
                                           quantization_config=bnb_config,
                                          )

tokenizer = AutoTokenizer.from_pretrained("01-ai/Yi-6B-Chat", use_fast = False)

"""# Data Pre Processing"""

# Load The Dataset
counseling_data = load_dataset("Intuit-GenSRF/es_mental_health_counseling", split = "train")
M_data = load_dataset("marmikpandya/mental-health", split = "train")

counseling_data.remove_columns("text")

M_data

def counseling_preprocess(example):
    if example["Response"] != None and example["Context"] != None:
      example["text"] = ("[INST]" + example["Context"] +" " + "role: system: If you are a licensed psychologist, please provide this patient with a helpful response to their concern. Your response should be similar to the following response to such queries"+"\nrole: assistant: "+ example["Response"]+"[/INST] ")
    return example

def Mpreprocess(example):
    if example["input"] != None and example["instruction"] != None and example["output"] != None:
      example["text"] = ("[INST]"+  example["input"]+" "+"role: system: " + example["instruction"]  + "Your response should be similar to the following response to such queries:"+"\nrole: assistant:" + example["output"] +"[/INST] ")
    return example

counseling_data = counseling_data.map(counseling_preprocess, remove_columns = ["Context","Response", "split","text_spanish"])

M_data = M_data.map(Mpreprocess, remove_columns = ["instruction","output", "input"])

Mental_Health_Counselling = concatenate_datasets([counseling_data, M_data])
Mental_Health_Counselling

Mental_Health_Counselling = Mental_Health_Counselling.train_test_split(test_size=0.2)
Mental_Health_Counselling

Mental_Health_Counselling.push_to_hub("Aditya149/Mental_Health_Counselling_Dataset")

"""# Ready to use Data"""

# Load The Dataset
dataset = load_dataset("Aditya149/Mental_Health_Counselling_Dataset", split = "train[:25%]")
eval_data = load_dataset("Aditya149/Mental_Health_Counselling_Dataset", split = "test[:25%]")

def tokenize_function(examples):
    return tokenizer(examples["text"], max_length=512, truncation=True, padding="max_length")

def copy_input_ids(example):
    example["labels"] = example["input_ids"].copy()
    return example

dataset = dataset.map(tokenize_function, num_proc = 4, remove_columns = ["text"])
eval_data = eval_data.map(tokenize_function, num_proc = 4, remove_columns = ["text"])

dataset = dataset.map(copy_input_ids)
eval_data = eval_data.map(copy_input_ids)

"""# Training"""

from peft import LoraConfig,get_peft_model

peft_config = LoraConfig(
    r=8,
    lora_alpha=16,
    lora_dropout=0.1,
    bias="none",
    task_type="CAUSAL_LM",
)
peft_model = get_peft_model(model, peft_config)

training_arguments = TrainingArguments(
    output_dir="Mental-Yi-7B-V2",
    num_train_epochs=5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    save_steps=500,
    logging_steps=1000,
    warmup_ratio = 0.1,
    learning_rate=2e-5,
    fp16=True,
    lr_scheduler_type="cosine",
    report_to="tensorboard",
    evaluation_strategy="steps"
)

trainer = Trainer(
    model = peft_model,
    train_dataset = dataset,
    eval_dataset = eval_data,
    tokenizer = tokenizer,
    args = training_arguments,
)
trainer.train()

trainer.push_to_hub()
