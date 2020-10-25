import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import web_actions


def read_json_files():
    jsons = dict()
    """ Config File """
    with open('json_files/config.json') as file:
        data_conf = json.load(file)
        jsons['base_url'] = data_conf['base_url']
        jsons['implicit_wait'] = data_conf['implicit_wait']
        jsons['is_headless'] = (data_conf['headless'] == 'True')

    with open('json_files/state.json') as file:
        data_states = json.load(file)
        jsons['list_states'] = data_states['states']

    with open('json_files/district.json') as file:
        jsons['dict_districts'] = json.load(file)

    with open('json_files/sub_district.json') as file:
        jsons['dict_sub_districts'] = json.load(file)

    with open('json_files/gram_panchayat.json') as file:
        jsons['dict_gram_panchayats'] = json.load(file)

    with open('json_files/village.json') as file:
        jsons['dict_villages'] = json.load(file)

    return jsons


def init_driver(headless, imp_wait):
    """ Setting up selenium webdriver """
    options = Options()
    if headless:
        options.add_argument("--headless")
        print('[INFO] RUNNING HEADLESS')
    options.add_argument("--window-size=1920x1080")
    chrome_driver_path = "drivers/chromedriver"
    driver = webdriver.Chrome(chrome_options=options,
                              executable_path=chrome_driver_path)
    driver.implicitly_wait(imp_wait)
    return driver


def _test():
    json_dicts = read_json_files()
    driver = init_driver(
        json_dicts['is_headless'], json_dicts['implicit_wait'])
    driver.get(json_dicts['base_url'])
    web_actions.search_with_filters(
        driver, 'Punjab', 'Bathinda', 'Bathinda', 'BARKANDI', 'Warkandi (172)')
    web_actions.get_all_reports(driver)
    driver.quit()


if __name__ == "__main__":
    _test()
