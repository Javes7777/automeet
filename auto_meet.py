import sys
import time
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
import argparse 



class Automeet:
    def __init__(self, meeting_link = None):
        self.chromedriver_binary = "/usr/local/bin/chromedriver"
        self.chrome_binary = "/Users/lucifer/Documents/projects/auto-meet/chrome/Google Chrome"
        self.meeting_link = meeting_link

    def join_meeting(self):
        chrome_options = webdriver.ChromeOptions()
        driver_service=Service(self.chromedriver_binary)
        chrome_options.binary_location = self.chrome_binary
        chrome_options.add_argument("--start-maximized")
        browser = webdriver.Chrome(options=chrome_options, service=driver_service)

        # get meeting link
        browser.get(self.meeting_link)
        time.sleep(1)
        wait = True
        while wait:
            try:
                # mute and disable video monitoring
                mute_button = browser.find_element("xpath", "//div[@jsname='BOHaEe']")
                is_displayed = mute_button.is_displayed()
                is_enabled = mute_button.is_enabled()    
                if is_displayed ==True and is_enabled == True:
                    mute_button.click()
                # join the meeting
                join_button = browser.find_element("xpath", "//button[@jsname='Qx7uuf']")
                is_displayed = join_button.is_displayed()
                is_enabled = join_button.is_enabled()    
                mute_button.click()
                time.sleep(1)
                # turn on captions and capture everything
                captions_button = browser.find_element("xpath", "//button[@jscontroller='xzbRj]")
                is_displayed = captions_button.is_displayed()
                is_enabled = captions_button.is_enabled()    
                time.sleep(1) # give time for captions to be activated.
                # check for string in captions.

                captions = browser.find_element("xpath", "//div[@jsname='tgaKEf']")
                # unmute 
                is_displayed = mute_button.is_displayed()
                is_enabled = mute_button.is_enabled()  

                # play recording "Present"
            except NoSuchElementException: 
                wait = True
                time.sleep(1)
        # exit meeting.
        return 

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--meeting_link", help="provide link for the google meeting",
                    type=str, default=None)
    args = parser.parse_args()

    # am = Automeet(args.meeting_link) 
    am = Automeet("https://meet.google.com/jco-fhxe-ech")
    am.join_meeting()