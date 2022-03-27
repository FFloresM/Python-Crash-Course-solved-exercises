guest_list = ['Walter White', 'Barack Obama', 'Alien']
invitation = "Let me invite you to my dinner Mr. "
print(invitation + guest_list[0])
print(invitation + guest_list[1])
print(invitation + guest_list[2])

print(f"Ooh, {guest_list[2]} can't make it :(")
guest_list[2] = "Uncle Bob"

print(invitation + guest_list[0])
print(invitation + guest_list[1])
print(invitation + guest_list[2])

print("I found a bigger dinner table! So, I can make new invitations")

guest_list.insert(0,"The Queen")
guest_list.insert(3,"Alf")
guest_list.append("Bad Bunny")

print(invitation + guest_list[0])
print(invitation + guest_list[3])
print(invitation + guest_list[5])

print("guests list")
print(guest_list)

print("I can invite only two people for dinner.")
print("I'm sorry, Mr. "+guest_list.pop()+", I can't invite you to dinner.")
print("I'm sorry, Mr. "+guest_list.pop()+", I can't invite you to dinner.")
print("I'm sorry, Mr. "+guest_list.pop()+", I can't invite you to dinner.")
print("I'm sorry, Mr. "+guest_list.pop()+", I can't invite you to dinner.")

print("people in the list")
print(guest_list)

print(f"{guest_list[0]} you're still invited.")
print(f"{guest_list[1]} you're still invited.")

del guest_list[1]
del guest_list[0]

print("the list must be empty")
print(guest_list)