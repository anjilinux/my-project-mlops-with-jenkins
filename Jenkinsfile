pipeline {
    agent any
    stages{
        stage("checkout from git "){
            steps{
                git branch: "master"
                url:  "https://github.com/anjilinux/my-project-mlops-with-jenkins.git"
            }
        }
    }
}


