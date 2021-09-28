import os
from dotenv import load_dotenv, find_dotenv

def get_env(name):
	load_dotenv(find_dotenv())
	return os.getenv(f'{name}')