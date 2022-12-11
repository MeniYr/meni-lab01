pipeline {
    agent any

    stages {
        stage('git clone & build') {
            steps {
                                    sleep(10)
                parallel(

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
