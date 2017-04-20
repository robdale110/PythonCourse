import time
from datetime import datetime as dt

hosts_path = "/etc/hosts"
hosts_temp = "hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 16) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working hours!")
        with open(hosts_temp, "r+") as file:
            contents = file.read()
            
            for website in website_list:
                if website in contents:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_temp, "r+") as file:
            contents = file.readlines()

            file.seek(0)

            for line in contents:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours!")

    time.sleep(5)
