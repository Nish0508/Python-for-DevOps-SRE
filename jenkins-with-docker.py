import subprocess

command_docker = subprocess.run(["docker run --name jenkins --publish 8080:8080 --detach jenkins/jenkins:lts"],
                                shell=True)
command_pwd = subprocess.run(["pwd"], shell=True)

print(command_pwd.stdout)
print(command_docker.stdout)
