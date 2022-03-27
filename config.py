from environs import Env
import os


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'private_key.json'

env = Env()
env.read_env()

TOKEN = env.str('TOKEN')
GROUP_ID = env.str('GROUP_ID')
