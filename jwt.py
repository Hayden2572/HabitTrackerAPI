import json
import base64
from datetime import timedelta, datetime
import hmac
import hashlib 

SECRET_KEY = "ttTTT-march-tTzTTffff"

class JWT:
    def __init__(self, SECRET_KEY):
        self.SECRET_KEY = SECRET_KEY

    def _base64Encode(self, data: dict) -> str:
        pass

    def _base64Decode(self, b64Str: str) -> dict:
        pass

    def createAccessToken(self, userID: int, expireMinutes: int = 15) -> str:
        pass

    def createRefreshToken(self, userID: int, expireMinutes: int = 15) -> str:
        pass