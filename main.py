from selenium import webdriver
import time
import sqlite3
import re
from elements import chem_data

conn = sqlite3.connect('Data/Chemistry.db')
c = conn.cursor()

driver = webdriver.Chrome(executable_path='Driver/chromedriver.exe')


def SearchChemical(Chemical):
    driver.get("https://kinetics.nist.gov/kinetics/index.jsp")
    driver.find_element_by_xpath('/html/body/table/tbody/tr/td[2]/form/table/tbody/tr/td[1]/input').send_keys(Chemical)
    driver.find_element_by_xpath('/html/body/table/tbody/tr/td[2]/form/table/tbody/tr/td[8]/input').click()
    count_text = driver.find_element_by_xpath('/html/body/table/tbody/tr/td[2]').text

    searchpattern = '[0-9]*\srecords\.'

    m = re.search(searchpattern, count_text)
    count = int(str(m.group(0)).replace(' records.', ''))

    i=2

    while 1:
        try:
            results_xpath = f'/html/body/table/tbody/tr/td[2]/table[2]/tbody/tr[{i}]/td[3]'

            info = driver.find_element_by_xpath(results_xpath).text

            c.execute(f"INSERT INTO REACTIONS VALUES ('{info}')")

        except:

            print('Complete . . . yeah that DID work.')
            break
        i+=1

#SearchChemical('Na')
print(chem_data)




for e in chem_data:
    print(e)
    SearchChemical(e[1])
time.sleep(3)

driver.close()

conn.commit()

conn.close()



