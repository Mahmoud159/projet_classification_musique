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
                    'docker-compose build'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    'docker-compose up -d'
                    // sh 'docker exec svm_service pytest tests/'
                    // sh 'docker exec vgg_service pytest tests/'
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub-credentials', url: 'https://index.docker.io/v1/']) {
                    'docker-compose push'
                }
            }
        }
        stage('Cleanup') {
            steps {
                'docker-compose down'
            }
        }
    }
}
