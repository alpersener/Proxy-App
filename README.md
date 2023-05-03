# Python-with-Proxy-App
#ARALIK 2022
Şu anlık Python ile proxy’i yazdım..Ayrıca elimde olan Proxy ip’lerini ise internetten bulduğum free Proxy listelerinden çekip csv dosyasına getiriyorum.Yazdığım kodda csv dosyasını okuyup çalışan proxyleri console’a yazdırıyor çalışmayanlar ile çalışanları böylece görmüş oluyorum.Ardından çalışan proxy’leri başka bir csv dosyasına düzgün bir şekilde yazdırıyorum.

Başka csv dosyasına atılmasının sebebi ilk listede gereksiz bir sürü ip var böylece elimde temiz bir liste olmuş oluyor.

Gui ile kısmında butonlar ile aç kapa yapıp proxy’i istediğim zaman açıp kapatabiliyorum.Proxy açıkken aşağı tarafta Proxy açık diye yeşil renkte buton gösteriliyor kapalıyken de kırmızı şekilde Proxy kapalı butonu gösteriliyor.Kullanılan Proxy ip’sini gösteren bir buton daha var böylece proxyi açtıktan sonra hangi Proxy ip’sine bağlı olduğumu görebiliyorum.Eğer Proxy açık değil ise  kullanıcıya Proxy ayarı açık değil diye bir error mesajı veriliyor.

Sıradaki ip geç butonu var bu buton ise çalışan proxyleri proxylistesine göre sırayla değiştirmeye yarıyor.
Proxy’i kapattıktan sonra düzgün olması açısından sadece çalışan proxy’lerin olduğu csv dosyasını siliyor açıldığında ise yeniden oluşturuyor.



----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#OCAK 2023 Güncelleme

Projeye timer eklendi ve her 5 dakikada bir yeni bir messagebox açıp diğer proxy’e geçmek ister misiniz? Diye bildirim çıkıyor böylelikle 5 dakikada bir proxyleri isteğimize göre değiştirebiliyoruz.
GetContent adında bir button var ve butona tıkladığımızda yeni bir pencere açılıyor ve entry kısmına url olarak http://www.ankara.gov.tr/ girerek siteden veri çekip,çektiği veriyi yukarı yeni açılan pencerede üst taraftaki listbox’ta gösteriyor.
Ayrı olarak veri çekmek için beatifulsoup kütüphanesini kullanılıyor.
