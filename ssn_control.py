class CheckSSN(Exception):
    pass #Fonksiyonun hata vermemesi icin 

def check_ssn(ssn):
    # TC kimlik numarasinin uzunluğu 11 olmali
    if len(ssn) != 11:
        raise CheckSSN("TC kimlik numarasi 11 rakamdan olusmalidir.")

    # TC kimlik numarasindaki her karakter rakam olmali
    if not ssn.isdigit():
        raise CheckSSN("TC kimlik numarasinda harf bulunmamalidir.")

    # TC kimlik numarasindaki her karakter özel bir karakter olmamali
    ozel_karakterler = set("!@#$%^&*()-_+=<>?/:;{}|,.`~")
    if any(char in ozel_karakterler for char in ssn):
        raise CheckSSN("TC kimlik numarasinda özel karakter bulunmamalidir.")

    # TC kimlik numarasindaki her karakter büyük harf olmamali
    if any(char.isupper() for char in ssn):
        raise CheckSSN("TC kimlik numarasinda büyük harf bulunmamalidir.")
    
    

# Kullanicidan TC kimlik numarasi girisi alinmasi
try:
    kullanici_tc = input("Lütfen TC kimlik numaranizi girin: ")
    son_karakter = kullanici_tc[-1]
    if int(son_karakter) % 2 == 1 :
        raise CheckSSN("Son rakam tek olmamalidir.")

    check_ssn(kullanici_tc)
    print("Giris gecerli.")
except CheckSSN as e:
    print(f"Hata: {e}")
except Exception as e:
    print(f"Beklenmeyen bir hata olustu: {e}")