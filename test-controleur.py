import Controleur 
import Modele

#cette teste est generel et peut etre utilise avec quelquer etat du JSON animal et equipement


def test_nourrir():
    animalJson = Modele.openReadJsonAnimal()
    
    Controleur.nourrir('Tic')
    if Modele.verifie_disponibilite('mangeoire') == 'libre' or animalJson['Tic']['LIEU'] == 'mangeoire':
        if ( animalJson['Tic']['ETAT'] == 'affamé'): #si avant il etait affamé, donc il va changer d'etat
            assert Modele.lit_etat('Tic') == 'repus'
            assert Modele.lit_lieu('Tic') == 'mangeoire'
            assert Modele.verifie_disponibilite('mangeoire') == 'occupé'
        else:
            assert Modele.lit_etat('Tic') == animalJson['Tic']['ETAT']
            assert Modele.lit_lieu('Tic') == animalJson['Tic']['LIEU']
    else:
        assert Modele.lit_etat('Tic') == animalJson['Tic']['ETAT'] #after == before
        assert Modele.lit_lieu('Tic') == animalJson['Tic']['LIEU']

    Controleur.nourrir('Tac')
    if Modele.verifie_disponibilite('mangeoire') == 'libre' or animalJson['Tac']['LIEU'] == 'mangeoire':
        if ( animalJson['Tac']['ETAT'] == 'affamé'): #si avant il etait affamé, donc il va changer d'etat
            assert Modele.lit_etat('Tac') == 'repus'
            assert Modele.lit_lieu('Tac') == 'mangeoire'
            assert Modele.verifie_disponibilite('mangeoire') == 'occupé'
        else:
            assert Modele.lit_etat('Tac') == animalJson['Tac']['ETAT']
            assert Modele.lit_lieu('Tac') == animalJson['Tac']['LIEU']
    else:
        assert Modele.lit_etat('Tac') == animalJson['Tac']['ETAT'] #after == before
        assert Modele.lit_lieu('Tac') == animalJson['Tac']['LIEU']

    Controleur.nourrir('Patrick')
    if Modele.verifie_disponibilite('mangeoire') == 'libre' or animalJson['Patrick']['LIEU'] == 'mangeoire':
        if ( animalJson['Patrick']['ETAT'] == 'affamé'): #si avant il etait affamé, donc il va changer d'etat
            assert Modele.lit_etat('Patrick') == 'repus'
            assert Modele.lit_lieu('Patrick') == 'mangeoire'
            assert Modele.verifie_disponibilite('mangeoire') == 'occupé'
        else:
            assert Modele.lit_etat('Patrick') == animalJson['Patrick']['ETAT']
            assert Modele.lit_lieu('Patrick') == animalJson['Patrick']['LIEU']
    else:
        assert Modele.lit_etat('Patrick') == animalJson['Patrick']['ETAT'] #after == before
        assert Modele.lit_lieu('Patrick') == animalJson['Patrick']['LIEU']

    Controleur.nourrir('Totoro')
    if Modele.verifie_disponibilite('mangeoire') == 'libre' or animalJson['Totoro']['LIEU'] == 'mangeoire':
        if ( animalJson['Totoro']['ETAT'] == 'affamé'): #si avant il etait affamé, donc il va changer d'etat
            assert Modele.lit_etat('Totoro') == 'repus'
            assert Modele.lit_lieu('Totoro') == 'mangeoire'
            assert Modele.verifie_disponibilite('mangeoire') == 'occupé'
        else:
            assert Modele.lit_etat('Totoro') == animalJson['Totoro']['ETAT']
            assert Modele.lit_lieu('Totoro') == animalJson['Totoro']['LIEU']
    else:
        assert Modele.lit_etat('Totoro') == animalJson['Totoro']['ETAT'] #after == before
        assert Modele.lit_lieu('Totoro') == animalJson['Totoro']['LIEU']
    
    Controleur.nourrir('Pocahontas')
    if Modele.verifie_disponibilite('mangeoire') == 'libre' or animalJson['Pocahontas']['LIEU'] == 'mangeoire':
        if ( animalJson['Pocahontas']['ETAT'] == 'affamé'): #si avant il etait affamé, donc il va changer d'etat
            assert Modele.lit_etat('Pocahontas') == 'repus'
            assert Modele.lit_lieu('Pocahontas') == 'mangeoire'
            assert Modele.verifie_disponibilite('mangeoire') == 'occupé'
        else:
            assert Modele.lit_etat('Pocahontas') == animalJson['Pocahontas']['ETAT']
            assert Modele.lit_lieu('Pocahontas') == animalJson['Pocahontas']['LIEU']
    else:
        assert Modele.lit_etat('Pocahontas') == animalJson['Pocahontas']['ETAT'] #after == before
        assert Modele.lit_lieu('Pocahontas') == animalJson['Pocahontas']['LIEU']
   
    Controleur.nourrir('Bob')
    assert Modele.lit_etat('Bob') == None
    assert Modele.lit_lieu('Bob') == None

def test_divertir():
    animalJson = Modele.openReadJsonAnimal()

    Controleur.divertir('Tic')
    if Modele.verifie_disponibilite('roue') == 'libre' or animalJson['Tic']['LIEU'] == 'roue':
        if ( animalJson['Tic']['ETAT'] == 'repus'): 
            assert Modele.lit_etat('Tic') == 'fatigué'
            assert Modele.lit_lieu('Tic') == 'roue'
            assert Modele.verifie_disponibilite('roue') == 'occupé'
        else:
            assert Modele.lit_etat('Tic') == animalJson['Tic']['ETAT']
            assert Modele.lit_lieu('Tic') == animalJson['Tic']['LIEU']
    else:
        assert Modele.lit_etat('Tic') == animalJson['Tic']['ETAT'] #after == before
        assert Modele.lit_lieu('Tic') == animalJson['Tic']['LIEU']

    Controleur.divertir('Tac')
    if Modele.verifie_disponibilite('roue') == 'libre' or animalJson['Tac']['LIEU'] == 'roue':
        if ( animalJson['Tac']['ETAT'] == 'repus'): 
            assert Modele.lit_etat('Tac') == 'fatigué'
            assert Modele.lit_lieu('Tac') == 'roue'
            assert Modele.verifie_disponibilite('roue') == 'occupé'
        else:
            assert Modele.lit_etat('Tac') == animalJson['Tac']['ETAT']
            assert Modele.lit_lieu('Tac') == animalJson['Tac']['LIEU']
    else:
        assert Modele.lit_etat('Tac') == animalJson['Tac']['ETAT'] #after == before
        assert Modele.lit_lieu('Tac') == animalJson['Tac']['LIEU']

    Controleur.divertir('Patrick')
    if Modele.verifie_disponibilite('roue') == 'libre' or animalJson['Patrick']['LIEU'] == 'roue':
        if ( animalJson['Patrick']['ETAT'] == 'repus'): 
            assert Modele.lit_etat('Patrick') == 'fatigué'
            assert Modele.lit_lieu('Patrick') == 'roue'
            assert Modele.verifie_disponibilite('roue') == 'occupé'
        else:
            assert Modele.lit_etat('Patrick') == animalJson['Patrick']['ETAT']
            assert Modele.lit_lieu('Patrick') == animalJson['Patrick']['LIEU']
    else:
        assert Modele.lit_etat('Patrick') == animalJson['Patrick']['ETAT'] #after == before
        assert Modele.lit_lieu('Patrick') == animalJson['Patrick']['LIEU']

    Controleur.divertir('Totoro')
    if Modele.verifie_disponibilite('roue') == 'libre' or animalJson['Totoro']['LIEU'] == 'roue':
        if ( animalJson['Totoro']['ETAT'] == 'repus'): 
            assert Modele.lit_etat('Totoro') == 'fatigué'
            assert Modele.lit_lieu('Totoro') == 'roue'
            assert Modele.verifie_disponibilite('roue') == 'occupé'
        else:
            assert Modele.lit_etat('Totoro') == animalJson['Totoro']['ETAT']
            assert Modele.lit_lieu('Totoro') == animalJson['Totoro']['LIEU']
    else:
        assert Modele.lit_etat('Totoro') == animalJson['Totoro']['ETAT'] #after == before
        assert Modele.lit_lieu('Totoro') == animalJson['Totoro']['LIEU']

    Controleur.divertir('Pocahontas')
    if Modele.verifie_disponibilite('roue') == 'libre' or animalJson['Pocahontas']['LIEU'] == 'roue':
        if ( animalJson['Pocahontas']['ETAT'] == 'repus'): 
            assert Modele.lit_etat('Pocahontas') == 'fatigué'
            assert Modele.lit_lieu('Pocahontas') == 'roue'
            assert Modele.verifie_disponibilite('roue') == 'occupé'
        else:
            assert Modele.lit_etat('Pocahontas') == animalJson['Pocahontas']['ETAT']
            assert Modele.lit_lieu('Pocahontas') == animalJson['Pocahontas']['LIEU']
    else:
        assert Modele.lit_etat('Pocahontas') == animalJson['Pocahontas']['ETAT'] #after == before
        assert Modele.lit_lieu('Pocahontas') == animalJson['Pocahontas']['LIEU']

    Controleur.divertir('Bob')
    assert Modele.lit_etat('Bob') == None
    assert Modele.lit_lieu('Bob') == None

def test_coucher():
    animalJson = Modele.openReadJsonAnimal()

    Controleur.divertir('Tic')
    if Modele.verifie_disponibilite('nid') == 'libre' or animalJson['Tic']['LIEU'] == 'nid':
        if ( animalJson['Tic']['ETAT'] == 'fatigué'): 
            assert Modele.lit_etat('Tic') == 'endormi'
            assert Modele.lit_lieu('Tic') == 'nid'
            assert Modele.verifie_disponibilite('nid') == 'occupé'
        else:
            assert Modele.lit_etat('Tic') == animalJson['Tic']['ETAT']
            assert Modele.lit_lieu('Tic') == animalJson['Tic']['LIEU']
    else:
        assert Modele.lit_etat('Tic') == animalJson['Tic']['ETAT'] #after == before
        assert Modele.lit_lieu('Tic') == animalJson['Tic']['LIEU']

    Controleur.divertir('Tac')
    if Modele.verifie_disponibilite('nid') == 'libre' or animalJson['Tac']['LIEU'] == 'nid':
        if ( animalJson['Tac']['ETAT'] == 'fatigué'): 
            assert Modele.lit_etat('Tac') == 'endormi'
            assert Modele.lit_lieu('Tac') == 'nid'
            assert Modele.verifie_disponibilite('nid') == 'occupé'
        else:
            assert Modele.lit_etat('Tac') == animalJson['Tac']['ETAT']
            assert Modele.lit_lieu('Tac') == animalJson['Tac']['LIEU']
    else:
        assert Modele.lit_etat('Tac') == animalJson['Tac']['ETAT'] #after == before
        assert Modele.lit_lieu('Tac') == animalJson['Tac']['LIEU']
    
    Controleur.divertir('Patrick')
    if Modele.verifie_disponibilite('nid') == 'libre' or animalJson['Patrick']['LIEU'] == 'nid':
        if ( animalJson['Patrick']['ETAT'] == 'fatigué'): 
            assert Modele.lit_etat('Patrick') == 'endormi'
            assert Modele.lit_lieu('Patrick') == 'nid'
            assert Modele.verifie_disponibilite('nid') == 'occupé'
        else:
            assert Modele.lit_etat('Patrick') == animalJson['Patrick']['ETAT']
            assert Modele.lit_lieu('Patrick') == animalJson['Patrick']['LIEU']
    else:
        assert Modele.lit_etat('Patrick') == animalJson['Patrick']['ETAT'] #after == before
        assert Modele.lit_lieu('Patrick') == animalJson['Patrick']['LIEU']

    Controleur.divertir('Totoro')
    if Modele.verifie_disponibilite('nid') == 'libre' or animalJson['Totoro']['LIEU'] == 'nid':
        if ( animalJson['Totoro']['ETAT'] == 'fatigué'): 
            assert Modele.lit_etat('Totoro') == 'endormi'
            assert Modele.lit_lieu('Totoro') == 'nid'
            assert Modele.verifie_disponibilite('nid') == 'occupé'
        else:
            assert Modele.lit_etat('Totoro') == animalJson['Totoro']['ETAT']
            assert Modele.lit_lieu('Totoro') == animalJson['Totoro']['LIEU']
    else:
        assert Modele.lit_etat('Totoro') == animalJson['Totoro']['ETAT'] #after == before
        assert Modele.lit_lieu('Totoro') == animalJson['Totoro']['LIEU']
    
    Controleur.divertir('Pocahontas')
    if Modele.verifie_disponibilite('nid') == 'libre' or animalJson['Pocahontas']['LIEU'] == 'nid':
        if ( animalJson['Pocahontas']['ETAT'] == 'fatigué'): 
            assert Modele.lit_etat('Pocahontas') == 'endormi'
            assert Modele.lit_lieu('Pocahontas') == 'nid'
            assert Modele.verifie_disponibilite('nid') == 'occupé'
        else:
            assert Modele.lit_etat('Pocahontas') == animalJson['Pocahontas']['ETAT']
            assert Modele.lit_lieu('Pocahontas') == animalJson['Pocahontas']['LIEU']
    else:
        assert Modele.lit_etat('Pocahontas') == animalJson['Pocahontas']['ETAT'] #after == before
        assert Modele.lit_lieu('Pocahontas') == animalJson['Pocahontas']['LIEU']


def test_reveiller():
    animalJson = Modele.openReadJsonAnimal()

    Controleur.reveiller('Tac')
    if Modele.lit_etat('Tac') == 'endormi':
        assert Modele.lit_etat('Tac') == 'affamé'
        assert Modele.lit_lieu('Tac') == 'litière'
    else:
        assert Modele.lit_etat('Tac') == animalJson['Tac']['ETAT']
        assert Modele.lit_lieu('Tac') == animalJson['Tac']['LIEU']

    Controleur.reveiller('Tic')
    if Modele.lit_etat('Tic') == 'endormi':
        assert Modele.lit_etat('Tic') == 'affamé'
        assert Modele.lit_lieu('Tic') == 'litière'
    else:
        assert Modele.lit_etat('Tic') == animalJson['Tic']['ETAT']
        assert Modele.lit_lieu('Tic') == animalJson['Tic']['LIEU']

    Controleur.reveiller('Patrick')
    if Modele.lit_etat('Patrick') == 'endormi':
        assert Modele.lit_etat('Patrick') == 'affamé'
        assert Modele.lit_lieu('Patrick') == 'litière'
    else:
        assert Modele.lit_etat('Patrick') == animalJson['Patrick']['ETAT']
        assert Modele.lit_lieu('Patrick') == animalJson['Patrick']['LIEU']

    Controleur.reveiller('Totoro')
    if Modele.lit_etat('Totoro') == 'endormi':
        assert Modele.lit_etat('Totoro') == 'affamé'
        assert Modele.lit_lieu('Totoro') == 'litière'
    else:
        assert Modele.lit_etat('Totoro') == animalJson['Totoro']['ETAT']
        assert Modele.lit_lieu('Totoro') == animalJson['Totoro']['LIEU']

    Controleur.reveiller('Pocahontas')
    if Modele.lit_etat('Pocahontas') == 'endormi':
        assert Modele.lit_etat('Pocahontas') == 'affamé'
        assert Modele.lit_lieu('Pocahontas') == 'litière'
    else:
        assert Modele.lit_etat('Pocahontas') == animalJson['Pocahontas']['ETAT']
        assert Modele.lit_lieu('Pocahontas') == animalJson['Pocahontas']['LIEU']


test_nourrir()
test_divertir()
test_coucher()
test_reveiller()