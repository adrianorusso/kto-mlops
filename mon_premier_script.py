import unittest

def count_sup_length(liste_prenoms: list, length: int) -> int:
    """
    Compte le nombre de lettres de chaque élément dans une liste d'élements de chaine de caractères
    et affiche si l'élément a plus de lettres ou non que l'entier dans le paramètre [length].
    Et compte le nombre d'éléments ayant plus de lettres que l'entier dans le paramètre [length].

    Paramètres : liste(chaine de caractères)
    Retourne : entier (nombre d'éléments ayant plus de [length] lettres)
    """
    
    nb_more_than_length = 0 #Initialise à 0 la variable pour compter le nb d'élements >length(paramètre)
    for prenom in liste_prenoms: #Sur chaque élément
        sentance = prenom + " est un prénom avec un nombre de lettres " #facilite en cas de changement de phrase ou ajout de conditions
        if len(prenom) > length: #Si nombre de lettres >length(paramètre)
            nb_more_than_length += 1 #ajoute +1 dans le compteur
            print(sentance + "supérieur à " + str(length))
        else: #Si nombre de lettres <=length(paramètre)
            print(sentance + "inférieur ou égal à " + str(length))
    return nb_more_than_length #retourne nb éléments ayant nb lettres>length(paramètre)

class TestNamesMethod(unittest.TestCase):
     def test_names(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"] #liste de prénoms
        nb_more_than_seven = count_sup_length(liste_prenoms=prenoms, length=7) #appel fonction compter lettres de chaque éléments de la liste paramètres liste et entier
        self.assertEqual(nb_more_than_seven, 4) #vérifie si la fonction fonctionne bien

if __name__ == '__main__':
    unittest.main()