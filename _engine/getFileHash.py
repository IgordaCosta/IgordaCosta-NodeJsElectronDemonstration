import hashlib
 

def getFileHash(filename):
    md5_hash = hashlib.md5()
    try:
        with open(filename,"rb") as f:
            # Read and update hash in chunks of 4K
            for byte_block in iter(lambda: f.read(4096),b""):
                md5_hash.update(byte_block)
                ouput = md5_hash.hexdigest()
    except FileNotFoundError:
        ouput = filename
        return ouput