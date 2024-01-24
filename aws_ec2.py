import boto3

class ec2:
    def __init__(self, instance):
        self.instance = instance
    global resource_ec2
    resource_ec2 = boto3.client("ec2")

    def create(self):
        try:
            print('Creating')
            resource_ec2.run_instances(
                ImageId=self.instance.get("ImageId", "ami-05b456c21fa3bfe7f"),
                MaxCount=1,
                MinCount=1,
                InstanceType=self.instance.get("InstanceType", "t2.micro"),
                # Hard-coded KeyName for testing
                KeyName=self.instance.get("KeyName", "vockey"),

            )
            print("Instance creation successful")

        except Exception as e:
            print(f"Error creating instance: {e}")

    def terminate(self):

        if self.instance==None:
            print("Please enter an instance")

        try:
            resource_ec2.terminate(
                InstanceIds=[
                    self.instance.get("Id")
                ]
            )
            print("instance with id "+str(self.instance.id))
        except Exception as e:
            print(e)

    def discribe(self):
        if self.instance == None:
            print("Please enter an instance")
        try:
            res=resource_ec2.describe_instances(
            )
            print(res)
        except Exception as e:
            print(e)