# import random
# num = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
# def randpass(n=8):
#     a = ' '
#     for i in range(n):
#         a += random.choice(num)
#     return a
# # if __name__ == '__main__':
# #     print(randpass(8))
#
#
# s1 = int(input('输入数字: '))
# re = randpass(s1)
# print(re)

# # if __name__ == '__main__':
# # #     randpass()


# import random
# def rand():
# num =
#
#
#
# s1 = int(input('your number: '))
# re = rand(s1)
# print(re)


from random import choice
from string import ascii_letters, digits
nums = ascii_letters + digits
def ranpass(n=8):
    b = ''
    for i in range(n):
        b += choice(nums)
    return b

sr = input('输入数字: ')

if sr == '':
    result = ranpass()
else:
    result = ranpass(int(sr))
print(result)

