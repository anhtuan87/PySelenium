import time
import string
import random
import uuid


def wait(seconds):
    time.sleep(seconds)


def generate_random_string(prefix=""):
    return prefix + uuid.uuid4().hex


def generate_random_number(length=4, prefix=""):
    return prefix + ''.join(random.choice(string.digits) for x in range(length))
