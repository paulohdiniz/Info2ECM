# import the library
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo 
from tkinter import messagebox

import Modele
import Controleur
#from appJar import gui
#app = gui()
#app.addLabel("title", "Welcome to appJar")
#app.setLabelBg("title", "red")
#app.go()


liste_animaux = ['Tic', 'Tac', 'Totoro', 'Patrick', 'Pocahontas']
liste_action = ['nourrir', 'divertir', 'coucher', 'reveiller']

fenetre = Tk()
fenetre.geometry("700x500")



p = PanedWindow(fenetre, orient=VERTICAL)
p.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)

l1 = LabelFrame(fenetre, text="Actions", padx=5, pady=5)
l1.pack(fill="both", expand="yes")

l2 = LabelFrame(fenetre, text="List animaux", padx=5, pady=5)
l2.pack(fill="both", expand="yes")

for animal_id in liste_animaux:
    p.add(Label(p, text = f"{animal_id}: {Modele.lit_etat(animal_id)}, {Modele.lit_lieu(animal_id)}", bg = "blue", anchor=CENTER))
p.pack(padx =100, pady=10)


valueAnimal = StringVar()
buttonAnimal = []
for i in range(len(liste_animaux)):
    buttonAnimal.append(Radiobutton(l2, text = liste_animaux[i], variable=valueAnimal, value = i))
    buttonAnimal[i].pack()

valueAction = StringVar()
buttonActions =[]
for j in range(len(liste_action)):
    buttonActions.append(Radiobutton(l1, text = liste_action[j], variable=valueAction, value = j))
    buttonActions[j].pack()



def press(action):
    action = valueAction.get()
    animal = valueAnimal.get()

    if (action == '0'):
        info = Controleur.nourrir(liste_animaux[int(animal)])
        showinfo(title = 'Information', message =  info + " si mis à jour, redémarrez le programme pour voir le nouveau statut\lieu de l'animal")
    if (action == '1'):
        info = Controleur.divertir(liste_animaux[int(animal)])
        showinfo(title = 'Information', message =  info + " si mis à jour, redémarrez le programme pour voir le nouveau statut\lieu de l'animal")
    if (action == '2'):
        info = Controleur.coucher(liste_animaux[int(animal)])
        showinfo(title = 'Information', message =  info + " si mis à jour, redémarrez le programme pour voir le nouveau statut\lieu de l'animal")
    if (action == '3'):
        info = Controleur.reveiller(liste_animaux[int(animal)])
        showinfo(title = 'Information', message =  info + " si mis à jour, redémarrez le programme pour voir le nouveau statut\lieu de l'animal")


   



#def mise_a_jour():
    #fenetre.destroy()
    

btn = ttk.Button(fenetre, text = "Go",  command = lambda: press(valueAction.get()))
btn.pack()
fenetre.mainloop()