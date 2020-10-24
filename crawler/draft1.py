import json
from selenium import webdriver
from time import sleep
from random import randint

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

""" ----------------------------------------  """


"""" ----- ALPHA TEST ARENA ----"""
print(
    dict_villages[dict_gram_panchayats[dict_sub_districts[dict_districts[list_states[-1]][-1]][-1]][-1]][-1])
""" ----------------------------------------  """

t_state = list_states[-1]
t_district = dict_districts[t_state][-1]
t_sub_district = dict_sub_districts[t_district][-1]
t_gram_panchayat = dict_gram_panchayats[t_sub_district][-1]
t_village = dict_villages[t_gram_panchayat][-1]

print(base_url)

print("{0} > {1} > {2} > {3} > {4}".format(t_state, t_district, t_sub_district,
                                           t_gram_panchayat, t_village))


# For Chrome
driver = webdriver.Chrome(executable_path="drivers/chromedriver")
driver.get(base_url)
driver.implicitly_wait(20)


with open('json_files/page_objects.json') as file:
    page_objects = json.load(file)

driver.find_element_by_xpath(page_objects["state_selection"].
                             replace("$STATE$", t_state)).click()
sleep(1)
driver.find_element_by_xpath(page_objects["dist_selection"].
                             replace("$DIST$", t_district)).click()
sleep(1)
driver.find_element_by_xpath(page_objects["sub_dis_selection"].
                             replace("$SUB_DIS$", t_sub_district)).click()
sleep(1)
driver.find_element_by_xpath(page_objects["gram_panchayat_selection"].
                             replace("$GRAMPANCHAYAT$", t_gram_panchayat)).click()
sleep(1)
driver.find_element_by_xpath(page_objects["village_selection"].
                             replace("$VILLAGE$", t_village)).click()
sleep(1)
driver.find_element_by_xpath(page_objects["search_button"]).click()
