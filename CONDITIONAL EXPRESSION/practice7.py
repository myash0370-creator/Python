#Write a program to find out whether a given post is talking about “yash” or not.
post = input("Enter your post: ")

if("yash" in post.lower()):
    print("This post is talking about yash")

else:
    print("This post is not talking about yash")