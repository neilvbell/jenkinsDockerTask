# jenkinsDockerTask
jenkinsDockerTask repo to practice running docker build and deploy from a Jenkins pipeline.

Plan is to have sub-folders for each container with dockerfiles in each
Parent folder will hold jenkinsfile with stages for cleanup, git clone from repo (?, also do I need to do this to both Jenkins machine and to docker node), building images, deploy, test

