import os

# print(os.listdir())

# os.rename("hello.py", "dog.py")
# print(os.listdir())

# os.rename("dog.py", "hello.py")
# print(os.listdir())

# print(os.system('ls'))
os.chdir('report')

for i in range(100):
    os.system(f"touch report{i}.txt")

input()

for i in os.listdir():
    os.rename(i, "samsung_"+i)

input()


for i in os.listdir():
    os.rename(i, i.replace("samsung", "ssafy"))

input()

for i in range(100):
    os.system(f"rm ssafy_report{i}.txt") 