""" Contains all the actions that are performed on the website
during scrapping """

import json
import time
from selenium.common.exceptions import NoSuchElementException

with open('json_files/page_objects.json') as file:
    """"
    Loads locators for page objects from `json_files/page_objects.json`,
    and stores it to gloabl variable 'page_objects' (dict).
    """
    page_objects = json.load(file)


def search_with_filters(driver, state, dist, subdist, grampanch, village):
    """
    Selects the given parameter in the respective dropdown fields and hits
    search button.

    Parameters
    ----------
    driver (selenium.webdriver): driver on which the actions are to be
                                 performed.
    state (str): name of state to be selected.
    dist (str): name of district to be selected.
    subdist (str): name of sub-district to be selected.
    grampanch (str): name of gram-panchayat to be selected.
    village (str): name of village to be selected.

    Returns
    -------
    None
    """
    driver.find_element_by_xpath(page_objects["state_selection"].
                                 replace("$STATE$", state)).click()
    # time.sleep(1)
    driver.find_element_by_xpath(page_objects["dist_selection"].
                                 replace("$DIST$", dist)).click()
    # time.sleep(1)
    driver.find_element_by_xpath(page_objects["sub_dis_selection"].
                                 replace("$SUB_DIS$", subdist)).click()
    # time.sleep(1)
    driver.find_element_by_xpath(page_objects["gram_panchayat_selection"].
                                 replace("$GRAMPANCHAYAT$", grampanch)).click()
    # time.sleep(1)
    driver.find_element_by_xpath(page_objects["village_selection"].
                                 replace("$VILLAGE$", village)).click()
    # time.sleep(1)
    driver.find_element_by_xpath(page_objects["search_button"]).click()

    print('[ACTION] Searched for filters %s' % (state + " > " + dist + " > " +
                                                subdist + " > " + grampanch +
                                                " > " + village))


def get_SHC_New_list(driver):
    """
    Fetches the list of Print links under SHC New columns.

    Parameters
    ----------
    driver (selenium.webdriver): driver on which the actions are to be
                                 performed.
    Returns
    -------
    list_of_links (list): list of webelements containing all print links.
    """
    time.sleep(2)
    list_of_links = driver.find_elements_by_xpath(
        page_objects["print_SHC_new_link"])
    return list_of_links


def save_frame(driver):
    """
    Saves the Soil health card frame as html file under `crawledHtmls`.

    Parameters
    ----------
    driver (selenium.webdriver): driver on which the actions are to be
                                 performed.
    Returns
    -------
    None
    """
    js_script = "return window.frames[0].document.body.innerHTML"
    report_content = driver.execute_script(js_script)
    ts = time.time()
    loc = "crawledHtmls/" + str(ts).replace('.', '_') + ".html"
    with open(loc, "a") as file:
        file.write(report_content)
        print("[ACTION] Wrote report contents to --> '%s'" % loc)


def click_SHC_New_and_fetch_reports(driver):
    """
    Clicks on print tag under SHC new and saves the Soil health card frame as
    html file under `crawledHtmls`.

    Parameters
    ----------
    driver (selenium.webdriver): driver on which the actions are to be
                                 performed.
    Returns
    -------
    None
    """
    all_SN_print_links = get_SHC_New_list(driver)
    for i, SN_print in enumerate(all_SN_print_links):
        SN_print.click()
        print('[ACTION] Clicked on SHC New')
        time.sleep(20)
        save_frame(driver)
        print('[ACTION] Save report for result number %d' % (i+1))


def get_all_reports(driver):
    """
    One-by-One navigates through the pages of the search results; and clicks
    on print tag under SHC new columns. Saves the Soil health card frame as
    html file. And hence, saving all the SHC for the search
    results under `crawledHtmls`.

    Parameters
    ----------
    driver (selenium.webdriver): driver on which the actions are to be
                                 performed.
    Returns
    -------
    None
    """
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
