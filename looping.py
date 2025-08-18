passwords = ["1234","admin","test","lucas","qwerty"]

for pwd in passwords:
    if pwd == "lucas":
        print(f"Password found. {pwd}")
        break
    else:
        print("Trying...")

