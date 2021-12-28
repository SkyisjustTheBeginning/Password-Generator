import random
print("""
==============================================
   Password Generator
   Made by SkyIsJustTheBeginning
==============================================""")
characters = [1,2,3,4,5,6,7,8,9]
num = int(input("Number of Characters : "))
passcode = ""
for i in range(num):
    passcode += str(random.choice(characters))
print("Your passcode :" + passcode)

print("""

░█▀▀▀█ █─█ █──█ ▀█▀ █▀▀ ───░█ █──█ █▀▀ ▀▀█▀▀ ▀▀█▀▀ █──█ █▀▀ ░█▀▀█ █▀▀ █▀▀▀ ─▀─ █▀▀▄ █▀▀▄ ─▀─ █▀▀▄ █▀▀▀
─▀▀▀▄▄ █▀▄ █▄▄█ ░█─ ▀▀█ ─▄─░█ █──█ ▀▀█ ──█── ─░█── █▀▀█ █▀▀ ░█▀▀▄ █▀▀ █─▀█ ▀█▀ █──█ █──█ ▀█▀ █──█ █─▀█
░█▄▄▄█ ▀─▀ ▄▄▄█ ▄█▄ ▀▀▀ ░█▄▄█ ─▀▀▀ ▀▀▀ ──▀── ─░█── ▀──▀ ▀▀▀ ░█▄▄█ ▀▀▀ ▀▀▀▀ ▀▀▀ ▀──▀ ▀──▀ ▀▀▀ ▀──▀ ▀▀▀▀""")
