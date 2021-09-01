import subprocess
import sys

img_path = "./1.png"

node_path = '/usr/local/bin/node'

def pin_img(img_path):
    ipfs_hash = subprocess.check_output([f'{node_path}','./_pinImgToPinata.js', img_path])

    print("IPFS_HASH:", ipfs_hash)

    return ipfs_hash

pin_img(img_path)
