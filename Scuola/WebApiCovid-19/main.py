from selenium import webdriver
from time import sleep
import sqlite3
import schedule

class Coronavirus():
    def __init__(self):
        user_agent = "Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36"

        options = webdriver.FirefoxOptions()

        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", user_agent)

        options.add_argument('-headless')

        self.driver = webdriver.Firefox(profile, executable_path='geckodriver', options=options)

        self.driver.set_window_size(500, 720)

    def clean(self, current):
        for x in current:
            if x.startswith('+'):
                current.remove(x)

        return current[0:3]

    def saveOnDb(self, table):
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute('DELETE FROM DatiCovid')
        for t in table:
            current = t.split(' ')
            cleaned = self.clean(current)

            if str.isnumeric(cleaned[1]):
                cur.execute('INSERT INTO DatiCovid(country, total_cases, total_deaths) VALUES(?,?,?)', (cleaned[0], cleaned[1], cleaned[2],))
                conn.commit()


        conn.close()

    def table(self):
        table = str(self.driver.find_element_by_xpath('//*[@id="main_table_countries_today"]').text).split('\n')[10:]
        self.saveOnDb(table)

def job():
    bot = Coronavirus()
    bot.driver.get('https://www.worldometers.info/coronavirus/')
    sleep(4)
    bot.table()

schedule.every().day.at("12:00").do(job)
schedule.every().day.at("15:00").do(job)
schedule.every().day.at("18:00").do(job)
schedule.every().day.at("21:00").do(job)


while True:
    schedule.run_pending()
    sleep(1)
