pipeline {
    agent any
    stages{
        stage("checkout from git "){
            steps{
                git branch: "master",
                url:  "https://github.com/anjilinux/my-project-mlops-with-jenkins.git"
            }
        }
        stage('Install Dependencies') {
            steps {
                sh "pwd"
                sh '''
                mkdir -p /opt/mlflow/artifacts
                chown -R jenkins:jenkins /opt/mlflow
                chmod -R 777 /opt/mlflow
                python3 -m venv .venv
                .venv/bin/pip install --upgrade pip
                pwd
                

                .venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Train Model with MLflow') {
            steps {
                sh '''
                .venv/bin/python train.py
                '''
            }
        }

        stage('evaluate.') {
            steps {
                sh '''
                .venv/bin/python evaluate.py
                '''
            }
        }
        stage("code-test-pytest"){
            steps{
                sh '''
                    .venv/bin/python  test.py

                '''
            }
        }
    
    
    
    
    
    }
}


