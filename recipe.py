
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
    print('6 total price')
    print('7 price of each categorys')
    print('8 Starting letter of name of recepi')
    print('exit')

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
        print('update the food')
        categorys = input('enter the category such as veg or non-veg : ')
        name = input('enter the name of the recipe : ')
        taste = input('enter the taste you need : ')
        price = input('enter the price : ')

        sql = f"UPDATE `recipes` SET `name`='{name}',`taste`='{taste}',`categorys`='{categorys}' WHERE `price`={price}"
        mycursor.execute(sql)
        mydb.commit()
    elif(choice==5):
        print('delete the recipe')
        name = input('enter the name of the recipe to be deleting : ')
        sql = "DELETE FROM `recipes` WHERE `Name`='"+name+"'"
        mycursor.execute(sql)
        mydb.commit()
    elif(choice==6):
        print('total price')
        sql = 'SELECT SUM(`Price`) FROM `recipes` '
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)
    elif(choice == 7):
        print('total price for each categorys')
        sql = "SELECT `Categorys`, SUM(`price`) FROM `recipes` GROUP BY `Categorys`"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)
    elif(choice==8):
        print('Starting letter of name of recepi')
        st = input('Enter the first character of the name : ')
        sql = "SELECT * FROM `recipes` WHERE `Name` LIKE '%"+st+"%'"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)
    elif(choice==9):
        break
    
        
        

        break