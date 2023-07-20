def cozumle(sayilar):
    
    sayilar.sort()
    
    cozumlenmis = []
    
    for sayi in sayilar:
        cozumlenmis.append(sayi)
        kalan = sayi % 3
        
        if kalan == 0:
            while kalan == 0:
                sayi //= 3
                cozumlenmis.append(sayi)
                kalan = sayi % 3
            
            cozumlenmis.append(sayi * 2)
    
    return cozumlenmis

sayilar = [16, 21, 11, 8, 12, 22]
cozum = cozumle(sayilar)
print(cozum)

