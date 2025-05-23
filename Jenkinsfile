pipeline {
    agent any

    stages {
        stage('Verificar cambios en app.py') {
            steps {
                script {
                    def cambios = sh(script: "git diff --name-only HEAD~1 HEAD", returnStdout: true).trim()
                    if (cambios.contains('app.py')) {
                        echo "Se detectaron cambios en app.py"
                        
                    } else {
                        echo "No hay cambios en app.py. Terminando ejecución."
                        currentBuild.result = 'SUCCESS'
                        return
                    }
                }
            }
        }
    }
}
