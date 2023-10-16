from user import *


def main():
    
    users: list = [
        User('Gandalf', 'wiZaRd@123', Role.MANAGER),
        User('Frodo', 'the.Shire', Role.DEVELOPER),
        User('Aragorn', 'AragornTheRanger', Role.ANALIST),
        User('Legolas', 'hobbits2isengard', Role.SALES),
        User('Gimli', 'full.bearded', Role.SALES)
    ]
    
    for user in users:
        print(user)

    users[1].change_username(new_username='Bilbo', password='the.Shire')
    users[3].role = Role.DEVELOPER
    users[4].change_password(new_password='SharpenMyAxe', password='full.bearded')

    for user in users:
        print(user)


if __name__ == "__main__":
    main()
