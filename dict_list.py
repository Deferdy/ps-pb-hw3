
account1 = {"login": "ivan", "password": "q1"}
account2 = {"login": "petr", "password": "q2"}
account3 = {"login": "olga", "password": "q3"}
account4 = {"login": "anna", "password": "q4"}

user1 = {"name": "Иван", "age": 20, "account1": {"login": "ivan", "password": "q1"} }
user2 = {"name": "Петр", "age": 25, "account2": {"login": "petr", "password": "q2"} }
user3 = {"name": "Ольга", "age": 18, "account3": {"login": "olga", "password": "q3"} }
user4 = {"name": "Анна", "age": 27, "account4": {"login": "anna", "password": "q4"} }

user_list = [{"name": "Иван", "age": 20, "account": {"login": "ivan", "password": "q1"} }, {"name": "Петр", "age": 25, "account": {"login": "petr", "password": "q2"} }, {"name": "Ольга", "age": 18, "account": {"login": "olga", "password": "q3"} }, {"name": "Анна", "age": 27, "account": {"login": "anna", "password": "q4"} } ]


key = input("Введите ключ (name или account):").lower() 

try: 
    print("значение ключа "+ key + " для юзера 1 = " + user1[key] ) 
    print("значение ключа "+ key + " для юзера 2 = " + user2[key] ) 
    print("значение ключа "+ key + " для юзера 3 = " + user3[key] ) 
    print("значение ключа "+ key + " для юзера 4 = " + user4[key] )
except: 
    print("Введенный ключ не найден")

number = int(input("Введите порядковый номер:"))

try: 
    print("Данные по юзеру №"+ str(number)+":") 
    print("имя: " + user_list[number-1]["name"] ) 
    print("возраст: " + str(user_list[number-1]["age"]) ) 
    print("логин: " + user_list[number-1]["account"]["login"] ) 
    print("пароль: " + user_list[number-1]["account"]["password"])
except: 
    print("Пользователь с указанным номером не найден")



number = int(input("Введите номер пользователя, которого нужно переместить в конец: "))

print("Пользователь с именем "+ user_list[number-1]["name"]+ " перемещен в конце")
print("Список до изменения:")
print(user_list)
print("Список после изменения:")

x = user_list.pop(number-1) 
user_list.append(x)

print(user_list)
age_all = [user1["age"], user2["age"], user3["age"], user4["age"]]
print("средний возраст всех юзеров " + str(sum(age_all)/len(age_all)))