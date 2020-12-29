import random, string
import requests
c = open("keywords.txt", "r")
keywords = c.readline()
        acc = f"https://pastebin.com/raw/{y}"
        url = acc
        s = requests.session()
        response = s.get(url)
        if f"{keywords}" in response.text:
          print("Found a valid paste! " + url)
          k.write(url)
###
num=input('Threads : ')
f=open("pastes.txt","w", encoding='utf-8')
print("Generating and checking")
for n in range(int(num)):
   y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(8))
   f.write("https://pastebin.com/raw/") 
   f.write(y)
   f.write("\n")     
f.close()
k=open("combo.txt","w", encoding='utf-8')
with open("pastes.txt") as f:
    for line in f:
