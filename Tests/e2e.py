from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("chromedriver.exe")


def test_scores_service():
    driver.get("http://127.0.0.1:5000/")
    score_element = int(driver.find_element(by=By.ID, value="score").text)
    print(score_element)
    driver.close()
    if 1000 >= score_element >= 1:
        return True
    else:
        return False


def main_function():
    test = test_scores_service()
    if test:
        return 0
    else:
        return -1


print(main_function())
