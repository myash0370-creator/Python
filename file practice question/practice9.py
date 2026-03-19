#Write a program to find out whether a file is identical & matches the content of another file.
with open("file.txt" , "r") as f:
    content1 = f.read()

with open("this_copy.txt" , "r") as f:
    content2 = f.read()

if(content1 == content2):
    print("Yes files are identical")

else:
    print("files are not identical")
