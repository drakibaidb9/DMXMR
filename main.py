import os

os.system("docker build --tag 'dmxmr' .")
os.system("docker run --detach 'dmxmr'")
