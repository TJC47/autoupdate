import requests
print("This Program is running autoupdate by TJC47")
def check(filename, url):
    print(f"Checking {filename} for updates...")
    try:
        file = open(filename)
        text = file.read()
        file.close
        text1 = requests.get(url).text
    except:
        print("Could not check for updates.  Did you mistype? If not the servers are probably down.")
    try:
        if text == text1:
            print(f"{filename} is up to date!")
        else:
            print("File is not up to date!\nUpdating...")
            try:
                file = open(filename,"w")
                file.write("")
                file.close()
                file = open(filename,"w")
                file.writelines(text1.split("\n"))
                file.close()
                print(f"{filename} is up to date!")
                print(text1)
            except:
                print(f"Could not update {filename}! Is the file in use?")
    except:
        pass
check("autoupdate.py", "https://raw.githubusercontent.com/TJC47/autoupdate/main/autoupdate.py")
