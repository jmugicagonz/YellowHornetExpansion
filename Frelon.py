#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 11:06:53 2019

@author: jojo
"""
import numpy as np
import pygal.maps.fr

#Constante


#Variables intéressants
#N=[] #liste du nombre de nids par départements
#pour chaque départements, Qi=nombre de reine par nids
#D=[départements]
#V=[voisins], V[i:] est la liste des voisins de Di à partir de la matrice, à construire

#fonctions


##Juan
from pygal.style import Style
def neigbours(x,vectDep,Matrix): #retourne liste des voisins éléments x
    neigh=[]
    for y in Matrix[x]:
        if (Matrix[x][y]==1):
            neigh.append(y)
    return neigh
def SetNeighbours(Matrix): #Pour créer la matrice 
    Matrixin= []
    Matrixin.append((1,3,4))
    for i in np.arange(1):
        for j in np.arange(len(Matrixin[i])):
            index=Matrixin[i][j]
            Matrix[i][index-1]=1
    return

Departments = np.zeros(95) #Nb de nids par départements
Neighbours = np.zeros((95,95))
SetNeighbours(Neighbours)
custom_style = Style(
  #background='transparent',
  #plot_background='transparent',
  #foreground='#53E89B',
  #foreground_strong='#53A0E8',
  #foreground_subtle='#630C0D',
  #opacity='.6',
  #opacity_hover='.9',
  #transition='400ms ease-in',
  #colors=('#E853A0', '#E8537A', '#E95355', '#E87653', '#E89B53'))
  colors=('#0000FF', '#FF0000'))
fr_chart = pygal.maps.fr.Departments(human_readable=True,style=custom_style)
fr_chart.title = 'Population by department'
fr_chart.add('Abeilles en 2011', {'01': Departments[0], '02': Departments[1], '03': Departments[2], '04': Departments[3], '05': Departments[4], '06': Departments[5], '07': Departments[6], '08': Departments[7], '09': Departments[8], '10': Departments[9], '11': Departments[10], '12': Departments[11], '13': Departments[12], '14': Departments[13], '15': Departments[14], '16': Departments[15], '17': Departments[16], '18': Departments[17], '19': Departments[18], '20': Departments[19], '21': Departments[20], '22': Departments[21], '23': Departments[22], '24': Departments[23], '25': Departments[24], '26': Departments[25], '27': Departments[26], '28': Departments[27], '29': Departments[28], '30': Departments[29], '31': Departments[30], '32': Departments[31], '33': Departments[32], '34': Departments[33], '35': Departments[34], '36': Departments[35], '37': Departments[36], '38': Departments[37], '39': Departments[38], '40': Departments[39], '41': Departments[40], '42': Departments[41], '43': Departments[42], '44': Departments[43], '45': Departments[44], '46': Departments[45], '47': Departments[46], '48': Departments[47], '49': Departments[48], '50': Departments[49], '51': Departments[50], '52': Departments[51], '53': Departments[52], '54': Departments[53], '55': Departments[54], '56': Departments[55], '57': Departments[56], '58': Departments[57], '59': Departments[58], '60': Departments[59], '61': Departments[60], '62': Departments[61], '63': Departments[62], '64': Departments[63], '65': Departments[64], '66': Departments[65], '67': Departments[66], '68': Departments[67], '69': Departments[68], '70': Departments[69], '71': Departments[70], '72': Departments[71], '73': Departments[72], '74': Departments[73], '75': Departments[74], '76': Departments[75], '77': Departments[76], '78': Departments[77], '79': Departments[78], '80': Departments[79], '81': Departments[80], '82': Departments[81], '83': Departments[82], '84': Departments[83], '85': Departments[84], '86': Departments[85], '87': Departments[86], '88': Departments[87], '89': Departments[88], '90': Departments[89], '91': Departments[90], '92': Departments[91], '93': Departments[92], '94': Departments[93], '95': Departments[94]})
fr_chart.render_to_file('departments.svg')



##MARC

#Nombre de colonies dans le département D
N_D=100
#Superficie du département D
A_D=4111
r_0=0.9 #caractérise environnement par géographique


#Densité du département
C_D=N_D/A_D
    #On fixe r en fonction du département et on trouve le coefficient gamma tel que la moyenne soit égale à 5
gamma_0=(r_0-5)/(5*C_D) #calculé pour que la moyenne du nombre de reine soit égale à 5


def nbQueens(N,A,r,gamma):
    """return Q the number of new-born hornet queen in one departement, it is a random variable
    following a Poisson probability law with 5 as mean value"""
    C=N/A
    return np.random.poisson(r/(1+gamma*C), 1)[0]


#def moyenne(liste): #fonction auxiliaire de vérification que l'on tourne bien autour de 5
    #S=0
    #for element in liste:
        #S+=element
    #return S/len(liste)    
#print(moyenne(np.random.poisson(r_0/(1+gamma_0*C_D), 10000)))

##Jeff
m=28 #Distance moyenne: discutable
s=2 #distance influence ruches
def Voisin(T):
    n=len(T)
    V=[]
    for i in range(n):
        for j in range(n):
            temp=[]
            if T[i][j]==1:
                temp.append(j)
        V.append(temp)
    return(V)

def Queen(N,A,r,gamma): #Marc
    return(nbQueens(N,A,r,gamma))
def C(D,A,i):
    return(D[i-1]/A[i-1])

    
D_test=[1,2,3,4]
V_test=[[2,3],[1],[1,4],[3]]
A_test=[100,200,150,300]
N_0_test=[1,0,0,0]
Aocc_test=[15,0,0,0]


##Initialisation
N_0=[0]*93
N_0[13]=1

#P=len(D)
P=95 #à vérifier

def remplissageDépartement(N,D,V,A,Aocc): #A liste des aires par départements en 1 tour
    p=len(D)
    Q_born=[0]*p
    temp_tot=[]
    for i in range (p):#Naissance de reines par départements.
        A_dep=A[i]# aire totale du département
        A_occ=Aocc[i] #aire déjà prise par ruche existente
        Q=Queen(D[i])#nombre de queen à placer
        Q_born[i]=Q
        R=[] #rayon parcouru par queen par département mais non utile pour avalanche simple
        rho=[] # rayon influence par ruche
        t=[]
        for j in range(Q):
            r_i=np.random.normal(s)
            rho.append(r_i) #rayon d'influence 
            R_p=np.random.poisson(m)
            R.append(R_p) #rayon parcourable
            t.append([r_i,R_p])
        t.sort() #tri dans l'ordre des R croissant, donc de la distance parcouru
        temp=[] #liste des frelons à replacer
        for j in range (Q):
            if (A_dep-A_occ)**1/2>t[j][1]: #le frelon reste dans la zone accessible
                if A_dep>A_occ+np.pi*((t[j][0])**2): #il y'a de la place pour sa zone d'influence
                    N[j]+=1
                    A_occ+=np.pi*((t[j][0])**2)
                else: 
                    temp.append(t[j]) #à replacer: il n'y a pas la plac
            else:
                temp.append(t[j]) #à replacer: il va trop loin
        Aocc[i]=A_occ
        temp_tot.append(temp) #sortie de boucle, on a placer tous les frelons à placer du département, les autres sont dans temp et placé dans temp_tot par département
    return(N,Aocc,temp_tot) #Nombre de Nids par département, aire occupée par Département, nombre de frelons à replacer avec leur infos

#Ok pour remplissage! avec le format test
N_1_test,Aocc_1_test,temp_tot_test=remplissageDépartement(N_0_test,D_test,V_test,A_test,Aocc_test)    
    
    
def avalanche(N,Aocc,temp_tot,V,D,A): #V sont les voinsins, temp_tot=[[[Ri,rhoi]par nids non placés]par département]
    Concentration=[] #densité des nids
    q=len(N)
    p=len(D)
    t=[]
    for i in range (p): #Création d'une liste (concentration, département, nb reines à replacer)
        Concentration.append(C(D,A,i)) #fonction concentration de Marc
        t.append([Concentration[i],i,temp_tot[i]])
    t.sort(reverse=True) # on trie par concentratrion décroissante
    q=len(t)
    for m in range (q):
        j=t[m][1] #le département le plus concentré au moins concentré
        temp_tot_utile=t[m][2]#donne accès au (ri,Rj) à répartir
        N_tot=len(temp_tot_utile)
        Aocc_ajout=0
        for l in range(N_tot):
            Aocc_ajout+=np.pi*(temp_tot_utile[l][0]**2)
        N_temp=[0]*q
        Concentration_voisin=[0]*q
        Normalisation=0
        Dj=j #départements du plus concentrés au moins
        Vj=V[Dj] #Attention à la forme de V! Ici ok si tableau
        V_libre=libre(Vj,temp_tot) #Voisin apte à récupérer des reines
        for k in V_libre: # pb de recherche: il faut determiner les voisins libres (tq temp_tot de Dk est nul) puis calculer C(Dk) et répartir dans tous les voisins libres N=len(temp_tot[i])*(1/Cj)/sum(1/Cp))
           Ck=C(D,A,k)
           Concentration_voisin[k-1]=Ck
           N_temp[k-1]=N_tot*(1/Ck)
           Normalisation+=1/Ck
        for k in V_libre:
            ratio=N_temp[k-1]/Normalisation
            N[k-1]=ratio
            Aocc[k-1]+=ratio*Aocc_ajout #attention ça quelque soit la taille limite ==> Bug!!!
    return(N,Aocc)

N_2_test,Aocc_2_test=avalanche(N_1_test,Aocc_1_test,temp_tot_test,V_test,D_test)  
  
##Fonctionne
    
def libre(Vj,temp_tot):#liste des voisins de Dj, t=[[[Ri,rhoi]par départements]]
    libre=[]
    for k in Vj:
        temp=temp_tot[k-1] #liste des [ri,Ri]pour le département D[k]  #-1 car permet de récupérer le 0 à partir le dép 1
        if len(temp)==0:
            libre.append(k)
    return(libre)
            
    
    

        
            
            
            
            
            
            
            

        
        
        
    
    
        
        
    
    







