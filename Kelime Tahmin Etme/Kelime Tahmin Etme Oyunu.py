import random

kelimeler = ["elma", "armut", "muz", "çilek", "portakal", "üzüm", "kiraz"]

def kelime_sec(kelimeler):
    return random.choice(kelimeler)

def harf_al(tahminler):
    while True:
        tahmin = input("Bir harf girin: ").lower()
        if not tahmin.isalpha() or len(tahmin) != 1:
            print("Lütfen geçerli bir harf girin!")
        elif tahmin in tahminler:
            print("Bu harfi zaten tahmin ettiniz. Lütfen başka bir harf seçin!")
        else:
            return tahmin

def kelime_yazdir(kelime, tahminler):
    for harf in kelime:
        if harf in tahminler:
            print(harf, end=" ")
        else:
            print("_", end=" ")
    print("")

def oyun():
    kelime = kelime_sec(kelimeler)
    tahminler = set()
    hak = 6

    while hak > 0:
        tahmin = harf_al(tahminler)
        tahminler.add(tahmin)

        if tahmin in kelime:
            kelime_yazdir(kelime, tahminler)
            if set(kelime) == tahminler:
                print("Tebrikler, kazandınız!")
                return
        else:
            hak -= 1
            print("Yanlış harf! Kalan hak:", hak)

    print("Kaybettiniz! Kelime:", kelime)

oyun()