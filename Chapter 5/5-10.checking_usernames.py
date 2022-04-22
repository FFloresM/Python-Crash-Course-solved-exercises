current_users = ['bob', 'jonny', 'dogg', 'kitten', 'admin', 'lily']
new_users = ['bob', 'mike', 'vicky', 'andrew', 'jonny']
current_users = [user.lower() for user in current_users]
for user in new_users:
    if user in current_users:
        print("the person will need to enter a new username.")
    else:
        print("the username is available.")