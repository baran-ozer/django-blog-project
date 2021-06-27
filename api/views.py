from os import listxattr
from django.http.response import HttpResponse
from django.shortcuts import render
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import requests
import urllib3

def main(request):
    if request.method == "GET":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {
            #"download.default_directory": download_dir, #Change default directory for downloads
            "download.prompt_for_download": False, #To auto download the file
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True, #It will not show PDF directly in chrome
        })

        driver = webdriver.Chrome(chrome_options=options)

        driver.get("https://www.sahibinden.com/kiralik-daire/istanbul-kadikoy?address_region=2&sorting=price_asc")
        elem = driver.find_element_by_xpath('//*[@id="searchResultsTable"]')
        html_doc = elem.get_attribute('innerHTML')
        soup = BeautifulSoup(html_doc, 'html.parser')
        ilan_list = soup.find_all('tr')
        ilan_url_list = []
        for ilan in ilan_list:
            if len(ilan.find_all('td')) > 2:
                ilan_link = ilan.find_all('td')[1].find("a", {"class": "classifiedTitle"})
                if ilan_link:
                    print(ilan_link["href"])
                    ilan_url_list.append("https://www.sahibinden.com" + ilan_link["href"])
        
        for link in ilan_url_list:
            driver.get(link)
            details = driver.find_element_by_xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]')
            html_doc = details.get_attribute('innerHTML')
            soup_2 = BeautifulSoup(html_doc, 'html.parser')
            children = soup_2.findChildren()
            detail_list = soup_2.find("ul", {"class": "classifiedInfoList"})
            for d in detail_list.find_all('li'):
                if d.find("strong"):
                    print(d.find("strong").text.strip() + " : " + d.find("span").text.strip())
                time.sleep(0.5)
            
            time.sleep(500)
            cnt = 0
            for child in children:
                print(child.text + "  " + str(cnt))
                cnt += 1
            time.sleep(5)
            break

        #print(soup.prettify())
        """ driver.find_element_by_id('UserName').send_keys(account['username'])
        driver.find_element_by_id('Password').send_keys(account['password'])
        driver.find_element_by_xpath('//*[@id="printing"]/div/form/fieldset/div[5]/input[1]').click()

        time.sleep(sleep_secs / 3)

        driver.get(account['udf_url'])

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="reportFilterForm"]/span[1]/span'))).click()
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,f'//*[text()="{account["account_country"]}"]'))).click()
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,'//*[text()="Select Report Type"]'))).click()
        time.sleep(6)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="reportType_listbox"]/li[1]'))).click()
        time.sleep(6)

        if account["account_country"] == "RJO UK":
            WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="reportFilterForm"]/span[4]/span/span[1]'))).click()
            WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, f'//*[text()="{account["account_name"]}"]'))).click()
            WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="applyubixReportsFilters"]'))).click()
        elif account["account_country"] == "RJO US":
            WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Select Watchlist"]'))).click()
            WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, f'//*[text()="{account["account_name"]}"]'))).click()
            WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="applyReportsFilters"]'))).click()
        
        date_time_obj = datetime.datetime.strptime(yyyymmdd, '%Y%m%d')
        formatted_date = date_time_obj.strftime("%d-%b-%y")
        print(formatted_date)
        ext = 'pdf'
        old_files = get_files(path, ext)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, f'//*[text()="{formatted_date}"]'))).click()
        time.sleep(5)
        filename = file_differ(get_files(path, ext), old_files)
        if pretty_name:
            p_filename = generate_pretty_filename(account, yyyymmdd, ext)
            filename = forced_rename(path, filename, p_filename)
        driver.quit() """
        
        return HttpResponse("WELL DONE", status=200)
