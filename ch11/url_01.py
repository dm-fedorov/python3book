# url_01.py
import urllib.request
import logging

def url_open(url):
    lst = list()    
    try:     
        with urllib.request.urlopen(url) as webpage:
            for line in webpage: 
                lst.append(line.decode('utf-8').strip())
        return lst
    except Exception as e:       
        # https://realpython.com/the-most-diabolical-python-antipattern/ 
        logging.exception(e)
        
if __name__ == '__main__':
    logging.basicConfig(filename='log.txt', 
                        format='%(asctime)s - %(message)s', 
                        filemode='a', 
                        level=logging.ERROR) 
    
    print(url_open("http://dfedorov.spb.ru/python3/src/romeo.txt")) 
