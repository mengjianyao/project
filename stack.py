stack = []


def push_it():
    data = input('数据: ').strip()
    if data:
        stack.append(data)
    else:
        print('数据为空!')

def pop_it():
    if stack:
        print('从栈中弹出: %s' %  stack.pop())
    else:
        print('空栈')

def view_it():
    print('stack')


def show_menu():
    prompt = """
(0) 压栈
(1) 出栈
(2) 查询
(3) 退出
请选择(0/1/2/3): """


    while True:
        choice = input(prompt).strip()

        if choice not in ['0','1','2','3']:
            print('无效输入,请重新输入')
            continue

        if  choice == '0':
            push_it()
        elif   choice == '1':
            pop_it()
        elif choice == '2':
            view_it()
        else:
           print('bey-bey')
           break


if __name__ == '__main__':
    show_menu()
