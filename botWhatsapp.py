from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

# parameters
WP_URL = "https://web.whatsapp.com/"

# xpaths
CONTACTS = '//*[@id="main"]/header/div[2]/div[2]/span'
SEND = '//*[@id="main"]/footer/div[1]/div[3]/button'
MESSAGE_BOX = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
NEW_CHAT = '//*[@id="side"]/header/div[2]/div/span/div[2]/div'
SEARCH_CONTACT = (
    '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/div/div[2]'
)
FIRST_CONTACT = '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div/span'


class WhatsAppBot:
    def __init__(self):
        self.driver = self._setup_driver()
        self.driver.get(WP_URL)
        print("Scan QR Code, And then Enter")

    @staticmethod
    def _setup_driver():
        print("Loading...")
        chrome_options = Options()
        chrome_options.add_argument("disable-infobars")
        driver = webdriver.Chrome(options=chrome_options)
        return driver

    def _get_element(self, xpath, attempts=5, _count=0):
        """Safe get_element method with multiple attempts"""
        try:
            element = self.driver.find_element_by_xpath(xpath)
            return element
        except Exception as e:
            if _count < attempts:
                sleep(1)
                self._get_element(xpath, attempts=attempts, _count=_count + 1)
            else:
                print("Element not found")

    def _click(self, xpath):
        el = self._get_element(xpath)
        el.click()

    def _send_keys(self, xpath, message):
        el = self._get_element(xpath)
        el.send_keys(message)

    def write_message(self, contact, message):
        self._click(NEW_CHAT)
        self._send_keys(SEARCH_CONTACT, contact)
        sleep(2)
        self._click(FIRST_CONTACT)
        sleep(2)
        self._click(MESSAGE_BOX)
        self._send_keys(MESSAGE_BOX, message)
        self._click(SEND)

    def send_message(self, contact, message):
        self.write_message(contact, message)
        sleep(2)

    def send_messages(self, contacts, message):
        for contact in contacts:
            self.send_message(contact, message)
        print("Messages sent to all users")

    def get_group_numbers(self):
        try:
            el = self.driver.find_element_by_xpath(CONTACTS)
            return el.text.split(",")
        except Exception as e:
            print(e)
            print("Failed to get group numbers")

    # def get_group_numbers(self):
    #     try:
    #         self._click(CONTACTS)
    #         sleep(2)
    #         contacts = self.driver.find_elements_by_class_name('_3ko75')
    #         contacts = [c.text for c in contacts]
    #         return contacts
    #     except Exception as e:
    #         print(e)
    #         print('Failed to get group numbers')
    #         return None

    def send_message_to_new_users(self, new_users, message):
        for user in new_users:
            self.send_message(user, message)
        print("Messages sent to new users")

    def search_contact(self, keyword):
        """Write and send message"""
        self._click(NEW_CHAT)
        self._send_keys(SEARCH_CONTACT, keyword)
        sleep(2)
        self._click(FIRST_CONTACT) 
        sleep(2)
        try:
            self._click(FIRST_CONTACT)
        except Exception as e:
            print(e)
            print("Contact not found")

    def get_all_messages(self):
        """Get all messages in chat"""
        try:
            messages = self.driver.find_elements_by_class_name("_12pGw")
            messages = [m.text for m in messages]
            return messages
        except Exception as e:
            print(e)
            print("Failed to get all messages")
            return None

    def get_last_message(self):
        """Get last message in chat"""
        try:
            messages = self.get_all_messages()
            return messages[-1]
        except Exception as e:
            print(e)
            print("Failed to get last message")
            return None

if __name__ == "__main__":
    bot = WhatsAppBot()
    bot.send_message_to_new_users(["111111111111"], "Hi, welcome!")
    bot.send_messages(["111111111111"], "Hello!")
    bot.search_contact("111111111111")
    print(bot.get_all_messages())
    print(bot.get_last_message())
