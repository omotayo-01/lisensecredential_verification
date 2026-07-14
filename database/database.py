import sqlite3
DATABASE_NAME= "Credential_verification.db"
def get_connection():
  return sqlite3.connect(DATABASE_NAME)

