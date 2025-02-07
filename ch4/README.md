
# Todo
background story
We dont do the training part, are you comfortable in doing the application side?



# fuck ibriz
endpoint for posting a tweet
cofounder interaction

# deepseek-nepali
* run the code (their dataset, their model)
* multi GPU training
* TPU training
* swap with custom dataset, custom tokenizer
* custom dataloader
* feature to resume dataloader


lightning flash
provides standerized framework for us to quickly access all the pretrained model architecture as well as some popular dataset
1. supply data
2. Define task and backbone (pre=defined end network to choose from )
3. Fine tune the model
4. Predictions: (excludes defining cNN, lr, optimizer)

video classification with flash
kinetics 400 human action video dataset (10s videos)


slowFast architecture: architecture for video classification (combination of slow and fast pathway for making prediction)


Steps for Video classification model usign flash:
1. importing libraries
loading the dataset
3. configuring the backbone
4. Training and fine tuning the model
5. Predicting action based on the model

train_folder, val_folder
clip_sampler (how the frames would be sampled), clip_duration(duration in seconds)
decode_audio (whether or not to load the audio with video) vid. tensor: CTHW, Audio tensor shape: S
batch_size: no. of videos in a single batch

can try slowfast directly from model zoo


# Automatic speech recognition (ASR) using flash
*custom dataset and architecture like web2vec 
web2vec is improvement of bert model by facebook
use the concept of self supervision and contrastive loss


1. importing libraries
2. loading the dataset
    - create dataframe
    - train test split (80-20)
    * note: higher the batch size higher the GPU & memory usage (very low batch size may not yield any learning either)

3. configuring the backbone
    - select the backbone
    - configure the task
4. training and fine tuning the model
5. predict speech based on the model


