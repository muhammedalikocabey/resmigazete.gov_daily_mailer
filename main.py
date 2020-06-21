# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 19:44:52 2020

@author: muham
"""


#%% Web Scraping 

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import os



chrome_options = Options()

chrome_options.add_argument('--lang=tr')

chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

chrome_options.add_argument("--headless")

chrome_options.add_argument("--disable-dev-shm-usage")

chrome_options.add_argument("--no-sandbox")


browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

browser.maximize_window()

browser.get("https://resmigazete.gov.tr/")



tarih_xpath = "//h6/u/span[@id='spanGazeteTarih']"
tarih = browser.find_element_by_xpath(tarih_xpath).get_attribute("innerHTML")


gunluk_akis_xpath = "//div[@id='gunluk-akis']"
gunluk_akis = browser.find_element_by_xpath(gunluk_akis_xpath)


html_content = browser.execute_script("return arguments[0].outerHTML;", gunluk_akis)
html_content = html_content.replace("""<hr> Resmî Gazete'nin kurumsal mobil uygulaması Android ve Apple marketlerde "T.C. Resmî Gazete" adıyla yerini almıştır. <hr>""", "")
html_content = html_content.strip()

developer_html = """<br/><br/><hr style="width:75%;text-align:left;margin: 0 auto">
<center><br/><small><a href="https://www.sinerjik.org/resmi-gazete-e-posta-hizmeti/" target="_blank">Resmi Gazete E-Posta Hizmeti</a>, ticari amaç gütmeyen ücretsiz bir hizmettir.<br/> Geliştirici: <strong><a href="https://www.muhammedalikocabey.com/hakkimda/" target="_blank"> Muhammed Ali KOCABEY</a></strong>  |  Fikir: <a href="https://www.sinerjik.org/hakkinda/furkan-guven-tastan/" target="_blank"><strong>Furkan Güven TAŞTAN</strong></a></small><br/><br/><hr style="width:75%;text-align:left;margin: 0 auto">
<br/><small>Mail listesinden ayrılmak için <a href="https://sinerjik.us10.list-manage.com/unsubscribe?u=b91b7e9fb96346dee295ef820&id=b4bc9cb5af">tıklayınız.</a></small>
"""
developer_html = developer_html.strip()


html_content = html_content + " " + developer_html


browser.close()


#%%     Get Mail List
from mailchimp3 import MailChimp

client = MailChimp(mc_api="2d88b44f09e8f52291d63056e0e2032d-us10", mc_user="sinerjik")

subscribers = (client.lists.members.all('b4bc9cb5af', get_all=True, fields="members.email_address"))["members"]

recipients = [str(i["email_address"]) for i in subscribers]


#%%     Sending E-Mail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText





SENDER_USERNAME = "resmigazete@sinerjik.org"
SENDER_PASSWORD = "?Ak7$Yz5"



for receiver in recipients:
    msg = MIMEMultipart()
    msg['From'] = "Resmi Gazete <resmigazete@sinerjik.org>"
    msg['To'] = receiver
    msg['Subject'] = tarih
    
    part1 = MIMEText(html_content, 'html')
    msg.attach(part1)
    
    mailserver = smtplib.SMTP('webmail.sinerjik.org',587)
    # identify ourselves to smtp gmail client
    mailserver.ehlo()
    # secure our email with tls encryption
    mailserver.starttls()
    # re-identify ourselves as an encrypted connection
    mailserver.ehlo()
    mailserver.login(SENDER_USERNAME, SENDER_PASSWORD)

    mailserver.sendmail(SENDER_USERNAME, receiver, msg.as_string())
    print(receiver," 'a mail gönderildi")
    
    mailserver.quit()

