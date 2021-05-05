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
def array_to_string(t):
	s = ""
	for i in range(3):
		for j in range(3):
			s = s + str(t[i][j])
	return s


def string_to_array(s):
	nb = 0
	t = [0] * 3
	for i in range(3):
		t[i] = [0] * 3
	for i in range(3):
		for j in range(3):
			t[i][j] = int(s[nb], 10)
			nb = nb + 1
	return t


def aStar(start):
	# The open and closed sets
	openset = set()
	closedset = set()
	G = {}
	H = {}
	parent = {}
	Current = array_to_string(start)
	G[Current] = 0
	H[Current] = 0


	for i in range(3):
		for j in range(3):
			if (start[i][j] != etat_final[i][j]):
				H[Current] = H[Current] + 1
	openset.add(Current)
	parent[Current] = Current
	# While the open set is not empty
	while openset:
		Current = min(openset, key=lambda st: G[st] + H[st])
		if string_to_array(Current) == etat_final:
			path = []
			while parent[Current] != Current:
				path.append(Current)
				Current = parent[Current]
			path.append(Current)
			return path[::-1]
		openset.remove(Current)
		closedset.add(Current)
		currentarray = string_to_array(Current)
		for node in transitions(currentarray):
			NodeToStr = array_to_string(node)
			if NodeToStr in closedset:
				continue
			if NodeToStr in openset:
				new_g = G[Current] + 1
				if G[NodeToStr] > new_g:
					G[NodeToStr] = new_g
					parent[NodeToStr] = Current
			else:
				G[NodeToStr] = G[Current] + 1
				H[NodeToStr] = 0
				for i in range(3):
					for j in range(3):
						if (node[i][j] != etat_final[i][j]):
							H[NodeToStr] = H[NodeToStr] + 1
				parent[NodeToStr] = Current
				openset.add(NodeToStr)
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
#fonctionnement du taquin


for k in aStar(etat_initial):
	nb=nb+1
	tableau= string_to_array(k)
	affiche(tableau,images)
	afficher_taquin(tableau)
		#for evenement in pygame.event.get():
		#	affiche(tableau, images)
		#	if evenement.type == QUIT:
			#	pygame.quit()
				#sys.exit()
	pygame.display.update()
	pygame.time.wait(2000)
	if(nb==len(aStar(etat_initial))):
		pygame.time.wait(20000)
