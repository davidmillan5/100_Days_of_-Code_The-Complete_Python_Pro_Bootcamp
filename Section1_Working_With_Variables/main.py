name = input('What is your name?')
print(name)

print(len(input('What is your last name?')))

lastname = input('What is your last name?')
length = len(name)
print(length)

# Interactive Exercise

firstVariable = input('Enter your first Value: ')
secondVariable = input('Enter your second Value: ')

print('The First Variable is:  '+firstVariable)
print('The Second Variable is:  '+secondVariable)

thirdVariable = firstVariable
firstVariable = secondVariable
secondVariable = thirdVariable

print('The First Variable is:  '+firstVariable)
print('The Second Variable is:  '+secondVariable)


# Variable Naming

user_name = input('What is your name?')
length1 = len(user_name)
print(length1)


#Band Name Generator

print('Hello people from around the multiverse')

city_name = input('What is the name of the city where you grew up?\n')

pet_name = input('What is the name of your last pet?\n')

bandName = city_name + " "+pet_name

print('Your bands name should be: \n'+bandName)

