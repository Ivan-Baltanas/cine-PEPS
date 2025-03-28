import bcrypt

def cipher_password(password):
  hashAndSalt = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(10))
  return hashAndSalt

def compare_password(password_hash,password):
   if password_hash is None:
      return False
   try:
      return bcrypt.checkpw(password,password_hash)
   except:
      return False