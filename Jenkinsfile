pipeline {
    agent any

    environment {
        BUILD_FILE_NAME = 'result.xml'
    }

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        
        stage('Python') {
            steps {
                withDockerContainer('python_pytest') {
                    sh '''
                    python --version
                    ls -la
                    python -m pytest -v --junitxml=result.xml
                    python -m doctest -v adder.py
                    '''
                }
            }
        }
    }
    
    post {
        success {
            archiveArtifacts artifacts: 'result.xml', followSymlinks: false
            junit stdioRetention: '', testResults: 'result.xml'
        }
    }
}
