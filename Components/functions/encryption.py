import os
import hashlib
from Crypto.Cipher import AES, DES, DES3 ARC2
from Crypto import Random
from Crypto.Hash import SHA256

#AES Encryption
def encrypt(key, filename):
    chunksize =64 * 1024
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = Random.new().read(16)
    key = SHA256.new(key.encode('utf-8')).digest()
    encryptor = AES.new(key, AES.MODE_CBC, IV)
     
    with open(filename, 'rb') as infile:
        with open("enc.jpg", 'wb') as outfile:
            outfile.write(filesize.encode('utf-8'))
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk +=b' '* (16 - (len(chunk) % 16))

                outfile.write(encryptor.encrypt(chunk))
    outfile.close()
    return outfile


#DES Encryption
def des_encrypt(key, filename):
    chunksize =64 * 1024
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = Random.new().read(8)
    
    salt = '\x28\xAB\xBC\xCD\xDE\xEF\x00\x33'
    key = (hashlib.md5((key + salt).encode())).digest()
    dk = key[:8]

    encryptor = DES.new(dk, DES.MODE_OFB, IV)
     
    with open(filename, 'rb') as infile:
        with open("enc.jpg", 'wb') as outfile:
            outfile.write(filesize.encode('utf-8'))
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk +=b' '* (16 - (len(chunk) % 16))

                outfile.write(encryptor.encrypt(chunk))
    outfile.close()
    return outfile


#Triple DES Encryption
def des3_encrypt(key, filename):
    chunksize =64 * 1024
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = Random.new().read(8)
    
    salt = '\x28\xAB\xBC\xCD\xDE\xEF\x00\x33'
    key = (hashlib.md5((key + salt).encode())).digest()
    dk = key[:24]

    encryptor = DES3.new(dk, DES3.MODE_OFB, IV)
     
    with open(filename, 'rb') as infile:
        with open("enc.jpg", 'wb') as outfile:
            outfile.write(filesize.encode('utf-8'))
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk +=b' '* (16 - (len(chunk) % 16))

                outfile.write(encryptor.encrypt(chunk))
    outfile.close()
    return outfile


#RC2 Encryption
def rc2_encrypt(key, filename):
    chunksize =64 * 1024
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = Random.new().read(8)
    
    salt = '\x28\xAB\xBC\xCD\xDE\xEF\x00\x33'
    key = (hashlib.md5((key + salt).encode())).digest()
    dk = key[:8]
    
    encryptor = ARC2.new(dk, ARC2.MODE_OFB, IV)
     
    with open(filename, 'rb') as infile:
        with open("enc.jpg", 'wb') as outfile:
            outfile.write(filesize.encode('utf-8'))
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk +=b' '* (16 - (len(chunk) % 16))

                outfile.write(encryptor.encrypt(chunk))
    outfile.close()
    return outfile
  
