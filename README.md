# ChatBot-with-Deep-Learining

Welcome to the Chatbot project! This readme provides a comprehensive guide to creating a chatbot using Neural Machine Translation (NMT) techniques with TensorFlow. The chatbot is designed to take text inputs and generate text responses. Below is a step-by-step guide, starting from data creation, to help you set up and train your chatbot.

# Table of Contents
- Introduction  
- Data Preparation 
   - Acquiring Data
   - Database Setup 
   - Data Extraction and Processing 
- Training Data Preparation 
- Setting Up the NMT Model 
- Training the Model
   - Monitoring with TensorBoard 
   - Evaluation Metrics
- Interactive Mode 
- Batch Processing 

# Introduction
This project aims to create a chatbot using Neural Machine Translation (NMT) techniques. The chatbot can take text input and generate text responses. The project utilizes a seq2seq architecture from TensorFlow, employing an encoder-decoder model. This readme explains the entire process, from acquiring data to using the trained chatbot.

# Data Preparation
 
## Acquiring Data
To build a chatbot, you need training data. The project proposes using publicly available Reddit comment data. You can acquire the data from the Reddit comment dataset and possibly from a torrent file.

## Database Setup
Create a SQLite database where you'll store the acquired Reddit comment data. The database will hold information like comment IDs, parent IDs, comment text, and other relevant fields.

## Data Extraction and Processing
Now, let's process the Reddit comment data to structure it for training:

- The data is in a tree-like structure, where comments and replies are organized hierarchically. To train an NMT model, we need to structure the data as comment-reply pairs.
- Consider factors like upvotes and select upvoted responses, as they may be of higher quality.

# Training Data Preparation
After the database is populated with Reddit comment data, create training and testing data files.
Organize the data into "parent" and "reply" text files. Each line in the "parent" file corresponds to a parent comment, and each line in the "reply" file corresponds to a response to the parent comment.

# Setting Up the NMT Model

To tarin model for the chatbot, follow these steps:
The model is 
Clone the project repository:

```bash
 $  git clone --recursive https://github.com/daniel-kukiela/nmt-chatbot
```

Go to the model directory

```bash
 $ cd nmt-chatbot
```

Install the required dependencies:

```bash
  $ pip install -r requirements.txt

```
- Ensure TensorFlow-GPU, CUDA Toolkit, and cuDNN correctly installed on your system alongwith the complatible python version. <br />
- (For TensorFlow version = 1.15, I used CUDA 10 and cuDNN 7.4.15 )

Tweak settings of the model

```bash
  $ cd setup

```
Before training Configure project settings by editing the setup/settings.py file. Customize parameters like vocabulary size based on your system's specifications.
For model I used:<br />
- Vocab_size =15000 (suitable for 4GB of VRAM) 
- Training steps = 5000000
- Learing Rate = 0.001

Prepare data for training

```bash
  $ python prepare_data.py

```

# Training the Model

```bash
  $ cd ../

```
```bash
  $ python train.py

```


## Monitoring with TensorBoard
The training process can be monitered using TensorBoard. Open a command prompt inside the model directory and run:

```bash
$ Tensorboard --logdir=train_log/

```
This provides visual insights into training metrics, including BLEU score, Perplexity, Train Loss, and Gradient Norm.

## Evaluation Metrics
The model's performance can be assessed using the following metrics:

- BLEU Score: Measures the effectiveness of the chatbot by comparing its responses to reference responses. BLEU scores may vary based on data and language pairs.

- Perplexity (PPL): Evaluates how effectively the model predicts output from input. Lower perplexity values indicate better model performance.

- Train Loss and Gradient Norm: These metrics are monitored during training for tracking model convergence and performance.
# Interactive Mode

After training, you can interact with the chatbot in interactive mode using the inference.py script. The script processes questions and provides responses marked with different colors:

- Green: The top candidate response.
- Orange: Proper responses with lower scores.
- Red: Improper responses below the threshold.
To start an interactive session, run:

```bash
  $ python inference.py


```
## Batch Processing
For batch processing of questions and answers, you can redirect input from a file using the following command:
 ```bash
$ python inference.py < input.txt > output.txt


```

This way, you can process multiple questions and receive corresponding responses.
