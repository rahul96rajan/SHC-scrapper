import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import web_actions

""" Config File """
with open('json_files/config.json') as file:
    data_conf = json.load(file)
    base_url = data_conf['base_url']
    headless = (data_conf['headless'] == 'True')


""" --- Filter Selection Hierarchy ---  """

with open('json_files/state.json') as file:
    data_states = json.load(file)
    list_states = data_states['states']

with open('json_files/district.json') as file:
    dict_districts = json.load(file)

with open('json_files/sub_district.json') as file:
    dict_sub_districts = json.load(file)

with open('json_files/gram_panchayat.json') as file:
    dict_gram_panchayats = json.load(file)

with open('json_files/village.json') as file:
    dict_villages = json.load(file)


""" Setting up selenium webdriver """
options = Options()
if headless:
    options.add_argument("--headless")
    print('[INFO] RUNNING HEADLESS')
options.add_argument("--window-size=1920x1080")
chrome_driver_path = "drivers/chromedriver"
driver = webdriver.Chrome(chrome_options=options,
                          executable_path=chrome_driver_path)
driver.get(base_url)
driver.implicitly_wait(20)


web_actions.search_with_filters(
    driver, 'Punjab', 'Bathinda', 'Bathinda', 'BARKANDI', 'Warkandi (172)')

web_actions.get_all_reports(driver)
