# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 11:28:05 2022

@author: sojeb
"""


from values import *
from owlready2 import *
#onto_path.append("/path/to/your/local/ontology/repository")
#onto = get_ontology("SB.owl")
onto = get_ontology("lailaowlv1.owl")
onto.load()


def storeVille(onto):
    for v in villes:
        v=str(v)
        ville = onto.Ville(supprimerAccent(v).capitalize().replace(" ","_"))
        ville.nomVille=[v]
        ville.nomPays = ["France"]

def storeUniversite(onto):
    for u in universites:
        u=str(u)
        universite = onto.Universite(supprimerAccent(u).capitalize().replace(" ","_"))
        universite.nomUniversite=[u]
        if(len(list(onto.search(iri = ("*"+universitesVilles[u])))) > 0):
            universite.nomVilleUniversite=[list(onto.search(iri = ("*"+universitesVilles[u])))[0]]

def storeVaccins(onto):
    for i in list(range(10)):
        for vc in vaccins:
            vc=str(vc)
            vaccin = onto.Vaccin(supprimerAccent(vc).capitalize().replace(" ","_")+"_"+str(i))
            vaccin.nomVaccin=[vc]
            vaccin.numVaccin=[str(i)]
        
        for vc in vaccinsHepatite:
            vc=str(vc)
            vaccin = onto.VaccinHepatite(supprimerAccent(vc).capitalize().replace(" ","_")+"_"+str(i))
            vaccin.nomVaccin=[vc]
            vaccin.numVaccin=[str(i)]
    for i in list(range(25)) :
        for vc in vaccinsCovid:
            vc=str(vc)
            vaccin = onto.VaccinCovid(supprimerAccent(vc).capitalize().replace(" ","_")+"_"+str(i))
            vaccin.nomVaccin=[vc]
            vaccin.numVaccin=[str(i)]


def storeMaladie(onto):
    for m in maladiesGrave:
        m=str(m)
        maladieGrave = onto.MaladieGrave(supprimerAccent(m).capitalize().replace(" ","_"))
    for m in maladiesGenetique:
        m=str(m)
        maladieGrave = onto.MaladieGenetique(supprimerAccent(m).capitalize().replace(" ","_"))
    for m in maladies:
        m=str(m)
        maladieGrave = onto.Maladie(supprimerAccent(m).capitalize().replace(" ","_"))
        

def storePatients(onto):
    for i in list(range(60)):  #150
        nom = get_radom_name()
        prenom = get_radom_name()
        p = onto.Patient(nom.upper()+"_"+prenom)
        p.nomPersonne = [nom]
        p.prenomPersonne = [prenom]
        p.anneeDeNaissance = [str(randint(1940,2005))]
        p.villeDeNaissance = [str(villes[randint(0,len(villes)-1)])]
        nbMaladieOnto = len(onto.search(type = onto.Maladie))
        listMaladieOnto = onto.search(type = onto.Maladie)
        nbMaladie = randint(0,3)
        listMaladies = []
        for j in list(range(nbMaladie)):
            listMaladies.append(listMaladieOnto[randint(0,nbMaladieOnto-1)])
        if len(listMaladies)>0 : p.atteinte = listMaladies

        

def storeInfirmier(onto):
    for i in list(range(20)): #"150"
        nom = get_radom_name()
        prenom = get_radom_name()
        p = onto.Infirmier(nom.upper()+"_"+prenom)
        p.nomPersonne = [nom]
        p.prenomPersonne = [prenom]
        p.anneeDeNaissance = [randint(1940,2000)]
        p.villeDeNaissance = [str(villes[randint(0,len(villes)-1)])]
        nbUnivOnto = len(onto.search(type = onto.Universite))
        listUnivOnto = onto.search(type = onto.Universite)
        nbUniv = randint(1,1)
        listUniv = []
        for j in list(range(nbUniv)):
            listUniv.append(listUnivOnto[randint(0,nbUnivOnto-1)])
        p.est_diplome = listUniv
        #print(listUniv)
        
        nbPatientOnto = len(onto.search(type = onto.Patient))
        listPatientOnto = onto.search(type = onto.Patient)
        nbpatients = randint(1,5)
        listPatient = []
        for j in list(range(nbpatients)):
            if (len(listPatientOnto)>0) : 
                listPatient.append(listPatientOnto[randint(0,nbPatientOnto-1)])
        p.soigne = listPatient
        #print(listPatient)
        listHopitauxOnto = onto.search(type = onto.Hopital)
        nbHopitaux = len(listHopitauxOnto)
        p.travaille = [listHopitauxOnto[randint(0, nbHopitaux-1)]]
        #print(p.travaille)


def storeHopital(onto):
    for h in hopitaux.keys():
        hopital = onto.Hopital(supprimerAccent(h).capitalize().replace(" ","_"))
        hopital.nomHopital = [h]
        hopital.nomVilleHopital = [onto.search(iri = ("*"+hopitaux[h].lower()))[0]]
        

def storeService(onto):
    for h in hopitaux:
        hopitalOnto = onto.search(iri = "*"+supprimerAccent(h.lower()).capitalize().replace(" ","_"))[0]
        listService = []
        for s in serviceOphtalmologie:
            service = onto.ServiceOphtalmologie(supprimerAccent(s).capitalize().replace(" ","_")+"_"+supprimerAccent(h).capitalize().replace(" ","_"))
            service.nomService = [str(s)]
            listService.append(service)
        for s in serviceDermatologie:
            service = onto.ServiceDermatologie(supprimerAccent(s).capitalize().replace(" ","_")+"_"+supprimerAccent(h).capitalize().replace(" ","_"))
            service.nomService = [str(s)]
            listService.append(service)
        for s in serviceCardiologie:
            service = onto.ServiceCardiologie(supprimerAccent(s).capitalize().replace(" ","_")+"_"+supprimerAccent(h).capitalize().replace(" ","_"))
            service.nomService = [str(s)]
            listService.append(service)
        hopitalOnto.est_compose = listService
 

#storeHopital(onto)

def storeMedecin(onto):
    for i in list(range(12)): #210 50
    
        listHopitauxOnto = onto.search(type = onto.Hopital)
        nbHopitaux = len(listHopitauxOnto)
        hopital = listHopitauxOnto[randint(0, nbHopitaux-1)]
        
        nom = get_radom_name()
        prenom = get_radom_name()
        typeMed = randint(0,3)
        if(typeMed==0):
            p = onto.MedecinGeneraliste(nom.upper()+"_"+prenom)
            listServicesOnto = []
        elif (typeMed==1):
            p = onto.Ophtalmologiste(nom.upper()+"_"+prenom)
            listServicesOnto = onto.search(type = onto.ServiceOphtalmologie, iri="*"+hopital.name)
        elif (typeMed==2):
            p = onto.Dermatologue(nom.upper()+"_"+prenom)
            listServicesOnto = onto.search(type = onto.ServiceDermatologie, iri="*"+hopital.name)
        elif (typeMed==3):
            p = onto.Cardiologue(nom.upper()+"_"+prenom)
            listServicesOnto = onto.search(type = onto.ServiceCardiologie, iri="*"+hopital.name)

        p.nomPersonne = [nom]
        p.prenomPersonne = [prenom]
        p.anneeDeNaissance = [randint(1940,1990)]
        p.villeDeNaissance = [str(villes[randint(0,len(villes)-1)])]
        nbUnivOnto = len(onto.search(type = onto.Universite))
        listUnivOnto = onto.search(type = onto.Universite)
        nbUniv = randint(1,3)
        listUniv = []
        for j in list(range(nbUniv)):
            listUniv.append(listUnivOnto[randint(0,nbUnivOnto-1)])
        p.est_diplome = listUniv
        
        nbPatientOnto = len(onto.search(type = onto.Patient))
        listPatientOnto = onto.search(type = onto.Patient)
        nbpatients = randint(1,7)
        listPatient = []
        for j in list(range(nbpatients)):
            listPatient.append(listPatientOnto[randint(0,nbPatientOnto-1)])
        p.soigne = listPatient
        


        p.travaille = [hopital]
        
        
        nbServicesOnto = len(listServicesOnto)
        nbpatients = randint(1,1)
        listService = []
        if(typeMed!=0):
            for j in list(range(nbpatients)):
                listService.append(listServicesOnto[randint(0, nbServicesOnto-1)])
            p.est_affecte = listService

#for h in hopitaux.keys():
#    hopital = onto.Hopital(supprimerAccent(h).capitalize().replace(" ","_"))
#    hopital.nomHopital = h
#    hopital.est_situe = [onto.search(iri = ("*"+hopitaux[h]))[0]]
        
def storeVacinnation(onto):

    listVaccinsOnto = onto.search(type = onto.Vaccin)
    nbVaccinsOnto = len(listVaccinsOnto)
    
    listPersonneOnto = onto.search(type = onto.Personne)
    nbPersonneOnto = len(listPersonneOnto)
    
    for j in listVaccinsOnto:
        
        print(j)
        
        personne = listPersonneOnto[randint(1,nbPersonneOnto-1)]
        print(personne)
        tmp = personne.reçoit
        
        try:
           personne.reçoit = personne.reçoit.append(j)
        except Exception:
            pass
        
        
        listPersoMedOnto = onto.search(type=onto.PersonnelMedical)
        nbPersoMedOnto = len(listPersoMedOnto)
        persoMedVacc = listPersoMedOnto[randint(0,nbPersoMedOnto-1)]
        
        try:
            persoMedVacc.injecte = persoMedVacc.injecte.append(j)
        except Exception:
            pass
        
        print(persoMedVacc)
        print(" \n ")


def storeChambre(onto):
    for s in onto.search(type=onto.Service):
        cp = 0
        for i in list(range(5)):
            c = onto.Chambre("CH_"+str(cp)+"_"+str(s.name))
            c.appartient = [s]
            cp+=1
        



#p.has_topping = []
#storeVille(onto)
storeUniversite(onto)
storeVaccins(onto)
storeMaladie(onto)
storePatients(onto)
storeHopital(onto)
storeInfirmier(onto)
storeChambre(onto)
storeService(onto)
storeMedecin(onto)
storeVacinnation(onto)

onto.save(file = "SB2.owl", format = "rdfxml")

