from googletrans import Translator
with open('24.txt', 'r',encoding="UTF-8") as file:
    F_rab = file.read().split('\n')
i2 = len(F_rab)
def perevodchik(stroka):
    transl = Translator()
    return str(transl.translate(stroka,dest="ru").text)
for i in range(0,i2):
    F = F_rab[i]
    if F.find("'")!=-1:
        if F.find("{")!=-1:
            stroka = F[F.find("'")+3:F.find("{")]
            if stroka.strip() != "":
                perevod = perevodchik(stroka)
                print(perevod)
                F_rab[i] = F_rab[i].replace(stroka, perevod)
        else:
            stroka = F[F.find("'")+1:-1]
            if stroka.strip() != "":
                perevod = perevodchik(stroka)
                print(perevod)
                F_rab[i] = F_rab[i].replace(stroka, perevod)

with open('25.txt', 'a',encoding="UTF-8") as file:
    for i in range(0,i2):
        file.write(F_rab[i]+"\n")


