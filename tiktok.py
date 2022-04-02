# coding: utf-8
# ©2022 Jean-Hugues Roy. GNU GPL v3.

### IMPORTATION DE LA BIBLIOTHÈQUE DE PARSING HTML BEAUTIFULSOUP
from bs4 import BeautifulSoup

### CRÉATION D'UNE VARIABLE CONTENANT LE NOM DE NOS 8 FICHIERS HTML
html = ["24h.html",
	"devoir.html",
	"latribune.html",
	"maj.html",
	"noovo.html",
	"rad.html",
	"tva.html",
	"urbania.html"]

### BOUCLE POUR TRAITER CHACUN DES FICHIERS HTML
for h in html:
	page = BeautifulSoup(open(h), "html.parser")

	### ON VA CHERCHER LES 3 ÉLÉMENTS D'INFO GÉNÉRALE CONTENUS EN HAUT DE PAGE (ABONNEMENTS, ABONNÉS ET J'AIME)
	infos = page.find_all("div", class_="tiktok-xeexlu-DivNumber")

	### ON NE RECUEILLE QUE LE NB D'ABONNÉS ET DE J'AIME DE CHAQUE COMPTE
	for info in infos:
		# print(d.text)
		if "Abonnés" in info.text:
			abonnes = info.text.replace("Abonnés","").strip()
		elif "J'aime" in info.text:
			jaime = info.text.replace("J'aime","").strip()

	### ON REGROUPE MAINTENANT TOUTES LES VIDÉOS
	vidz = page.find_all("div", class_="tiktok-x6y88p-DivItemContainerV2")

	### ON INITIALISE À ZÉRO UNE VARIABLE QUI VA ADDITIONNER LE NB DE VUES DE TOUTES LES VIDÉOS
	vues = 0

	### CETTE BOUCLE TRAITE CHAQUE VIDÉO UNE À LA FOIS
	for v in vidz:

		### ON VA CHERCHER LE NOMBRE DE VUES
		nb = v.find("strong", class_="video-count").text
		# print(nb)

		### SI CE NOMBRE CONTIENT UN «K» (POUR MILLIER),
		### CE CODE TRADUIT CETTE EXPRESSION EN UN NOMBRE QU'ON PEUT ENSUITE ADDITIONNER À L'ENSEMBLE
		if "K" in nb:
			elem = nb.replace("K","").split(".")
			if len(elem) == 2:
				vue = int(elem[0])*1000 + int(elem[1])*100
			else:
				vue = int(elem[0])*1000

		### SI CE NOMBRE CONTIENT UN «M» (POUR MILLION),
		### CE CODE TRADUIT CETTE EXPRESSION EN UN NOMBRE QU'ON PEUT ENSUITE ADDITIONNER À L'ENSEMBLE
		elif "M" in nb:
			elem = nb.replace("M","").split(".")
			if len(elem) == 2:
				vue = int(elem[0])*1000000 + int(elem[1])*100000
			else:
				vue = int(elem[0])*1000000
		
		### SI CE NOMBRE NE CONTIENT NI «K», NI «M», ON SE CONTENTE DE LE TRANSFORMER EN NOMBRE ENTIER
		else:
			vue = int(nb)

		### ON ADDITIONNE LE NB DE VUES DE CHAQUE VIDÉO À L'ENSEMBLE
		vues += vue

	### AU FINAL, LE SCRIPT IMPRIME:
	### >>> LE NOM DU MÉDIA
	### >>> LE NOMBRE DE VIDÉO TIKTOK QU'IL A MISES EN LIGNE
	### >>> LE NOMBRE DE SES ABONNÉS
	### >>> LE NOMBRE DE J'AIME QU'IL A RECUEILLIS AU 22 MARS 22
	### >>> LE NOMBRE DE VUES RÉCOLTÉES PAR SES VIDÉOS AU 22 MARS 22
	print(h,len(vidz), abonnes, jaime, vues)

	print(".....")
