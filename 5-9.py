usernames = ['admin','apaz','jperez','amines','rgalvez']
for x in range(1,6): 
 del usernames[0]

if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"Hello {username}, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")


    