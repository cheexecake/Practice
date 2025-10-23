names = ['Ben', 'Noah', 'Nick', 'Asher', 'William', 'Nell', 'Yohan', 'Grace', 'Gwen', 'Evelyn', 'Malcolm', 'Grace']
#print(names[0])
#print(names[3])
#print(names[-1])
#print(names[-3])

greeting = f"Congratulations {names[8]} on making this list. This means you are someone I hold dearly in my heart, some may even reffer to it as friendship."
#print(greeting)
#This code generates a personalized message to the people in the list. In this case I have chosen gwen

vehichles = ['Harley Davidson', 'Honda Civic', 'Audi R8', 'Tesla', 'Corvette']
car_message =  f"I would like to own a {vehichles[-1]}"
#print(car_message)

vehichles.append('Rolls Royce')
vehichles.insert(0,'Dodge Challanger')
#print(vehichles)

vehichles.insert(3,'Audi R8')
del vehichles[4]
#print(vehichles)

last_owned = vehichles.pop()
print(vehichles)
print(last_owned)
print(f"the last vehichle I owned was a {last_owned}")

ugly = 'Tesla'
vehichles.remove(ugly)
print(f"\nA {ugly.title()} is way to ugly to be in my collection.")