guest_list = ['gwen', 'mom', 'dad', 'kay', 'chido']
print(f"Dear {guest_list[0].title()}, you have been invited to my dinner at the Mont Sur Cafe.")
print(f"Dear {guest_list[1].title()}, you have been invited to my dinner at the Mont Sur Cafe.")
print(f"Dear {guest_list[2].title()}, you have been invited to my dinner at the Mont Sur Cafe.")
print(f"Dear {guest_list[3].title()}, you have been invited to my dinner at the Mont Sur Cafe.")
print(f"Dear {guest_list[4].title()}, you have been invited to my dinner at the Mont Sur Cafe.")

cannot_attend = guest_list.pop(4)
print(f"Unfortunately, {cannot_attend.title()} will not be joining us tonight for dinner")

guest_list.insert(4, 'noah')
print(f"Thank you for your patients, you are invited for dinner {guest_list[0].title()}")
print(f"Thank you for your patients, you are invited for dinner {guest_list[1].title()}")
print(f"Thank you for your patients, you are invited for dinner {guest_list[2].title()}")
print(f"Thank you for your patients, you are invited for dinner {guest_list[3].title()}")
print(f"Thank you for your patients, you are invited for dinner {guest_list[4].title()}")

print('\nAttention Everyone! A bigger table has been located, so I would like to formaly invite you to dine with me there as we also invite 3 more members to the crew.')
guest_list.insert(0, 'Tim')
guest_list.insert(3, 'Micheal')
guest_list.append('Susan') 

print(f"\nYou are invited {guest_list[0].title()}")
print(f"\nYou are invited {guest_list[1].title()}")
print(f"\nYou are invited {guest_list[2].title()}")
print(f"\nYou are invited {guest_list[3].title()}")
print(f"\nYou are invited {guest_list[4].title()}")
print(f"\nYou are invited {guest_list[5].title()}")
print(f"\nYou are invited {guest_list[6].title()}")
print(f"\nYou are invited {guest_list[7].title()}")

print('\nAttention everyone! I have frightful news. I unfortunately can only invite 2 pepple to dine as our table will not be ready in time. Apologies!!')

cannot_attend = guest_list.pop(0)
print(f"\nVery Sorry {cannot_attend.title()}, I hope we can reorganize")
cannot_attend = guest_list.pop(3)
print(f"Very Sorry {cannot_attend.title()}, I hope we can reorganize")
cannot_attend = guest_list.pop(1)
print(f"Very Sorry {cannot_attend.title()}, I hope we can reorganize")


print(f"\n{guest_list[0].title()} I am happy to inform you, you are still invited.")
print(f"{guest_list[1].title()} I am to inform, you're still on the list")








