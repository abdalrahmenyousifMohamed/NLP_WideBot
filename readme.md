# NLP Engineering Tasks
## Overview
> Hey there! Welcome to our NLP engineering challenges. We've lined up two exciting tasks for you to showcase your skills in natural language processing and software engineering. These tasks focus on named entity recognition and spelling correction - essential components in boosting our chatbot's capabilities. Get ready to dive in!

## Task 1: Named Entity Recognition (NER)
### Description
> Imagine you're chatting with a friend, and they're trying to tell you something important. Your job is to pick out the key details - that's what our chatbots aim to do with NER. We want you to build a NER system from the ground up using either deep learning or machine learning techniques. The goal is to identify and classify named entities like people, organizations, or locations from text. And here's the twist - you can't use any large language models (LLMs) or pre-trained models. We're excited to see what you can create with your own hands!

### Constraints
* Please create your model from scratch using the provided data. No pre-trained models or LLMs allowed.
### Files
* Dataset: `ner_data.csv`
  - Two columns: one for text sentences and the other for labels of each word, separated by space.
  - "x" indicates no entity present.
### Deliverables
* A notebook detailing your solution.
* Save your model and any other artifacts for testing on a private dataset.
### Please answer these questions in the readme:
* What were the main challenges you faced, and how did you address them given the limited time?
- Data Labeling , Used Label Studio to address each category that text going around 
- for instance Mapped "عايزه" => Show , "الله يسلمك" => "GBU" etc.
* In your opinion, what is the best approach to handle much larger number of entities like 100?
- in my own submission ,used The dimension of the embedding vector and the hidden state of the LSTM were set Since it is a many-to-many problem, the return_sequences value of the LSTM was set to True, and the LSTM was wrapped with Bidirectional() for bidirectional use. Test data was entered as validation_data to check the accuracy of the test data during training
- for more entities we could use Conditional Random Field (CRF), By adding this as a layer on top of the bidirectional LSTM model, a bidirectional LSTM + CRF model was created. Here, we understand the intuition of the two-way LSTM + CRF model, not the mathematical understanding of CRF.

## Task 2: Spelling Correction API
### Description
> For our second task, we're looking at spelling correction - a vital feature for any text-based service. Your mission is to build a super-efficient spelling correction API. It should take a word as input and return a list of probable corrections, sorted by likelihood, or the word itself if it's already correct. Wrap this functionality up nicely in an API, and you're golden!

### Example
* Input: "عربيياة" → Output: "عربية", "عربي", "عرب", "غربية"
* Input: "بحر" → Output: "بحر"
### Constraints
* The response time for each word should be between 50-200 ms.
* Feel free to use any technique or approach - whether it's a ready-made solution or something you build from scratch. We're looking for efficiency and precision.
### Files
* Dataset: **Private-test-set**
### Deliverables
* The codebase for an API developed using any framework (FastAPI, Flask, Django, etc.).

## General Instructions
* Aim for clarity and structure in your code – it helps us better understand your thought process.
* Strive for a balance between efficiency and accuracy in your solutions.
* Adhere to the deadline, as late submissions will not be accepted. Remember, even if your solution isn't complete or as optimal as you hoped, submit it anyway. The focus of this task is not just on completion but on how you efficiently and creatively approach problems and manage your time.
* Most importantly, have fun with these tasks!
* If you need any clarification, please don't hesitate to reach out!

**Best of luck! We're eagerly looking forward to seeing the innovative solutions you come up with.**