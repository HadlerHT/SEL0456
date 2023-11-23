from hashlib import sha256
import os

class Password():
    
    @staticmethod
    def __file_path(file_name: str) -> str:
        script_path = os.path.dirname(os.path.abspath(__file__))
        return f'{script_path}/../files/{file_name}'

    @staticmethod
    def hash(password: str) -> str:
        return sha256((password).encode('utf-8')).hexdigest()

    @staticmethod
    def save(hash: str) -> None:
        try:
            with open(Password.__file_path('hashed_password.txt'), 'w') as file:
                file.write(hash)

        except Exception as excep:
            print(f'Something went wrong: {excep}')

    @staticmethod
    def get_entry() -> str | None:
        try:
            with open(Password.__file_path('password_entry.txt'), 'r') as file:
                password_entry = file.read()

            return password_entry

        except Exception as excep:
            print(f'Something went wrong: {excep}')


    @staticmethod
    def verify(password_to_test: str) -> bool:
        with open(Password.__file_path('hashed_password.txt'), 'r') as file:
            stored_hash = file.read()

        return stored_hash == Password.hash(password_to_test)


def main():

    # correct_password = 'myPassword@123'
    # Password.save(hash=Password.hash(password=correct_password))

    entry = Password.get_entry()
    print(entry, Password.verify(entry))


if __name__ == '__main__':
    main()