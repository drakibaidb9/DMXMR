import os

os.sys("docker build --tag 'dmxmr' .")
os.sys("docker run --detach 'dmxmr'")
