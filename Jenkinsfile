pipeline {
    agent {label "docker"}
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/neilvbell/jenkinsDockerTask.git', branch: 'main'
            }
        }
        stage('Confirm git pull') {
            steps {
                    sh "echo $NODE_NAME"
                    sh "pwd"
                    sh "ls"
            }
        }
        stage('Trivy scan of repo directories') {
            steps {
                    sh "trivy fs --severity HIGH,CRITICAL -f json -o trivy_repo_fs.json ${pwd}"
            }
        }
        stage('Cleanup containers with same name') {
            steps {
                    sh "docker rm -f mysql1 flask-app nginx1 || true "
            }
        }
        stage('Create docker network if not exist') {
            steps {
                    sh "docker network create my-network || true"
            }
        }
        stage('Build mysql image from Dockerfile and Trivy scan image') {
            steps {
                    sh "cd db/ && docker build -t mysql_img . && trivy image --severity HIGH,CRITICAL -f json -o trivy_mysql_img.json mysql_img"
            }
        }
        stage('Build flask image from Dockerfile and Trivy scan image') {
            steps {
                    sh "cd flask-app/ && docker build -t flask_new_img . && trivy image --severity HIGH,CRITICAL -f json -o trivy_mysql_img.json mysql_img"
            }
        }
        stage('Deploy mysql container from image') {
            steps {
                    sh "docker run -dit --network my-network --name mysql1 mysql_img"
            }
        }
        stage('Deploy flask container from image') {
            steps {
                    sh "docker run -dit --network my-network --name flask-app flask_new_img"
            }
        }
        stage('Deploy nginx container from image') {
            steps {
                    sh "cd nginx/ && docker run -dit -p 80:80 --network my-network -v ./nginx.conf:/etc/nginx/nginx.conf --name nginx1 nginx"
            }
        }
        stage('Confirm docker build and deploy') {
            steps {
                    sh "docker images"
                    sh "docker ps -a"
                    sh "sleep 15s"
                    sh "curl localhost"
            }
        }
        
        stage('Archive') {
            steps {
                archiveArtifacts artifacts: 'trivy*.json'
                archiveArtifacts artifacts: 'db/trivy*.json'
                archiveArtifacts artifacts: 'flask-app/trivy*.json'
            }
        }
    }
}
