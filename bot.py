from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time
opts = Options()
opts.headless = True
driver = Chrome(options=opts, executable_path='/usr/local/bin/chromedriver')
import discord

user = "" #hetzner login 
userpass = ""

def restartserver():
    try:
        driver.get('https://robot.your-server.de/server')
        time.sleep(3)
        inputElement = driver.find_element_by_id("_username")
        inputElement.send_keys(user)
        inputElement = driver.find_element_by_id("_password")
        inputElement.send_keys(userpass)
        time.sleep(3)
        driver.find_element_by_id("submit-login").click()
        time.sleep(3)
        driver.find_element_by_id("id").click() #replace id with your id 
        time.sleep(3)
        driver.find_element_by_id("reset_id_tab").click() #replace id with your id 
        time.sleep(3)
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="resetid"]/table/tbody/tr[3]/td/input[3]').click() #replace id with your id  
        time.sleep(3)
    except Exception as e:
        print(e)
    finally:
        print("server restarted.")
        driver.quit()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('.restart'):
            await message.reply('Restarting the ENTIRE server.', mention_author=True)
            restartserver()
client = MyClient()
client.run('Token') #replace token with your token 
