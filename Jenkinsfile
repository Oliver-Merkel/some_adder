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

        stage('vcs') {
            steps {
                sh '''
                # git clone https://github.com/Oliver-Merkel/some_adder.git
                cd some_adder
                ls -la
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Testing...'
                sh '''
                mkdir -p build
                echo ok > build/$BUILD_FILE_NAME
                '''
            }
        }
        
        stage('Python') {
            steps {
                withDockerContainer('safesecurity/pytest') {
                    sh '''
                    python --version
                    ls -la
                    cd some_adder
                    python -m pytest -v --junitxml=result.xml
                    python -m doctest -v adder.py
                    '''
                }
            }
        }
    }
    
    post {
        success {
            archiveArtifacts artifacts: 'some_adder/result.xml', followSymlinks: false
            junit stdioRetention: '', testResults: 'some_adder/result.xml'
        }
    }
}
