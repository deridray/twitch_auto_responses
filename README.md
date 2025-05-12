# make auto responces from your name!
this script allows you to configure auto-responces in your twitch chat, and it will responce to it from your name!
![example](https://github.com/user-attachments/assets/d703c0a6-0a93-4287-a173-6297e055a9d4)
## preparation
you need to install `python`and `python-pip`. you can do this with this command:
### arch
```
sudo pacman -S python python-pip
```
### ubuntu / debian / pop!_os / linux mint
```
sudo dnf install python3 python3-pip -y
```
### fedora
```
sudo dnf install python3 python3-pip -y
```
### openSUSE
```
sudo zypper install python3 python3-pip
```
### void
```
sudo xbps-install -S python3 python3-pip
```
## installation
you need to write this commands in your terminal
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
and you're ready! enjoy!
