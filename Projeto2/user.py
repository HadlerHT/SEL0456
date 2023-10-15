from random import randint
from string import printable
from enum import Enum
from hashlib import sha256


class Role(Enum):
    MANAGER  = 0
    SALES = 1
    DEVELOPER = 2
    ANALIST = 3
    INTERN = 4

    def __str__(self):
        return self.name


class User:

    def __init__(self, username: str, password: str, role: Role) -> None:
        self.__username: str = username
        self.__role: Role = role
        self.__hash_salt: str = ''.join([printable[randint(0, 61)] for i in range(4)])
        self.__password_hash: str = self.__evaluate_hash(password)

        
    def __evaluate_hash(self, password: str) -> str:
        return sha256((password + self.__hash_salt).encode('utf-8')).hexdigest()


    def verify_password(self, password) -> bool:
        return self.__evaluate_hash(password) == self.__password_hash


    @property
    def role(self) -> Role:
        return self.__role
    

    @role.setter
    def role(self, new_role: Role):
        if isinstance(new_role, Role):
            self.__role = new_role
        else:
            raise(ValueError)    


    def change_password(self, new_password: str, password: str) -> bool:
        if self.verify_password(password):
            self.__password_hash = self.__evaluate_hash(new_password)
            return True
        return False

    
    def change_username(self, new_username: str, password: str) -> bool:
        if self.verify_password(password):
            self.__username = new_username
            return True
        return False


    def __str__(self) -> str:
        return 'Username: {}\nRole: {}\nHash: {}...{}\n'.format(
            self.__username, 
            self.__role,
            self.__password_hash[0:3],
            self.__password_hash[-4:-1]
        )
        
