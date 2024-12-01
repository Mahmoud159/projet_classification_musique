pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Images') {
            steps {
                script {
                    powershell 'docker-compose build'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    powershell 'docker-compose down'
                    powershell '''
                    try {
                        docker rm -f svm_service
                        docker rm -f vgg_service
                    } catch {
                        Write-Host "Les conteneurs n'ont pas été trouvés, continuation du processus."
                    }
                    '''
                    powershell 'docker-compose up -d'
                    // sleep(10)
                    // powershell 'docker exec svm_service pytest tests/'
                    // powershell 'docker exec vgg_service pytest tests/'
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub-credentials', url: 'https://index.docker.io/v1/']) {
                    powershell 'docker-compose push'
                }
            }
        }
        stage('Cleanup') {
            steps {
                powershell 'docker-compose down'
            }
        }
    }
}
