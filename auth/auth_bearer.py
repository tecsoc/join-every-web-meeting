from decouple import config
from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

SECRET = config("secret")


class AuthBearer(HTTPBearer):
  def __init__(self, auto_error: bool = True):
    super().__init__(auto_error=auto_error)

  async def __call__(self, request: Request):
    credentials: HTTPAuthorizationCredentials = await super().__call__(request)
    if credentials:
      if credentials.scheme != "Bearer":
        raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
        
      token = credentials.credentials
      if not self.verify_token(token):
        raise HTTPException(status_code=403, detail="Invalid token or expired token.")
      return token
      
    else:
      raise HTTPException(status_code=403, detail="Invalid authorization code.")

  def verify_token(self, token: str):
    return token == SECRET
