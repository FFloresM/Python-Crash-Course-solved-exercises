guest_list = ['Walter White', 'Barack Obama', 'Alien']
invitation = "Let me invite you to my dinner Mr "
print(invitation + guest_list[0])
print(invitation + guest_list[1])
print(invitation + guest_list[2])
print(f"Number of people invited: {len(guest_list)}")
#uncomment the following line to produce an IndexError
#print(invitation + guest_list[3])