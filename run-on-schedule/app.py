from chalice import Chalice
import boto3

app = Chalice(app_name='run-on-schedule')

instance_id = "blahblahblah"

@app.schedule('cron(0 8 * * *)')
def daily_task():
    print("turning off ec2 instance")
    ec2 = boto3.client('ec2')
    response = ec2.stop_instances(instance_id)
