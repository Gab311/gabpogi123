import random
import requests
from pyfiglet import figlet_format
import time
import sys

def randomized_number():
    return random.randint(0, 10)


def gab_program(msg, webhook):
    print(figlet_format("gab pogi")
    while True:
        try:
            data.requests.post(webhook, json={"content": msg})
        except:
            print("bad webhook %s" $ (webhook))
            wait(5)
            sys.exit()
            
