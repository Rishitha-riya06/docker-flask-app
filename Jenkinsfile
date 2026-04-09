pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Pulling code from GitHub...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t rishitha-flask-app:latest .'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'docker run --rm rishitha-flask-app:latest python -c "import flask; print(flask.__version__)"'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh 'docker stop flask-prod || true'
                sh 'docker rm flask-prod || true'
                sh 'docker run -d -p 5000:5000 --name flask-prod rishitha-flask-app:latest'
                echo 'Application deployed successfully!'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs above.'
        }
    }
}
