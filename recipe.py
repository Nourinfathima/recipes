from unicodedata import category
import mysql.connector

mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'recipesdb')

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
        
        taste = input('enter the taste you need : ')
        categorys = input('enter the category such as veg or non-veg : ')
        price = input('enter the price : ')
        
        sql = 'INSERT INTO `recipes`(`name`,`taste` ,`categorys`,`price`) VALUES (%s,%s,%s,%s)'
               
        data = (name,taste,categorys,price)
        mycursor.execute(sql , data)
        mydb.commit()
    elif(choice==2):
        print('view recipe')
        sql = 'SELECT * FROM `recipes`'
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
    elif(choice==3):
        print('search a food')
        categorys = input('enter the category such as veg or non-veg : ')
    
        sql = "SELECT `Name`, `taste`, `categorys`, `Price` FROM `recipes` WHERE `Categorys`='"+categorys+"'"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
    elif(choice==4):
        print('update the student')
    elif(choice==5):
        print('delete the student')
    elif(choice==6):

        break