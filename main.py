from os import sys

sys("docker build --tag 'dmxmr' .")
sys("docker run --detach 'dmxmr'")
