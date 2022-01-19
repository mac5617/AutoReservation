from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from autopass import secrets


def main():
    html = extractCalendar()
    xpath = readCalendar(html, 15)
    print(xpath)
    submitInformation(xpath)
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
                   return f'//*[@id="equip_"]/div[6]/div[1]/table/tbody/tr[{trCount}]/td[{tdCount}]'
            if currentDay == td.contents[0]:
                curr = True
                counter = 1
def submitInformation():
    
    
    
    firstName = secrets.FNAME()
    lastName = secrets.LNAME()
    email = secrets.EMAIL()
    uid = secrets.UID()

    dateSubmitButton = '//*[@id="submit_times"]'
    continueButton = '//*[@id="terms_accept"]'
    firstNameInput = '//*[@id="fname"]'
    lastNameInput = '//*[@id="lname"]'
    emailInput = '//*[@id="email"]'
    UIDInput = '//*[@id="q16114"]'
    submitBookingButton = '//*[@id="btn-form-submit"]'



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
