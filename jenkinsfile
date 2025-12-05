pipeline {
    agent any

    stages{
        stage('checkout code'){
            steps{
             checkout scm
            }
        }
         stage('execute  code'){
            steps{
             bat "C:\\Users\\sakha\\AppData\\Local\\Programs\\Python\\Python311\\python.exe extract.py"
            }
        }
    }
}