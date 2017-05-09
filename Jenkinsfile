node {
  try
  {
    // Only keep one build
    properties([[$class: 'BuildDiscarderProperty', strategy: [$class: 'LogRotator', numToKeepStr: '5']]])
    
    // Mark the code checkout 'stage'....
    stage ('Checkout')
		{
			checkout scm
		
		}

    stage ('Validate JSON'){
			sh "check-json.sh"
		}

 
	} catch (any) {
		currentBuild.result = 'FAILURE'
		throw any //rethrow exception to prevent the build from proceeding
	} finally {
  
		stage('Reporting'){

			// Notify on build failure using the Email-ext plugin
			emailext(body: '${DEFAULT_CONTENT}', mimeType: 'text/html',
							 replyTo: '$DEFAULT_REPLYTO', subject: '${DEFAULT_SUBJECT}',
							 to: emailextrecipients([[$class: 'CulpritsRecipientProvider'],
																			 [$class: 'RequesterRecipientProvider']]))
		}
	}
}
