from bs4 import BeautifulSoup
import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from autopass import secrets


def main():
    html = extractCalendar()
    readCalendar(html, 15)
# Load webpage and extract the


def extractCalendar():
    url = "https://umd.libcal.com/reserve/mckeldin/carrels-8hr"
    driver = webdriver.Chrome()
    driver.get(url)
    calendarOpenButton = '//*[@id="eq-time-grid"]/div[1]/div[1]/button[1]'
    driver.find_element_by_xpath(calendarOpenButton).click()
    html = driver.page_source
    return html
# Read in calendar to find the date you want to return the xpath for that day


def readCalendar(html, date):
    soup = BeautifulSoup(html, 'html.parser')
    currentDay = soup.find('td', {'class': 'today day'}).contents[0]
    curr = False
    counter = 0
    dateResult = 0
    calTable = soup.find_all('table', {'class': 'table-condensed'})[0]
    for tr in calTable.find_all('tr'):
        for td in tr.find_all('td'):
            if curr:
                counter += 1
                if counter == 15:
                   dateResult = td.contents[0]
            if currentDay == td.contents[0]:
                curr = True
                counter = 1
            if dateResult > 0:
                pass


#steps
#load the page
#click on calendar
# Read calendar dates
# Choose timeframe
#submit time slot
#Click on continue
#fill out personal information
#submit booking
if __name__ == "__main__":
    my_function()
