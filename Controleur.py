import Modele

def nourrir(id_animal):
    lieuxJson = Modele.openJsonEquip()
    animalJson = Modele.openReadJsonAnimal()

    if(len(Modele.cherche_occupant('mangeoire')) != 0):
        ilyaqqndanslamangeoire = True
    else:
        ilyaqqndanslamangeoire = False

    if(Modele.lit_etat(id_animal) != None):
        if (lieuxJson['mangeoire']['DISPONIBILITÉ'] == 'occupé'):
            if(ilyaqqndanslamangeoire):
                if(Modele.cherche_occupant('mangeoire')[0] != id_animal):
                    print('Impossible, la mangeoire est actuellement occupée par ' + Modele.cherche_occupant('mangeoire')[0])
                    return "Impossible, la mangeoire est actuellement occupée par " + Modele.cherche_occupant('mangeoire')[0]
                elif Modele.lit_etat(id_animal) == 'affamé':
                    Modele.change_lieu(id_animal, 'mangeoire')
                    Modele.change_etat(id_animal, 'repus')
                    msg = 'nourri avec succès'
                    return msg
                else:
                    msg = 'Désolé, ' + id_animal + " n'a pas faim!"
                    print(msg)
                    return msg
                    
        elif Modele.lit_etat(id_animal) == 'affamé':
            Modele.change_lieu(id_animal, 'mangeoire')
            Modele.change_etat(id_animal, 'repus')
            msg = 'nourri avec succès'
            return msg
        else:
            msg = 'Désolé, ' + id_animal + " n'a pas faim!"
            print(msg)
            return msg


        
def divertir(id_animal):
    lieuxJson = Modele.openJsonEquip()
    animalJson = Modele.openReadJsonAnimal()

    if(len(Modele.cherche_occupant('roue')) != 0):
        ilyaqqndanslaroue = True
    else:
        ilyaqqndanslaroue = False
    
    if(Modele.lit_etat(id_animal) != None):
        if ( lieuxJson['roue']['DISPONIBILITÉ'] == 'occupé'):
            if(ilyaqqndanslaroue):
                if( Modele.cherche_occupant('roue')[0] != id_animal):
                    print('Impossible, la roue est actuellement occupée par ' + Modele.cherche_occupant('roue')[0])
                    return "Impossible, la roue est actuellement occupée par " + Modele.cherche_occupant('roue')[0]
                elif Modele.lit_etat(id_animal) == 'repus':
                    Modele.change_lieu(id_animal, 'roue')
                    Modele.change_etat(id_animal, 'fatigué')
                    msg = "Amusement fait avec succès."
                    return msg
                else:
                    msg = 'Désolé, ' + id_animal + " n'est pas en état de faire du sport!"
                    print(msg)
                    return msg

        elif Modele.lit_etat(id_animal) == 'repus':
            Modele.change_lieu(id_animal, 'roue')
            Modele.change_etat(id_animal, 'fatigué')
            msg = "Amusement fait avec succès."
            return msg
        else:
            msg = 'Désolé, ' + id_animal + " n'est pas en état de faire du sport!"
            print(msg)
            return msg

def coucher(id_animal):
    lieuxJson = Modele.openJsonEquip()
    animalJson = Modele.openReadJsonAnimal()

    if(len(Modele.cherche_occupant('nid')) != 0):
        ilyaqqndanslenid = True
    else:
        ilyaqqndanslenid = False

    if(Modele.lit_etat(id_animal) != None):
        if ( lieuxJson['nid']['DISPONIBILITÉ'] == 'occupé'):
            if(ilyaqqndanslenid):
                if( Modele.cherche_occupant('nid')[0] != id_animal):
                    print('Impossible, le nid est actuellement occupée par ' + Modele.cherche_occupant('nid')[0])
                    return "Impossible, le nid est actuellement occupée par " + Modele.cherche_occupant('nid')[0]
                elif Modele.lit_etat(id_animal) == 'fatigué':
                    Modele.change_lieu(id_animal, 'nid')
                    Modele.change_etat(id_animal, 'endormi')
                    msg = "Endormir avec succès."
                    return msg
                else:
                    msg = "Désolé, " + id_animal + " n'est pas fatigué!"
                    print(msg)
                    return msg
        elif Modele.lit_etat(id_animal) == 'fatigué':
            Modele.change_lieu(id_animal, 'nid')
            Modele.change_etat(id_animal, 'endormi')
            msg = "Endormir avec succès."
            return msg
        else:
            msg = "Désolé, " + id_animal + " n'est pas fatigué!"
            print(msg)
            return msg

def reveiller(id_animal):
    animalJson = Modele.openReadJsonAnimal()

    if(Modele.lit_etat(id_animal) != None):
        if(animalJson[id_animal]['ETAT'] != 'endormi'):
            print("Désole, " + id_animal + " ne dort pas !")
            return("Désole, " + id_animal + " ne dort pas !")
        else:
            Modele.change_lieu(id_animal, 'litière')
            Modele.change_etat(id_animal, 'affamé')
            msg = "Réveillé avec succès."
            return msg
            
