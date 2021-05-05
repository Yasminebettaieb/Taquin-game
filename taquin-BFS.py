import pygame,sys,random
from pygame.locals import *

pygame.init()
fen=pygame.display.set_mode((181,179))

etat_initial=[[3,2,7],[8,6,9],[1,5,4]]

def position_case_vide (tableau):
  for i in range(3):
    for j in range(3):
      if tableau[i][j] ==9:
        return [i,j]

def initImages():#Chargement images
	images=[]
	for i in range(9):
		images.append(pygame.image.load("t"+str(i)+".png"))
	return images

def estEtatFinal(t, etat_final):
	return etat_final == t

def numero(t, x, y):
	return t[x][y]

from copy import deepcopy

def permuter(t, c1, c2):
	tperm = deepcopy(t)
	a = tperm[c1[0]][c1[1]]
	tperm[c1[0]][c1[1]] = tperm[c2[0]][c2[1]]
	tperm[c2[0]][c2[1]] = a
	return tperm

def valid(x, y):
	return x > -1 and x < 3 and y > -1 and y < 3


def transitions(t):
	pos = position_case_vide(t)
	tab = []
	dx = [1, -1, 0, 0]
	dy = [0, 0, 1, -1]
	for i in range(4):
		if (valid(pos[0] + dx[i], pos[1] + dy[i])):
			tab.append([pos[0] + dx[i], pos[1] + dy[i]])
	nvmatrice = []
	for i in tab:
		nvmatrice.append(permuter(t, pos, i))
	return nvmatrice

etat_final=[[3,2,7],[8,6,4],[1,9,5]]
images=initImages()
#affichage du tableau
def affiche(tableau,images):
	for i in range(3):
		for j in range(3):
			numeroCase=tableau[i][j]
			case=images[numeroCase-1]
			fen.blit(case,(i*60,j*60))

def afficher_taquin (t):
    for row in t:
      print('+++++++++++++')
      print('|',row[0],'|',row[1],'|',row[2],'|')
    print('+++++++++++++')
nb=0
trace= []
visited= []
success= False
etat_final=[[3,2,7],[8,6,4],[1,9,5]]
def bfs(node):
    global success
    global etat
    global visited
    global trace
    q = []
    q.append(node)
    while(len(q) != 0 and success==False):
        p=q.pop(0)
        trace.append(p)
        visited.append(p)
        if estEtatFinal(p,etat_final):
            success=True
        else:
            tab=transitions(p)
            for w in tab:
                if (w not in visited and success==False):
                    q.append(w)
bfs(etat_initial)
tableau = etat_initial = [[3, 2, 7], [8, 6, 9], [1, 5, 4]]
for k in trace:
	nb=nb+1
	affiche(k,images)
	afficher_taquin(tableau)
		#for evenement in pygame.event.get():
		#	affiche(tableau, images)
		#	if evenement.type == QUIT:
			#	pygame.quit()
				#sys.exit()
	pygame.display.update()
	pygame.time.wait(2000)
	if(nb==len(trace)):
		pygame.time.wait(20000)