# Write a program to mine a log file and find out whether it contains ‘python’.
with open("log.txt" , "r") as f:
    content = f.read()

if("python" in content):
    print("yes python is in the log file")

else:
    print("no python is in the file")