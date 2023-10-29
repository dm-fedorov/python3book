# url_02.py
import requests

if __name__ == '__main__':
    print(requests.get("http://dfedorov.spb.ru/python3/src/romeo.txt").text)