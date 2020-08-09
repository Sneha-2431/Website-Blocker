import time
from datetime import datetime as dt

hosts_temp = "Hosts.txt"
hosts_path =r"C:\Windows\System32\drivers\etc\hosts"  #r means passing a raw string
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 0) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 23):
        print("Working Hours...")
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
        with open(hosts_temp, 'r+') as file:
            content = file.readlines()  #Places the pointer at the end
            file.seek(0)  #Places the pointer at 0 index
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)  #Places the pointer at the end
            file.truncate()        
        print("Fun Hours...")    
    time.sleep(5)