import Modele

#cette teste est generel et peut etre utilise avec quelquer etat du JSON animal et equipement

def test_verifie_disponibilite_nul():
    assert Modele.verifie_disponibilite('nintendo') == None

def test_cherche_occupant():
    assert Modele.cherche_occupant('nid') == ['Pocahontas']
    assert 'Tac' in Modele.cherche_occupant('litière')
    assert 'Tac' not in Modele.cherche_occupant('mangeoire')    

def test_cherche_occupant_nul():
    assert Modele.cherche_occupant('casino') == None

def test_change_etat():
    animalJson = Modele.openReadJsonAnimal()

    Modele.change_etat('Totoro', 'fatigué')
    if ('fatigué' in Modele.etats_autorises):
        assert Modele.lit_etat('Totoro') == 'fatigué'
    else:
        assert Modele.lit_etat('Totoro') == animalJson['Totoro']['ETAT']

    Modele.change_etat('Tac', 'excité comme un pou')
    if ('excité comme un pou' in Modele.etats_autorises):
        assert Modele.lit_etat('Tac') == 'excité comme un pou'
    else:
        assert Modele.lit_etat('Tac') == animalJson['Tac']['ETAT']

    Modele.change_etat('Bob', 'fatigué')
    assert Modele.lit_etat('Bob') == None

def test_change_lieu():
    equipementsJson = Modele.openJsonEquip()
    animalJson = Modele.openReadJsonAnimal()

    Modele.change_lieu('Tac', 'roue')
    if (equipementsJson['roue']['DISPONIBILITÉ'] == 'libre'):
        assert Modele.lit_lieu('Tac') == 'roue'
        assert Modele.verifie_disponibilite('roue') == 'occupé'  
    else:
        assert Modele.lit_lieu('Tac') == animalJson['Tac']['LIEU']

def test_change_lieu_occupé():
    animalJson = Modele.openReadJsonAnimal()
    equipementsJson = Modele.openJsonEquip()

    Modele.change_lieu('Totoro', 'nid')
    if(equipementsJson['nid']['DISPONIBILITÉ'] == 'libre'):
        assert Modele.lit_lieu('Totoro') == 'nid'
    else:
        assert Modele.lit_lieu('Totoro') == animalJson['Totoro']['LIEU']

def test_change_lieu_nul_1():
    animalJson = Modele.openReadJsonAnimal()
    Modele.change_lieu('Totoro', 'casino')
    if ('casino' in Modele.lieux_autorises):
        assert Modele.lit_lieu('Totoro') == 'casino'
    else:
        assert Modele.lit_lieu('Totoro') == animalJson['Totoro']['LIEU']

def test_change_lieu_nul_2():
    Modele.change_lieu('Bob', 'litière')
    assert Modele.lit_lieu('Bob') == None


test_verifie_disponibilite_nul()

test_cherche_occupant()
test_cherche_occupant_nul()

test_change_etat()

test_change_lieu()
test_change_lieu_occupé()
test_change_lieu_nul_1()
test_change_lieu_nul_2()