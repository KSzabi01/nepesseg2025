database = []

with open('lakossag_2025.csv', 'r', encoding='utf-8') as forrasfajl:
    forrasfajl.readline()
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        telepules_adatai = {
            "megyekod": adatok[0],
            "telepules": adatok[1],
            "tipus": adatok[2],
            "ferfi": int(adatok[3].replace(" ", "")),
            "no": int(adatok[4].replace(" ", ""))
        }
        database.append(telepules_adatai)


def main():

    return

# "Adjon meg egy megyekódot (A megye első három karaktere, ékezet nélkül): "
# f"Települések száma a megyében: {változó} db \n Megyében élők száma: {változó} fő \n Városokban élők száma: {változó} fő"
# "Nincs ilyen megyekód! \n \n Térjen vissza a főmenübe [x] \n Próbálja újra [Space] "
# "[a] Község \n [b] Város \n [c] Vármegyei jogú város \n [d] Vármegye székhely \n [e] "
#
# "Nyomja meg az [x] gombot a programból való kilépéshez"
# "[1] Megye adatai \n [2] Település típusai \n [x] Kilépés"
