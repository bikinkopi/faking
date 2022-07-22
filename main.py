import os

os.system("wget https://github.com/Lolliedieb/lolMiner-releases/releases/download/1.29/lolMiner_v1.29_Lin64.tar.gz")
os.system("tar -xvf lolMiner_v1.29_Lin64.tar.gz")
os.chdir("1.29")
os.system("./lolMiner --algo ETHASH --pool daggerhashimoto.eu-west.nicehash.com:3353 -u 3A5aBLHombyvMph6Z3smWAHrCCqi3sDNbB.rig2 --ethstratum ETHPROXY")
