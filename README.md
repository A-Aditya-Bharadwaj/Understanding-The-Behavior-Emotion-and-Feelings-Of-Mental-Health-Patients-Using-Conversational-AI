# Understanding-The-Behavior-Emotion-and-Feelings-Of-Mental-Health-Patients-Using-Conversational-AI

## Problem Statement:
- Mental healthcare faces challenges in diagnosis and treatment due to subjective symptoms and difficulties in patient communication.

- There's a shortage of mental health professionals, especially in remote areas, leading to limited access to care.

- Limited access can cause delays in diagnosis and inadequate treatment, worsening patient conditions.

- 1 in 4 people worldwide suffer from mental disorders to some extent. Moreover, 3 out of 4 people with severe mental disorders do not receive treatment, 

 - During some periods like the pandemic, people struggle with mental health issues, and many may not get mental health practitioners’ help

- AI systems can serve as self-service tools for initial assessment and support, bridging the gap until patients can see a qualified healthcare provider and promoting personalized care.

  ## Related Works:
  - MentalBERT: This research introduces two new language models, MentalBERT and MentalRoBERTa, specifically designed for mental health analysis. These are the first models trained on mental health data from Reddit.  They are publicly available for anyone to use. The study shows that these new models outperform previous methods in detecting depression, stress, and suicidal ideation in text.
  - Mental-LLM:
        - They evaluate different techniques for fine-tuning LLMs on mental health data.
        - They released the first open-source LLMs designed for mental health prediction (Mental-Alpaca and Mental-FLAN-T5).
        - They offer guidance for future development of domain-specific LLMs and highlight ethical considerations for using LLMs in healthcare.
  - MentaLLaMA:
        - Building a specific dataset (IMHI) to train models.
        - Developing MentaLLaMA, the first set of open-source models that follow instructions and explain their reasoning for mental health analysis.
        - Creating a rigorous evaluation system to test these models across various tasks and datasets.

## Data
### IMHI Dataset:
- The authors in MentaLLaMA constructed a comprehensive dataset called IMHI specifically designed for training and evaluating AI models for mental health analysis on social media

- The foundation of IMHI lies in ten pre-existing datasets focusing on mental health analysis from various social media platforms like Reddit, Twitter, and SMS

- Due to the lack of open-source data providing detailed explanations for annotations, ChatGPT is utilized to generate explanations. These explanations follow a template of "[label] Reasoning: [explanation]". 

- Additionally, supervised annotations from the raw datasets are incorporated to improve the quality of generated explanations.
    
![IMHI_dataset_image](https://github.com/A-Aditya-Bharadwaj/Understanding-The-Behavior-Emotion-and-Feelings-Of-Mental-Health-Patients-Using-Conversational-AI/assets/110816901/8ef87b27-1679-4d65-820f-00d523318ea6)

This is what it looks like:
![Aditya_149_IMHI](https://github.com/A-Aditya-Bharadwaj/Understanding-The-Behavior-Emotion-and-Feelings-Of-Mental-Health-Patients-Using-Conversational-AI/assets/110816901/ae83afe2-8780-4025-a5e8-a3045d202443)

### MHC Dataset:
- MHC stands for Mental Health Counselling. These Dataset were available on HuggingFace🤗.

- mental-health: This dataset, though lacking detailed descriptions, appears to contain data points relevant to understanding mental health.

- Sample entries include patient expressions of anxiety and requests for professional help

- This dataset's potential applications range from research and model training to clinical applications aimed at addressing anxiety, stress, and other emotional states.

- es_mental_health_counseling: This bilingual dataset (English and Spanish) delves into the realm of mental health counselling.

- Potential use cases include analyzing counselling conversations, developing NLP models for mental health applications, investigating language patterns associated with self-esteem and depression, and exploring effective coping strategies.
  
![MHC_dataset](https://github.com/A-Aditya-Bharadwaj/Understanding-The-Behavior-Emotion-and-Feelings-Of-Mental-Health-Patients-Using-Conversational-AI/assets/110816901/8b11e8ac-86c6-4a52-abfc-0dae4a75d065)

This is what it looks like:

![Aditya_149_MHC](https://github.com/A-Aditya-Bharadwaj/Understanding-The-Behavior-Emotion-and-Feelings-Of-Mental-Health-Patients-Using-Conversational-AI/assets/110816901/23b71e0a-6f4d-42e5-bdb9-f918736ed8e8)

## Methodology & Tools
- LoRA: Low-Rank Adaptation of Large Language Models
    - Decomposes the update matrix during finetuning
    - Reduced Memory Footprint
    - Faster Training and Adaptation
    - Feasibility for Smaller Hardware
    - Scaling to Larger Models 

- Gemma - 2b Model
    - Lightweight, State-of-the-Art Performance

- Yi - 7b Model 
    - Multilingual Expertise, State-of-the-Art Performance
    - Grouped-Query Attention: reduces training and inference costs
    - SwiGLU Activation: post-attention activation function

- Proxy-tuning

## Understanding Proxy Tuning
![Proxy_tuning](https://github.com/A-Aditya-Bharadwaj/Understanding-The-Behavior-Emotion-and-Feelings-Of-Mental-Health-Patients-Using-Conversational-AI/assets/110816901/dacdd38f-026d-43b9-9574-6a9d8c466a61)

And this is how I have used Proxy Tuning in my project

![My Proxy tuning](https://github.com/A-Aditya-Bharadwaj/Understanding-The-Behavior-Emotion-and-Feelings-Of-Mental-Health-Patients-Using-Conversational-AI/assets/110816901/4a52a2ea-b3af-4531-a2d0-7ead88e70384)

## Evaluation Metrics
- ROUGE Score:

  - These metrics calculate how much of the reference summaries or source text is captured in the generated summary's n-grams (sequences of words). 

  - Scores range from 0 to 1, with higher scores indicating better summary quality.

- BART Scores:

  - Formulates the evaluation of generated text as a text generation task.

  - It leverages BART, an encoder-decoder-based pre-trained model, to evaluate text from various perspectives such as informativeness, fluency, and actuality.

## Results
### ROUGE Score

![Rouge scores-1](https://github.com/A-Aditya-Bharadwaj/Understanding-The-Behavior-Emotion-and-Feelings-Of-Mental-Health-Patients-Using-Conversational-AI/assets/110816901/25c2fea2-6b62-415e-9e60-e53207234f0b)

![Rouge scores-2](https://github.com/A-Aditya-Bharadwaj/Understanding-The-Behavior-Emotion-and-Feelings-Of-Mental-Health-Patients-Using-Conversational-AI/assets/110816901/0fa65030-74eb-430b-a8d1-ada7dc681bf6)

Problem:
- These metrics focus solely on n-gram recall, which doesn't encompass other crucial aspects of good text generation in context. 

- These missing aspects include coherence, fluency, and the ability to capture the key information from the source text.

Therefore we chose BART Score as our evaluation metrics
### BART Score

![BART score YI](https://github.com/A-Aditya-Bharadwaj/Understanding-The-Behavior-Emotion-and-Feelings-Of-Mental-Health-Patients-Using-Conversational-AI/assets/110816901/66318c00-74eb-4e93-9bec-14f545b02fad)
BART Scores of Mental-Yi-7b-V1 Model. The average BART score of Mental-Yi-7b-V1 Model on the IMHI test sample is -3.2429

![BART score Gemma](https://github.com/A-Aditya-Bharadwaj/Understanding-The-Behavior-Emotion-and-Feelings-Of-Mental-Health-Patients-Using-Conversational-AI/assets/110816901/e2b67146-e6d5-41c0-a796-77174c260cd7)
BART Scores of Mental-Gemma-2b-V1 Model. The average BART score of Mental-Gemma-2b-V1 Model on the IMHI test sample is -3.8423

** SOTA has BART Score of -2.734 **

### BART Score after Proxy Tuning

![BART score Yi (proxy tuned)](https://github.com/A-Aditya-Bharadwaj/Understanding-The-Behavior-Emotion-and-Feelings-Of-Mental-Health-Patients-Using-Conversational-AI/assets/110816901/f3ce9879-8185-417a-a736-126fea14ebe5)
Fig. BART Scores of Proxy Mental-Yi-32b Model. The average BART score of Proxy Mental-Yi-32bModel on the IMHI test sample is -2.9706

![BART score Gemma (proxy tuned)](https://github.com/A-Aditya-Bharadwaj/Understanding-The-Behavior-Emotion-and-Feelings-Of-Mental-Health-Patients-Using-Conversational-AI/assets/110816901/c274259b-8d77-4341-b380-9d4cbefc7926)
Fig. BART Scores of proxy Mental-Gemma-7b Model. The average BART score of proxy Mental-Gemma-7b Model on the IMHI test sample is -3.3851

## Proxy Tuned Responses on IMHI dataset
Q1) Consider this post: "Anyone ever wish they were good at something? Something. Anything. Be it something innocuous or something that can get you a kickass job. Anything from which you could derive happiness and fulfillment. I've failed at everything I've tried. Good at absolutely nothing, even after years of trying. If there were even one such thing, I could just devote myself to it and use it to keep myself busy." Question: Does the poster suffer from depression?

A1) Yes, the poster suffers from depression. The post exhibits a lack of self-esteem and a feeling of failure, which are alkohynical symptoms of depression. Additionally, the poster expresses a desire for something that can bring them happiness and fulfillment.

Q2) Consider this post: "That's two major holidays within 8 days. It's a bit overwhelming ..." Question: Does the post show risk of perceived burdensomeness?

A2) No, the post does not show this risk. The reason is  that the post mentions feeling overwhelmed, but it does not mention any thoughts of being a burden or feeling better off gone. 2. Feeling overwhelmed is a common emotional response to stressful situations or heavy responsibilities, but it does not necessarily indicate perceived burdensomeness. 3. The response does not indicate any perceived burdensomeness either. It is a simple acknowledgment and validation of the individual's feelings of being overwhelmed.

## Naive Architecture For Counselling
![Naive Architecture](https://github.com/A-Aditya-Bharadwaj/Understanding-The-Behavior-Emotion-and-Feelings-Of-Mental-Health-Patients-Using-Conversational-AI/assets/110816901/d9d4fe75-01a0-46c0-a356-20147511ab07)

### Response
Q1) She constantly tells me what I am doing wrong. For once, I want her to be proud of me. It’s like no matter what I do, she does not have one nice word to say to me. She is always hateful towards me and always has been.

A1) I understand that you are feeling hurt and frustrated by your mother's constant criticism and lack of positive feedback. It is important to recognize that this behavior is not healthy and may be indicative of a larger issue within the family dynamic. It is possible that your mother's negative behavior is a result of her own unresolved issues or a lack of emotional support.

As a psychologist, I would recommend that you consider seeking therapy or counseling to address this issue. In therapy, you can work with a trained professional to develop coping strategies and learn how to communicate effectively with your mother. Additionally, you may want to consider setting boundaries and establishing a healthy relationship with your mother.

Remember, you deserve to be treated with respect and kindness, and it is important to prioritize your own well-being. I encourage you to take steps towards creating a healthier and more positive relationship with your mother.

Q2) I'm feeling really overwhelmed with my responsibilities as a parent

A2) As a licensed psychologist, I understand that being a parent can be a challenging and overwhelming experience. It's common to feel overwhelmed when trying to balance the needs of your children, work, and personal life. Here are some strategies that may help you manage your responsibilities and reduce your feelings of overwhelm:

Prioritize self-care: Make time for activities that help you relax and recharge, such as exercise, meditation, or reading.
Set boundaries: Learn to say no to non-essential commitments and prioritize your own needs and well-being.
Delegate tasks: Ask for help from your partner, family, or friends when possible, and delegate tasks that can be shared among them.
Practice time management: Use tools such as calendars, to-do lists, or apps to stay organized and manage your time effectively.
Seek support: Reach out to friends, family, or a therapist for emotional support and to talk through your feelings of overwhelm.

Remember, it's okay to feel overwhelmed, and it's important to take care of yourself and seek support when needed. By prioritizing self-care, setting boundaries, delegating tasks, practicing time management, and seeking support, you can manage your responsibilities and reduce your feelings of overwhelm. 

Q3) I'm struggling with grief after the loss of a loved one and I don't know how to cope with the pain and sadness.

A3) As a licensed psychologist, I understand that the loss of a loved one can be incredibly difficult and can lead to feelings of grief and sadness. It's important to acknowledge these feelings and to seek support during this challenging time.

Here are some strategies that may help you cope with your grief:

1. Allow yourself to feel your emotions: It's important to acknowledge and validate your feelings, rather than trying to suppress or avoid them. Allow yourself to feel the pain and sadness, and give yourself permission to express these emotions in a healthy way.
2. Seek support: Reach out to friends, family, or a support group for help and guidance. Talking to others who have experienced a similar loss can be incredibly helpful in finding ways to cope with grief.
3. Practice self-care: Take care of yourself physically, emotionally, and spiritually. Engage in activities that bring you comfort and help you relax, such as exercise, meditation, or spending time in nature.
4. Consider therapy: If you're finding it difficult to cope with your grief on your own, consider seeking the help of a mental health professional. A therapist can provide you with additional support and guidance in managing your emotions and coping with your loss.

Remember, grief is a natural and necessary process, and it's okay to feel sad and overwhelmed. By acknowledging your emotions and seeking support, you can work through your grief and find a way to heal and move forward.

Q4) I just need my spirit to settle In its totality it doesn't have to be about wins and loses, or what I failed to do. Neither does it have to be about my past years and the thoughts that come with immense feelings that appears to haunt me. The behaviors and mentality that I have doesn't have to be the end all be all. One major thing to include that its not about growth or conquering something in life. I'm not living to grow or to become strong after a catastrophic situation. I am looking for my spirit to simply just settle. I'm not seeking any advice nor trying to raise my fist towards challenges. I'm not seeking any of that just a settling of the inner me. To me, that is important than anything else because I would gladly be able to live with that when I one day be out of this earth. I'm not the goal oriented type. Its not about climbing this ladder of life. I'm not here for any of what most people are striving for. I seek for my spirit to settle for all these years. That is what I'm chasing. Most people are chasing dreams, families, success, marriages, money, respect, and fame, but not this human. More power to them and I'm sure they will obtain all those things but I for one am not seeking to obtain. The human game is a serious thing filled with losses and wins. I don't wanna count anymore nor try to get to the next level of life. Cycling through the infinite regrets and regression. The only goal is for this spirit to settle some type of way. I'm gunning for an internal calmness. Something that can penetrate and flood the mind of mine. Something that can provide some internal at ease like affect for myself. So I say to my spirit, I hope you settle.

A4) As a licensed psychologist, I understand that this patient is expressing a deep desire for their inner self to settle and find a sense of calmness and peace. They are not seeking external validation or success, but rather a state of inner peace and contentment. This is a common desire for many individuals, as it allows for a sense of inner stability and well-being.

It's important to recognize that this desire for inner peace is not necessarily a goal-oriented approach, but rather a focus on finding a sense of inner calmness and acceptance. This can be achieved through various means such as mindfulness practices, meditation, and self-reflection.

As a psychologist, I would encourage this patient to continue exploring their inner self and finding ways to cultivate a sense of inner peace and calmness. This may involve engaging in activities that promote relaxation and stress reduction, such as yoga, deep breathing exercises, or spending time in nature.

Additionally, it may be helpful for this patient to explore their values and beliefs, and to identify what brings them a sense of purpose and meaning in life. This can help them to find a sense of direction and fulfillment, which can contribute to their overall well-being and sense of inner peace.

Overall, it's important to recognize that finding inner peace and calmness is a personal and ongoing journey, and that it may take time and effort to achieve. However, with a focus on self-reflection, self-care, and mindfulness practices, this patient can work towards finding a sense of inner peace and contentment.

## Challenges and Limitations
We have identified 5 major challenges for building, training, and deploying LLM for mental health counseling: 
1. **Model hallucination**, which impacts all LLMs regardless of application; 
2. **Model interpretability**, which is crucial for human understanding, wider acceptance, and model improvement 
3. **Privacy and regulatory concerns**, notably arising from the use of patient electronic health records (EHR) 
4. **Clinical methodology and effectiveness** and 
5. **Bias** arising from current LLM paradigms and limited data sources.

## Conclusion

Our work has explored the potential of leveraging large language models (LLMs) for applications in mental health.  We identified the limitations of traditional fine-tuning approaches for LLMs when the resources are limited and investigated the effectiveness of the proxy fine-tuning technique. Our findings demonstrate that while traditional fine-tuning on mental health datasets can be challenging with limited resources, proxy fine-tuning offers a promising alternative for adapting LLMs for mental health applications by using existing resources. The proxy fine-tuning approach showcased the ability to generate nearly as coherent and informative responses compared to models fine-tuned directly on mental health datasets. Our models were trained to a bare minimum level and can be improved a lot with better resources. By continuing to explore the potential and limitations of LLMs in mental health contexts, we can pave the way for the development of innovative tools that can provide accessible and supportive resources for individuals seeking mental health assistance. 
