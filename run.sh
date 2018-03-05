#!/bin/sh

#  Script.sh
#  shell
#
#  Created by Micheli Knechtel on 04/03/2018.
#  Copyright © 2018 Micheli Knechtel. All rights reserved.

GIT_HUB=https://raw.githubusercontent.com/micheliknechtel/Email-Extraction-Project/master/
GIT_HUB_SOURCE=https://raw.githubusercontent.com/micheliknechtel/Email-Extraction-Project/master/email/
OUTPUT_PATH=json
INPUT_PATH=email
CODE_PATH=code


#Creating folders ...
if [ -d $OUTPUT_PATH ]
then
echo "Directory $OUTPUT_PATH already exists "
exit 1
else
mkdir $OUTPUT_PATH
fi

if [ -d $INPUT_PATH ]
then
echo "Directory $INPUT_PATH already exists "
rm -r $OUTPUT_PATH
exit 1
else
mkdir $INPUT_PATH
fi

if [ -d $CODE_PATH ]
then
echo "Directory $CODE_PATH already exists "
rm -r $OUTPUT_PATH
rm -r $INPUT_PATH
exit 1
else
mkdir $CODE_PATH
fi

#Downloading files from github
curl -LkSs $GIT_HUB'CodecDetection.py'       -o CodecDetection.py
curl -LkSs $GIT_HUB'DataManipulation.py'     -o DataManipulation.py
curl -LkSs $GIT_HUB'Extractor.py'            -o Extractor.py
curl -LkSs $GIT_HUB'Nslookup.py'             -o Nslookup.py
curl -LkSs $GIT_HUB'PrintManager.py'         -o PrintManager.py
curl -LkSs $GIT_HUB'Repository.py'           -o Repository.py
curl -LkSs $GIT_HUB'SerialiseData.py'        -o SerialiseData.py
curl -LkSs $GIT_HUB'Utilities.py'            -o Utilities.py
curl -LkSs $GIT_HUB'Industrialization.py'    -o Industrialization.py

#Moving files
mv *.py ./code

for i in {1..1000}
do
curl -LkSs $GIT_HUB_SOURCE$i       -o $i
mv $i ./email
done


#Running Module 1 --- check if it finshed sucessifully
python36 ./code/DataManipulation.py

#Running Module 2 --- run as nohup still need
export FLASK_APP=$(pwd)/code/Industrialization.py
flask run
