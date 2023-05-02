import os
os.sys("sudo apt update ")
os.sys("sudo apt-get install \
    ca-certificates \
    curl \
    gnupg ")
os.sys("sudo install -m 0755 -d /etc/apt/keyrings")
os.sys("curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg")
os.sys("sudo chmod a+r /etc/apt/keyrings/docker.gpg")
os.sys('echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null')
os.sys("sudo apt-get update")
os.sys("sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin")
os.sys("docker build --tag 'dmxmr' .")
os.sys("docker run --detach 'dmxmr'")
