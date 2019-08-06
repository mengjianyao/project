import  getpass

userdb = {}

def register():
    username = input('用户名: ').strip()
    if username == '':
        print('用户名不能为空')
    elif not username.isalnum():
        print('用户名只能包含字母和数字')
    elif username in userdb:
        print('用户名已存在')
    else:
        password = input('密码')
        userdb[username] = password
        print('\033[32;1m注册成功\033[0m')

def login():
     username = input('用户名: ').strip()
     password = getpass.getpass('密码: ').strip()
     if userdb.get(username) != password:
         print('\033[31;1m登录失败\033[0m')
     else:
         print('\033[32;1m登录成功\033[0m')
         print('\033[32;1m欢迎来到英雄联盟!!!\033[0m')





def show_menu():
    cmds = {'0' : register, '1' : login}
    prompt = """
(0) 注册
(1) 登录
(2) 退出
请选择(0/1/2): """

    while True:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2']:
            print('无效的选项,请重新选择!')
            continue

        if choice == '2':
            print('bey-bey')
            break

        cmds[choice]()



if __name__ == '__main__':
    show_menu()


def kaishi():

    cmds = []
    jiemian = """
(0) 创建角色
(1) 开始游戏
(2) 退出游戏 
请选择(0/1/2):     
"""
    while True:
        youxi = input(jiemian).strip()

        if


