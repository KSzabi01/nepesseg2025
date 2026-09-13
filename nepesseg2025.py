import math
import os

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


def print_oldal(bejovo_lista, oldal):
    terminal_meret = os.get_terminal_size()
    per_oldal = terminal_meret.lines - 7  # terminál magasság sorokban
    total = math.ceil(len(bejovo_lista) / per_oldal)    # felfelé kerekít
    oldal = max(1, min(oldal, total))                   # nem lehessen a max oldalszámon túl ugrani vagy 0 alá menni
    start = (oldal - 1) * per_oldal                     # első sor indexe
    print("\nSorszám | Település | Népesség (fő)\n")
    for i, sor in enumerate(bejovo_lista[start:start + per_oldal], start + 1):
        print(f"{i:>7}  {sor["telepules"]:<11}, {sor["ferfi"] + sor["no"]}")
    print(f"\n--- {oldal}/{total} oldal ---\n")


def telepules_tipusai(bejovo_tipus):
    tipusu_telepulesek = []
    match bejovo_tipus:
        case "a":
            keresett = "község"
        case "b":
            keresett = "nagyközség"
        case "c":
            keresett = "város"
        case "d":
            keresett = "vármegyei jogú város"
        case "e":
            keresett = "vármegye székhely"
        case "f":
            keresett = "fővárosi kerület"
        case _:
            return
    
    for i in database:
        if i["tipus"] == keresett:
            tipusu_telepulesek.append(i)
    
    return tipusu_telepulesek


def main():
    print()
    while True:
        print("Népesség 2025")
        print("--------\n Főmenü\n--------\n [1] Megye adatai \n [2] Település típusai \n [X] Kilépés")
        valasztas = input("Írja be a menüpont előtti karaktert, majd nyomjon [Enter]-t: ").strip().lower()
        match valasztas:
            case "x":
                break
            case "1":
                while True:
                    print("\033[2J\033[H", end="")
                    bekert_megye_kod = input("Adjon meg egy megyekódot (a megye első három karaktere, ékezet nélkül): ").upper()
                    megye_adatok = megye_adatai(bekert_megye_kod)
                    print()
                    if megye_adatok:
                        print(f"Települések száma a megyében: {megye_adatok["telepulesek_szama"]} db \n Megyében élők száma: {megye_adatok["lelekszam"]} fő \n Városokban élők száma: {megye_adatok["v_lelekszam"]} fő")
                        print()
                        break
                    else:
                        print("Nincs ilyen megyekód!\n\n [X] Térjen vissza a főmenübe\n [Space] Próbálja újra")
                        megye_ujra = input("Írja be a menüpont előtti karaktert, majd nyomjon [Enter]-t: ")
                        print()
                        if megye_ujra.lower() == "x":
                            break
            case "2":
                print("\033[2J\033[HVálasszon egy település típust:\n [A] Község\n [B] Nagyközség\n [C] Város\n [D] Vármegyei jogú város\n [E] Vármegye székhely\n [F] Fővárosi kerület")
                bekert_tipus = input("Adja meg a választott típus betűjét: ")
                kert_telepulesek = telepules_tipusai(bekert_tipus)
                if kert_telepulesek:
                    navigalt_oldal = 1
                    print_oldal(kert_telepulesek, navigalt_oldal)
                    while True:
                        print("<-[J] előző oldal -- <szám> ugrás az oldalra -- [L] következő oldal ->")
                        bekert_oldal = input("Válasszon a fentiek közül majd nyomjon [Enter]-t ([X] - főmenü): ")
                        match bekert_oldal.lower():
                            case "x":
                                break
                            case "j":
                                navigalt_oldal -= 1
                            case "l":
                                navigalt_oldal += 1
                            case _:
                                if bekert_oldal.isnumeric():
                                    navigalt_oldal = int(bekert_oldal)
                                else:
                                    print("\nNincs ilyen opció!")
                        print_oldal(kert_telepulesek, navigalt_oldal)
                else:
                    print("Nincs ilyen opció")
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
