from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from autopass import secrets


def main():
    html = extractCalendar()
    readCalendar(html, 15)
    submitInformation(datexpath)
# Load webpage and extract the


def extractCalendar():
    url = "https://umd.libcal.com/reserve/mckeldin/carrels-8hr"
    driver = webdriver.Chrome()
    driver.get(url)
    calendarOpenButton = '//*[@id="eq-time-grid"]/div[1]/div[1]/button[1]'
    driver.find_element_by_xpath(calendarOpenButton).click()
    html = driver.page_source
    return html
# Read in calendar to find the date you want and select


def readCalendar(html, date):
    soup = BeautifulSoup(html, 'html.parser')
    currentDay = soup.find('td', {'class': 'today day'}).contents[0]
    curr = False
    counter = 0
    dateResult = 0
    tdCount = 0
    trCount = 0
    calTable = soup.find_all('table', {'class': 'table-condensed'})[0]
    for tr in calTable.find_all('tr'):
        trCount+=1
        for td in tr.find_all('td'):
            tdCount+=1
            if curr:
                counter += 1
                if counter == date:
                   datexpath = f'//*[@id="equip_"]/div[6]/div[1]/table/tbody/tr[{trCount}]/td[{tdCount}]'
                   driver.find_element_by_xpath(datexpath).click()
            if currentDay == td.contents[0]:
                curr = True
                counter = 1
# Click on date
def selectTime(html,time):
    pass


def submitInformation(datexpath):
    dateSubmitButton = '//*[@id="submit_times"]'
    driver.find_element_by_xpath(dateSubmitButton).click()
    continueButton = '//*[@id="terms_accept"]'
    driver.find_element_by_xpath(continueButton).click()
    firstNameInput = '//*[@id="fname"]'
    firstName = secrets.FNAME()
    driver.find_element_by_xpath(firstNameInput).send_keys(firstName)
    lastNameInput = '//*[@id="lname"]'
    lastName = secrets.LNAME()
    driver.find_element_by_xpath(firstNameInput).send_keys(lastName)
    emailInput = '//*[@id="email"]'
    email = secrets.EMAIL()
    driver.find_element_by_xpath(firstNameInput).send_keys(email)
    uid = secrets.UID()
    UIDInput = '//*[@id="q16114"]'
    driver.find_element_by_xpath(firstNameInput).send_keys(uid)
    submitBookingButton = '//*[@id="btn-form-submit"]'
    driver.find_element_by_xpath(submitBookingButton).click()

    
    



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
    main()
