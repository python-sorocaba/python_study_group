import os

# You need install youtube-dl command first:
#
# sudo apt-get install youtube-dl

with open('links.txt') as fp:
    for line in fp:
        os.system('youtube-dl {}'.format(line.strip()))
