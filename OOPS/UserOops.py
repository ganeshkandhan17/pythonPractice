from User import User

user1 = User('Keerthi', 'Hi')
print(user1.name)
print(user1.password)

user2= User('Ganesh Kandhan', 'vivek')
print(user2.name)
print(user2.password)
user2.register()
user1.login()

print(User.users)
User.users = 10
print(User.users)