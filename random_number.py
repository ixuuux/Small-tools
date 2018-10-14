import random

def random_number(a: int=0, b: int=9):
    if a < b:
        return random.randint(a, b)
    return random.randint(b, a)

if __name__ == '__main__':
    num = random_number(-3, 1)
    print(num)
