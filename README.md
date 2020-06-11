# snapshotalyzer-30000
Demo project to manage AWS EC2 instance snapshots

### About

This project is a demo, and uses boto3 to manage AWS EC2 instance snapshots

### Configuring

shotty uses the configuration file created the AWS cli

`aws configure --profile shotty`


### Running

`pipenv run "python shotty/shotty.py <command> <subcommand> <--project=Project>"`

*command* is instances, volumes, or snapshots
*subcommand* depends on a command: (for instances) list, start, or stop, (for volumes) list, (for snapshots) list
*project* is optional

=============

added --profile option

$ python shotty/shotty.py --profile=shotty instances list
i-0e152c31937f0358a,t2.micro,us-east-1e,stopped,,Scorpio
i-00454c9df27399636,t2.micro,us-east-1e,stopped,,Scorpio
i-0759efc0dded5ac12,t2.micro,us-east-1e,stopped,,Scorpio

