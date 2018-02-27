#!/bin/bash
# Script to be run from cron.
# Checking exchange rate, if condition met, sending email
# If not, results are collected in file, and email is send on Monday 

# checking if docker container with phantomjs is running, if not, start it 
pjs_c_stat=$(sudo docker ps -a|grep phantomjs|awk '{print $8}');if [[ $pjs_c_stat -eq "Exited" ]]; then sudo docker start $(sudo docker ps -a|grep phantomjs|awk '{print $1}');fi

# get the exchange rate 
pyenv_dir="/home/mstanojlovic/github/websraping/exrate"
RATE=$(${pyenv_dir}/exrate/bin/python3 ${pyenv_dir}/get_rate.py)

# put result into file
echo $(date) $RATE >> ${pyenv_dir}/rate.log

# if rate bellow 25.2 or higher than 25.5 send email
condition=$(python ${pyenv_dir}/condition.py $RATE)
if [[ $condition == '1' ]]
then 
  email_API_dir="/home/mstanojlovic/gmail_API_python"
  cd $email_API_dir
  python send_msg.py "EUR-CZK $RATE"
fi

