import getpass

dict = {}

def useradd():
    while True:
        rester = input('请输入新用户名: ').strip()
        if rester in dict:
            print('已存在,请重新注册: ')
            break
        password = input('请输入密码: ').strip()
        dict.update({rester: password})
        print('注册成功')
        break


def login():
    while True:
        n = input('请输入用户名: ').strip()
        p = input('请输入密码: ').strip()
        if n in dict and p == dict.get(n):
            print('登录成功')
            break
        else:
            print('用户名或密码错误,请重新输入')
            break



def chenxu():
    cmds = {'0': useradd, '1':login}
    prompt  = """
(0) 注册
(1) 登录
(2) 退出
请选择(0/1/2): """

    while True:
        choice = input(prompt).strip()
        if choice not in ['0', '1','2']:
            print('无效的选择,请重新选择')
            continue

        if choice == '0':
            useradd()

        elif choice == '1':
            login()
        else:
            print('bey-bey')
            break


if __name__ == '__main__':
    chenxu()





