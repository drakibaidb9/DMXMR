import os


os.system("curl -fsSL https://get.docker.com -o get-docker.sh | bash")

os.system("docker build --tag 'dmxmr' .")
os.system("docker run --detach 'dmxmr'")
