
class User:
    def __init__(self, username = None, password = None):
        self.password = password
        self.username = username

class Admin(User):
    def ban_user(self):
        print(f"Користувач {self.username} заблокований")

class Moderator(Admin, User):
    def warn_user(self):
        print(f"Користувач {self.username} попереджений")

def login(users_list, username, password):
    for user in users_list:
        if user.username == username:
            if user.password == password:
                print('Вітаю!')
            else:
                raise TypeError
    else:
        raise TypeError

user1 = User("Hum", "Pass1")
admin1 = Admin("Adm", "Super")
mod1 = Moderator("Mod", "Hiper")

users_list = [user1, admin1, mod1]

try:
    print(login(users_list, "Hum", "Pass1"))
except TypeError:
    print('Шось не так!')
