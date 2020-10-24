
'''
wexpect是windows 下的交互式模块

pexpect是linux 系统下的交互式模块
'''
import wexpect

child = wexpect.spawn(r'D:\unzip.exe C:\Users\Administrator\Desktop\rabbitmq配置.zip -d d:\124')
child.expect('password:')
child.sendline('123456')
print(child.before)
child.sendline('exit')