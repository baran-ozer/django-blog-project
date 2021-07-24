from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import PackageForm

from selenium import webdriver
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
    profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}], "download.extensions_to_open": "applications/pdf"}

    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", profile)
    options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=options)  # Optional argument, if not specified will search path.

    driver.get('https://www.yurticikargo.com/tr/online-servisler/fiyat-hesapla')
    #WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="logonIdentifier"]'))).send_keys(account['username'])
    time.sleep(2)
    driver.quit()


