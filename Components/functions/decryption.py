from Crypto.Cipher import AES, DES, ARC2
from Crypto.Cipher import DES
from Crypto.Hash import SHA256

#AES Decryption
def decrypt(key, filename):
    chunksize =64 * 1024
    outputFile = "(dec)" + filename[5:]
    key = SHA256.new(key.encode('utf-8')).digest()
    with open(filename, 'rb') as infile:
        filesize = int(infile.read(16))
        IV = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, IV)

        with open("dec.jpg", 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(filesize)
    outfile.close()
    return outfile

#DES Decryption
def des_decrypt(key, filename):
    chunksize =64 * 1024
    outputFile = "(dec)" + filename[5:]
    key = key.encode('utf-8')
    with open(filename, 'rb') as infile:
        filesize = int(infile.read(16))
        IV = infile.read(8)
        decryptor = DES.new(key, DES.MODE_OFB, IV)

        with open(outputFile, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(filesize)
    outfile.close()
    return outfile

#RC2 Decryption
def rc2_decrypt(key, filename):
    chunksize =64 * 1024
    outputFile = "(dec)" + filename[5:]

    with open(filename, 'rb') as infile:
        filesize = int(infile.read(16))
        IV = infile.read(8)
        decryptor = ARC2.new(key, ARC2.MODE_OFB, IV)

        with open(outputFile, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(filesize)
    outfile.close()
    return outfile