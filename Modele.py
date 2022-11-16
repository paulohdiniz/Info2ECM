import json
from operator import truediv

etats_autorises = ["affamé","fatigué","repus","endormi"]
lieux_autorises = ["litière","mangeoire","roue","nid"]

def autorisationChangementDeEtat(etat):
        if etat in etats_autorises:
            return True
        else:
            return False

def verifieAnimalinJson(id_animal):
    animal = openReadJsonAnimal()
    if id_animal in animal:
        return True
    else:
        return False

def openReadJsonAnimal():
    with open('animal.json', "r") as file:
        animal = json.load(file)
    return animal

def writeAnimalInJson(animal):
    json.dump(animal, open("animal.json", "w"), indent=4)

        
def openJsonEquip():
    with open('équipement.json', "r") as file:
        equipament = json.load(file)
    return equipament

def writeJsonEquip(equipement):
    json.dump(equipement, open("équipement.json", "w"), indent=4)

def verifieEquip(equip):
    equipements = openJsonEquip()
    if equip in equipements:
        if equipements[equip] == 'libre' :
            return True
        else :
            False

def lit_etat(animal_id):
    animal = openReadJsonAnimal()
    if animal_id in animal:
        return animal[animal_id]['ETAT']
    else:
        print('Désolé, ' + animal_id + " n'est pas un animal connu")
        return None

def lit_lieu(animal_id):
    animal = openReadJsonAnimal()
    if animal_id in animal:
        return animal[animal_id]['LIEU']
    else:
        print('Désolé, ' + animal_id + " n'est pas un animal connu")
        return None

def verifie_disponibilite(équipement_id):
    equipement = openJsonEquip()
    if équipement_id in equipement:
        return equipement[équipement_id]['DISPONIBILITÉ']
    else:
        print('Désolé, ' + équipement_id + " n'est pas un équipement connu")
    return None

def cherche_occupant(lieu):
    animalJson = openReadJsonAnimal()
    lieuxJson = openJsonEquip()
    list = []
    for animal in animalJson:
        if (animalJson[animal]['LIEU'] == lieu):
            list.append(animal)
    if not(lieu in lieuxJson):
        print ("Désolé, " + lieu + " n'est pas un lieu connu")
        return None
    return list

def change_etat(id_animal, etat):
    animalJson = openReadJsonAnimal()
    if(verifieAnimalinJson(id_animal)):
        if(autorisationChangementDeEtat(etat)):
            animalJson[id_animal]['ETAT'] = etat
            writeAnimalInJson(animalJson)
        else:
            print("L'état " + etat + " n'est pas autorisé.")
    else: 
        print('Désolé, ' + id_animal + " n'est pas un animal connu")
        return None

def change_lieu(id_animal, lieu):
    animalJson = openReadJsonAnimal()
    equipements = openJsonEquip()
    
    if(lit_etat(id_animal) != None):
        lieu_animal_actuel = animalJson[id_animal]['LIEU']
        if(lieu in equipements):
            if(equipements[lieu]['DISPONIBILITÉ'] == 'libre' or lieu == 'litière'): #litière accepte plus d'un animal
                animalJson[id_animal]['LIEU'] = lieu
                writeAnimalInJson(animalJson)
                if (lieu_animal_actuel == 'litière'): #litière accepte plus d'un animal
                    if (len(cherche_occupant('litière')) == 0):
                        equipements[lieu_animal_actuel]['DISPONIBILITÉ'] = 'libre'
                else:
                    equipements[lieu_animal_actuel]['DISPONIBILITÉ'] = 'libre'
                equipements[lieu]['DISPONIBILITÉ'] = 'occupé'
                writeJsonEquip(equipements)
            else:
                print ("Désolé, le lieu " + lieu + " est déjà occupé.")
                return None
        else:
            print ("Désolé, le lieu " + lieu + " n'existe pas")
            return None
    else:
        return None
