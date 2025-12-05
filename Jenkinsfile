// pipeline {
//     agent any

//     stages {
//         stage('Checkout Code') {
//             steps {
//                 checkout scm
//             }
//         }

//         stage('Execute Code') {
//             steps {
//                 echo "Running Python Script..."
//                 bat "C:\\Users\\sakha\\AppData\\Local\\Programs\\Python\\Python311\\python.exe extract.py"
//             }
//         }
//     }

//     post {
//         success {
//             echo 'Pipeline completed successfully!'
//         }

//         failure {
//             echo 'Pipeline failed!'
//         }
//     }
// }


// scripted

node {

    try{
    stage('checkout code'){
        checkout scm

    }
    stage('extract code'){

        bat "C:\\Users\\sakha\\AppData\\Local\\Programs\\Python\\Python311\\python.exe extract.py"

    }
    }catch(err){
        echo "Error: ${err}"
}
finally{
    echo "Pipeline finished"
}
}