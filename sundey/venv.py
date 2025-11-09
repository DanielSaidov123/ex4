with open('my_file.txt','w')as f:
    f.write("my name daniel saidov")

with open('my_file.txt','r')as f:
    temp=f.read()

def io():
    text=input("enter text")
    return text

def xor(text):
    tx=""
    for i in text:
        if 65<=ord(i)<=90 :
           tx+=chr(90-ord(i)+65)
        elif 97<=ord(i)<=122:
           tx+=chr(122-ord(i)+97)
        else:
            tx+=i
    return tx


print(xor(io()))
         
def write():
    with open("daniel.txt","w") as d:
        d.write(xor(io(),xorr))

def read():
    with open("daniel.txt","r")as r:
        text=r.read()
    return text

 
 

def write():
    with open("daniel.txt","w") as w:
        w.write("daniel daidov\ndaniel levi\nbarak\ndavid")
    

def read():
    i=0
    with open("daniel.txt","r")as r:
        for line in r:
            if i%2==0:
                with open("daniel1.txt","w") as a:
                    a.write(line)
            if i%2!=0:
                with open("daniel2.txt","w") as a:
                    a.write(line)
            i+=1

    
write()
read()







