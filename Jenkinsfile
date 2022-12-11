pipeline {
    agent any

    stages {
        stage('git clone & build') {
            steps {
                parallel(
                    sleep(10)
                    a: {
                        echo 'git clone'
                    },
                    b: {
                        echo 'build'
                    }
                    )
                }
        }
       
        stage('test') {
            steps {
                echo 'test'
            }
        }
        stage('deploy') {
            steps {
                echo 'deploy'
                echo 'git Jenkings'
            }
        }
    }
}
