with open("file1.txt",'w+') as f:
    f.write("Hello Audience!!")
    f.seek(0)
    data=f.read()
    print("Previous:",data)
    new_data=data.replace("Audience!!","Future IT Employees")
    f.seek(0)
    f.write(new_data)
    #f.truncate()
with open("file1.txt",'r') as f:
    print("Latest:",f.read())