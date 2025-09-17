#!/usr/bin/env bash
set -e
set -u  # fail if variable is undefined
set -o pipefail  # fail if command before pipe fails

DEBIAN_CODENAME="${1}"
REPO_NAME="${2}"
JENKINSFILE="${LOCAL_GIT_REPOS}/${REPO_NAME}/Jenkinsfile"


# Build debian packaging on bookworm distribution
sed -i "s/value: \"\${JOB_NAME}\"/value: \"${REPO_NAME}\"/" "${JENKINSFILE}"
if ! grep -q 'name: "BRANCH"' "${JENKINSFILE}"; then
    sed -i "/.*PACKAGE.*/a \          string(name: \"BRANCH\", value: \"${DEBIAN_CODENAME}\")," "${JENKINSFILE}"
    sed -i "/.*BRANCH.*/a \          string(name: \"DISTRIBUTION\", value: \"wazo-dev-${DEBIAN_CODENAME}\")," "${JENKINSFILE}"
fi

# Tag docker image with bookworm
sed -i "s/:latest/:${DEBIAN_CODENAME}/g" "${JENKINSFILE}"
sed -i "s/wazoplatform\/\${JOB_NAME}/wazoplatform\/${REPO_NAME}/" "${JENKINSFILE}"
