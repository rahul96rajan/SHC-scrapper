""" Contains all the actions that are performed on the website
during scrapping """

import json
import time
from selenium.common.exceptions import NoSuchElementException

with open('json_files/page_objects.json') as file:
    """" Loading locators for page objects from json_files/page_objects.json
         And storing it to gloabl object 'page_objects'. """
    page_objects = json.load(file)


def search_with_filters(driver, state, dist, subdist, grampanch, village):
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


def get_SHC_New_list(driver):
    time.sleep(2)
    return driver.find_elements_by_xpath(page_objects["print_SHC_new_link"])


def save_frame(driver):
    js_script = "return window.frames[0].document.body.innerHTML"
    report_content = driver.execute_script(js_script)
    ts = time.time()
    loc = "crawledHtmls/" + str(ts).replace('.', '_') + ".html"
    with open(loc, "a") as file:
        file.write(report_content)
        print("[ACTION] Wrote report contents to --> '%s'" % loc)


def click_SHC_New_and_fetch_reports(driver):
    all_SN_print_links = get_SHC_New_list(driver)
    for i, SN_print in enumerate(all_SN_print_links):
        SN_print.click()
        print('[ACTION] Clicked on SHC New')
        time.sleep(10)
        save_frame(driver)
        print('[ACTION] Save report for result number %d' % (i+1))


def get_all_reports(driver):
    flag = True
    counter = 1
    while flag:
        try:
            print("[INFO] On page number : ", counter)
            click_SHC_New_and_fetch_reports(driver)
            driver.find_element_by_xpath(page_objects["next_page"]).click()
            counter += 1
            time.sleep(1)
        except NoSuchElementException:
            print("[INFO] Reached on the last page")
            flag = False
