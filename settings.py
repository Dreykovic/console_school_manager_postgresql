from dotenv import load_dotenv
import os
load_dotenv()
database =  os.environ.get('DATABASE')
username = os.environ.get('USERNAME')
passwd = os.environ.get('PASSWORD')
host =  os.environ.get('DATABASE_HOST')
port = int( os.environ.get('DATABASE_PORT'))

