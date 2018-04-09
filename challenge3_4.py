# -*- coding: utf-8 -*-

import re 
from datetime import datetime

# ????????????????????
def open_parser(filename):
    with open(filename) as logfile:
        # ?????????????
        pattern = (r''
                   r'(\d+.\d+.\d+.\d+)\s-\s-\s'  # IP ??
                   r'\[(.+)\]\s'  # ??
                   r'"GET\s(.+)\s\w+/.+"\s'  # ????
                   r'(\d+)\s'  # ???
                   r'(\d+)\s'  # ????
                   r'"(.+)"\s'  # ???
                   r'"(.+)"'  # ?????
                   )
        parsers = re.findall(pattern, logfile.read())
    return parsers

def main():
    ip_dict = {}
    url_dict = {}
    # ?????????????
    logs = open_parser('/home/shiyanlou/Code/nginx.log')
    for data in logs:
      time = data[1]
      if '11/Jan/2017' in time:
        ip_dict.setdefault(data[0],0)
        ip_dict[data[0]] = ip_dict[data[0]]+1

      state = data[3]
      if '404' in state:
        url_dict.setdefault(data[2],0)
        url_dict[data[2]] = url_dict[data[2]]+1
    #print(logs)
    with open('test.txt','a') as file:
      file.write(str(ip_dict))
    return ip_dict, url_dict


if __name__ == '__main__':
    ip_dict, url_dict = main()
    print(ip_dict, url_dict)