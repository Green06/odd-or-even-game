import random

print("Hey Human , let's play odd or even")
num_type = input("odd or even??")

c_ip = random.randint(0, 10)
u_ip = int(input("enter any integers from 0 to 10: "))
print(f"machine's input: {c_ip}")
total = c_ip + u_ip;
if num_type == "even":
    if total % 2 == 0:
        print("you win")
    else:
        print("machine win")
else:
    if total % 2 == 1:
        print("you win")
    else:
        print("machine win")
