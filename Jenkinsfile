pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''script {
          docker.build registry + ":$BUILD_NUMBER"
        }'''
        }
      }

    }
  }