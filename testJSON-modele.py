import Modele

#cette teste est specific et il doit etre utilise avec quelquer le JSON initial fournit pour le prof dans son site.


def test_lit_etat():
    assert Modele.lit_etat('Tac') == 'affamé'
 
def test_lit_etat_nul():
    assert Modele.lit_etat('Bob') == None

def test_lit_lieu():
    assert Modele.lit_lieu('Tac') == 'litière'
 
def test_lit_lieu_nul():
    assert Modele.lit_lieu('Bob') == None

def test_verifie_disponibilite():
    assert Modele.verifie_disponibilite('litière') == 'libre'
    assert Modele.verifie_disponibilite('nid') == 'occupé'

def test_verifie_disponibilite_nul():
    assert Modele.verifie_disponibilite('nintendo') == None

def test_cherche_occupant():
    assert Modele.cherche_occupant('nid') == ['Pocahontas']
    assert 'Tac' in Modele.cherche_occupant('litière')
    assert 'Tac' not in Modele.cherche_occupant('mangeoire')

test_lit_etat()
test_lit_etat_nul()

test_lit_lieu()
test_lit_lieu_nul()

test_verifie_disponibilite()
test_verifie_disponibilite_nul()

test_cherche_occupant()