pipeline {
    agent any

    stages {
        stage('Contruyendo nueva versión') {
            steps {
                echo 'Construyendo la nueva versión...'
            }
        }
    }

    post {
        success {
            script {
                withCredentials([string(credentialsId: 'SLACK_WEBHOOK_URL', variable: 'WEBHOOK')]) {
                    sh """
                    curl -X POST -H 'Content-type: application/json' \\
                    --data '{"text": "✅ Jenkins: La nueva versión se ha subido correctamente."}' \\
                    \$WEBHOOK
                    """
                }
            }
        }
        failure {
            script {
                withCredentials([string(credentialsId: 'SLACK_WEBHOOK_URL', variable: 'WEBHOOK')]) {
                    sh """
                    curl -X POST -H 'Content-type: application/json' \\
                    --data '{"text": "❌ Jenkins: La subida de la nueva versión ha fallado."}' \\
                    \$WEBHOOK
                    """
                }
            }
        }
    }
}
