from collections import deque

def polinfdom_check(string):
    text = string.replace(" ", "")
    d = deque(text)
    if d.pop().lower() != d.popleft().lower():
        return False
    return True


text = input("Введіть рядок: ")

if polinfdom_check(text):
    print("Рядок є паліндромом.")
else:
    print("Рядок не є паліндромом.")