from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import pandas as pd
import numpy as np
import os

url_proyect = os.getcwd()

url = "https://www.losmundialesdefutbol.com/selecciones.php"

# Ejecutar el driver
serv_obj = Service(url_proyect + '/chromedriver.exe')  # Required in Selenium 4
driver = webdriver.Chrome(service=serv_obj)

# Acceder a la pagina
driver.get(url)
print(driver.current_url)

# Extraer los links de los que queremos obtener la data
countries = driver.find_elements(By.XPATH, '//table[@class="panel a-left color-alt max-1"]//tr/td/div[1]/div')
name_countries = [element.text.split(" ")[1] for element in countries]

mundial_a_mundial = driver.find_elements(By.XPATH, '//table[@class="panel a-left color-alt max-1"]//tr/td/div[2]/div/div[1]/div[2]/a')
links_mundial_a_mundial = [element.get_attribute("href") for element in mundial_a_mundial]

resultados = driver.find_elements(By.XPATH, '//table[@class="panel a-left color-alt max-1"]//tr/td/div[2]/div/div[2]/div[1]/a')
links_resultados = [element.get_attribute("href") for element in resultados]


def extract_data_mundial_a_mundial(driver):
    table_array = []
    for j in range(len(links_mundial_a_mundial)):
        link = links_mundial_a_mundial[j]
        name_country = name_countries[j]
        driver.get(link)
        table = driver.find_elements(By.XPATH, '//table[@class="a-right"]/tbody//tr/td')
        table = [element.text for element in table][13:]
        print("Country screapping now: ", name_country)
        n_rows = int(len(table)/14)

        for i in range(n_rows):
            row = table[(i+0)*14: (i+1)*14][:12]
            if row[3] == 'no participó':
                row[2], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11] = 0, 0, 0, 0, 0, 0, 0, 0, 0
            table_array.append([name_country]+row)

    table_array = np.array(table_array)
    df = pd.DataFrame(table_array)
    df.columns = ['name_pais', 'Mundial', 'Selección', 'Posición', 'Etapa', 'PTS', 'PJ', 'PG', 'PE', 'PP', 'GF', 'GC', 'Dif']
    df.to_csv("data - mundial a mundial.csv", index=False)


# equipo izquierda  -> //div[@class="max-1 margen-b8 bb-2"]//div[@class="margen-y3 clearfix"]//div[@class="right-sm a-right"]/div/div/div[1]/div[3]
# equipo derecha    -> //div[@class="max-1 margen-b8 bb-2"]//div[@class="margen-y3 clearfix"]//div[@class="right-sm a-right"]/div/div/div[3]/div[3]
# resultado (goles) -> //div[@class="max-1 margen-b8 bb-2"]//div[@class="margen-y3 clearfix"]//div[@class="right-sm a-right"]/div/div/div[2]/div[2]
# fecha del partido -> //div[@class="max-1 margen-b8 bb-2"]//div[@class="margen-y3 clearfix"]//div[@class="left-sm clearfix a-center margen-b3"]/div[2]
# etapa del partido -> //div[@class="max-1 margen-b8 bb-2"]//div[@class="margen-y3 clearfix"]//div[@class="left-sm clearfix a-center margen-b3"]/div[3]


def extract_data_resultados(driver):
    table_array = []
    total_pages = len(links_resultados)

    p = 0
    for link in links_resultados:
        driver.get(link)

        country = driver.find_element(By.XPATH, '//div[@class="rd-100-33 size-11 negri a-center clearfix margen-t3"]').text
        p += 1
        progress = "("+str(p)+"/"+str(total_pages)+")"
        print("Scrapping 'resultados' of: ", country, progress)

        left_team = driver.find_elements(By.XPATH, '//div[@class="max-1 margen-b8 bb-2"]//div[@class="margen-y3 clearfix"]//div[@class="right-sm a-right"]/div/div/div[1]/div[3]')
        left_team = [element.text for element in left_team]
        right_team = driver.find_elements(By.XPATH, '//div[@class="max-1 margen-b8 bb-2"]//div[@class="margen-y3 clearfix"]//div[@class="right-sm a-right"]/div/div/div[3]/div[3]')
        right_team = [element.text for element in right_team]
        goals = driver.find_elements(By.XPATH, '//div[@class="max-1 margen-b8 bb-2"]//div[@class="margen-y3 clearfix"]//div[@class="right-sm a-right"]/div/div/div[2]/div[2]')
        goals = [element.text.split(" - ") for element in goals]
        date = driver.find_elements(By.XPATH, '//div[@class="max-1 margen-b8 bb-2"]//div[@class="margen-y3 clearfix"]//div[@class="left-sm clearfix a-center margen-b3"]/div[2]')
        date = [element.text for element in date]
        round = driver.find_elements(By.XPATH, '//div[@class="max-1 margen-b8 bb-2"]//div[@class="margen-y3 clearfix"]//div[@class="left-sm clearfix a-center margen-b3"]/div[3]')
        round = [element.text for element in round]
        left_goals = [element[0] for element in goals]
        right_goals = [element[1] for element in goals]

        n_clashes = len(left_team)

        for i in range(n_clashes):
            table_array.append([date[i], round[i], left_team[i], left_goals[i], right_team[i], right_goals[i]])

    table_array = np.array(table_array)
    df = pd.DataFrame(table_array)
    df.columns = ["fecha", "etapa", "equipo_izq", "goles_izq", "equipo_der", "goles_der"]
    # df.head(5)
    df.to_csv("data - resultados.csv", index=False)


if __name__ == '__main__':

    extract_data_mundial_a_mundial(driver)

    extract_data_resultados(driver)
