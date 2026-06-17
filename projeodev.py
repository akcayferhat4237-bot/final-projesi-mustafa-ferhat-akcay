import streamlit as st
import requests

# Kopyaladığın AQ. ile başlayan anahtarı buraya yapıştır
API_KEY = "AQ.Ab8RN6Jj3jGjOb1fbW-JbvOGsFIaaab-1323PljtLVWa4Xeqmg"

st.title("KodRehberi: C++ ve Java Asistanı")
st.write("Nesne Yönelimli Programlama (OOP) kavramları hakkında sormak istediklerinizi aşağıya yazabilirsiniz.")

# Kullanıcıdan soruyu alıyoruz
soru = st.text_input("Sorunuzu buraya yazın (Örn: Polimorfizm nedir?):")

# Butona basıldığında çalışacak kısım
if st.button("Sor"):
    if soru:
        st.success(f"Senin sorun: {soru}")
        
        with st.spinner("Asistan cevabı hazırlıyor..."):
            try:
                # Bozuk kütüphane yerine doğrudan Google'ın sunucusuna bağlanıyoruz
                url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
                headers = {
                    "Content-Type": "application/json",
                    "x-goog-api-key": API_KEY
                }
                data = {
                    "contents": [{"parts": [{"text": soru}]}]
                }
                
                # İsteği gönder
                response = requests.post(url, headers=headers, json=data)
                
                if response.status_code == 200:
                    cevap = response.json()["candidates"][0]["content"]["parts"][0]["text"]
                    st.info("Asistanın Cevabı:")
                    st.write(cevap)
                else:
                    st.error(f"Google API Hatası: {response.text}")
                    
            except Exception as e:
                st.error(f"Bir hata oluştu: {e}")
    else:
        st.warning("Lütfen önce bir soru yazın!")