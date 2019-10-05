import hashlib
import string
import random


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


loop = True
count = 0

print("Υπολογίζεται ο μέσος όρος παρακαλώ περιμένετε...")
for x in range(0, 19):

    loop = True
    while loop:
        result = hashlib.sha256(id_generator().encode('utf-8')).hexdigest()
        firstTwo = result[:2]
        lastThree = result[-3:]
        count += 1
        if firstTwo == "a3" and lastThree == "fff":
            loop = False

print(count / 20)
