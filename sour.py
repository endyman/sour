#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import datetime
import dateutil.relativedelta
import shade
import sys

args = None
now = datetime.datetime.now()

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def get_cloud(cloudname):
    cloud = shade.openstack_cloud(cloud=cloudname)
    return cloud

def get_projects(cloud):
    projects = cloud.list_projects()
    project_names = []
    for project in projects:
        project_names.append(project.name)
    return project_names

def get_usage(cloud, projects, end=now, start=now + dateutil.relativedelta.relativedelta(months=-1)):
    usage = {}
    for project in projects:
        if project:
            usage[project] = cloud.get_compute_usage(project, start, end)
            usage[project].update(cloud.get_project(project))
    return usage

def output(usage):
    output_template = "Project: {name}, total_hours: {total_hours}, total_memory_mb_usage: {total_memory_mb_usage}"
    for property in args.property:
        output_template += ", {0}: {{{0}}}".format(property)

    for v in usage.values():
        print output_template.format(**v.toDict())

def main():
    global args
    parser = argparse.ArgumentParser(description='Process args')
    parser.add_argument('-v', '--verbose',
        help='turn on verbose logging', action="store_true" )
    parser.add_argument('-c', '--cloud', help='cloud name', required=True)
    parser.add_argument('-p', '--project', help='project name', required=False)
    parser.add_argument('-s', '--start', help='start_time', required=False)
    parser.add_argument('-e', '--end', help='end_time', required=False)
    parser.add_argument('--property', help='project property', required=False, action='append', default=[])

    try:
        args = parser.parse_args()
        cloud = get_cloud(args.cloud)
        if not args.project:
            projects = get_projects(cloud)
        else:
            projects = [args.project]
        usage = get_usage(cloud, projects)
        output(usage)
    except Exception as e:
        raise Usage(e)

if __name__ == "__main__":
    sys.exit(main())
