#!/usr/bin/env bash
set -e
set -u  # fail if variable is undefined
set -o pipefail  # fail if command before pipe fails

REPO_NAME="${1}"
ORGANIZATION="${2:-wazo-platform}"
REPO_PATH="${LOCAL_GIT_REPOS}/${REPO_NAME}"
BRANCH_NAME='bullseye'
SCRIPT_DIR=$(pwd)

"${SCRIPT_DIR}"/manage-debian-branch.py create -o "${ORGANIZATION}" -r "${BRANCH_NAME}" "${REPO_NAME}" || true

pushd "${REPO_PATH}" > /dev/null
git fetch
git checkout "${BRANCH_NAME}"

"${SCRIPT_DIR}"/update-jenkinsfile-bullseye.sh "${REPO_NAME}"

git add Jenkinsfile
git commit --no-verify -m 'DO NOT MERGE: build package for bullseye distro'
git push --set-upstream origin "${BRANCH_NAME}"
popd > /dev/null

"${SCRIPT_DIR}"/jenkins-create-bullseye-job.py --doit "${REPO_NAME}"

"${SCRIPT_DIR}"/manage-debian-branch.py protect -o "${ORGANIZATION}" -r "${BRANCH_NAME}" "${REPO_NAME}" || true
