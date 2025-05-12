# make auto responces from your name!
this script allows you to configure auto-responces in your twitch chat, and it will responce to it from your name!
![example](https://github.com/user-attachments/assets/d703c0a6-0a93-4287-a173-6297e055a9d4)
# installation
you need  to install `python`and `python-pip`.
after that do this commands:
```
git clone https://github.com/deridray/twitch_auto_responces.git
cd twitch_auto_responces
python -m venv venv
source venv/bin/activate
pip install twitchio
```
also,  you need to open `bot.py` file and modify it. replace `your_oauth_token` with your access token(you can get it from https://twitchtokengenerator.com/) and `your_channel_name` with your twitch channel name

after that, write in your terminal
```
python bot.py
```
