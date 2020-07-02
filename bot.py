from selenium import webdriver
from webdriver_manager.opera import OperaDriverManager
import passwordd

#or "from webdriver_manager.chrome import ChromeDriverManager"
# you don't need to boring gecko driver docs and settings

import time

driver = webdriver.Opera(executable_path=OperaDriverManager().install())
driver.get("https://www.instagram.com")
time.sleep(1)

username=driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
username.send_keys(passwordd.username1)
password=driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")
password.send_keys(passwordd.password1)
time.sleep(1)

log_in=driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[4]/button/div")
log_in.click()
time.sleep(3)

mainpage=driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[1]/a/div/div/img")
mainpage.click()
time.sleep(2)

not_now=driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
not_now.click()
time.sleep(2)

profile=driver.find_element_by_xpath("//*[@id='react-root']/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a")
profile.click()
time.sleep(2)

fffollower=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")
fffollower.click()
time.sleep(2)

jscomand="""
followers=document.querySelector(".isgrP");
followers.scrollTo(0, followers.scrollHeight);
var lenOfPage=followers.scrollHeight;return lenOfPage;
"""
lenOfPage = driver.execute_script(jscomand)
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(2)
    lenOfPage = driver.execute_script(jscomand)
    if lastCount == lenOfPage:
        match=True
time.sleep(2)

followersList=[]
followers=driver.find_elements_by_css_selector(".FPmhX.notranslate._0imsa ")
for follower in followers:
    followersList.append(follower.text)

with open("followers.txt","w",encoding="UTF-8") as file:
    for follower in followersList:
        file.write(follower + "\n")
