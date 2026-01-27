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
                conda activate  kaira-310
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
                conda activate  kaira-310
                # Run the Python training script that uses MLflow
                python3 train.py
                '''
            }
        }
        
        stage('Test Model') {
            steps {
                sh '''
                conda activate  kaira-310
                # Run evaluation or testing script
                python3 evaluate.py
                '''
            }
        }

        // Optional: Add stages for linting, building Docker images, or deployment to production
    }
}
