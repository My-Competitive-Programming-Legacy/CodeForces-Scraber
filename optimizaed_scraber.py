from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import os
import pyperclip
import traceback
from LANGUAGES import extensions  # languages supported by codeforces
from PARAMETERS import *


def add_problems_to_directory(problem_name, source_code, language):
    extension = 'cpp'
    if language in extensions:
        extension = extensions[language]
    else:
        print("Error in finding the extensions of the language {}. We will".format(language))

    try:
        f = open("{}/{}.{}".format(result_folder_name, problem_name, extension), "w")
        f.write(source_code)
        f.close()
    except:
        print("We couldn't name problem {}".format(problem_name))


def login(driver):
    driver.get("https://codeforces.com/enter")
    driver.find_element_by_id("handleOrEmail").send_keys(handle_name)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_class_name("submit").click()
    time.sleep(10)


def get_problems(driver):
    problems_done = set()
    unlisted_problems = []
    for page in range(first_page, last_page + 1, 1):
        driver.get("https://codeforces.com/submissions/{}/page/{}".format(handle_name, page))
        table = driver.find_element_by_class_name("status-frame-datatable")
        submissions = table.find_elements_by_tag_name("tr")
        for submission in submissions:
            data = submission.find_elements_by_tag_name("td")
            if len(data) > 0 and (data[5].text == "Accepted"):
                problem_name = data[3].text
                language = data[4].text
                if problem_name not in problems_done:
                    try:
                        problems_done.add(problem_name)
                        print(problem_name)
                        data[0].find_element_by_tag_name('a').click()
                        popup = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "facebox")))
                        popup = popup.find_element_by_class_name("popup")
                        copy_code_button = WebDriverWait(popup, 10).until(
                            EC.element_to_be_clickable((By.ID, "program-source-text-copy")))
                        copy_code_button.click()
                        source_code = pyperclip.paste()
                        source_code = "\n".join(source_code.splitlines())
                        add_problems_to_directory(problem_name, source_code, language)
                        popup = WebDriverWait(popup, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "close")))
                        popup.click()
                    except:
                        traceback.print_exc()
                        print("Sorry but problem {} couldn't be listed".format(problem_name))
                        unlisted_problems.append(problem_name)
            time.sleep(1)
        print("Page {} done successfully ".format(page))
    return unlisted_problems
