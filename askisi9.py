import hashlib
import requests


def showHax(file):
    resp = requestReport(file)
    if resp["response_code"] != 1:
        print(resp["verbose_msg"])
    else:
        print("Ο αριθμός τον antivirus που βρήκαν το αρχείο μολυσμένο είναι:", resp["positives"])
        return resp["positives"]


def hashFile(file):
    BLOCK_SIZE = 65536  # The size of each read from the file
    file_hash = hashlib.sha256()  # Create the hash object, can use something other than `.sha256()` if you wish
    with open(file, 'rb') as f:  # Open the file to read it's bytes
        fb = f.read(BLOCK_SIZE)  # Read from the file. Take in the amount declared above
        while len(fb) > 0:  # While there is still data being read from the file
            file_hash.update(fb)  # Update the hash
            fb = f.read(BLOCK_SIZE)  # Read the next block from the file
    return file_hash.hexdigest()


def requestReport(file):
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': '39149b2be190b418d11fed86481abf0c4584f988e0cd89a861d54ebc29f660d9', 'resource': hashFile(file)}
    response = requests.get(url, params=params)
    return response.json()

#showHax("C:\\Users\\Desktop\\test.txt")
