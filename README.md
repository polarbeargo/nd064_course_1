# nd064_C1

[//]: # (Image References)

[image1]: ./project/screenshots/docker-run-local.png
[image2]: ./project/screenshots/ci-github-action.png
[image3]: ./project/screenshots/ci-dockerhub.png
[image4]: ./project/screenshots/k8s-nodes.png
[image5]: ./project/screenshots/kubernetes-declarative-manifests.png
[image6]: ./project/screenshots/argocd-ui.png
[image7]: ./project/screenshots/argocd-techtrends-prod.png
[image8]: ./project/screenshots/argocd-techtrends-staging.png

## TechTrends Background
TechTrends is an online website used as a news sharing platform, that enables consumers to access the latest news within the cloud-native ecosystem. In addition to accessing the available articles, readers are able to create new media articles and share them.  
## Project Steps Overview:  
In this project we will:  
- Apply the best development practices and develop the status and health check endpoints for the TechTrends application.  
- Package the TechTrends application by creating a Dockefile and Docker image.  
- Implement the Continuous Integration practices, by using GitHub Actions to automate the build and push of the Docker image to DockerHub.  
- Construct the Kubernetes declarative manifests to deploy TechTrends to a sandbox namespace within a Kubernetes cluster. The cluster should be provisioned using k3s in a vagrant box.  
- Template the Kubernetes manifests using a Helm chart and provide the input configuration files for staging and production environments.  
- Implement the Continuous Delivery practices, by deploying the TechTrends application to staging and production environments using ArgoCD and the Helm chart.  
## Project Instructions:  
- Step 1: Best Practices For Application Deployment  
- Step 2: Docker for Application Packaging  
- Step 3: Continuous Integration with GitHub Actions  
- Step 4: Kubernetes Declarative Manifests  
- Step 5: Helm Charts  
- Step 6: Continuous Delivery with ArgoCD  
## Deployment Results:  
docker-run-local| ci-github-action
:-----------------:|:-----------------:|
![][image1]        |![][image2]        |  
ci-dockerhub| k8s-nodes
![][image3]        |![][image4]        |
kubernetes-declarative-manifests| argocd-ui |
![][image5]        |![][image6]                  |
argocd-techtrends-prod| argocd-techtrends-staging|
![][image7]        |![][image8]                  |
