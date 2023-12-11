# pytube kütüphanesini projeye ekliyoruz. Bu kütüphane, YouTube videolarını indirmek için kullanılır.
import pytube

# Kullanıcıdan bir video URL'si alıyoruz.
url = input("enter video url :")

# İndirilen video dosyasının kaydedileceği dizini belirliyoruz. Boş bir dize ("") kullanıldığından,
# video dosyası, mevcut çalışma dizinine indirilecek.
path = ""

# pytube kütüphanesini kullanarak YouTube'dan videoyu indirme işlemi gerçekleştiriliyor.
# YouTube(url) ile belirtilen URL'ye sahip videoya erişiyoruz.
# .streams.get_highest_resolution() ile en yüksek çözünürlüklü video akışını seçiyoruz.
# .download(path) ile belirtilen dizine videoyu indiriyoruz.
pytube.YouTube(url).streams.get_highest_resolution().download(path)