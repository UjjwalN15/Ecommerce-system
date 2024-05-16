# Login and register
# Ask the user if he/she wants to login or register
# If the user says register ask for username and password and store this data in a file
# Elif the user says login the ask for username and password and check this data in the file where user data is stored in such a way if the username and password matches print 'Login successfull' else 'Invalid credentials'
# After login successfull
# If the user is seller print his/her choices : 1. Add product, 2. View bills 3. View your product
# Elif the user is buyer print his/her choices : 1. View products 2. Purchase products 3. View your bills
# Ask the user choice in input and for seller if he/she enters the choice of add product : ask for product name, description , price and make this data a dict and write it on a file

# During add product : add the seller name in product data
# During seller's choice view your product : List the logged in seller's product only
import json
import time
import random
import os
from tabulate import tabulate
open('C:/Users/prajw/OneDrive/Desktop/Python Programming/Buyer_purchase.txt','w').close()
def main():
    while True:
        print ("Enter 1 for login\nEnter 2 for register\nEnter 3 for exit.")
        try:
            choice = int(input("Enter your choice: "))
            time.sleep(1)
            os.system("cls")
        except ValueError:
            print("You have entered the wrong choice. Please entered a valid choice.")
            time.sleep(3)
            os.system("cls")
            continue
        if choice == 1:
            login()
            time.sleep(1) 
        elif choice == 2:
            register()
            time.sleep(1)
        elif choice == 3:
            exit(0)
        else:
            print("You have entered the wrong choice.Please try again.")
            time.sleep(1)
            continue
        again()

def login():
    try:
        data_file = open("C:/Users/prajw/OneDrive/Desktop/Python Programming/Ecommerce_Task/Ecommerce_Task_User_data.txt","r")
    except FileNotFoundError:
        print("File not found.You should create a file name 'Ecommerce_Task_User_data.txt' ")
        exit(0)
    user_data = data_file.read()
    data_file.close()
    if user_data == "":
        print("No data in the database.Please register to continue.")
        register()
    else:
        login_username = input("Enter your login username: ")
        login_password = input("Enter your login password: ")
        list_user_data = user_data.split("-")
        login = False
        for i in list_user_data:
            if i != "":
                dict_user_data = json.loads(i)
                if login_username in dict_user_data and dict_user_data.get(login_username) == login_password:
                     login = True
                     user_type = dict_user_data.get("type")  
        if login :
            print(f"Login successful.Hello {login_username}")
            if user_type == "buyer":
                buyer_panel()
            elif user_type == "seller":
                seller_panel(login_username)
        else:
            print("Invalid Credentials.")
def register():
    register_username = input("Enter your register username: ")
    if register_username.isdigit():
        print("Username cannot be only number.")
        register()
    elif register_username == "":
        print("Username cannot be empty.")
        register()
    register_password = input("Enter your register password: ")
    if register_password == "":
        print("Password cannot be empty.")
        register()
    elif len(register_password) < 6:
        print("Password must be at least 6 characters")
        register()
    user_type = input("Are you a buyer or a seller?")
    try:
        data_file = open("C:/Users/prajw/OneDrive/Desktop/Python Programming/Ecommerce_Task/Ecommerce_Task_User_data.txt","r")
    except FileNotFoundError:
        print("File not found.You should create a file name 'Ecommerce_Task_User_data.txt' ")
        exit(0)
    user_existing_data = data_file.read()
    data_file.close()
    list_user_existing_data = user_existing_data.split("-")
    for datas in list_user_existing_data:
        if datas != "":
            dict_user_existing_data = json.loads(datas)
            if register_username in dict_user_existing_data and dict_user_existing_data.get("type") == user_type:
                print("Username already exists")
                register()
    if register_username.isdigit():
        print("Username cannot be only number.")
        register()
    elif register_username == "":
        print("Username cannot be empty.")
        register()
    else:
        while True:
            captcha = random.randint(1000,9999)
            print("The captcha is ",captcha)
            try:
                captcha_input = int(input("Enter the captcha: "))
            except ValueError:
                print("Please enter the mentioned captcha.")
                time.sleep(1)
                continue
            if captcha == captcha_input:
                time.sleep(1)
                user_data = {register_username: register_password,"type": user_type}
                json_user_data = json.dumps(user_data)
                file = open("C:/Users/prajw/OneDrive/Desktop/Python Programming/Ecommerce_Task/Ecommerce_Task_User_data.txt", "a")
                file.write(json_user_data + "-")
                file.close()
                print(f"Registration Successful with the username {register_username}")
                break
            else:
                print("Please enter the valid captcha.")
                time.sleep(1)
                continue
def buyer_panel():
    print("1. View products 2. Purchase products 3. View your bills 4. Exit")
    try:
        buyer_choice = int(input("ENter your choice: "))
    except ValueError:
        print("You have entered the wrong choice. Please entered a valid choice.")
        buyer_panel()
    if buyer_choice == 1:
        buyer_view_products()
        buyer_panel()
    elif buyer_choice == 2:
        buyer_purchase_product()
        buyer_panel()
    elif buyer_choice == 3:
        os.system("cls")
        buyer_view_bills()
        buyer_panel()
    elif buyer_choice == 4:
        again()
    else:
        print("You have entered the wrong choice. Please entered a valid choice.\n")
        time.sleep(1)
        buyer_panel()
                
                    
                
def buyer_purchase_product():
    try:
        purchase_index = int(input("Enter the index of an item you want to purchase:"))
        purchase_quantity = int(input("Enter the quantity of the item: "))
    except ValueError:
        print("You have entered the wrong choice. Please enter a valid choice.")
        buyer_panel()
    try:
        f = open('C:/Users/prajw/OneDrive/Desktop/Python Programming/Ecommerce_Task/Ecommerce_Task_Item_data.txt','r')
    except FileNotFoundError:
        print("File not found.You should create a file named 'Ecommerce_Task_Item_data.txt'")
        exit(0)
    product_data = f.read()
    f.close()
    list_product_data = product_data.split('-')
    list_product_data = list_product_data[:-1]
    if purchase_index > len(list_product_data)-1:
        print("You have entered the wrong index number. Please entered a valid index number.")
        buyer_panel()
    for index, products in enumerate(list_product_data):
        dict_product_data = json.loads(products)
        if index == purchase_index:
            purchased_item_data = {"Name":dict_product_data.get('Name'),"Model":dict_product_data.get("Model"),"Price":dict_product_data.get('Price'),"Seller":dict_product_data.get('Seller'),"Quantity":purchase_quantity} 
            json_purchased_item_data = json.dumps(purchased_item_data)      
            file = open("C:/Users/prajw/OneDrive/Desktop/Python Programming/Ecommerce_Task/Buyer_purchase.txt","a")
            file.write(json_purchased_item_data + "-")
            file.close()
            print(f"The item on the index {index} has been purchased successfully.")

    
def buyer_view_bills():
    try:
        data_file = open("C:/Users/prajw/OneDrive/Desktop/Python Programming/Ecommerce_Task/Buyer_purchase.txt","r")
    except FileNotFoundError:
        print("FILE NOT FOUND. You should create a file named 'Buyer_purchase.txt'")
        exit(0)
    purchased_item_data = data_file.read()
    data_file.close()
    list_purchased_item_data = purchased_item_data.split("-")
    print("You have purchased the following items: ")
    total_price = 0
    # print("S.N\t\tItem Name\t\tItem Model\t\tRate\t\tQuantity\t\tSeller\t\tPrice")
    for datas in list_purchased_item_data:
        if datas != "":
            dict_purchased_item_data = json.loads(datas)
            
            # print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            data = [(list_purchased_item_data.index(datas)+1,dict_purchased_item_data.get('Name'),dict_purchased_item_data.get("Model"),dict_purchased_item_data.get("Price"),dict_purchased_item_data.get("Quantity"),dict_purchased_item_data.get("Seller"),int(dict_purchased_item_data.get("Price")) * int(dict_purchased_item_data.get("Quantity")))]           # print("Product No: ", list_purchased_item_data.index(datas))
            # print("Product Name: " , dict_purchased_item_data.get('Name'))
            # print("Product Model: " , dict_purchased_item_data.get('Model'))
            # print("Product Price: " , dict_purchased_item_data.get('Price'))
            # print("Product Seller: ", dict_purchased_item_data.get('Seller'))
            print(tabulate(data, headers = ["S.N","Item Name","Item Model","Rate","Quantity","Seller","Price"], tablefmt = "grid"))
            # print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            total_price += int(dict_purchased_item_data.get('Price')) * int(dict_purchased_item_data.get("Quantity"))
            
    print("Your total price is ",total_price)
    
def buyer_view_products():
    try:
        data_file = open("C:/Users/prajw/OneDrive/Desktop/Python Programming/Ecommerce_Task/Ecommerce_Task_Item_data.txt","r")
    except FileNotFoundError:
         print("File not found.You should create a file named 'Ecommerce_Task_Item_data.txt'")
         exit(0)
    item_data = data_file.read()
    data_file.close()
    list_item_data = item_data.split("-")
    for datas in list_item_data:
        if datas != "":
            dict_item_data = json.loads(datas)
            print("-----------------------------------------------")
            print("Product No: ", list_item_data.index(datas))
            print("Product Name: " , dict_item_data.get('Name'))
            print("Product Model: " , dict_item_data.get('Model'))
            print("Product Price: " , dict_item_data.get('Price'))
            print("Product Seller: ", dict_item_data.get('Seller'))
            print("-----------------------------------------------")
            # print("Name: ", dict_item_data.get("Name")," Model",dict_item_data.get("Model")," Price: ", dict_item_data.get("Price")," Seller: ",dict_item_data.get("Seller"))
def seller_panel(username):
    print("1. Add product 2. View bills 3. View your product 4. Delete item 5. Exit")
    try:
        seller_choice = int(input("Enter your choice: "))
    except ValueError:
        print("You have entered the wrong choice. Please entered a valid choice.")
        seller_panel(username)
    while True:
            if seller_choice == 1:
                seller_add_products(username)
                seller_panel(username)
            elif seller_choice == 2:
                seller_view_bills(username)
                seller_panel(username)
            elif seller_choice == 3:
                seller_view_products(username)
                seller_panel(username)
            elif seller_choice == 4:
                seller_delete_product(username)
                seller_panel(username)
            elif seller_choice == 5:
                again()
            else:
                print("You have entered the wrong choice.Please try again.\n")
                time.sleep(1)
                seller_panel(username)

def seller_add_products(username):
    add_item_name = input("Enter the name of the item to add: ")
    add_item_model = input("Enter the model of the item to add: ")
    try:
        data_file = open("C:/Users/prajw/OneDrive/Desktop/Python Programming/Ecommerce_Task/Ecommerce_Task_Item_data.txt","r")
    except FileNotFoundError:
        print("File not found.You should create a file named 'Ecommerce_Task_Item_data.txt'")
        exit(0)
    file_existing_data = data_file.read()
    data_file.close()
    list_file_existing_data = file_existing_data.split("-")
    for datas in list_file_existing_data:
        if datas != "":
            dict_file_existing_data = json.loads(datas)
            if dict_file_existing_data.get("Model") == add_item_model and dict_file_existing_data.get("Seller") == username:
                print("Item model already exists.")
                seller_panel(username)
    add_item_price = input("Enter the price of the item to add: ")
    item_data_add = {"Name":add_item_name,"Model":add_item_model,"Price":add_item_price,"Seller":username}
    json_item_data_add = json.dumps(item_data_add)
    file = open("C:/Users/prajw/OneDrive/Desktop/Python Programming/Ecommerce_Task/Ecommerce_Task_Item_data.txt","a")
    file_existing_data = file.write(json_item_data_add+"-")
    file.close()
    print(f"{add_item_name} added Successfully with its model {add_item_model} and price {add_item_price} by {username}.")
    
def seller_view_bills(username):
    try:
        data_file = open("C:/Users/prajw/OneDrive/Desktop/Python Programming/Ecommerce_Task/Ecommerce_Task_Item_data.txt","r")
    except FileNotFoundError:
        print("File not found.You should create a file named 'Ecommerce_Task_Item_data.txt'")
        exit(0)
    file_existing_data = data_file.read()
    list_file_existing_data = file_existing_data.split("-")
    data_file.close()
    total_price = 0
    print("Your Items are:")
    for datas in list_file_existing_data:
        if datas != "":
            dict_file_existing_data = json.loads(datas)
            if dict_file_existing_data.get("Seller") == username:
                # print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                data = [(list_file_existing_data.index(datas)+1,dict_file_existing_data.get('Name'),dict_file_existing_data.get("Model"),dict_file_existing_data.get("Price"),dict_file_existing_data.get("Seller"),int(dict_file_existing_data.get("Price")))]           # print("Product No: ", list_purchased_item_data.index(datas))
                # print("Product Name: " , dict_purchased_item_data.get('Name'))
                # print("Product Model: " , dict_purchased_item_data.get('Model'))
                # print("Product Price: " , dict_purchased_item_data.get('Price'))
                # print("Product Seller: ", dict_purchased_item_data.get('Seller'))
                print(tabulate(data, headers = ["S.N","Item Name","Item Model","Rate","Seller","Price"], tablefmt = "grid"))
                # print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                total_price += int(dict_file_existing_data.get('Price'))
    print(f"Total Price: {total_price}")
def seller_view_products(username):
    item_found = False
    try:
        data_file = open("C:/Users/prajw/OneDrive/Desktop/Python Programming/Ecommerce_Task/Ecommerce_Task_Item_data.txt","r")
    except FileNotFoundError:
        print("File not found.You should create a file named 'Ecommerce_Task_Item_data.txt'")
        exit(0)
    file_existing_data = data_file.read()
    data_file.close()
    list_file_existing_data = file_existing_data.split("-")
    for datas in list_file_existing_data:
        if datas != "":
            dict_file_existing_data = json.loads(datas)
            if dict_file_existing_data.get("Seller") == username:
                item_found = True
                print("-----------------------------------------------")
                print("Product No: ", list_file_existing_data.index(datas))
                print("Product Name: " , dict_file_existing_data.get('Name'))
                print("Product Model: " , dict_file_existing_data.get('Model'))
                print("Product Price: " , dict_file_existing_data.get('Price'))
                print("Product Seller: ", dict_file_existing_data.get('Seller'))
                print("-----------------------------------------------")
    if not item_found:
        print("You have no items to show.You can add items.")
        seller_panel(username)

def seller_delete_product(username):
    try:
        data_file = open("C:/Users/prajw/OneDrive/Desktop/Python Programming/Ecommerce_Task/Ecommerce_Task_Item_data.txt","r")
    except FileNotFoundError:
        print("File not found.You should create a file named 'Ecommerce_Task_Item_data.txt'")
        exit(0)
    product_data = data_file.read()
    data_file.close()
    deleted = False
    list_product_data = product_data.split('-')
    list_product_data = list_product_data[:-1]
    choice = int(input("Enter Product No. to delete: "))
    for index, products in enumerate(list_product_data):
        dict_product_data = json.loads(products)
        if dict_product_data.get("Seller") == username and index == choice:
            item_found = True
            list_product_data.pop(choice)
            deleted = True
        else:
            pass
            
        open('C:/Users/prajw/OneDrive/Desktop/Python Programming/Ecommerce_Task/Ecommerce_Task_Item_data.txt','w').close() 

        for i in list_product_data:
            product_data = json.loads(i)
            
            product_dict = {"Name":product_data.get('Name'),"Model":product_data.get("Model"),"Price":product_data.get('Price'),"Seller":product_data.get('Seller')}
            f = open('C:/Users/prajw/OneDrive/Desktop/Python Programming/Ecommerce_Task/Ecommerce_Task_Item_data.txt','a')
            json_product_dict = json.dumps(product_dict)
            f.write(json_product_dict+'-')
            f.close()
    if deleted == True:
        print(f"Item on the index {choice} deleted successfully.")
    else:
        print("You can't delete other seller's item.")
        time.sleep(1)
        seller_panel(username)
    if not item_found:
        print("You have no items to delete.You can add items.")
        time.sleep(1)
        seller_panel(username)
def again():
    while True:
        again = input("Do you want to use the system again?(y/n) : ").lower()
        if again == "n":
            exit(0)
        if again == "y":
            time.sleep(1)
            main()
        else:
            print("You have to enter either y or n. Thank you.")
            time.sleep(1)
            continue
        
main()