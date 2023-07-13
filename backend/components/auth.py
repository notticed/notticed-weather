from config import *
from tokens import *
from coords import *

@app.post('/login', tags=['auth'])
def login(user: User, res: Response, req: Request):
  """
  The login method take the data from Login scheme and then compare this data with data in database,
  after this send a response with tokens or with errors
  """
  # check for no tokens
  token.auth_token(res, req)

  # get user_indentity from database
  payload = users_weather.find_one({'email': user.email})
  
  # check the user in database
  if payload != None:
    if check_hashing(user.password, payload['password']):
      
      res.set_cookie(key="access_token_cookie", value=token.create_access_token(str(payload['_id']), coords()), samesite="none", secure=True, max_age=900, expires=ACCESS_TOKEN_EXPIRE_DELTA)
      res.set_cookie(key="refresh_token_cookie", value=token.create_refresh_token(), samesite="none", secure=True, max_age=900, expires=REFRESH_TOKEN_EXPIRE_DELTA)
      return 'OK'
    else:
      raise HTTPException(status_code=401, detail='Password is incorrect')
  users_weather.insert_one(user_payload(user.email, user.password))
  payload = users_weather.find_one({'email': user.email})
  res.set_cookie(key="access_token_cookie", value=token.create_access_token(str(payload['_id']), coords()), samesite="none", secure=True, max_age=900, expires=ACCESS_TOKEN_EXPIRE_DELTA)
  res.set_cookie(key="refresh_token_cookie", value=token.create_refresh_token(), samesite="none", secure=True, max_age=900, expires=REFRESH_TOKEN_EXPIRE_DELTA)
  return 'User created'

@app.get('/api/logout', tags=['auth'])
def logout (res: Response):

  """
  The simplest method in this file. Just unset tokens from cookies and that's all.
  """
  res.delete_cookie(key="access_token_cookie")
  res.delete_cookie(key="refresh_token_cookie")
  return "Tokens have been deleted"

@app.get("/users")
def users():
  result = []
  for n in users_weather.find():
    n['_id'] = str(n['_id'])
    result.append(n)

  return result

@app.post("/change_city")
def change_city(city, res: Response, req: Request):
  payload = token.tokens(res, req)
  res.set_cookie(key="access_token_cookie", value=token.create_access_token(str(payload['user_id']), city))
  res.set_cookie(key="refresh_token_cookie", value=token.create_refresh_token())
  return "City was changed"