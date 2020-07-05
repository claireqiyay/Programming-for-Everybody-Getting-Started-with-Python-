#Hello
print('Hello. I am the chatbot that Claire made')
print('I like to eat ice cream and hate cornavirus')
name = input('What is your name?')
print('Hello', name, ', Nice to meet you')

#year
year = input('I am not very good at dates. What is the year?: ')
print('Yes I think that is correct. Thanks!')

#my age
myage = input('Can you guess my age? - enter a number: ')
print('Yes you are correct. I am ', myage)

#when I'm a hundred
myage = int(myage)
nyears = 100 - myage
print('I will be 100 in', nyears, 'years')
print('That will be the year', int(year) + nyears)

print('How old are you?')
yage = input('Please tell me your age: ')

yage = int(yage)
ynyears = 100 - yage
print('You will be 100 in', ynyears, 'years')
print('That will be the year', int(year) + ynyears)

print('I love chocolate and ice cream, and I like trying out new foods')
food = input('How about you? What is your favorite food?')
print('I like', food, 'too')
question = 'How often do you eat ' + food +'?: '
howoften = input(question)
print('Interesting. I wonder if that is good for your health')

animal = input('My favorite animal is a rabbit. What is yours?: ')
print(animal, '! I do not like them. ')
print('I wonder if a', animal, 'likes to eat', food)

feeling = input('How are you feeling today?: ')
print('Why are you feeling', feeling, 'now?')
reason = input('Please tell me: ')
print('I understand. Thanks for sharing')

print('It has been a long day')
print('I am too tired to talk. We can chat again later')
print('Goodbye', name, 'I liked chatting with you')
