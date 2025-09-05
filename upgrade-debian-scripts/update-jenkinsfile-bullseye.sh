#!/usr/bin/env bash
set -e
set -u  # fail if variable is undefined
set -o pipefail  # fail if command before pipe fails

REPO_NAME="${1}"
JENKINSFILE="${LOCAL_GIT_REPOS}/${REPO_NAME}/Jenkinsfile"

# Build debian packaging on bullseye distribution
sed -i "s/value: \"\${JOB_NAME}\"/value: \"${REPO_NAME}\"/" "${JENKINSFILE}"
sed -i '/.*PACKAGE.*/a \          string(name: "BRANCH", value: "bullseye"),' "${JENKINSFILE}"
sed -i '/.*BRANCH.*/a \          string(name: "DISTRIBUTION", value: "wazo-dev-wip-bullseye"),' "${JENKINSFILE}"

# Tag docker image with bullseye
sed -i 's/:latest/:bullseye/g' "${JENKINSFILE}"
