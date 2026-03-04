def ievade():
    cementa_daudzums=float(input("Ievadiet cementa daudzumu"))
    if cementa_daudzums<0:
        print("cementa daudzumam jābūt pozitīvam, aprēķini ir nepareizi")
    smilsu_cena=float(input("Ievadiet smilšu cenu"))
    if smilsu_cena<0:
        print("smilšu cenai jābūt pozitīvai, aprēķini ir nepareizi")
    cementa_cena=float(input("Ievadiet cementa cenu"))
    if cementa_cena<0:
        print("cementa cenai jābūt pozitīvai, aprēķini ir nepareizi")
    return(cementa_daudzums, smilsu_cena, cementa_cena)
def aprekini(cementa_daudzums, smilsu_cena, cementa_cena):
    smilsu_daudzums=cementa_daudzums*3
    udens_daudzums=cementa_daudzums*0.5
    betona_masa=smilsu_daudzums+udens_daudzums+cementa_daudzums
    kopejas_izmaksas=round((cementa_cena*cementa_daudzums+smilsu_daudzums*smilsu_cena), 2)
    



def izvade(smilsu_daudzums, udens_daudzums, kopejas_izmaksas, betona_masa):


    a, b, c=ievade()
    d, e, f, g=aprekini(a, b, c)
    izvade(d, e, f, g)