pipeline{
    agent any
    environment{
        VENV='venv'
    }
    stages{
        stage('checkout'){
            steps{
                git branch: 'main', url: 'https://github.com/Asthme256/june25-classdemo2.git' 

            }
        }
        stage('setup virtual enviroment'){
            steps{
                sh '''
                python3 -m venv $VENV
                . $VENV/bin/activate
                pip install -r requirements.txt
            '''
            }
        }
        stage('run tests'){
            steps{
                sh '''
                . $VENV/bin/activate
                pytest
            '''
            }
        }
    }
}