#serial numbered data-deletion

ldel=input("enter exact line:")
with open('ex.txt','r')as f:
    lines=f.readlines()
with open('ex4.txt','w') as f:
    for line in lines:
        if line.strip()!=ldel.strip():
            f.write(line)