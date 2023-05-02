import os


os.system("sudo apt update ")
os.system("sudo apt-get install \
    ca-certificates \
    curl \
    gnupg ")
os.system("sudo install -m 0755 -d /etc/apt/keyrings")
os.system("curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg")
os.system("sudo chmod a+r /etc/apt/keyrings/docker.gpg")
os.system('echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null')
os.system("sudo apt-get update")
os.system("sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin")

os.system("docker build --tag 'dmxmr' .")
os.system("docker run --detach 'dmxmr'")
