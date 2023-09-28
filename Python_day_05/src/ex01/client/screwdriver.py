import requests
import mimetypes
from bs4 import BeautifulSoup
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('action', choices=['list', 'upload'], help='Action to perform (upload, list)')
parser.add_argument('file_path', nargs='?', help='Path to the file to upload (only for "upload" action)')

args = parser.parse_args()

url = 'http://127.0.0.1:8888/'
# headers = {'Content-type': mimetypes.guess_type(args.file_path)[0]}

if args.action == 'list':
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    for music in soup.find_all('p'):
        print(music.text)
elif args.action == 'upload':
    file = {'music': open(args.file_path, 'rb')}
    x = requests.post(url, files=file)