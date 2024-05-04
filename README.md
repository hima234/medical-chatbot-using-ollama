# My Medical Chatbot Project

## What I wanted to do

I wanted to make a chatbot that can answer questions about medical topics. A chatbot is a computer program that can have conversations like talking to a real person. Medical chatbots can help people get information about health and illnesses.

## The big challenge

I needed to "train" it on a lot of medical data to make a good medical chatbot. Training means feeding the chatbot lots of information to learn and understand. But, training a chatbot requires very powerful computers and special hardware called GPUs.

I tried to train my chatbot using the GPU I had, but it was too slow and took forever. Even with my GPU, training the chatbot would take months or years!

## My solution

Since training my chatbot was too hard, I used a chatbot that someone else had already trained. This pre-trained chatbot is called "medllama2." Medllama2 was trained in medical information, so it knows a lot about health topics.

## How I did it

I got help using medllama2 from a program called "ollama." Ollama makes it easy to access and run pre-trained chatbots like medllama2.

First, I installed Olla on my MacBook computer. Then, I used Olla to download (or "pull") the entire Medllama2 chatbot. After that, I started Olla's special interface called an "API." An API lets other programs talk to Olla.

On the front end (the user side), I made a website using a tool called Chainlit. My Chainlit website connects to Olla's API, letting users chat with the Medllama2 chatbot through a nice web interface.

## The result

Ultimately, my medical chatbot project uses the pre-trained medllama2 model from Ollama. Users can access medllama2 through my Chainlit website. This solution allowed me to make a medical chatbot without the huge cost and effort of training my model from scratch.

Old GitHub Project Link nextjs as frontend: https://github.com/hima234/chatbot

Try 1 using hugging face: https://github.com/hima234/medical-chatbot

Final Project Link: https://github.com/hima234/medical-chatbot-using-ollama
