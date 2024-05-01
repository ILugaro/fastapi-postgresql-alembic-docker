"""Application main"""
from app.service import api_service

app = api_service.get_app()

if __name__ == "__main__":
    api_service.serve(path_to_app="main:app")
