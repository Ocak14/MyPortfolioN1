import requests

from environs import Env

env = Env()
env.read_env()


def  send_message(text):
  BOT_TOKEN = env.str("BOT_TOKEN")
  CHAT_ID = env.str("CHAT_ID")
  PHOTO = "https://images.msha.ke/79435acc-ce5f-4bd8-8ef3-04a4a73497c7?auto=format%2Ccompress&cs=tinysrgb&q=30&w=828"
  TEXT = text
  url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendphoto?chat_id={CHAT_ID}&photo={PHOTO}&caption={TEXT}"
  response = requests.get(url)



