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
