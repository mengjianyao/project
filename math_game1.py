from random import  randint, choice

def exam():
    cmds = {'+': lambda  x, y : x + y, '-': lambda x, y: x - y}
    nums = [randint(0 , 100) for i in range(2)]
    nums.sort(reverse=True)
    op = choice('+-')
    result = cmds[op](*nums)

    prompt = '%s %s %s = ' % (nums[0], op , nums[1])
    counter = 0
    while counter < 3:
        try:
            answer = int(input(prompt))
        except:
            print('输入有误,请重新输')
            continue
        if answer == result:
            print('非常棒!!!')
            break

        print('不对哦!!!')
        counter += 1
    else:
        print('正确答案是: %s%s' % (prompt, result))


def main():
    while True:
        exam()
        try:
            yn = input('还要继续吗(y/n)?').strip()[0]
        except IndexError:
            yn = 'y'
        except (KeyboardInterrupt,EOFError):
            yn = 'n'

        if yn in 'nN':
            print('\nBYE-BYE')
            break

if __name__ == '__main__':
    main()
