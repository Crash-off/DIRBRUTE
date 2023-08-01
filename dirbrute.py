import requests
import sys

try:
    url = sys.argv[1]
    words = open(sys.argv[2], "r")
    for word in words.readlines():
        dirb = f"{urle}{palavra}"
        r = requests.get(dirb)
        s = r.status_code
        if s == 200:
            print("#--$ DIR: ", dirb)
        elif s == 403:
            print("#--# Forbidden:", dirb)
        elif s == 408:
            print("#--* Timeout", dirb)
except:
    print("* >> Error in some argument passed, use the correct form:\n./dirbrute.py url wordlist")
