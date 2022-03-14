import random
from replit import db

def keygenupdate():
    db["todayskey"] = random.randint(1, 999999999999)

