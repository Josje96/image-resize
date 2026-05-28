import os
from PIL import Image

#img = Image.open("bear.png")
#w, h = img.size
#new_w = 400
#new_h = int(h * (new_w / w))
#out = img.resize((new_w, new_h), Image.BICUBIC)
#out.show()

def choose_size()
    print("What width would you like your photos?")
    pic_width = input("example: 250")

# get the path that the user wants to use to scale the directory
print("What is the absolute path of the folder you wish to scale? Hint: you can right click the folder and select copy as path.")

user_path = input(r"Example: C:\Users\jkj09\Documents\n> ")

# Remove surrounding quotes if present
if (user_path.startswith('"') and user_path.endswith('"')) or \
   (user_path.startswith("'") and user_path.endswith("'")):
    user_path = user_path[1:-1]

# 2. Check if the path actually exists and is a directory
if os.path.exists(user_path) and os.path.isdir(user_path):
    
    # 3. List and print the contents
    contents = os.listdir(user_path)
    print(f"Contents of '{user_path}':")
    for item in contents:
        print(item)
else:
    print("The path provided is not a valid directory.")

print("Does this path look correct to you?")
right_path = input("yes / no: ")
if right_path.lower() =="yes":
    print("Good, lets move on")
    new_width = choose_size()


else:
    print("Lets try that again")
