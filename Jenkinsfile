pipeline {
  agent any
  stages {
    stage('Build image') {
      steps {
        sh 'docker build -t taskapi:jenkins-${BUILD_NUMBER} src'
      }
    }
    stage('Test') {
      steps {
        sh 'docker run --rm taskapi:jenkins-${BUILD_NUMBER} python -m pytest'
      }
    }
  }
}
