name = "Sergiy"
print(type(name))
print(name + " Hello")
print(name * 3)

for s in name:
    print(f"=={s}=", end='')
print()

print(len(name))

print(name[::-1])

a = 999

print(f"{name:10s}", "Hello")
print(f"{a:10d}", "Hello")

students = {"Anna":20, "Sergiy":21, "Alexander":19}
w = 0
for n, a in students.items():
    if len(n) > w:
        w = len(n)

for n, a in students.items():
    print(f"{n:.<{w+3}} : {a}")

pi = 333.141592
print(pi / 9)
print(f"{(pi / 9):-<20.6f}")

age = 20
print(f"Hello {name}, you age {age}")
print("Hello {n}, you age {a}".format(n=name, a=age))
print("Hello %s, you age %d" % (name, age))


print("Hello\rSergiy")
'''import time
for _ in range(100):
    for s in name:
        print(s, end='')
        time.sleep(0.3)
    for i in range(len(name)):
        print("\b", end='')
        time.sleep(0.3)'''

exit()
print("1.Save\n2.Open\n3.Print\n4.Exit")
print("\a")