
attempt = 3

while attempt > 0:
    password = input("Enter the password: ")
    if password != "Admin123":
        attempt -= 1
    else:
        print("Login Successful")
print("Max attempt reach!")