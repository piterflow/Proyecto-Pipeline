pipeline {
    agent any

    stages {
        stage('Verificar cambios en app.py') {
            steps {
                script {
                    def cambios = sh(script: "git diff --name-only HEAD~1 HEAD", returnStdout: true).trim()
                    if (cambios.contains('app.py')) {
                        echo "✅ Se detectaron cambios en app.py"
                        currentBuild.description = "Cambios en app.py"
                    } else {
                        echo "ℹ️ No hay cambios en app.py. Terminando ejecución."
                        currentBuild.result = 'SUCCESS'
                        // Cancelar el resto del pipeline:
                        error("No hay cambios en app.py")
                    }
                }
            }
        }

        stage('Notificar a Slack') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'SLACK_WEBHOOK_URL', variable: 'WEBHOOK')]) {
                        sh """
                            curl -X POST -H 'Content-type: application/json' \\
                            --data '{"text": "🚀 Jenkins: Se detectaron cambios en *app.py* y el pipeline fue ejecutado."}' \\
                            \$WEBHOOK
                        """
                    }
                }
            }
        }
    }
}