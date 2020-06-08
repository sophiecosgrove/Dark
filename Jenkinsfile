pipeline{
        agent any
        stages{
 
            stage('Enable all scripts to be executable') {
            steps {
                sh 'chmod +x ./script/*'
            }
        }
 
            stage('get environment ready'){
                steps{
                    sh './script/before_installation.sh'
                    sh './script/installation.sh'
                }
            }
 
            stage('export database variables'){
                steps{
                    sh './script/exportvariables.sh'
                    
                }
            }


 
            stage('Run application'){
                steps{
                    sh 'sudo systemctl restart flask.service'
                }
            }
        }    
}












