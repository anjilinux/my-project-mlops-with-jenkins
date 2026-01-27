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
                sh '''
                python3 -m venv .venv
                source .venv/bin/activate
                #/home/bny/anaconda3/envs/kaira-310
                # Install necessary Python packages including mlflow and project dependencies
                pip install --upgrade pip
                pip install mlflow pandas scikit-learn # Add your other dependencies here
                '''
            }
        }

        stage('Train Model with MLflow') {
            steps {
                sh '''
                source .venv/bin/activate
                # Run the Python training script that uses MLflow
                python3 train.py
                '''
            }
        }
        
        stage('Test Model') {
            steps {
                sh '''
                source .venv/bin/activate
                # Run evaluation or testing script
                python3 evaluate.py
                '''
            }
        }

        // Optional: Add stages for linting, building Docker images, or deployment to production
    }
}
