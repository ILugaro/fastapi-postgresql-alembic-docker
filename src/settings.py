"""Конфигурации"""
from yaml import SafeLoader, load

import os


dir = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(dir, 'settings.yaml')


class PostgreSQL:
    """Конфигурация SQL"""
    host = ""
    port = ...
    user = ...
    password = ...
    database = ""
    database_test = ""

    def __init__(self):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            config = load(f, SafeLoader)
            if postgres := config.get("Postgres"):
                self.host = postgres.get("host", self.host)
                self.port = int(postgres.get("port", self.port))
                self.user = postgres.get("user", self.user)
                self.password = postgres.get("password", self.password)
                self.database = postgres.get("database", self.database)

class PostgreSQLTest:
    """Конфигурация тестовой БД (для pytest)"""
    host = ""
    port = ...
    user = ...
    password = ...
    database = ""
    database_test = ""

    def __init__(self):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            config = load(f, SafeLoader)
            if postgres := config.get("PostgresTest"):
                self.host = postgres.get("host", self.host)
                self.port = int(postgres.get("port", self.port))
                self.user = postgres.get("user", self.user)
                self.password = postgres.get("password", self.password)
                self.database = postgres.get("database", self.database)


class Service:
    """Конфигурация REST API"""
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
