## diy-ml
DIY ML API Service for EC530

DIY ML is an API to train, test, and deploy ML models.

# User Stories

Below is a list of User Stories for reference, from the class slides

- API user should be able to create a ML image classification or Object detection project for Training and Inference
- API user should be able to upload data (images) for training in a project
- API user should be able to upload label or class data for images in a project
- API user should be able to analyze data before training
- API user should be able to add or remove training points
- API user should be able to configure training parameters
- API user should be able when the training is completed to get training stats
- API user should be able to test a model using new dataset and get results
- API user should be able to deploy a model to be used for inference and should be able to get a unique API to use for a project-iteration combination
- API user should be able to run and track iterations of training
- API user should be able to use inference API to run and get results on an image
- ALL APIs should be independent of the ML model and data
- A project is associated with a user

# Routes
Endpoint                 Methods  Rule                                          
-----------------------  -------  ----------------------------------------------
datasets_create          POST     /diyml/datasets/create                        
datasets_objects_create  POST     /diyml/datasets/objects/create                
datasets_objects_delete  POST     /diyml/datasets/objects/delete                
index                    GET      /                                             
inference_delete         POST     /diyml/inference/delete                       
inference_deploy         POST     /diyml/inference/deploy                       
inference_infer          POST     /diyml/inference/<inferenceDeploymentId>/infer
preprocess               POST     /diyml/preprocess                             
projects_create          POST     /diyml/projects/create                        
projects_delete          POST     /diyml/projects/delete                        
test_create              POST     /diyml/test/start                             
test_results             GET      /diyml/test/results                           
test_status              POST     /diyml/test/status                            
test_stop                POST     /diyml/test/stop                              
training_results         GET      /diyml/training/results                       
training_start           POST     /diyml/training/start                         
training_status          GET      /diyml/training/status                        
training_stop            POST     /diyml/training/stop                          
users_create             POST     /diyml/users/create  

## Setup

1. Clone repo
```
git clone https://github.com/AxelSariel/diy-ml
cd diy-ml
```
2. Setup Python Virtual Environment
```
python3 -m venv ml
```

3. Activate Virtual Environment
```
source ml/bin/activate
```

4. Install Requirements
```
pip install -r requirements.txt
```

5. Run Server
```
python server.py
```

## Docker Run
1. Build the docker image
```
docker build -t diyml .
```

2. Run the docker container
```
docker rum diyml
```

### Export Docker Image
1. Export image
```
docker save -o diyml.tar diyml
```

2. Import image on another computer
```
docker load -i diyml.tar
```