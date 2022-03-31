pipeline {
    agent {label 'agent_1'}
       
       
    stages {
        stage('Checkout the repo') {
            steps {
                cleanWs() 
                echo "checkout a repo"
                sh 'mkdir dekel'
                sh 'git clone https://github.com/dekelsaar/Dekel_Games.git dekel'

            }
        }
        stage('Build image') {
            steps {
                sh 'docker build -t dekelsaar/wogi:latest dekel'
            }
        }
        stage('Test') {
            agent{
                docker {
                    image 'dekelsaar/wogi:first'
                    reuseNode true
                }
            }
            steps {
                sh 'python3 dekel/app/MainScores.py'
                sh 'sleep 10'
                sh 'python3 dekel/Tests/e2e.py'


            }
        }
        stage('Terminate&Push') {
            steps {
                sh 'docker stop dekelsaar/wogi:first'
                
                script {
                    withCredentials([string(credentialsId: 'dekelsaar', variable: 'dockerhubcar')]) {
              }
                    sh 'docker push dekelsaar/wogi'
              }

            }
    
        } 
    }
}

