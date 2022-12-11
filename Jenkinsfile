pipeline {
    agent any

    stages {
        stage('git clone & build') {
            steps {
                parallel(

                    a: {
//                         sleep(10)
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
