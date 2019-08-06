import randpass
import sys
import subprocess

def adduser(username, password, fname):

    result = subprocess.run(
        'id %s' % username,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    if result.returncode == 0:
        print('%s已存在' % username)
        return False


    subprocess.run('useradd %s' % username , shell=True)
    subprocess.run(
        'echo %s | passwd --stdin %s' % (password, username),
        shell=True
    )

    info = """user info:
username: %s
password: %s
""" % (username, password)
    with open(fname, 'a')  as fobj:
        fobj.write(info)


if __name__ == '__main__':
    username = sys.argv[1]
    password = randpass.ranpass()
    fname ='/tmp/users.txt'
    adduser(username,password,fname)