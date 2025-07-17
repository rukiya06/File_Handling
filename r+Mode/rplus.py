with open('file1.txt','w') as f:
    data=f.write("Welcome to Python practice session")
    print(f.data())
with open("file1.txt",'r+') as f:
    data=f.read()
    print("Previous:",data)
    new_data=data.replace("Python","file handling")
    f.seek(13)
    f.write(new_data)
    f.truncate()
with open('file1.txt','r') as f:
    print("Latest:",f.read())