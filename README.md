# Simple Openstack Usage Report ###

```pip install -r requirements.txt```

## Basic Usage

```./soure.py -c <cloud-name>```

*cloud-name* is the name of your ```cloud.yaml``` cloud definiton.

## Help

```./sour.py -h                                                         [✓][101s](git)-[master][]
usage: sour.py [-h] [-v] -c CLOUD [-p PROJECT] [-s START] [-e END]
               [--property PROPERTY] [--csv]

Process args

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         turn on verbose logging
  -c CLOUD, --cloud CLOUD
                        cloud name
  -p PROJECT, --project PROJECT
                        project name
  -s START, --start START
                        start_time
  -e END, --end END     end_time
  --property PROPERTY   project property
  --csv                 format output as CSV
```
