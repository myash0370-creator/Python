# A file contains a word “Donkey” multiple times. You need to write a programwhich replace this word with ##### by updating the same file. 
word = "Donkey"
with open("file.txt" , "r") as f:
    content = f.read()

content_new =content.replace(word , "####")

with open("file.txt", "w") as f:
    f.write(content_new)