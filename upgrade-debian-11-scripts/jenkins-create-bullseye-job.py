#!/usr/bin/env python3

import argparse
import os

import jenkins
from lxml import etree

server = jenkins.Jenkins(
    os.getenv("JENKINS_URL"),
    username=os.getenv("JENKINS_USER_ID"),
    password=os.getenv("JENKINS_API_TOKEN"),
)
user = server.get_whoami()
version = server.get_version()


parser = argparse.ArgumentParser()
parser.add_argument("--doit", action="store_true")
parser.add_argument("project")
args = parser.parse_args()

master = args.project
bullseye = f'{args.project}-bullseye'

xml_raw = server.get_job_config(master)
xml = etree.fromstring(xml_raw.encode())

branch = xml.xpath('definition/scm/branches/hudson.plugins.git.BranchSpec/name')[0]
branch.text = "bullseye"

print(f'* branch: {branch.text}')
print('')


if args.doit:
    output = etree.tostring(xml)
    server.create_job(bullseye, output.decode())
    server.build_job(bullseye)
