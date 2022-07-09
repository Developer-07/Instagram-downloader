import os
try:
    import instaloader
except:
    os.system('pip install instaloader')
    import instaloader
    os.system("cls")
print("You need to put your username because you the lib needs it for the stories and highlights")
name = input("Your Username: ")
os.system("cls")
print("""
Instagram Downloader

1. Download Profile
2. Download Stories
3. Download Post the user is tagged in
4. Download Highlights
""")
answer = int(input(">>> "))
profile = input("Instagram name: ")
if answer == 1:
    os.system(f"instaloader --fast-update profile {profile}")
elif answer == 2:
    os.system(f"instaloader --login={name} --stories profile {profile}")
elif answer == 3:
    os.system(f"instaloader --login={name} --tagged profile {profile}")
elif answer == 4:
    os.system(f"instaloader --login={name} --highlights profile {profile}")