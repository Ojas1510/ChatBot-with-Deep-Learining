
# ChatBot with Deep Learning
Welcome to the Chatbot project! This readme provides a comprehensive guide to creating a chatbot using Neural Machine Translation (NMT) techniques with TensorFlow. The chatbot is designed to take text inputs and generate text responses. Below is a step-by-step guide, starting from data creation, to help you set up and train your chatbot.

## Table of Contents
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
- Acknowledgements
## Introduction
This project aims to create a chatbot using Neural Machine Translation (NMT) techniques. The chatbot can take text input and generate text responses. The project utilizes a seq2seq architecture from TensorFlow, employing an encoder-decoder model. This readme explains the entire process, from acquiring data to using the trained chatbot.

## Data Preparation
 
### Acquiring Data
To build a chatbot, you need training data. The project proposes using publicly available Reddit comment data. You can acquire the data from the Reddit comment dataset <br/>
```bash
 https://www.reddit.com/r/datasets/comments/3bxlg7/i_have_every_publicly_available_reddit_comment/?st=j9udbxta&sh=69e4fee7
```

And possibly from a torrent file. <br/>
```bash
https://mega.nz/file/ysBWXRqK#yPXLr25PgJi184pbJU3GtnqUY4wG7YvuPpxJjEmnb9A
```

### Database Setup
Create a SQLite database where you'll store the acquired Reddit comment data. The database will hold information like comment IDs, parent IDs, comment text, and other relevant fields.

### Data Extraction and Processing
Now, let's process the Reddit comment data to structure it for training:

- The data is in a tree-like structure, where comments and replies are organized hierarchically. To train an NMT model, we need to structure the data as comment-reply pairs.
- Consider factors like upvotes and select upvoted responses, as they may be of higher quality.

## Training Data Preparation
After the database is populated with Reddit comment data, create training and testing data files.

#### File Structure:
- "train.from" and "train.to": These files contain pairs of comments and replies, where each line in "train.from" corresponds to a comment, and the corresponding line in "train.to" is the reply.
- "test.from" and "test.to": These files are used for testing the trained model and follow the same format as training data.
Each line in these files represents a comment or a reply. Organize your data into these files for training and evaluation.

#### Data Filtering:
Filter out comments with inappropriate content or those that do not meet your quality standards.
Select only the top-voted or upvoted responses for training to ensure high-quality input-output pairs.

## Setting Up the NMT Model

The chatbot model is built on a Neural Machine Translation (NMT) architecture. It consists of an encoder-decoder model, allowing it to capture long-range dependencies in languages and produce fluent translations.

The encoder processes the input sentence to build a "thought" vector that represents the sentence's meaning. The decoder takes the thought vector and generates the translation.

The provided NMT model uses the seq2seq architecture from TensorFlow, offering advanced capabilities for generating text responses from text inputs.

To tarin model for the chatbot, follow these steps:
The model is 
Clone the project repository:

Model training can be done TensorFlow's orignal Neural Machine Translation (seq2seq) model:
```bash
 $ git clone https://github.com/tensorflow/nmt/
```
But model I used was [Daniel-kukiela's](https://github.com/daniel-kukiela) nmt model.
It is modification of orignal NMT model well optimized and easy for training.


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

## Training the Model

```bash
  $ cd ../

```
```bash
  $ python train.py

```


### Monitoring with TensorBoard
The training process can be monitered using TensorBoard. Open a command prompt inside the model directory and run:

```bash
$ Tensorboard --logdir=train_log/

```
This provides visual insights into training metrics, including BLEU score, Perplexity, Train Loss, and Gradient Norm.

### Evaluation Metrics
The model's performance can be assessed using the following metrics:

- BLEU Score: Measures the effectiveness of the chatbot by comparing its responses to reference responses. BLEU scores may vary based on data and language pairs.

- Perplexity (PPL): Evaluates how effectively the model predicts output from input. Lower perplexity values indicate better model performance.

- Train Loss and Gradient Norm: These metrics are monitored during training for tracking model convergence and performance.
## Interactive Mode

After training, you can interact with the chatbot in interactive mode using the inference.py script. The script processes questions and provides responses marked with different colors:

- Green: The top candidate response.
- Orange: Proper responses with lower scores.
- Red: Improper responses below the threshold.
To start an interactive session, run:

```bash
  $ python inference.py


```
### Batch Processing
For batch processing of questions and answers, you can redirect input from a file using the following command:
 ```bash
$ python inference.py < input.txt > output.txt


```

This way, you can process multiple questions and receive corresponding responses.
## Acknowledgements

 - [NMT chatbot from TensorFlow](https://github.com/tensorflow/nmt)

 - [Daniel-kukiela's NMT chatbot](https://github.com/daniel-kukiela/nmt-chatbot)

 - [Sentdex ](https://www.youtube.com/channel/UCfzlCWGWYyIQ0aLC5w48gBQ)

