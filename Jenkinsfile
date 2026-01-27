pipeline {
    agent any
    stages{
        stage("checkout from git "){
            steps{
                git branch: "master"
                url:  "https://github.com/anjilinux/my-project-mlops-with-jenkins.git"
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

        // Optional: Add stages for linting, building Docker images, or deployment to production
    }
}
