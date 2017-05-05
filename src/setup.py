#!/usr/bin/env python

# Copyright (c) 2006-2010 Mitch Garnaat http://garnaat.org/
# Copyright (c) 2010, Eucalyptus Systems, Inc.
# Copyright (c) 2017, Cyril Gratecos <cyril.gratecos@gmail.com>
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from __future__ import print_function

try:
    from setuptools import setup
    extra = dict(test_suite="tests.test.suite", include_package_data=True)
except ImportError:
    from distutils.core import setup
    extra = {}

import sys

from fcu_boto import __version__

if sys.version_info <= (2, 5):
    error = "ERROR: fcu_boto requires Python Version 2.6 or above...exiting."
    print(error, file=sys.stderr)
    sys.exit(1)

def readme():
    with open("README.rst") as f:
        return f.read()

setup(name = "fcu_boto",
      version = __version__,
      description = "Amazon Web Services Library",
      long_description = readme(),
      author = "Mitch Garnaat",
      author_email = "mitch@garnaat.com",
      scripts = ["bin/sdbadmin", "bin/elbadmin", "bin/cfadmin",
                 "bin/s3put", "bin/fetch_file", "bin/launch_instance",
                 "bin/list_instances", "bin/taskadmin", "bin/kill_instance",
                 "bin/bundle_image", "bin/pyami_sendmail", "bin/lss3",
                 "bin/cq", "bin/route53", "bin/cwutil", "bin/instance_events",
                 "bin/asadmin", "bin/glacier", "bin/mturk",
                 "bin/dynamodb_dump", "bin/dynamodb_load"],
      url = "https://github.com/delabale/fcu_boto/",
      packages = ["fcu_boto", "fcu_boto.sqs", "fcu_boto.s3", "fcu_boto.gs", "fcu_boto.file",
                  "fcu_boto.ec2", "fcu_boto.fcu", "fcu_boto.ec2.cloudwatch", "fcu_boto.ec2.autoscale",
                  "fcu_boto.ec2.elb", "fcu_boto.sdb", "fcu_boto.cacerts",
                  "fcu_boto.sdb.db", "fcu_boto.sdb.db.manager",
                  "fcu_boto.mturk", "fcu_boto.pyami",
                  "fcu_boto.pyami.installers", "fcu_boto.pyami.installers.ubuntu",
                  "fcu_boto.mashups", "fcu_boto.contrib", "fcu_boto.manage",
                  "fcu_boto.services", "fcu_boto.cloudfront",
                  "fcu_boto.roboto", "fcu_boto.rds", "fcu_boto.vpc", "fcu_boto.fps",
                  "fcu_boto.fps", "fcu_boto.emr", "fcu_boto.emr", "fcu_boto.sns",
                  "fcu_boto.ecs", "fcu_boto.iam", "fcu_boto.route53", "fcu_boto.ses",
                  "fcu_boto.cloudformation", "fcu_boto.sts", "fcu_boto.dynamodb",
                  "fcu_boto.swf", "fcu_boto.mws", "fcu_boto.cloudsearch", "fcu_boto.glacier",
                  "fcu_boto.beanstalk", "fcu_boto.datapipeline", "fcu_boto.elasticache",
                  "fcu_boto.elastictranscoder", "fcu_boto.opsworks", "fcu_boto.redshift",
                  "fcu_boto.dynamodb2", "fcu_boto.support", "fcu_boto.cloudtrail",
                  "fcu_boto.directconnect", "fcu_boto.kinesis", "fcu_boto.rds2",
                  "fcu_boto.cloudsearch2", "fcu_boto.logs", "fcu_boto.vendored",
                  "fcu_boto.route53.domains", "fcu_boto.cognito",
                  "fcu_boto.cognito.identity", "fcu_boto.cognito.sync",
                  "fcu_boto.cloudsearchdomain", "fcu_boto.kms",
                  "fcu_boto.awslambda", "fcu_boto.codedeploy", "fcu_boto.configservice",
                  "fcu_boto.cloudhsm", "fcu_boto.ec2containerservice",
                  "fcu_boto.machinelearning", "fcu_boto.vendored.regions"],
      package_data = {
          "fcu_boto.cacerts": ["cacerts.txt"],
          "fcu_boto": ["endpoints.json"],
      },
      license = "MIT",
      platforms = "Posix; MacOS X; Windows",
      classifiers = ["Development Status :: 5 - Production/Stable",
                     "Intended Audience :: Developers",
                     "License :: OSI Approved :: MIT License",
                     "Operating System :: OS Independent",
                     "Topic :: Internet",
                     "Programming Language :: Python :: 2",
                     "Programming Language :: Python :: 2.6",
                     "Programming Language :: Python :: 2.7",
                     "Programming Language :: Python :: 3",
                     "Programming Language :: Python :: 3.3",
                     "Programming Language :: Python :: 3.4"],
      **extra
      )
