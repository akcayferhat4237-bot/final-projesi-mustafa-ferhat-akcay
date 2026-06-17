# KodRehberi: C++ ve Java Asistanı

## [cite_start]Proje Tanımı 
Bu proje, üniversite öğrencilerinin Nesne Yönelimli Programlama (OOP) derslerinde karşılaştıkları soyut ve karmaşık konseptleri (Polimorfizm, Kalıtım, Interface vb.) daha rahat kavrayabilmeleri ve sınavlara/mülakatlara hazırlanabilmeleri için geliştirilmiş yapay zeka destekli bir etkileşimli öğrenme asistanıdır.

## [cite_start]Hedef Kullanıcı 
* Veri Bilimi ve Analitiği öğrencileri
* Bilgisayar ve Yazılım Mühendisliği öğrencileri
* Teknik mülakatlara hazırlanan junior geliştiriciler

## [cite_start]Çözümün Kısa Açıklaması 
Uygulama, kullanıcının girdiği doğal dil sorularını doğrudan Google Gemini 2.5 Flash API'sine iletir. Geleneksel SDK hatalarını ve sürüm çakışmalarını önlemek amacıyla doğrudan REST API mimarisi kullanılmıştır. Asistan, gelen sorulara hem C++ hem de Java dillerindeki pratik kullanımları ve kod örneklerini içerecek şekilde optimize edilmiş yanıtlar sunar.

## [cite_start]Kullanılan Teknolojiler 
* **Dil:** Python 3.13
* **Arayüz:** Streamlit
* **Model:** Google Gemini 2.5 Flash API
* **Kütüphaneler:** Requests, Streamlit

## [cite_start]Sistem Mimarisi ve İş Akışı 
1. Kullanıcı Streamlit arayüzü üzerinden soruyu girer.
2. Soru, Python `requests` modülü ile JSON formatında Google Gemini API'sine (POST isteği) gönderilir.
3. API anahtarı güvenli erişim için URL parametresi olarak iletilir.
4. Gelen yanıt ayrıştırılarak Streamlit ekranında kullanıcıya temiz bir markdown formatında sunulur.

## [cite_start]Kurulum Adımları 
Projenin yerel bilgisayarda çalıştırılması için aşağıdaki adımları sırasıyla uygulayınız:

1. Depoyu bilgisayarınıza indirin:
   ```bash
   git clone [https://github.com/KULLANICI_ADINIZ/final-projesi-ferhat-akcay.git](https://github.com/KULLANICI_ADINIZ/final-projesi-ferhat-akcay.git)
   cd final-projesi-ferhat-akcay
