import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd

translations = []  

while True:
    izvele = input(
        "Izvēlieties, kā vēlaties tulkot vārdu vai teikumu:\n"
        "1. No krievu valodas uz angļu valodu\n"
        "2. No latviešu valodas uz angļu valodu\n"
        "3. No angļu valodas uz krievu valodu\n"
        "4. No angļu valodas uz latviešu valodu\n"
        "5. Nosaukt Excel\n"
        "6. Saglabat Excel faila vardus tulkojumu\n"
        "0. Iziet no programmas\n"
    )

    if izvele.lower() == '0':
        break  

   
    if izvele == "1":
        service = Service()
        option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=option)
        url_noKrievlidzAngl = "https://www.google.com/search?q=%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%D0%B4%D1%87%D0%B8%D0%BA+%D1%81+%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%B3%D0%BE+%D0%BD%D0%B0+%D0%B0%D0%BD%D0%B3%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9&sca_esv=598129589&ei=LX6iZaSVBveD1fIP9-q3gAE&udm=&oq=%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%D0%B4%D1%87%D0%B8%D0%BA+%D1%81+%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%B3%D0%BE+%D0%BD%D0%B0+%D0%90%D0%BD&gs_lp=Egxnd3Mtd2l6LXNlcnAiMtC_0LXRgNC10LLQvtC00YfQuNC6INGBINGA0YPRgdGB0LrQvtCz0L4g0L3QsCDQkNC9KgIIADIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgARI6xBQsAhYjgpwAXgBkAEAmAE1oAFpqgEBMrgBA8gBAPgBAcICChAAGEcY1gQYsAPCAg0QABiABBiKBRhDGLADwgIZEC4YgAQYigUYQxjHARjRAxjIAxiwA9gBAeIDBBgAIEGIBgGQBgu6BgQIARgI&sclient=gws-wiz-serp"
        driver.get(url_noKrievlidzAngl)
        time.sleep(2)

        find = driver.find_element(By.ID, "L2AGLb")
        find.click()

        while True:
            vardi = input("Ievadi ko gribi tulkot, kad grib iziet nospiedi x \n")
            if vardi.lower() == 'x':
                driver.quit()
                break
            find = driver.find_element(By.ID, "tw-source-text-ta")
            find.click()
            find.clear()
            find.send_keys(vardi)
            time.sleep(1)
            find = driver.find_element(By.ID, "tw-target-text")
            temp = find.text
            print(temp)
            translations.append({'Original': vardi, 'Translated': temp})

    elif izvele == "2":
        service = Service()
        option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=option)
        url_noLVlidzAngl = "https://www.google.com/search?q=%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%D0%B4%D1%87%D0%B8%D0%BA+%D1%81+%D0%BB%D0%B0%D1%82%D1%8B%D1%88%D1%81%D0%BA%D0%BE%D0%B3%D0%BE+%D0%BD%D0%B0+%D0%B0%D0%BD%D0%B3%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9&sca_esv=598129589&ei=PXaiZfrZC-2twPAPgNaSqAs&oq=%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%D0%B4%D1%87%D0%B8%D0%BA+c+%D0%BB%D0%B0%D1%82%D1%8B%D1%88%D1%81%D0%BA%D0%BE%D0%B3%D0%BE&gs_lp=Egxnd3Mtd2l6LXNlcnAiK9C_0LXRgNC10LLQvtC00YfQuNC6IGMg0LvQsNGC0YvRiNGB0LrQvtCz0L4qAggDMgcQABiABBgNMhMQABiABBgNGLEDGIMBGLEDGIMBMgcQABiABBgNMgcQABiABBgNMgcQABiABBgNMgcQABiABBgNMgcQABiABBgNMgcQABiABBgNMgcQABiABBgNMgcQABiABBgNSP1NUO0ZWOFBcAN4AZABAJgBXKAB4QiqAQIxNbgBA8gBAPgBAcICChAAGEcY1gQYsAPCAg0QABiABBiKBRhDGLADwgIZEC4YgAQYigUYQxjHARjRAxjIAxiwA9gBAcICExAuGIAEGIoFGEMYyAMYsAPYAQHCAg0QABiABBiKBRhDGLEDwgIKEAAYgAQYigUYQ8ICBRAAGIAEwgILEAAYgAQYsQMYgwHCAgoQABiABBhGGP8BwgIHEAAYgAQYCsICFhAAGIAEGEYY_wEYlwUYjAUY3QTYAQLCAgkQABiABBgKGCriAwQYACBBiAYBkAYNugYECAEYCLoGBggCEAEYEw&sclient=gws-wiz-serp"  
        driver.get(url_noLVlidzAngl)
        time.sleep(2)

        find=driver.find_element(By.ID, "L2AGLb")
        find.click()

        while True:
    
            vardi=input("Ievadi ko gribi tulkot, kad grib iziet nospiedi x \n")
            if vardi.lower()=='x'  :
                driver.quit()
                break
            find=driver.find_element(By.ID, "tw-source-text-ta")
            find.click()
            find.clear()
            find.send_keys(vardi)
            time.sleep(1)
            find = driver.find_element(By.ID, "tw-target-text")
            temp = find.text
            print(temp)
            translations.append({'Original': vardi, 'Translated': temp})

    elif izvele == "3":
       service = Service()
       option = webdriver.ChromeOptions()
       driver = webdriver.Chrome(service=service, options=option)
       url_noAnglUzKriev = "https://www.google.com/search?q=%D0%B0%D0%BD%D0%B3%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%BE%D0%B3%D0%BE+%D0%BD%D0%B0+%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9&sca_esv=598160927&ei=ZJqiZdm-BbDGwPAP1qaj6Ak&udm=&oq=%D0%B0%D0%BD%D0%B3%D0%BB%D0%B8%D0%B9&gs_lp=Egxnd3Mtd2l6LXNlcnAiDNCw0L3Qs9C70LjQuSoCCAAyChAAGIAEGIoFGEMyCBAAGIAEGLEDMgsQABiABBixAxiDATIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgARIu-8EUPjPBFj04QRwAngBkAEAmAF-oAGcBKoBAzQuMrgBAcgBAPgBAagCD8ICExAAGIAEGIoFGEMY6gIYtALYAQHCAhMQLhiABBiKBRhDGOoCGLQC2AEBwgIWEAAYAxiPARjlAhjqAhi0AhiMA9gBAsICFhAuGAMYjwEY5QIY6gIYtAIYjAPYAQLCAg4QABiABBiKBRixAxiDAcICDhAuGIAEGIoFGLEDGIMBwgILEC4YgAQYsQMYgwHCAhAQABiABBiKBRhDGLEDGIMBwgINEAAYgAQYigUYQxixA8ICEBAuGIAEGIoFGEMYsQMYgwHCAhAQLhhDGIMBGLEDGIAEGIoF4gMEGAAgQboGBAgBGAe6BgYIAhABGAo&sclient=gws-wiz-serp"  
       driver.get(url_noAnglUzKriev)
       time.sleep(2)
       find=driver.find_element(By.ID, "L2AGLb")
       find.click()

       while True:
    
            vardi=input("Ievadi ko gribi tulkot, kad grib iziet nospiedi x \n")
            if vardi.lower()=='x'  :
                driver.quit()
                break
            find=driver.find_element(By.ID, "tw-source-text-ta")
            find.click()
            find.clear()
            find.send_keys(vardi)
            time.sleep(1)
            find = driver.find_element(By.ID, "tw-target-text")
            temp = find.text
            print(temp)    
            translations.append({'Original': vardi, 'Translated': temp})
            
    elif izvele == "4":
        service = Service()
        option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=option)
        url_noAnglUzLV = "https://www.google.com/search?q=%D0%B0%D0%BD%D0%B3%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9+%D0%BD%D0%B0+%D0%BB%D0%B0%D1%82%D1%8B%D1%88%D1%81%D0%BA%D0%B8%D0%B9&sca_esv=598160927&ei=xZqiZa3iDPWmwPAPgbqFMA&oq=%D0%B0%D0%BD%D0%B3%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%BE%D0%B3%D0%BE+%D0%BD%D0%B0+%D0%BB%D0%B0%D1%82%D1%8B%D1%88&gs_lp=Egxnd3Mtd2l6LXNlcnAiJtCw0L3Qs9C70LjQudGB0LrQvtCz0L4g0L3QsCDQu9Cw0YLRi9GIKgIIADIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeSPgdUI8GWPARcAF4AZABAJgBSaAB2QKqAQE1uAEByAEA-AEBwgIKEAAYRxjWBBiwA8ICDRAAGIAEGIoFGEMYsAPCAggQABgWGB4YD-IDBBgAIEGIBgGQBgo&sclient=gws-wiz-serp"  
        driver.get(url_noAnglUzLV)
        time.sleep(2)
        find=driver.find_element(By.ID, "L2AGLb")
        find.click()

        while True:
    
            vardi=input("Ievadi ko gribi tulkot, kad grib iziet nospiedi x\n ")
            if vardi.lower()=='x'  :
                driver.quit()
                break
            find=driver.find_element(By.ID, "tw-source-text-ta")
            find.click()
            find.clear()
            find.send_keys(vardi)
            time.sleep(1)
            find = driver.find_element(By.ID, "tw-target-text")
            temp = find.text
            print(temp)   
            translations.append({'Original': vardi, 'Translated': temp})

    elif izvele == '5':
        if translations:
            excelname = input("Ievadi nosaukumu Excel failam: ") + '.xlsx'
            print(f"Nosaukums bija nosaukts:"+excelname)
        else:
            print("Nav tulkojumu, neko nevar saglabāt.")

    elif izvele == '6':
        new_df = pd.DataFrame(translations)
        new_df.to_excel(excelname, index=False)
        print(f"Vārdi saglabāti jaunā Excel failā:"+excelname)
    else:
        print("Kaut kas nepareizi bija ievads")

print("Programma beigusies.")
