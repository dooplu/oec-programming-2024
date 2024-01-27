import random

def add():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    ans = num1 + num2
    fake1 = ans + random.randint(1, 11)
    fake2 = ans - random.randint(1, 11)
    
    tuple = (f"{num1} + {num2} = ?", ans, fake1, fake2)
    
    return tuple

def sub():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    ans = num1 - num2
    fake1 = ans + random.randint(1, 11)
    fake2 = ans - random.randint(1, 11)
    
    tuple = (f"{num1} - {num2} = ?", ans, fake1, fake2)
    
    return tuple

def mult():
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    ans = num1 * num2
    fake1 = ans + random.randint(1, 11)
    fake2 = ans - random.randint(1, 11)
    
    tuple = (f"{num1} x {num2} = ?", ans, fake1, fake2)
    
    return tuple

def div():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    ans = num1 * num2
    fake1 = num2 + random.randint(1, 11)
    fake2 = num2 - random.randint(1, 11)
    
    tuple = (f"{ans} / {num1} = ?", num2, fake1, fake2)
    
    return tuple

