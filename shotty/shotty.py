import boto3
#import sys
import click


session = boto3.Session(profile_name='shotty')
ec2 = session.resource('ec2')

@click.command()
# decorator, decorates or wrapps your function
# we are handing off control of our function to click which will decide when and how it's called
def list_instances():
    "List EC2 instances"
    print(list(ec2.instances.all()))
    for i in ec2.instances.all():
        print(','.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name)))
    return


if __name__ == '__main__':
    #print(sys.argv)
    list_instances()

