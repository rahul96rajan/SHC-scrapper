import json
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
# from random import randint

""" Config File """
with open('json_files/config.json') as file:
    data_conf = json.load(file)
    base_url = data_conf['base_url']


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


# For Chrome
driver = webdriver.Chrome(executable_path="drivers/chromedriver")
driver.get(base_url)
driver.implicitly_wait(20)


with open('json_files/page_objects.json') as file:
    page_objects = json.load(file)


def search_with_filters(state, dist, subdist, grampanch, village):
    driver.find_element_by_xpath(page_objects["state_selection"].
                                 replace("$STATE$", state)).click()
    time.sleep(1)
    driver.find_element_by_xpath(page_objects["dist_selection"].
                                 replace("$DIST$", dist)).click()
    time.sleep(1)
    driver.find_element_by_xpath(page_objects["sub_dis_selection"].
                                 replace("$SUB_DIS$", subdist)).click()
    time.sleep(1)
    driver.find_element_by_xpath(page_objects["gram_panchayat_selection"].
                                 replace("$GRAMPANCHAYAT$", grampanch)).click()
    time.sleep(1)
    driver.find_element_by_xpath(page_objects["village_selection"].
                                 replace("$VILLAGE$", village)).click()
    time.sleep(1)
    driver.find_element_by_xpath(page_objects["search_button"]).click()

    print('[ACTION] Searched for filters %s' % (state + " > " + dist + " > " +
                                                subdist + " > " + grampanch +
                                                " > " + village))


def get_SHC_New_list():
    time.sleep(2)
    return driver.find_elements_by_xpath(page_objects["print_SHC_new_link"])


def save_frame():
    js_script = "return window.frames[0].document.body.innerHTML"
    report_content = driver.execute_script(js_script)
    ts = time.time()
    loc = "crawledHtmls/" + str(ts).replace('.', '_') + ".html"
    with open(loc, "a") as file:
        file.write(report_content)
        print("[ACTION] Wrote report contents to --> '%s'" % loc)


# def click_SHC_New_and_fetch_report():
#     driver.find_element_by_xpath(page_objects["print_SHC_new_link"]).click()
#     print('[ACTION] Clicked on SHC New')
#     time.sleep(10)
#     save_frame()

def click_SHC_New_and_fetch_reports():
    all_SN_print_links = get_SHC_New_list()
    for i, SN_print in enumerate(all_SN_print_links):
        SN_print.click()
        print('[ACTION] Clicked on SHC New')
        time.sleep(10)
        save_frame()
        print('[ACTION] Save report for result number %d' % (i+1))


# search_with_filters(t_state, t_district, t_sub_district,
#                     t_gram_panchayat, t_village)
search_with_filters('Punjab', 'Bathinda', 'Bathinda',
                    'BARKANDI', 'Warkandi (172)')

# click_SHC_New_and_fetch_reports()


def get_all_reports():
    flag = True
    counter = 1
    while flag:
        try:
            print("[INFO] On page number : ", counter)
            click_SHC_New_and_fetch_reports()
            driver.find_element_by_xpath(page_objects["next_page"]).click()
            counter += 1
            time.sleep(1)
        except NoSuchElementException:
            print("[INFO] Reached on the last page")
            flag = False


get_all_reports()
