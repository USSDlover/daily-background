import requests
import yaml
from yaml.loader import SafeLoader
import subprocess


class Unsplash:
    url = ''
    access_key = ''
    secret_key = ''

    def __init__(self, url, access_key, secret_key):
        self.url = url
        self.access_key = access_key
        self.secret_key = secret_key


def set_background(img):
    subprocess.run("gsettings set org.gnome.desktop.background picture-uri 'file://address'".format())


def get_config():
    with open('config.local.yml') as config:
        unsplash_data = yaml.load(config, Loader=SafeLoader)['unsplash']
        unsplash = Unsplash(unsplash_data[0]['url'], unsplash_data[1]['access_key'], unsplash_data[2]['secret_key'])
        get_photo(unsplash=unsplash)


def get_photo(unsplash):
    response = requests.get(unsplash.url, auth=('Client-ID', unsplash.access_key))
    print(response)


if __name__ == '__main__':
    get_config()
