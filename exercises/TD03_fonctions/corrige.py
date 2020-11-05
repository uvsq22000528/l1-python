#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def TempsEnSeconde(temps):
    """renvoi le temps (en jour, heure, minute, seconde) en seconde."""
    jour, heure, minute, seconde = temps
    return ((jour*24 + heure)*60 + minute)*60 + seconde 

temps = (1, 2, 3, 4)
print(type(temps))
print(TempsEnSeconde(temps)

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))

def secondeEnTemps(seconde) :
    jour = seconde // (24*60*60)
    seconde = seconde % (24*60*60)
    heure = heure // (60*60)
    minute = seconde // (60))
    seconde = seconde % 60
    return (jour,heure,minute,seconde)

temps = secondeEnTemps (100000)
print (temps[0], "jour", temps[1],"heures", temps[2],"minutes",temps[3],"secondes")


def affiche_pluriel(valeur, mot) : 
    if(valeur!= 0)
        print(valeur, "", end ="")
        print(mot, end="")
        if(valeur > 1) :
            print(" ", end ="")

def afficheTemps(temps):
    affiche_pluriel(temps[0], "jour")
    affiche_pluriel(temps[1], "heure")
    affiche_pluriel(temps[2]), "minute")
    affiche_pluriel(temps[3], "seconde")

afficheTemps((1,0,14,23))


def demandeTemps() :
    jour = int(input("Entrer un nombre de jour"))
    heure = int(input("Entrer un nombre d'heures"))
    if(heure > 23) :
        print("Nombre d'heures incorrect")
        return
    minute = int(input("Entrer un nombre de minutes"))
    if(minute > 59) :
        print("Nombre de minutes incorrect")
        return
    seconde= int(input("Entrer un nombre de secondes"))
    if(seconde > 59) :
        print("Nombre de minutes incorrect")
        return
    return (jour, heure, minute, seconde)
afficheTemps (demandeTemps())