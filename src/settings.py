from yaml import SafeLoader, load

import os


dir = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(dir, 'settings.yaml')


class PostgresQL:
    host = ""
    port = ...
    user = ...
    password = ...
    database = ""

    def __init__(self):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            config = load(f, SafeLoader)
            if postgres := config.get("Postgres"):
                self.host = postgres.get("host", self.host)
                self.port = int(postgres.get("port", self.port))
                self.user = postgres.get("user", self.user)
                self.password = postgres.get("password", self.password)
                self.database = postgres.get("database", self.database)

class Service:
    host = ...
    port = ...
    workers = 4


    def __init__(self):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            config = load(f, SafeLoader)
            if service := config.get("Service"):
                self.host = service.get("host", self.host)
                self.port = int(service.get("port", self.port))
                self.workers = service.get("workers", self.workers)
