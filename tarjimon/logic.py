import os

from mysite.settings import BASE_DIR


def read_file(Text_file):  # Fayldıń shaqırılǵan jeri

    import pandas as pd
    excel_file_path = os.path.join(BASE_DIR, 'media/excel/base1.xlsx')
    df = pd.read_excel(excel_file_path)

    Atliq = df.iloc[:, 0].values
    Feyil = df.iloc[:19676, 1].values
    Tirkewish = df.iloc[:59, 2].values
    Modal = df.iloc[:59, 3].values
    Daneker = df.iloc[:46, 4].values
    Tanlaq = df.iloc[:65, 5].values
    Eliklewish = df.iloc[:145, 6].values
    Almasiq = df.iloc[:49, 7].values
    Kelbetlik = df.iloc[:7225, 8].values
    Sanliq = df.iloc[:7560, 9].values

    def Analiz(text, Text4):  # разбивает слова в текстовом файле на функции
        kesh = ''
        for soz in text:
            if Almasiq_f(soz) != None:
                kesh = soz + ' : ' + Almasiq_f(soz)
                Text4.append(kesh)

            elif Tirkewish_f(soz) != None:
                kesh = soz + ' : ' + Tirkewish_f(soz)
                Text4.append(kesh)

            elif Daneker_f(soz) != None:
                kesh = soz + ' : ' + Daneker_f(soz)
                Text4.append(kesh)

            elif Tanlaq_f(soz) != None:
                kesh = soz + ' : ' + Tanlaq_f(soz)
                Text4.append(kesh)

            elif Eliklewish_f(soz) != None:
                kesh = soz + ' : ' + Eliklewish_f(soz)
                Text4.append(kesh)

            elif Hareket_f(soz) != None:
                kesh = soz + ' : ' + Hareket_f(soz)
                Text4.append(kesh)

            elif Modal_f(soz) != None:
                kesh = soz + ' : ' + Modal_f(soz)
                Text4.append(kesh)

            elif Sanliq_f(soz) != None:
                kesh = soz + ' : ' + Sanliq_f(soz)
                Text4.append(kesh)

            elif fun_atliq(soz) != None:
                kesh = soz + ' : ' + fun_atliq(soz)
                Text4.append(kesh)


            elif Kelbetlik_f(soz) != None:
                kesh = soz + ' : ' + Kelbetlik_f(soz)
                Text4.append(kesh)
            else:
                kesh = soz + ' : -------'
                Text4.append(kesh)

        return Text4

    def fun_atliq(a):
        aa = ''
        for i in Atliq:
            if a.lower() == i.lower():
                aa = 'Atliq'
                if len(a) > 3:
                    aa = Koplik(a, aa)
                    aa = Tartım(a, aa)
                    aa = Seplik(a, aa)
                    a = Seplik1(a)
                    a = Tartim1(a)
                    a = Koplik1(a)

                return '(' + a + ')' + aa
            elif len(a) > 3:
                aa = Koplik(a, aa)
                aa = Tartım(a, aa)
                aa = Seplik(a, aa)
                a = Seplik1(a)
                a = Tartim1(a)
                a = Koplik1(a)

                if aa != '':
                    return '(' + a + ')' + ' Atliq ' + aa

    def Tartım(a, aa):
        if a[-4:] == 'imiz' or a[-6:-2] == 'imiz' or a[-7:-3] == 'imiz':
            return aa + " + (imiz) tartım"
        elif a[-4:] == 'ımız' or a[-6:-2] == 'ımız' or a[-7:-3] == 'ımız':
            return aa + " + (ımız) tartım"
        else:
            return aa

    def Tartim1(a):
        if a[-4:] == 'imiz' or a[-4:] == 'ımız':
            return a[:-4]
        elif a[-3:] == 'miz' or a[-3:] == 'mız':
            return a[:-3]
        else:
            return a

    def Seplik(a, aa):  # определяет падеж
        if a[-3:] == 'niń':
            return aa + " + (niń) Iyelik sepligi"
        elif a[-3:] == 'diń':
            return aa + " + (diń) Iyelik sepligi"
        elif a[-3:] == 'tiń':
            return aa + " + (tiń) Iyelik sepligi"
        elif a[-3:] == 'nıń':
            return aa + " + (nıń) Iyelik sepligi"
        elif a[-3:] == 'dıń':
            return aa + " + (dıń) Iyelik sepligi"
        elif a[-3:] == 'tıń':
            return aa + " + (tıń) Iyelik sepligi"
        elif a[-2:] == 'ǵa':
            return aa + " + (ǵa) Baris sepligi"
        elif a[-2:] == 'ga':
            return aa + " + (ga) Baris sepligi"
        elif a[-2:] == 'ge':
            return aa + " + (ge) Baris sepligi"
        elif a[-2:] == 'ke':
            return aa + " + (ke) Baris sepligi"
        elif a[-2:] == 'qa':
            return aa + " + (qa) Baris sepligi"
        elif a[-2:] == 'na':
            return aa + " + (na) Baris sepligi"
        elif a[-2:] == 'ne':
            return aa + " + (ne) Baris sepligi"
        elif a[-2:] == 'di':
            return aa + " + (di) Tabis sepligi"
        elif a[-2:] == 'ti':
            return aa + " + (ti) Tabis sepligi"
        elif a[-2:] == 'ni':
            return aa + " + (ni) Tabis sepligi"
        elif a[-2:] == 'dı':
            return aa + " + (dı) Tabis sepligi"
        elif a[-2:] == 'tı':
            return aa + " + (tı) Tabis sepligi"
        elif a[-2:] == 'nı':
            return aa + " + (nı) Tabis sepligi"
        elif a[-2:] == 'ın':
            return aa + " + (ın) Tabis sepligi"
        elif a[-3:] == 'dan':
            return aa + " + (dan) Shigis sepligi"
        elif a[-3:] == 'den':
            return aa + " + (den) Shigis sepligi"
        elif a[-3:] == 'tan':
            return aa + " + (tan) Shigis sepligi"
        elif a[-3:] == 'ten':
            return aa + " + (ten) Shigis sepligi"
        elif a[-3:] == 'nan':
            return aa + " + (ten) Shigis sepligi"
        elif a[-3:] == 'nen':
            return aa + " + (nen) Shigis sepligi"
        elif a[-2:] == 'da':
            return aa + " + (da) Orin sepligi"
        elif a[-2:] == 'de':
            return aa + " + (de) Orin sepligi"
        elif a[-2:] == 'ta':
            return aa + " + (ta) Orin sepligi"
        elif a[-2:] == 'te':
            return aa + " + (te) Orin sepligi"
        elif a[-3:] == 'nda':
            return aa + " + (nda) Orin sepligi"
        elif a[-3:] == 'nde':
            return aa + " + (nde) Orin sepligi"
        else:
            return aa

    def Seplik1(a):
        if a[-2:] == 'ǵa' or a[-2:] == 'ga' or a[-2:] == 'ge' or a[-2:] == 'qa' or a[-2:] == 'ke' or a[
                                                                                                     -2:] == 'na' or a[
                                                                                                                     -2:] == 'ne' or a[
                                                                                                                                     -2:] == 'di' or a[
                                                                                                                                                     -2:] == 'ti' or a[
                                                                                                                                                                     -2:] == 'ni' or a[
                                                                                                                                                                                     -2:] == 'dı' or a[
                                                                                                                                                                                                     -2:] == 'tı' or a[
                                                                                                                                                                                                                     -2:] == 'nı' or a[
                                                                                                                                                                                                                                     -2:] == 'ın' or a[
                                                                                                                                                                                                                                                     -2:] == 'da' or a[
                                                                                                                                                                                                                                                                     -2:] == 'de' or a[
                                                                                                                                                                                                                                                                                     -2:] == 'ta' or a[
                                                                                                                                                                                                                                                                                                     -2:] == 'te':
            return a[:-2]
        elif a[-3:] == 'niń' or a[-3:] == 'diń' or a[-3:] == 'tıń' or a[-3:] == 'nıń' or a[-3:] == 'dıń' or a[
                                                                                                            -3:] == 'tıń' or a[
                                                                                                                             -3:] == 'tan' or a[
                                                                                                                                              -3:] == 'ten' or a[
                                                                                                                                                               -3:] == 'dan' or a[
                                                                                                                                                                                -3:] == 'den' or a[
                                                                                                                                                                                                 -3:] == 'nan' or a[
                                                                                                                                                                                                                  -3:] == 'nen' or a[
                                                                                                                                                                                                                                   -3:] == 'nda' or a[
                                                                                                                                                                                                                                                    -3:] == 'nde':
            return a[:-3]
        else:
            return a

    def Koplik(a, aa):  # определяет множествонное слово
        if a[-6:-3] == 'lar' or a[-5:-2] == 'lar' or a[-3:] == 'lar' or a[-9:-6] == 'lar' or a[-10:-7] == 'lar':
            return aa + " + (lar) ko'plik "
        elif a[-6:-3] == 'ler' or a[-5:-2] == 'ler' or a[-3] == 'ler' or a[-9:-6] == 'ler' or a[-10:-7] == 'ler':
            return aa + " + (ler) ko'plik "
        elif a[-4] == 'leri':
            return aa + " + (leri) ko'plik "
        elif a[-4] == 'lerı':
            return aa + " + (lerı) ko'plik "
        elif a[-4] == 'ları':
            return aa + " + (ları) ko'plik "
        elif a[-4] == 'lari':
            return aa + " + (lari) ko'plik "
        else:
            return aa

    def Koplik1(a):
        if a[-3:] == 'lar' or a[-3:] == 'ler':
            return a[:-3]
        elif a[-4:] == 'leri' or a[-4:] == 'lari' or a[-4:] == 'ları' or a[-4:] == 'lerı':
            return a[:-4]
        else:
            return a

    def Kelbetlik_f(sóz):  # определяет прилагательное
        for i in Kelbetlik:  # Bul jerdi kelbetlik bazaǵa tirkew kerek
            if sóz.lower() == i.lower():
                return "Kelbetlik"
            if sóz[-3:] == 'lıq' or sóz[-3:] == 'lik' or sóz[-3:] == 'góy' or sóz[-3:] == 'dar' or sóz[-3:] == 'xor':
                return "Kelbetlik"
            if sóz[-4:] == 'shań' or sóz[-4:] == 'sheń' or sóz[-4:] == 'shil' or sóz[-4:] == 'shıl':
                return "Kelbetlik"
            if sóz[-2:] == 'ıy' or sóz[-2:] == 'iy' or sóz[-4:] == 'qı' or sóz[-4:] == 'qi' or sóz[-4:] == 'ǵı' or sóz[
                                                                                                                   -4:] == 'ǵi':
                return "Kelbetlik"

    def Hareket_f(h):  # определяет движение
        for i in Feyil:  # Feyil bazaǵa baylanısıtırw kerek // Kiritildi
            if h.lower() == i.lower():
                return "Hareket feyil"

    def Tirkewish_f(h):
        for i in Tirkewish:
            if h.lower() == i.lower():
                return "Tirkewish"

    def Modal_f(h):
        for i in Modal:
            if h.lower() == i.lower():
                return "Modal soz"

    def Daneker_f(h):
        for i in Daneker:
            if h.lower() == i.lower():
                return "Daneker soz"

    def Tanlaq_f(h):
        for i in Tanlaq:
            if h.lower() == i.lower():
                return "Tanlaq soz"

    def Eliklewish_f(h):
        for i in Eliklewish:
            if h.lower() == i.lower():
                return "Eliklewish soz"

    def Almasiq_f(h):
        for i in Almasiq:
            if h.lower() == i.lower():
                return "Almasıq"

    def Almasıq_sep(h):
        for i in Almasiq:
            if h.lower() == i.lower():
                return 'Almasiq'

    def Daneker_f(h):
        for i in Daneker:
            if h.lower() == i.lower():
                return "Daneker"

    def Baylanis_f(b):  # определяет связи
        for i in Baylanis:  # baylanis basaga baylanistiriw kerek
            if i.lower() == b.lower():
                return "Baylanis"

    def Jagday_f(j):  # определяет состояние
        for i in Jagday:
            if i.lower() == j.lower():
                return "Jagday"

    def Sanliq_f(san):
        san = San_f(san)
        for i in Sanliq:
            j = str(i)
            if j.lower() == san.lower():
                return 'Sanliq'

    def San_f(san):
        b = ''
        for i in san:
            if i != '-' and i != '.' and i != ',':
                b = b + str(i)
            elif i == '-' or i == '.' or i == ',':
                return b
        return b

    # file = open(Text_file,'r',encoding='utf-8')
    # file_read=file.read()
    # file.close()

    Text1 = Text_file.split('.')
    Text3 = []
    Text4 = []
    Text5 = ''

    for gap in Text1:
        Text3 = []
        Text2 = gap.split(' ')

        for i in Text2:
            if i != '':
                if i[-1] == ',' or i[-1] == '?' or i[-1] == '!':
                    Text3.append(i[:-1])
                else:
                    Text3.append(i)

        Text4 = Analiz(Text3, Text4)
    return Text4  # kazirshe returnga qaaytarip qoyipban