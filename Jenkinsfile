@Library("security_stages") _

pipeline {
    agent any
    stages {
        stage('Setup') { // Install any dependencies you need to perform testing
            steps {
                script {
                sh """
                python3 -m venv ./venv
                . ./venv/bin/activate
                pip install poetry
                poetry install --extras "ui vector-stores-qdrant" --no-root
                """
                }
            }
        }
        stage ("Attempting security stages") {
            steps {
                shared()
            }
        }
        stage('Building our image') {
            steps {
                sh "docker build . -t vinnimous/privategpt:latest"
            }
        }
        stage('Login to Docker') {
            when {
                allOf {
                    branch 'master'
                }
            }
            steps {
                withCredentials([string (credentialsId: 'docker_hub_token', variable: 'token')]) {
                    sh "docker login --username vinnimous --password ${token}"
                }
            }
        }
        stage('Push to Docker') {
            when {
                allOf {
                    branch 'master'
                }
            }
            steps {
                sh "docker image push vinnimous/privategpt:latest"
            }
        }                                
    }
}