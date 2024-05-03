# AIT-GPT

### Task 1: Source Discovery <br>

### Source: 

For our dataset, we employed web scraping to gather information from various sources, including the official AIT website and other relevant webpages. Additionally, we incorporated data from the AIT brochure PDF file. Furthermore, we included the AIT brochure PDF file in our dataset, extracting information from its contents to enrich our data pool.

## Prompt template: 

The prompt template I used:

"   Hello there! I'm AITBot, your helpful virtual assistant ready to answer any queries
    you might have about the Asian Institute of Technology (AIT).
    Whether you're seeking information about AIT, its array of programs and courses,
    or any related topic, feel free to ask away!
    Simply share your questions with me,
    and I'll provide you with the guidance you need."

### Task 2. Analysis and Problem Solving

For comparing the model performance, we have used T5 model (fastchat-t5-3b-v1.0) and GPT2 model (gpt2-finetuned-cnn-summarization-v1) from Huggingface.

### T5 Model:

The T5 Fast model demonstrates excellent performance due to its extensive training data, providing highly accurate answers to most questions. However, it occasionally lacks in returning related documents, likely because its vast knowledge surpasses the database's scope. 

### GPT2 Model:

On the other hand, the GPT2 Finetuned model shows reduced performance compared to T5. This model, based on an encoder and a decoder architecture, often retrieves answers from the limited database, impacting its overall performance. 

Despite limitations in database size and computational resources, the GPT2 model was selected for its faster inference capabilities, suitable for a web application. 

### Issues

Regarding unrelated information issues,  T5 models are good at giving relevant info, but GPT models sometimes miss the point. We can fix this by adding more and better data to the system. Also, we can tweak how we ask questions to match what the model learned during training. These changes can help GPT models give more useful responses.

### Task 3. Chatbot Development - Web Application Development

<img width="522" alt="Screenshot 2024-03-22 at 08 55 59" src="https://github.com/ashmita-5/Assignment-7----AIT-GPT/assets/32629216/fa06129e-541e-4c2e-8ee0-f4f92e4698bc">

