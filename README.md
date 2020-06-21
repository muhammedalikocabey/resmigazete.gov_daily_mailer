# TR
## resmigazete.gov.tr Verilerini Günlük Olarak Çekme ve Kayıtlı Abonelere Mail Gönderme



*** Herokuapp üzerinde kurulmuş olması ve Heroku Scheduler sayesinde resmi gazeteyi 05.00'da web scraping ile çekip kayıtlı abonelerine mail atıyor.***



Web sitesi üzerinden veri çekerken istenilen veri spesifik olacağından element xpath-id seçimleri de spesifik olacaktır.
Örneğin [Resmi Gazete](https://resmigazete.gov.tr/)'de kullandığım element özellikleri

```
Tarih ve Sayı    =     //h6/u/span[@id='spanGazeteTarih']
Günlük Akış      =     //div[@id='gunluk-akis']
```

şeklinde, fakat siteyi incele seçeneğiyle veri çekeceğiniz web sitesine uygun element özelliklerini bulabilirsiniz.

Mail listesine kaydolmak için [tıklayınız.](https://www.sinerjik.org/resmi-gazete-e-posta-hizmeti/)

Daha fazlası için [web siteme](https://www.muhammedalikocabey.com/blog) göz atabilirsiniz.

Yardım ve sorularınız için mail adresimden [me@muhammedalikocabey.com](mailto:me@muhammedalikocabey.com) bana ulaşabilirsiniz.





# EN
## Scraping resmigazete.gov.tr Data Daily and Sending Mail to Registered Subscribers


*** Thanks to its establishment on Herokuapp and Heroku Scheduler, it sends the official newspaper via web scraping at 05.00 and sends mail to its registered subscribers. ***



The element xpath-id selections will be specific as the desired data will be specific when capturing data through the website.
For example, the element properties I use in [Turkey Official Newspaper Website](https://resmigazete.gov.tr/)

```
Tarih ve Sayı    =     //h6/u/span[@id='spanGazeteTarih']
Günlük Akış      =     //div[@id='gunluk-akis']
```

You can find the element properties that are suitable for the website where you will pull data with the option "Examine".

[Click here](https://www.sinerjik.org/resmi-gazete-e-posta-hizmeti/) to sign up for the mailing list.

You can browse my [website](https://www.muhammedalikocabey.com/blog) for more.

For help and questions, go to my mail address [me@muhammedalikocabey.com](mailto:me@muhammedalikocabey.com) you can contact me.


