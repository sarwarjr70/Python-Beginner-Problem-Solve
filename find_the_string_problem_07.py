post = input("Enter your post: ")

if ("sarwar".lower() in post.lower()):
    print(f"{post} \nThis post is about Sarwar")
else:
    print(f"{post} \nThis post is not about Sarwar")