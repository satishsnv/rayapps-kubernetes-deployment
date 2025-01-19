# rayapps-kubernetes-deployment
This repo provides example of deploying multiple applications using kuberay operator in kubernetes

# This repo contains the following artifacts

- couple of ml applications text summarizer and translator that exposes end points for performing summarizing and translation (which are taken from ray documentation)

- docker file with common dependencies and to dockerize the applications

- rayservice.yaml that helps in creating the ray cluster and deploying apps using kuberay operator

- client.py to test the service end points

# Steps to deploy the apps in kubernetes using kuberay

- kubernetes cluster with helm installed is a prerequisite to start with(This can be executed on local cluster using minikube)

- install kuberay operator by running following commands (reference https://github.com/ray-project/kuberay-helm)

    ***helm repo add kuberay https://ray-project.github.io/kuberay-helm/***  
    ***helm repo update***  
    ***helm install kuberay kuberay/kuberay-operator***

- build the docker image with applications using the following command
    ***docker buildx build -t ml-apps:latest .***

- in case minikube is used as cluster, copy the image to minikube using the following command  
    ***minikube image load ml-apps:latest***

- deploy the applications by running the following command  
    ***kubectl -f apply rayservice.yaml***

- once the services is up and running, port-forward the dashboard port for head-svc and serve-svc to access the dashboard and testing the service. run the following command for port forwarding  
    ***kubectl port-foward <svc_name> <host_port>:<pod_port>***