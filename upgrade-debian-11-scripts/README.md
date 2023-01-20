# Scripts

## Create Jenkins Job

- `pip install requirements.txt`
- define variables

  ```
  JENKINS_URL=https://jenkins.wazo.community
  JENKINS_USER_ID=<jenkins-id>
  JENKINS_API_TOKEN=<jenkins-token>
  ```

- `./jenkins-create-bullseye-job --doit wazo-chatd`

### Use Jenkins Job

Make a commit on the repo: `DO NOT MERGE: build package for bullseye distro`
```diff
diff --git a/Jenkinsfile b/Jenkinsfile
index 050ba47..317a9bf 100644
--- a/Jenkinsfile
+++ b/Jenkinsfile
@@ -12,18 +12,20 @@ pipeline {
     stage('Debian build and deploy') {
       steps {
         build job: 'build-package-no-arch', parameters: [
-          string(name: 'PACKAGE', value: "${JOB_NAME}"),
+          string(name: 'PACKAGE', value: "wazo-chatd"),
+          string(name: 'BRANCH', value: "bullseye"),
+          string(name: 'DISTRIBUTION', value: "wazo-dev-wip-bullseye"),
         ]
       }
     }
     stage('Docker build') {
       steps {
-        sh "docker build --no-cache -t wazoplatform/${JOB_NAME}:latest ."
+        sh "docker build --no-cache -t wazoplatform/${JOB_NAME}:bullseye ."
       }
     }
     stage('Docker publish') {
       steps {
-        sh "docker push wazoplatform/${JOB_NAME}:latest"
+        sh "docker push wazoplatform/${JOB_NAME}:bullseye"
       }
     }
   }
```
