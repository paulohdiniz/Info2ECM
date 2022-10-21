import Modele

def nourrir(id_animal):
    lieuxJson = Modele.openJsonEquip()
    animalJson = Modele.openReadJsonAnimal()

    if(Modele.lit_etat(id_animal) != None):
        if (not lieuxJson['mangeoire']['DISPONIBILITÉ'] == 'libre'):
            print('Impossible, la mangeoire est actuellement occupée par ' + Modele.cherche_occupant('mangeoire')[0])

        if(not Modele.lit_etat(id_animal) == 'affamé'):
            print('Désolé, ' + id_animal + " n'a pas faim!")
        elif lieuxJson['mangeoire']['DISPONIBILITÉ'] == 'libre':
            Modele.change_lieu(id_animal, 'mangeoire')
            Modele.change_etat(id_animal, 'repus')
        
def divertir(id_animal):
    lieuxJson = Modele.openJsonEquip()
    animalJson = Modele.openReadJsonAnimal()

    if(Modele.lit_etat(id_animal) != None):
        if(lieuxJson['roue']['DISPONIBILITÉ'] == 'occupé' and Modele.cherche_occupant('roue')[0] != id_animal):
            print("Impossible, la roue est actuellement occupée par " + Modele.cherche_occupant('roue')[0])
        else:
            if(not animalJson[id_animal]['ETAT'] == 'repus'):
                print("Désolé, " + id_animal + " n'est pas en état de faire du sport!")

        if (animalJson[id_animal]['ETAT'] == 'repus' and lieuxJson['roue']['DISPONIBILITÉ'] == 'libre'):
            Modele.change_lieu(id_animal, 'roue')
            Modele.change_etat(id_animal, 'fatigué')

def coucher(id_animal):
    lieuxJson = Modele.openJsonEquip()
    animalJson = Modele.openReadJsonAnimal()

    if(Modele.lit_etat(id_animal) != None):
        if(lieuxJson['nid']['DISPONIBILITÉ'] == 'occupé' and Modele.cherche_occupant('nid')[0] != id_animal):
            print("Impossible, le nid est actuellement occupée par " + Modele.cherche_occupant('nid')[0])
        else:
            if(not animalJson[id_animal]['ETAT'] == 'fatigué' and animalJson[id_animal]['ETAT'] != 'endormi'):
                print("Désolé, " + id_animal + " n'est pas fatigué!")
            if(animalJson[id_animal]['ETAT'] == 'endormi'):
                print(id_animal + " dort déjà !")
        if (animalJson[id_animal]['ETAT'] == 'fatigué' and lieuxJson['nid']['DISPONIBILITÉ'] == 'libre'):
            Modele.change_lieu(id_animal, 'nid')
            Modele.change_etat(id_animal, 'endormi')

def reveiller(id_animal):
    lieuxJson = Modele.openJsonEquip()
    animalJson = Modele.openReadJsonAnimal()

    if(Modele.lit_etat(id_animal) != None):
        if(animalJson[id_animal]['ETAT'] != 'endormi'):
            print("Désole, " + id_animal + " ne dort pas !")
        else:
            Modele.change_lieu(id_animal, 'litière')
            Modele.change_etat(id_animal, 'affamé')
            
