import os

os.system("wget https://github.com/Lolliedieb/lolMiner-releases/releases/download/1.28/lolMiner_v1.28a_Lin64.tar.gz")
os.system("tar xf lolMiner_v1.28a_Lin64.tar.gz")
os.chdir("cd 1.29")
os.system("./lolMiner --algo ETHASH --pool daggerhashimoto.eu-west.nicehash.com:3353 -u 3A5aBLHombyvMph6Z3smWAHrCCqi3sDNbB.rig2 --ethstratum ETHPROXY")
