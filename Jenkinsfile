pipeline 
{
   agent any
    environment 
    {
    registry = "1383/jenkins_docker"
    registryCredential = 'hub_id'
    dimage= ""
    }

   stages 
   {
      stage('git_checkout') 
      {
       steps 
         {
          checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'github_key', url: 'https://github.com/rohitbhakaregit/kubernetes_cicd.git']]])
         }
       }

      stage('Building image') 
       {
        steps
         {
          script 
             {
             dimage=docker.build registry + ":$BUILD_NUMBER","flask-app/"
             }
          }
        }
      stage(' image Push') 
       {
        steps
         {
          script 
           {
            docker.withRegistry('',registryCredential)
              {
               dimage.push()
              }
            }
          }
        }
      stage ('Helm_deploy') 
      {
        steps
          {
            sh label: 'helm', script: 'helm install  k8s-deploy --set appVersion=${BUILD_NUMBER} ./helm-deploy || helm upgrade  k8s-deploy --set appVersion=${BUILD_NUMBER} ./helm-deploy'
          }
      }
   }
}


//for dokcer either configure docker agent or store your credentials at /var/lib/jenkins/.docker/config.json
