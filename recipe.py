from unicodedata import category
import mysql.connector

mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'recipe_db')

mycursor = mydb.cursor()
while True:
    print("select an option from the menu")
    print('1 add recipe')
    print('2 view all recipe')
    print('3 search a recipe')
    print('4 update a recipe')
    print('5 delete a recipe')
    print('6 exit')

    choice = int(input('Enter an option: '))
    if(choice==1):
        print('enter the recipe selected')
        
        name = input('enter the name of the recipe : ')
        categorys = input('enter the category such as veg or non-veg : ')
        
        taste = input('enter the taste you need : ')
        price = input('enter the price : ')
        
        sql = 'INSERT INTO `food`(`Name`, `Category`, `Taste`, `Price`) VALUES (%s,%s,%s,%s)'
        data = (name, categorys,taste,price)
        mycursor.execute(sql , data)
        mydb.commit()
    elif(choice==2):
        print('view student')
    elif(choice==3):
        print('search a student')
    elif(choice==4):
        print('update the student')
    elif(choice==5):
        print('delete the student')
    elif(choice==6):
        break