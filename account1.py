import os
import pickle
from time import strftime


def save(fname):
    try:
        amount = int(input('金额: '))
        comment = input('备注: ')
    except (KeyboardInterrupt,EOFError,ValueError):
        print('\n输入有误,返回!!!')
        return
    date = strftime('%Y-%m-%d')
    with open(fname, 'rb') as fobj:
         records =  pickle.load(fobj)

    balance = records[-1][-2] + amount
    records.append([date,amount,0,balance,comment])
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)



def cost(fname):
    try:
        amount = int(input('金额: '))
        comment = input('备注: ')
    except (KeyboardInterrupt, EOFError, ValueError):
        print('\n输入有误,返回!!!')
        return
    date = strftime('%Y-%m-%d')
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)

    balance = records[-1][-22] - amount
    records.append([date, 0, amount, balance, comment])
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def query(fname):
    with open(fname, 'rb') as fobj:
       records =  pickle.load(fobj)
    print('%-12s%-6s%-6s%-10s%-20s' % ('date','save','cost','balance','comment'))
    for record in records:
        print('%-12s%-6s%-6s%-10s%-20s' % tuple(record))



def show_menu():
    init_data = [[strftime('%Y-%m-%d'),0 , 0 ,10000, 'init']]
    fname = 'zhangben.txt'
    if not os.path.exists(fname):
            with open(fname, 'wb') as fobj:
                pickle.dump(init_data, fobj)
    cmds = {'0': save, '1': cost,'2': query}
    prompt = """
(0) 收入
(1) 支出
(2) 查询
(3) 退出
请选择:"""
    while True:
        try:
            choice = input(prompt).strip()
        except (KeyboardInterrupt,EOFError):
            choice = '3'


        if choice not in ['0','1','2','3']:
            print('无效的选择,请重试!!!')
            continue

        if choice == '3':
            print('BYE-BYE')
            break

        cmds[choice](fname)

if __name__ == '__main__':
    show_menu()



