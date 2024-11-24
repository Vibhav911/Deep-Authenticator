from rope.base.utils import deprecated
import re
import sys
from typing import Optional

from pydantic.fields import Deprecated
from face_auth.exception import AppException
from passlib.context import CryptContext


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class LoginValidation:
    """ _summary_"""
    
    def __init__(self, email_id: str, password: str):
        """
        _summary_
        
        Args:
            email_id (str): _description_
            password (str): _description_
        """
        
        self.email_id = email_id
        self.password = password
        self.regrex = re.combine(
            r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
        )
        
        def validate(self):
            try:
                msg = ""
                if not self.email_id:
                    msg += "Email Id is not provided"
                if not self.password:
                    msg += "Password is not provided"
                if not self.is_email_valid():
                    msg += "Email Id is not valid"
                return msg
            except Exception as e:
                raise AppException(e, sys)
                
        def is_email_valid(self) -> bool:
            try:
                if re.fullmatch(self.regrex, self.email_id):
                    return True
                else:
                    return False
                
            except Exception as e:
                raise AppException(e, sys)
                
        def validate_login(self):
            try:
                if len(self.validate) != 0:
                    return {"status": False, "msg": self.validate()}
                return {"status":True}
            except Exception as e:
                raise AppException(e, sys)
                
        def verify_password(self, plain_password: str, hashed_password: str) -> bool:
            """Verify hashed password and plain password.
            Args:
                plain_password (str): _description_
                hashed_password (str): _description
            Returns:
                bool: _description_
            """    
            return bcrypt_context.verify(plain_password, hashed_password)