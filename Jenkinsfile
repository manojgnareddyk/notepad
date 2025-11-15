pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                echo "Building Docker Image"
                bat "docker build -t notepad:v1 ."
            }
        }

        stage('Docker Login') {
            steps {
                echo "Logging into Docker Hub"
                bat 'docker login'
                // More secure command:
                // sh 'echo <DOCKER_PASSWORD> | docker login -u nikhitha --password-stdin'
            }
        }

        stage('Tag & Push Docker Image to Docker Hub') {
            steps {
                echo "Tagging and Pushing Docker Image"
                bat "docker tag notepad:v1 manojgnareddyk/notepad:v1"
                bat "docker push manojgnareddyk/notepad:v1"
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying to Kubernetes"
                bat 'kubectl apply -f deployment.yaml --validate=false'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Please check the logs.'
        }
    }
}
