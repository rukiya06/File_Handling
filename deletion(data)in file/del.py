#data comparative deletion
with open("ex.txt","r")as f:
    lines=f.readlines()
with open("ex.txt","w")as f:
    for line in lines:
        if line.strip()!="4":
            f.write(line)

