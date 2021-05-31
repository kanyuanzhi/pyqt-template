import random
from time import sleep


def main():
    consuming_time = random.randint(2000, 3000)
    sleep(consuming_time/1000.0)
    value = random.randint(1, 10)
    print(value)
    return value
