from selenium import webdriver
from selenium.webdriver.common import keys
import time

lst = []
### ENTER YOUR INSTAGRAM USERNAME HERE AND THEN RUN THE FILE
username_email = input("your insta username comes here:> ")
### ENTER YOUR INSTAGRAM PASSWORD HERE AND THEN RUN THE FILE
user_password = input("your insta password comes here:> ")
print("PLEASE MAKE SURE THAT YOU HAVE A ACTIVE INTERNET CONNECTION.\nAuthenticating.......")


class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get("https://www.instagram.com/accounts/login/?hl=en&source=auth_switcher")
        time.sleep(5)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(keys.Keys.ENTER)
        time.sleep(5)

    def likehashtags(self,hashtag):
        bot = self.bot
        hashtags = '#' + hashtag
        bot.get("https://www.instagram.com/explore/tags/"+hashtag+'/')
        time.sleep(6)
        for i in range(1, 5):
            bot.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(4)
            hrefs = bot.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        print(len(pic_hrefs))
        try:
            pic_hrefs = pic_hrefs[0:len(pic_hrefs)+1]
        except:
            pass
        t = 1
        for i in pic_hrefs:
            print(t)
            t += 1
            bot.get(i)
            bot.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            try:
                time.sleep(2)
                bot.find_element_by_xpath('//span/button[@class="dCJp8 afkep _0mzm-"]').click()
                time.sleep(10)
            except Exception as e:
                time.sleep(20)

print("for BEST hashtags search GOOGLE \nfrom our opinion here are some: \n>instagood \n>love \n>photooftheday")
st = input("Please input your desired name or hashtag(without #) (please use best hashtags for the best results):> ")
if len(st) >= 1:
    lst.append(st)
    for i in lst:
        ls = i
        no = InstaBot(username_email, user_password)
        time.sleep(3)
        no.login()
        no.likehashtags(ls)
else:
    print("please enter any hashtag!!!!")
  
