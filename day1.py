print('Hello World')
FIRSTNAME = 'Simeon'
FIRST_NAME ='Job'
NUM1 = 45
NUM2 = 42.36
X = True
print(FIRSTNAME)
#DECLEAR A VARIABLE TO HOLD ANY INTEGER NUMBER
#DECLEAR A VARIABLE TO HOLD ANY FLOATING NUMBER
#DECLEAR A VARIABLE TO HOLD A STRING VALUE
#DECLEAR A VARIABLE TO HOLD A BOOLEAN VALUE

#ESCAPE CHARACTER
WORD = 'we\'re brothers from the other side of the town'
print(WORD)

#NEWLINE
WORD2 = 'python is fun,\npython is easy,\npython is good'
print(WORD2)


#MULTILINE STRING
print('\n')
WORD3 = '''python is fun
python is easy
python is good
'''
print(WORD3)


#STRING CONCATENATION
print('my name is' + ' '+ FIRSTNAME)
print(FIRSTNAME, FIRST_NAME)

#STRING FORMATTING
PRICE1 = 1000
price2 = 20000
price3 = 80000

report = 'i sold a jacket for {}, a shirt for {} and a suit for {}'
print(report.format(price1,price2,price3))


print(f'i sold a jacket for {price1}, a shirt for {price2} and a suit for {price3}')

#STRING METHOD
word1 = 'python'
word2 = 'PYTHON'
word3 = 'python is fun'
word4 = '  info@gmail.com'
print(word1.upper())
print(word2.lower())
print(word3.title())
print(word3.capitalize())
print(word3.split())
print(word4.strip())









