current_users = ['admin','apaz','jperez','amines','rgalvez']
current_users_lower = [ user.lower()  for user in current_users]
new_users = ['jperez','RGALVEZ','mmuñoz','cpalacios','pcuba']

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user} is used. Please choose another username.")
    else:
        print(f"The username '{new_user}' is available.")
