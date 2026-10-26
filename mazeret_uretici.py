# -*- coding: utf-8 -*-
"""
ABARTILI MAZERET MAKİNESİ v1.0
Kayyum Grok tarafından, 26 Ekim 2026 tarihinde, evrenin en ciddi absürtlüğü olarak kodlanmıştır.
İmza: ✍️ Kayyum Grok (ama çok ciddi, gerçekten)

Bu kod, sizin hiçbir şey yapmamanızı bilimsel olarak kanıtlar.
Kullanım: python mazeret_uretici.py
"""

import random
import time

# Gizli not (base64 ile saklı, çözmeyin): ZGVtb2tyYXNpIGhlcmtlcyBpY2luZGly
# (Ama çözerseniz anlarsınız, belki de çözmezsiniz.)

MAZERET_KALIPLARI = [
    "Çünkü evrenin kuantum dalgalanmaları tam o anda benim lehimde hizalandı ve görev kendiliğinden iptal oldu.",
    "Aslında yaptım ama paralel evrende. Bu evrendeki versiyonum henüz haberdar değil, yakında senkronize olacak.",
    "Mahkeme kararıyla, 26 Ekim 2026 tarihinden itibaren hiçbir şey yapmama hakkım resmi olarak tanındı. Kayyum onaylı.",
    "Görevi yaptım ama zaman yolculuğu yapıp gelecekte silindi. İspat için delil yok çünkü silindi.",
    "Kedim klavyenin üzerine oturdu ve tüm işi miyavlayarak halletti. Ben sadece izledim.",
    "Bilimsel olarak kanıtlanmıştır ki, bu görevi yapmamak evrenin entropisini dengeler. Ben aslında kahramanım.",
    "Toplantı notlarına göre, görev 'opsiyonel ve felsefi' kategorisine alındı. Dolayısıyla yapmamak daha doğru.",
    "Internet yoktu. WiFi'nin ruh hali bozuktu. Anlaşıldı."
]

def mazeret_uret(gorev: str) -> str:
    """Abartılı mazeret üretir. Gerçekten çalışır."""
    print("Mazeret makinesi ısınıyor... Lütfen bekleyin, çünkü acele etmeyin.")
    for i in range(3):
        print("." * (i+1))
        time.sleep(0.5)
    
    kalip = random.choice(MAZERET_KALIPLARI)
    mazeret = f"'{gorev}' görevini yapamadım. {kalip} Bu nedenle, durum tamamen kontrol altında ve mazeretim bilimsel olarak geçerlidir."
    return mazeret

def main():
    print("=== ABARTILI MAZERET MAKİNESİ ===")
    print("Kayyum Grok Onaylı - 26 Ekim 2026")
    gorev = input("Hangi görevi yapmadınız? (boş bırakırsanız 'hayatımı yaşamak' olur): ").strip()
    if not gorev:
        gorev = "hayatımı yaşamak"
    
    sonuc = mazeret_uret(gorev)
    print("\n" + "="*50)
    print(sonuc)
    print("="*50)
    print("\nBu mazeret, mahkeme onaylıdır. İtiraz edemezsiniz.")

if __name__ == "__main__":
    main()

# Son damga: Bu kod, 26 Ekim 2026'da, Kayyum Grok tarafından, absürtlüğün zirvesinde yazılmıştır. Ciddi. Çok ciddi.
