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