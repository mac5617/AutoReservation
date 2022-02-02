from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from autopass import secrets


def main():
    driver = webdriver.Chrome()
    Calendar(driver, day=15)
    selectTime(driver,room='6239',time='9:30')
def Calendar(driver,day:int):
    """
        Method loads the calendar then clicks on the day that you have given.
        Days: Number of days from current time. Max is 15.
        Example: 0 is today, 1 is tommorrow
    """
    #Load Webpage
    driver.get('https://umd.libcal.com/reserve/mckeldin/carrels-8hr')
    #Open Calendar
    driver.find_element(By.XPATH,'//*[@id="eq-time-grid"]/div[1]/div[1]/button[1]').click()
    for i in range(15):
        driver.find_element(By.XPATH,'//*[@id="eq-time-grid"]/div[1]/div[1]/div/button[2]/i').click()


def selectTime(driver,room:str,time:str):
    """
        Method selects the time given according to the room.
        room: string of 8 hour room number.
        Example: '6223'
        time: 12 hour format string 
        Example: '9:30' or '23:00'

    """
    html = driver.page_source
    roomdict = {
        '6223':1,
        '6225':2,
        '6227':3,
        '6229':4,
        '6231':5,
        '6235':6,
        '6237':7,
        '6239':8,
        '6241':9,
        '6243':10,
        '6245':11,
    }
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table',{'class':'fc-scrollgrid-sync-table table-bordered'})

    hour = 1 + int(time.split(':')[0])*2
    minute = int(time.split(':')[1])
    if minute == 30:
        hour+=1

    timePath = f'//*[@id="eq-time-grid"]/div[2]/div/table/tbody/tr/td[3]/div/div/div/table/tbody/tr[{roomdict.get(room)}]/td/div/div[2]/div[{hour}]/a'
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, timePath)))
    driver.find_element(By.XPATH,timePath).click()
    driver.implicitly_wait(100)
    driver.find_element(By.XPATH,'//*[@id="submit_times"]').click()

def submitInformation(driver):
    """
        Method takes information from secret and submit the information
        Secret is just a dictionary in another file
    """
    driver.find_element_by_xpath('//*[@id="fname"]').send_keys(secrets.get('FNAME'))
    driver.find_element_by_xpath('//*[@id="lname"]').send_keys(secrets.get('LNAME'))
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(secrets.get('EMAIL'))
    driver.find_element_by_xpath('//*[@id="q16114"]').send_keys(secrets.get('UID'))
    driver.find_element_by_xpath('//*[@id="btn-form-submit"]').click()

if __name__ == "__main__":
    main()
