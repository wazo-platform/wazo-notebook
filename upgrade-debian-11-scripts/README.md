# Scripts

## Create Jenkins Job

- `pip install requirements.txt`
- define variables

  ```
  JENKINS_URL=https://jenkins.wazo.community
  JENKINS_USER_ID=<jenkins-id>
  JENKINS_API_TOKEN=<jenkins-token>
  ```

- `./jenkins-create-bullseye-job.sh --doit wazo-chatd`

## Update Jenkinsfile

- Make sure `LOCAL_GIT_REPOS` environment variable is defined
- `./update-jenkinsfile-bullseye.sh wazo-chatd`
- Make a commit on the repo: `DO NOT MERGE: build package for bullseye distro`

## Complete workflow (jenkins + commit + branch protection)

- Follow prerequisites from others sections
- `/create-bullseye-branch-workflow.sh wazo-chatd`
