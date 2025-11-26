with open ("notes.txt","w") as f:
     f.write("this is my first file!")
with open ("notes.txt","r") as f:
    print(f.read())