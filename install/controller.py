from os import system
import art
from art import tprint
import shutil

def main():
    if shutil.which("fish"):
        print("fish is installed!")
    else:
        system("pkg install fish")

    system("echo 'alias proxy=\"cd ~/tg-ws-proxy/proxy && python3 tg_ws_proxy.py\"' >> ~/.config/fish/config.fish")
    system('chsh -s fish')
    system("source ~/.config/fish/config.fish")
    tprint("TERMUX PROXY")
    print("For running the proxy: proxy")

if __name__ == '__main__':
    main()
