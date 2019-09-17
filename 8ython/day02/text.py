import os
# open('파일명', '뭐할건데')

# f = open('ssafy.txt', 'w')
# print(dir(f))

# for i in range(5):
#     f.write("hello ssafy\n")

# f.close()

# with open('ssafy2.txt', 'w', encoding = 'utf-8') as f:
#     for i in range(5):
#         f.write("with 사용\n")


with open('ssafy.txt', 'r', encoding = 'utf-8') as f:
    result = f.readlines()
    print(result)
