database = []
varos_tipusok = ["város", "vármegyei jogú város", "vármegye székhely", "fővárosi kerület"]

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

def megye_adatai(kapott_megyekod):
    megye_telepulesei = []
    for i in database:
        if i["megyekod"] == kapott_megyekod:
            megye_telepulesei.append(i)
    
    if megye_telepulesei == []:
        return
    telepulesek_szama_megye = len(megye_telepulesei)
    ossz_lelekszam = 0
    varos_lelekszam = 0
    for i in megye_telepulesei:
        t_tipus = i["tipus"]
        if t_tipus == varos_tipusok[0] or t_tipus == varos_tipusok[1] or t_tipus == varos_tipusok[2] or t_tipus == varos_tipusok[3]:
            varos_lelekszam += i["ferfi"] + i["no"]
        ossz_lelekszam += i["ferfi"] + i["no"]
    osszes_adat = {
        "telepulesek_szama": telepulesek_szama_megye,
        "lelekszam": ossz_lelekszam,
        "v_lelekszam": varos_lelekszam
    }
    return osszes_adat


def main():
    print()
    while True:
        print("Népesség 2025")
        print("--------\n Főmenü\n--------\n [1] Megye adatai \n [2] Település típusai \n [x] Kilépés")
        valasztas = input("Írja be a menüpont előtti karaktert, majd nyomjon [Enter]-t: ")
        match valasztas:
            case "x" | "X":
                break
            case "1":
                while True:
                    bekert_megye_kod = input("Adjon meg egy megyekódot (A megye első három karaktere, ékezet nélkül): ").upper()
                    megye_adatok = megye_adatai(bekert_megye_kod)
                    print()
                    if megye_adatok:
                        print(f"Települések száma a megyében: {megye_adatok["telepulesek_szama"]} db \n Megyében élők száma: {megye_adatok["lelekszam"]} fő \n Városokban élők száma: {megye_adatok["v_lelekszam"]} fő")
                        print()
                        break
                    else:
                        print("Nincs ilyen megyekód!\n\n [x] Térjen vissza a főmenübe\n [Space] Próbálja újra")
                        megye_ujra = input("Írja be a menüpont előtti karaktert, majd nyomjon [Enter]-t: ")
                        print()
                        if megye_ujra.lower() == "x":
                            break
            case "2":
                pass
            case _:
                print("\nNincs ilyen opció!\n")

main()

# "Adjon meg egy megyekódot (A megye első három karaktere, ékezet nélkül): "
# f"Települések száma a megyében: {változó} db \n Megyében élők száma: {változó} fő \n Városokban élők száma: {változó} fő"
# "Nincs ilyen megyekód! \n \n Térjen vissza a főmenübe [x] \n Próbálja újra [Space] "
# "[a] Község \n [b] Város \n [c] Vármegyei jogú város \n [d] Vármegye székhely \n [e] "
#
# "Nyomja meg az [x] gombot a programból való kilépéshez"
# "[1] Megye adatai \n [2] Település típusai \n [x] Kilépés"
