from optimizaed_scraber import *

try:
    os.mkdir(result_folder_name)
except:
    print("Folder found, we won't create it again ")

driver = webdriver.Chrome(PATH)
driver.maximize_window()
login(driver)
unlisted_problems = get_problems(driver)
driver.close()

print("Scrabing finished Successfully :) ")

if len(unlisted_problems) == 0:
    print("All encountered problems were successfully added ")
else:
    print("{} problems couldn't be extracted:".format(len(unlisted_problems)))
    for problem in unlisted_problems:
        print(problem)
