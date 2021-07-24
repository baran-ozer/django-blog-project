from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import PackageForm

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


def main(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PackageForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            chromedriver(request)
            #return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PackageForm()

    return render(request, 'index.html', {'form': form})


def chromedriver(request):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("window-size=1400,1500")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("start-maximized")
    options.add_argument("enable-automation")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)  # Optional argument, if not specified will search path.

    driver.get('https://www.yurticikargo.com/tr/online-servisler/fiyat-hesapla')
    test =WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dynamic-content-section"]/div/div[2]/div/div/div[1]/div[1]/form/div[1]/h5')))
    print(test.text)
    #WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="logonIdentifier"]'))).send_keys(account['username'])
    time.sleep(2)
    driver.quit()


