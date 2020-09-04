from selenium import webdriver
import yaml

#conf = yaml.load(open('loginDetails.yml')) 

#with open('../loginDetails.yml') as f:
 #   my_yaml_file = yaml.load(f, Loader=yaml.FullLoader)
  #  print(my_yaml_file)

my_email = conf['bootcamp_user']['email']
my_password = conf['bootcamp_user']['password']

driver = webdriver.Chrome()

def login(url,usernameId, username, passwordId, password, submit_buttonId):
   driver.get(url)
   driver.find_element_by_id(usernameId).send_keys(username)
   driver.find_element_by_id(passwordId).send_keys(password)
   driver.find_element_by_id(submit_buttonId).click()

   login("https://www.bootcampspot.com/", "email", my_email, "pass", my_password, "loginbutton")