import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format = '[%(asctime)s]: %(message)s:')

list_of_files=[
    "controller/__init__.py",
    "controller/app_controller/__init__.py",
    "controller/auth_controller/__init__.py",
    "controller/auth_controller/authentication.py",
    "face_auth/logger/__init__.py",
    "face_auth/exception/__init__.py",
    "face_auth/utils/__init__.py",
    "face_auth/entity/__init__.py",
    "face_auth/data_access/__init__.py",
    "face_auth/config/__init__.py",
    "face_auth/business_val/__init__.py",
    "face_auth/business_val/user_val.py",
    "setup.py",
    "requirements.txt",
    "app.py"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
            
    else:
        logging.info(f"{filename} already exists")