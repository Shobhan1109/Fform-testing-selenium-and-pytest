import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setUp2():
    global moviename,year,director, distributor, producer ,driver
    moviename = input("Enter movie name:")
    year = input("Enter the release year:")
    director = input("Enter the director name:")
    distributor = input("Enter the distributor name:")
    producer = input("Enter the producer name:")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()

def test_moviedetails(setUp2):
    driver.get("https://iprimedtraining.herokuapp.com/movie.php")
    driver.find_element_by_name("mname").send_keys(moviename)
    time.sleep(1)
    driver.find_element_by_name("myear").send_keys(year)
    time.sleep(1)
    driver.find_element_by_name("mdirector").send_keys(director)
    time.sleep(1)
    driver.find_element_by_name("mdist").send_keys(distributor)
    time.sleep(1)
    driver.find_element_by_name("mproducer").send_keys(producer)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[6]/td[2]/select/option[1]").click()
    time.sleep(1)
    driver.find_element_by_name("subbtn").click()
    time.sleep(5)