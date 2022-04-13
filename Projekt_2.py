import random

space = "=" * 70
number = str(random.randint(1000, 9999))
moves = 1

def scan(num, bans) -> bool:
    for ban in bans:
        if ban == num:
            return False
    return True


def move() -> None:
    print(space)
    n = input(">>> ")
    if n == "exit":
        print(f"This is the number: {number}")
        print(space)
        print("You lost")
        exit()
    while len(n) != 4 or not n.isnumeric():
        print("Number must have 4 digits and it must contain only numbers")
        print(space)
        n = input(">>> ")
    count = -1
    cow, bull = 0, 0
    bansa = list()
    bansb = list()
    for digit in number:
        count += 1
        if digit == n[count]:
            bull += 1
            bansa.append(count)
            bansb.append(count)
    counta = -1
    for digita in n:
        counta += 1
        if scan(counta, bansa):
            countb = -1
            for digitb in number:
                countb += 1
                if scan(countb, bansb) and digita == digitb:
                    cow += 1
                    bansb.append(countb)
                    break
    bulls, cows = "s", "s"
    if bull == 1:
        bulls = ""
    if cow == 1:
        cows = ""
    print(f"{bull} bull{bulls}, {cow} cow{cows}")
    if bull == 4:
        return False
    else:
        return True

print("Hi there!")
print(space)
print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
print(space)
print("Type \"exit\" to exit")
print(space)
print("Enter a number:")
while move():
    moves += 1
print(space)
es = "es"
if moves == 1:
    es =""
print(f"Correct, you've guessed the right number\nin {moves} guess{es}!")
print(space)
if moves == 1:
    phrase = "almost impossible"
elif moves < 5:
    phrase = "pretty lucky"
elif moves < 13:
    phrase = "great"
else:
    phrase = "not so good, but you'll be lucky next time"
print(f"That's {phrase}!")