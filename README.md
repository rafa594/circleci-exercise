# Update a TaskDefinition in a ECS Service with CircleCI

Update a TaskDefinition through a JSON file, in a AWS ECS Service predefined.
CircleCI is used to automate deployment and test of the process.

## Files

 * .circleci/config.yml: Config file used to manage the deployment with CircleCI.
    Contains 2 blocks: Jobs and Workflow. 
    Jobs indicate the process itself. In this case, we use two jobs to build and upload a image to AWS ECR repository
    and another to generate a TaskDefinition, upload the AWS ECS Service and test it to complete the process.
 
 * site folder: Contains the html files that shows the webpage.

 * check.py: Python script to check if the update service process (reach a steady status) is complete.

 * Dockerfile: Used to generate the image to be uploaded to ECR.

 * taskdefinition.json: Template used to generate the taskdefinition to be used in the update process.

 * README.md: This file.


## Configurations

First of all, clone this repository to your local machine.

```
    git clone https://github.com/rafa594/circleci-exercise.git
```

Create an empty GitHub repository and add this origin to the local repository previously cloned.
```
    git add remote origin https://REPOSITORY_URL
```

Upload your repository to GitHub
```
    git add .
    git commit -m "Your commit name"
    git push origin master
```


After that, go to CircleCI login page (https://circleci.com/vcs-authorize/) and click on Log In with GitHub to access your repositories.
Select the organization that contains your repository.

Note: In order to maintain security and portability of the process, we need to set some Environment Variables to our jobs.
We will use Contexts to do this function (we could set hardcoded variables into config file, but that isn't the goal).

Click on Organization Setting menu and create a new Context and name it "aws_credentials" (if you want to write any name in this contexts, we need to change it in the Workflows block into Config file too).

Add the environment variables needed to work:

   1. AWS_ACCESS_KEY_ID
   1. AWS_SECRET_ACCESS_KEY
   1. AWS_SESSION_TOKEN
   1. AWS_DEFAULT_REGION
   1. AWS_ECR_IMAGE
   1. TASKDEFINITION_NAME
   1. SERVICE_NAME
   1. CLUSTER_NAME
   1. AWS_LOG_GROUP



Go to Dashboard page, Add Projects menu and seek for your repository to listen it.
Click on Start Building and choose Add Manually option (this option use the Config file in your repository).

You can check in real time the workflow of deployment, through CircleCI project that listen your repository.





