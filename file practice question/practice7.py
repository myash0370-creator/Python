#Write a program to find out the line number where python is present from ques 6.
with open("log.txt" , "r") as f:
    lines = f.read()
lineno = 1
for line in lines:
    if("python" in lines):
     print(f"yes python is in the log file, line number: {lineno}")
     break
    line +=1

else:
    print("no python is in the file")