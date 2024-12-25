import qrcode

# QR koda eklenecek veri
veri = "https://github.com/azatakan"

# QR kodu oluştur
qr = qrcode.QRCode(
    version=3,  # QR kodunun boyutunu belirler
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Hata düzeltme seviyesi
    box_size=10,  # Her bir kutunun piksel boyutu
    border=4,  # Çerçeve kalınlığı
)
qr.add_data(veri)
qr.make(fit=True)

# QR kodu görselleştir
resim = qr.make_image(fill_color="black", back_color="white")
resim.show()

# QR kodunu kaydet
resim.save("qrcode.png")