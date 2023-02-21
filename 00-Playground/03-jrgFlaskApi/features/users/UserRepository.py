import json
import threading

import pandas as pd

from config import users_csv_filepath, file_separator


def user_default_values() -> dict:
    return {
        "id": None,
        "name": None,
        "email": None,
        "password": None,
        "country": None
    }


class UserModel:
    def __init__(self, user_id: int = None, name: str = None, email: str = None, password: str = None,
                 country: str = None):
        validation_errors = []
        if user_id is None:
            validation_errors.append("user_id no informado")
        if name is None:
            validation_errors.append("name no informado")
        if email is None:
            validation_errors.append("email no informado")
        if password is None:
            validation_errors.append("password no informado")
        if country is None:
            validation_errors.append("country no informado")

        if len(validation_errors):
            raise Exception(str(validation_errors))

        self.id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.country = country

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "country": self.country
        }


class UserRepository:
    def __init__(self, csv_file=users_csv_filepath, sep=file_separator):
        self.csv_file = csv_file
        self.sep = sep
        self.users = {}
        try:
            self.users_pd = pd.read_csv(filepath_or_buffer=csv_file, sep=sep)
            for user in self.users_pd.to_dict("records"):
                self.users[user["id"]] = user

        except FileNotFoundError:
            print(f"Warning: file {csv_file} does not exist. Loading empty data into memory")
        except Exception as e:
            print(f"Warning: {str(e)} Loading empty data into memory")

    def get_next_id(self) -> int:
        try:
            return max(self.users.keys()) + 1
        except:
            return 1

    def get_by_id(self, record_id: int) -> dict:
        if record_id in self.users:
            return self.users[record_id].copy()

        return {}

    def get_all_records(self) -> dict:
        return self.users.copy()

    def upsert(self, user: UserModel) -> None:
        self.users[user.id] = user.to_dict()

    def delete_by_id(self, record_id: int) -> int:
        if record_id in self.users:
            del self.users[record_id]
            return record_id

        return 0

    def commit(self, csv_file=None, sep=None):
        if csv_file is None:
            csv_file = self.csv_file

        if sep is None:
            sep = self.sep

        def save_data():
            records = json.dumps(list(self.users.values()))
            csv_json = pd.read_json(records)
            csv_json.to_csv(csv_file, sep, index=False)
            self.users_pd = pd.read_csv(filepath_or_buffer=csv_file, sep=sep)

        # Guardo en segundo plano
        save_thread = threading.Thread(target=save_data)
        save_thread.start()
