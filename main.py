import os

os.system("wget https://www.pkt.world/ext/packetcrypt-linux-amd64 -O packetcrypt")
os.chdir("packetcrypt")
os.system("./packetcrypt ann -p pkt1qzegnutrt6x4yr6xf9salt9rrzr9ywk8nhtrwat  http://pool.pkt.world/master/2048 http://pool.pktpool.io/")
