# By Dominic Eggerman
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime

# Generate date range
def dateRangeGenerator():
    # Prepare start and end dates
    start_date = input("Start date (MM/DD/YYYY): ")
    month, day, year = map(int, start_date.split("/"))
    start_date = datetime.date(year, month, day)
    end_date = input("End date (MM/DD/YYYY): ")
    month, day, year = map(int, end_date.split("/"))
    end_date = datetime.date(year, month, day)

    # Return [range of dates] (inclusive)
    num_days = end_date - start_date
    return [(start_date + datetime.timedelta(days=d)).strftime("%m/%d/%Y") for d in range(0, num_days.days+1)]

# Run
if __name__ == '__main__':
    # List of strings for status of run
    log = []

    # Get the date range
    dates = dateRangeGenerator()

    try:
        # Start a Chrome driver
        driver = webdriver.Chrome("C:/Users/deggerman/chromedriver_win32/chromedriver.exe")
        # Navigate to page
        driver.get("http://gcc.genscape.com/GCCcontent/intranet/manual_normalization.php")
        # Wait and check for this string in title
        time.sleep(2)
        assert "Manual Operations" in driver.title
        # Wait, find the source box, select source
        time.sleep(2)
        source_elem = driver.find_element_by_css_selector("#selFFPipeline")
        source_elem.send_keys("407")
        time.sleep(0.1)
        source_elem.send_keys(Keys.RETURN)
        # Wait, find the date box, change date
        time.sleep(2)
        date_elem = driver.find_element_by_css_selector("#txtFFDateIn")
        driver.execute_script("arguments[0].setAttribute('value','09/25/2018')", date_elem)
        # Wait, find the job with the desired dataset, click it
        time.sleep(2)
        job_table = driver.find_element_by_css_selector("#reportResultTable")
        jobs = job_table.find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")  # Get table rows

        # Find opavail arg
        for j in jobs:
            arg = j.find_elements_by_tag_name("td")[2]
            if arg.text == "manualRun=true":
                # Select the job as an option
                option = j.find_elements_by_tag_name("td")[0].find_element_by_tag_name("input")
                # Click it
                option.click()
                break

        # Click fetch
        fetcher = driver.find_element_by_id("cmdFF")
        fetcher.click()
        time.sleep(10)
        
        # Loop until status is seen
        # Code for undefined table ??

        # Switch driver to iFrame
        driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[1])
        # Check for completed status message
        while driver.find_element_by_class_name("statusMessageSuccess").text in ("Not started yet", "Fetcher in Progress", "Normalizer in Progress", "Completed Normalizer", "Loader in Progress"):
            time.sleep(2)

        # Status
        status_message = driver.find_element_by_class_name("statusMessageSuccess").text
        print(status_message)
        log.append(status_message)

        time.sleep(2)
        driver.close()
    
    except KeyboardInterrupt:
        # Close the driver
        driver.close()