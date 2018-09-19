# By Dominic Eggerman
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

# Run
if __name__ == '__main__':
    # Start a Chrome driver
    driver = webdriver.Chrome("C:/Users/deggerman/chromedriver_win32/chromedriver.exe")
    # Navigate to page
    driver.get("http://gcc.genscape.com/GCCcontent/intranet/manual_normalization.php")
    # Check for this string in title
    assert "Manual Operations" in driver.title
    # Find the source box, select source
    source_elem = driver.find_element_by_css_selector("#selFFPipeline")
    source_elem.send_keys("274")
    source_elem.send_keys(Keys.RETURN)
    # Find the date box, change date
    date_elem = driver.find_element_by_css_selector("#txtFFDateIn")
    driver.execute_script("arguments[0].setAttribute('value','09/25/2018')", date_elem)
    # Find the job with the desired dataset, click it
    job_table = driver.find_element_by_css_selector("#reportResultTable")
    jobs = job_table.find_element_by_css_selector("*")  # Get child elements
    print(jobs)
    # # Close the driver
    # driver.close()