# -*- coding: utf-8 -*-

### Dependences
import datetime
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
import urllib
import pandas as pd
import requests
from _library.webdriver import Browser

### Manipulador da página
class get_tables():

  def __init__(self, browser=Browser):
    self.browser = browser

  def export(self):
    
    results = []

    html = self.browser.page_source (encode='utf-8')
    soup = BeautifulSoup(html, 'lxml')

    for row in soup.find_all('tr')[1:]:
      data = row.find_all('td')
      nome = data[0]
      fech = data[1]
      oscil = data[2]
      neg = data[3]
      vol = data[4]
      liq = data[5]
      var5 = data[6]
      var30 = data[7]
      var180 = data[8]
      cod = data[9]
      results.append(
        {
          'Nome':nome.text, 
          'Fechamento':fech.text, 
          'Oscilação':oscil.text,
          'Negociação':neg.text,
          'Volume': vol.text,
          'Liquidez': liq.text,
          'Variação 5 dias': var5.text,
          'Variação 30 dias': var30.text,
          'Variação 6 meses': var180.text,
          'Código': cod.text,
        }
      )

    df = pd.DataFrame(results)
    df.head()

    return results