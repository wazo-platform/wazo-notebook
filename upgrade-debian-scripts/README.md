# Scripts

## Create Jenkins Job

- `pip install requirements.txt`
- define variables

  ```shell
  JENKINS_URL=https://jenkins.wazo.community
  JENKINS_USER_ID=<jenkins-id>
  JENKINS_API_TOKEN=<jenkins-token>
  ```

- `./jenkins-create-job.sh <debian-codename> --doit wazo-chatd`

## Update Jenkinsfile

- Make sure `LOCAL_GIT_REPOS` environment variable is defined
- `./update-jenkinsfile.sh <debian-codename> wazo-chatd`
- Make a commit on the repo: `DO NOT MERGE: build package for <debian-codename> distro`

## Complete workflow (jenkins + commit + branch protection)

- Follow prerequisites from others sections
- `/create-branch-workflow.sh wazo-chatd`
