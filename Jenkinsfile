pipeline {
   agent any

   stages {
      stage('git_checkout') {
         steps {
          checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'github_key', url: 'https://github.com/rohitbhakaregit/kubernetes_cicd.git']]])
               }
                      }
      
      stage ('build_docker_image') {
          steps{
               sh label: '', script: 'docker build -t 1383/jenkins_docker:${BUILD_NUMBER}  flask-app/. '
               
               }
                           }
      stage ('Push_docker_image') {
          steps{
               sh label: '', script: 'docker push 1383/jenkins_docker:${BUILD_NUMBER} '
               }
                           }

      
      stage ('delete_dir') {
          steps{
            deleteDir()
               }
                           }
                          
                           
                           
                           
          }
}
