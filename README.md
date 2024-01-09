## Second-Hand-Car-Price-Prediction-Using-MLops

# WineQuality-Prediction-Using-MLOPS---II

# Procedure of Creating a Environment

<!-- pip install virtualenv (if not installed)

virtualenv myenv  # Replace "myenv" with the name you want for your environment -->


# environment = CarEnv
# Activate the env by pasting this on gitbash => source CarEnv/Scripts/activate 


# __init__.py -> This file is everywhere in folders as we are using those folders as local packages and in order to import that we have to create __init__.py

# utils are the functions that we use in our code frequently

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml


## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model


# MLflow Commands for Dagshub Experiment

MLFLOW_TRACKING_URI=https://dagshub.com/harsh-priyam/Second-Hand-Car-Price-Prediction-Using-MLops.mlflow \
MLFLOW_TRACKING_USERNAME=harsh-priyam \
MLFLOW_TRACKING_PASSWORD=d34676be0f7f95c5afd000a5be7be52ce1ba8d12 \
python script.py

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 625374339876.dkr.ecr.us-east-1.amazonaws.com/mlproj

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID= AKIAZDGZXEMSC54UW75Q

    AWS_SECRET_ACCESS_KEY= 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

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = 625374339876.dkr.ecr.us-east-1.amazonaws.com/mlproj

    ECR_REPOSITORY_NAME = simple-app




