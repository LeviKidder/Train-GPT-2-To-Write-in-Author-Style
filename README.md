# Train-GPT-2-To-Write-in-Author-Style

NOTE: THIS IS ON WINDOWS 10 RUNNING   conda version : 4.9.2, conda-build version : 3.20.5 -This is working as of 13 May 2021

You can download anaconda here: https://www.anaconda.com/products/individual

***I couldn't find a complete working guide to doing this for people who are bad at python like myself, so I made one.***


If you run into issues I can't help you. Run this code at your own risk. If you accidentally create skynet that's on you bud. 

I cobbled together a bunch of parts of other people's work to hopefully get GPT-2 able to read books you give it, to fine-tune it to your desired output. I am mainly posting this on my public Github to make sure the AI overlords can see my contribution to the inevitable AI Singularity.

It probably won't work on your machine. It barely works on mine. You can use whatever you like, but I had success using anaconda and creating an venv to run in. It allowed me to control my python version which is important as I only found it to work with the TensorFlow version 1.12 which needed 3.6 python. Anyway on we go.



****HOW TO START****
You can optionally open a conda cmd prompt and cd to an empty directory you plan to use for this and if you don't already have git do

> conda install -c anaconda git 
select y if prompted
> git clone https://github.com/LeviKidder/Train-GPT-2-To-Write-in-Author-Style
> cd Train-GPT-2-To-Write-in-Author-Style
 
You're in hackerman. But now you may need to change some files.  



Create a large single text file with all the training data you want to use in it. You can delete or add whatever you like, but it will change the training data and model. ***Once you have all the training data you want in one large file - name it merged_books.txt and store it in the same directory as the rest of the code*** You can replace the one that came with. Or just use it if you like. My understanding is that some data scientists look here https://the-eye.eu/ for good sources of data.

***You will also want to either clear or replace the output_cleaned.txt, val.txt and train.txt files, as they currently have data on them if you want to use your own training data***

***I am also happy to add your tokenized data sets to this repo so others can use them***



To start Open a conda prompt and ***cd to the file containing all the code pieces and data***

then enter 

>conda create -n gpt2authors python=3.6

enter y to any prompt

>conda activate gpt2authors

>pip install tensorflow-gpu==1.12

>python Cleandata.py

Now you should have cleanish data. You can go through and clean more. It might help. I don't know, because if I did, I wouldn't have had to hack this together so poorly.

>pip install torchvision 
>conda install -c conda-forge tensorboardx
select y
>pip install tqdm
>pip install transformers


***Make sure you replace the text in the train_data_file and eval file to the correct path on your machine.***


>python run_lm_finetuning.py --output_dir=output --model_type=gpt2 --model_name_or_path=gpt2-medium --do_train --train_data_file=THIS SHOULD BE WHATEVER THE PATH TO YOUR TRAIN.TXT FILE IS\train.txt --do_eval --eval_data_file=THIS SHOULD BE THE PATH TO YOUR VAL.TXT FILE\val.txt --overwrite_output_dir --block_size=200 --per_gpu_train_batch_size=6 --save_steps 5000 --num_train_epochs=2

You can fiddle around the epochs and steps and stuff. This took about 12 hours to run on my 9700k and didn't use my GPU at all. I don't have Cudnn or whatever the Nvidia thing is. You could probably get this to work on GPU much more efficiently on linux using docker and native NVIDIA support. But I didn't YMMV.

When that's done then the hardest part is over.

***locate the folder called \output*** it should be in the folder your venv is in. Make sure you replace the model_name_or_path to the correct full path for the \output file.



>python run_generation.py --model_type gpt2 --model_name_or_path THIS SHOULD BE WHATEVER THE PATH IS AND LINK TO THE OUTPUT FOLDER\output --length 300 --prompt "This is where you will type your prompt for the Algo. Make sure it is in these quotation marks."

There you go. Now you can watch your desktop think. 

There are a ton of little things that you can mess with including temperature and stuff, but I'm not going to get into them here, because I don't know enough about it. This is just how to get old GPT-2 Running on my personal rig, and it might work and it might not. have fun and good luck!




This was done using the code created by Priya Dwivedi adapted from this repo.  https://github.com/priya-dwivedi/Deep-Learning/tree/master/GPT2-HarryPotter-Training
