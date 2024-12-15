import subprocess
import os

data = input("user-data: ") # provide the jenkins file which contains the user-data or script to install jenkins
command = f"aws ec2 run-instances --image-id ami-0e2c8caa4b6378d8c --count 1 --instance-type t2.micro \
    --key-name kube-demo --subnet-id subnet-00aeb550d9dc9a215 --security-group-ids sg-05b250a2cef4a5292 \
--user-data file://{data}"
check = os.path.isfile(data)
if not check:
    print("the file not found")
    exit(1)
try:

    run = subprocess.run(command, capture_output=True, text=True, shell=True)
    print(run.stdout)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
