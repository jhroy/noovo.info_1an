# Noovo.info - 1 an déjà 🎂

<figure>
    <img src="https://media2.ledevoir.com/images_galerie/nwd_1175250_938688/image.jpg" alt="Le plateau du Fil de Noovo.info avec l'animatrice Noémi Mercier et le chroniqueur Yves Boisvert." width=500>
    <figcaption style="font-size:.5em;color:blue">Photo: François Perras (Noovo)</figcaption>
</figure>

---

Ce répertoire contient le code et des données ayant servi à une brève analyse réalisée pour *Le Devoir* et [publiée le 29 mars 2022](https://www.ledevoir.com/culture/medias/692412/noovo-info-l-information-vraiment-autrement-avec-noovo). Il s'agissait de vérifier la consultation des contenus vidéos de Noovo.info et d'autres médias du Québec et de la Francophonie dans **Facebook**, **Instagram** et **TikTok**, puis de les comparer avec des contenus vidéos d'information autres médias du Québec.

J'étudie depuis plusieurs années l'utilisation des réseaux socionumériques par les médias d'information et j'en ai sélectionné 19 qui ont le plus de *traction* sur ces réseaux en termes de nombre d'abonnées, d'interactions et ou de consultation, ou encore qui jouent un rôle national dans le paysage médiatique québécois:

## Facebook et Instagram

Les données pour Facebook et Instagram ont été puisées dans [CrowdTangle](https://www.crowdtangle.com/), une filiale de Meta Platforms, Inc. J'ai demandé d'extraire toutes les publications des pages Facebook et des comptes Instagram des 19 médias sélectionnés entre le 22 mars 2021 et le 22 mars 2022 inclusivement. Pour Facebook, en fait, la quantité de publications était telle que deux extractions ont été faites: du 22 mars au 22 septembre 2021, et du 23 septembre 2021 au 22 mars 2022.

### Facebook

Les 19 médias ont publié plus de 176&nbsp;000 *posts* durant la période examinée. En voici la répartition, par média et en fonction du type de publication (les appelations ci-dessous sont celles qui sont utilisées par Facebook).

| _**Média**_ | **Link** | **Live Video** | **Live Video Complete** | **Live Video Scheduled** | **Native Video** | **Photo** | **Status** | **Video** | **YouTube** | **Tous types** |
|------------|----:|----:|----:|----:|----:|----:|----:|----:|----:|----:|
| *24 heures* | 2&nbsp;162 | 0 | 0 | 0 | 161 | 32 | 0 | 0 | 0 | **2&nbsp;355** |
| *Journal Métro* | 5&nbsp;033 | 0 | 12 | 0 | 64 | 149 | 3 | 2 | 0 | **5&nbsp;263** |
| *La Presse* | 15&nbsp;975 | 0 | 3 | 5 | 16 | 34 | 0 | 0 | 0 | **16&nbsp;033** |
| *La Tribune*[^coops] | 8&nbsp;788 | 0 | 11 | 4 | 66 | 264 | 5 | 1 | 1 | **9&nbsp;140** |
| *La Voix de l'Est*[^coops] | 15&nbsp;832 | 0 | 2 | 1 | 82 | 102 | 8 | 0 | 0 | **16&nbsp;027** |
| *Le Devoir* | 8&nbsp;340 | 0 | 118 | 8 | 189 | 478 | 1 | 1 | 0 | **9&nbsp;135** |
| *Le Droit*[^coops] | 10&nbsp;893 | 0 | 13 | 2 | 49 | 228 | 11 | 0 | 0 | **11&nbsp;196** |
| *Le Journal de Montréal* | 13&nbsp;337 | 0 | 2 | 0 | 45 | 432 | 4 | 0 | 0 | **13&nbsp;820** |
| *Le Journal de Québec* | 13&nbsp;632 | 0 | 2 | 0 | 21 | 428 | 9 | 0 | 0 | **14&nbsp;092** |
| *Le Nouvelliste*[^coops] | 13&nbsp;724 | 0 | 1 | 0 | 96 | 258 | 18 | 6 | 1 | **14&nbsp;104** |
| *Le Quotidien*[^coops] | 8&nbsp;077 | 0 | 2 | 2 | 77 | 239 | 10 | 3 | 0 | **8&nbsp;410** |
| *Le Soleil*[^coops] | 11&nbsp;641 | 0 | 3 | 3 | 195 | 191 | 2 | 0 | 1 | **12&nbsp;036** |
| *MAJ* | 6 | 0 | 0 | 0 | 89 | 6 | 1 | 0 | 0 | **102** |
| *Noovo Info* | 1&nbsp;578 | 0 | 3 | 3 | 640 | 78 | 3 | 2 | 0 | **2&nbsp;307** |
| *RDS* | 8&nbsp;010 | 1 | 551 | 5 | 855 | 1&nbsp;101 | 11 | 0 | 0 | **10&nbsp;534** |
| *Rad* | 2 | 0 | 0 | 0 | 56 | 0 | 0 | 0 | 0 | **58** |
| *Radio-Canada Information* | 9&nbsp;209 | 0 | 234 | 3 | 1&nbsp;719 | 13 | 1 | 5 | 2 | **11&nbsp;186** |
| *TVA Nouvelles* | 12&nbsp;445 | 0 | 0 | 0 | 45 | 12 | 0 | 1 | 0 | **12&nbsp;503** |
| *URBANIA* | 1&nbsp;895 | 0 | 0 | 0 | 404 | 90 | 1 | 1 | 56 | **2&nbsp;447** |
| _**Tous médias**_ | *160&nbsp;639* | *1* | *1&nbsp;148* | *37* | *9&nbsp;771* | *4&nbsp;243* | *95* | *47* | *66* | _**176&nbsp;047**_ |

Seules les publications des types suivants ont été conservées: *`Live Video`*, *`Live Video Complete`*, *`Live Video Scheduled`*, *`Native Video`*, *`Video`* et *`YouTube`*. Elles regroupent tous les types de contenus vidéos qu'il est possible de diffuser dans Facebook.

Pour chacune de ces publications vidéo, trois différentes valeurs de vues étaient disponibles: *`Post Views`*, *`Total Views`* et *`Total Views For All Crossposts`*. Selon [la description que fait CrowdTangle de ses données](https://help.crowdtangle.com/en/articles/3213537-crowdtangle-codebook), la première mesure le nombre de vues d'une vidéo directement à partir du *post*. La deuxième (*Total Views*) inclut aussi le nombre de vues enregistrées lorsqu'une vidéo est partagée. La troisième inclut des vues enregistrées à l'extérieur du média lorsque celui-ci partage une vidéo qu'il n'a pas produite lui-même. **C'est la variable *`Total Views`* qui a été conservée**.

Il y a deux autres paramètres qui sont rattachés aux contenus vidéos:
* Le premier est appelé *`Video Share Status`*. Ce paramètre nous informe sur la provenance d'une vidéo publiée par une page. Il peut prendre quatre valeurs différentes: *`owned`*, *`share`*, *`crosspost`* ou être vide. **Seules les vidéos marquées *`owned`* ont été conservées**, car elles ont plus de chances d'avoir été réalisées par le média lui-même.
* Le deuxième est appelé *`Is video owner?`*. Ce paramètre nous dit si une vidéo mise en ligne par une page lui appartient ou pas. **Seules les vidéos marquées *`Yes`* ont été conservées**. Cette opération peut paraître redondante. Mais elle est quand même nécessaire, car étrangement, dans le jeu de données fourni par CrowdTangle, quatre vidéos dont le statut est *`owned`* indiquaient *`No`* au paramètre *`Is video owner?`*!

Le tableau ci-dessous donne les résultats pour tous les médias ayant mis en ligne 50 vidéos ou plus (environ un par semaine) correspondant aux critères ci-dessus.

| **_Média_** | **Nombre de vidéos<br>(_owned_ + _Yes_)** | **Vues totales** | **Vues/vidéo** |
|----------------------------|----------------:|-----------------:|---------------:|
| _Radio-Canada Information_ | 889 | 33&nbsp;041&nbsp;910 | **37&nbsp;167,5** |
| _Le Devoir_ | 301 | 10&nbsp;007&nbsp;449 | **33&nbsp;247,3** |
| _RDS_ | 808 | 26&nbsp;188&nbsp;215 | **32&nbsp;411,2** |
| _URBANIA_ | 194 | 6&nbsp;011&nbsp;950 | **30&nbsp;989,4** |
| _24 heures_ | 144 | 2&nbsp;438&nbsp;101 | **16&nbsp;931,3** |
| _Journal Métro_ | 58 | 627&nbsp;281 | **10&nbsp;815,2** |
| _Noovo Info_ | 609 | 5&nbsp;002&nbsp;130 | **8&nbsp;213,7** |
| _Coops de l'information_ | 416 | 3&nbsp;133&nbsp;078 | **7&nbsp;531,4** |

Vous pourrez reproduire toutes ces étapes à partir du fichier **[videosFB.csv](videosFB.csv)** qui contient les données brutes des 5&nbsp;946 *posts* vidéo mis en ligne par les 19 médias sur la période étudiée. Afin de respecter les [conditions d'utilisation de CrowdTangle](https://www.crowdtangle.com/terms/), certains champs textuels ont été retranchés.

### Instagram

Les données fournies par CrowdTangle pour les publications Instagram sont plus simples. Un *post* Instagram peut être de trois types différents:
* Album
* Photo
* Vidéo

Comme on ne s'intéresse qu'aux vidéos d'information, ce ne sont que les publications de ce troisième type qu'on a conservées. Il suffisait ensuite d'aller chercher le nombre total de vues pour ces vidéos. Le tableau ci-dessous nous donne, pour les médias de notre échantillon ayant mis en ligne plus de 50 vidéos au cours de l'année étudiée, les statistiques complètes de leurs publications dans Instagram. Les trois colonnes de droite concernent les vidéos que ces médias y ont diffusées.

| **_média_** | **Publications Instagram<br>(albmus+photos+vidéos)** | **Nombre d’albums** | **Nombre de photos** | **Nombre de vidéos** | **Vues (vidéos)** | **Vues/vidéo** |
|--------|---------:|------:|-------:|-------:|------:|-----:|
| _Rad_ | 435 | 382 | 1 | 52 | 1&nbsp;327&nbsp;303 | **25&nbsp;525,1** |
| _URBANIA_ | 343 | 103 | 63 | 177 | 2&nbsp;595&nbsp;228 | **14&nbsp;662,3** |
| _Le Devoir_ | 1&nbsp;729 | 697 | 935 | 97 | 1&nbsp;226&nbsp;261 | **12&nbsp;641,9** |
| _TVA Nouvelles_ | 158 | 17 | 9 | 132 | 1&nbsp;505&nbsp;795 | **11&nbsp;407,5** |
| _RDS_ | 1&nbsp;217 | 39 | 1&nbsp;013 | 165 | 1&nbsp;316&nbsp;152 | **7&nbsp;976,7** |
| _Radio-Canada Information_ | 1&nbsp;234 | 906 | 50 | 278 | 1&nbsp;756&nbsp;192 | **6&nbsp;&nbsp;317,2** |
| _MAJ_ | 181 | 68 | 31 | 82 | 380&nbsp;150 | **4&nbsp;636,0** |
| _24 heures_ | 522 | 339 | 51 | 132 | 184&nbsp;827 | **1&nbsp;400,2** |
| _Noovo Info_ | 557 | 106 | 37 | 414 | 316&nbsp;909 | **765,5** |
| _Coops de l'information_ | 993 | 404 | 505 | 84 | 11&nbsp;850 | **141,1** |

Le fichier **[videosIG.csv](videosIG.csv)** contient les donnéess brutes des quelque 9&nbsp;113 publications que les 19 médias sélectionnés ont mis en ligne au cours de la période couverte par cette analyse. Ici encore, afin de respecter les conditions d'utilisation de CrowdTangle, certains champs textuels ont été retranchés de ce fichier.

## TikTok

Cette plateforme a été ajoutée à cette analyse rapide parce que Noovo.info y diffuse des vidéos d'information. Seulement sept autres des 19 médias identifiés en font de même.

Ici, pour chaque média, le code HTML de la version web de son compte TikTok a été téléchargé le 22 mars 2022, vers 11h00:
* **[24h.html](24h.html)**
* **[devoir.html](devoir.html)**
* **[latribune.html](latribune.html)**
* **[maj.html](maj.html)**
* **[noovo.html](noovo.html)**
* **[rad.html](rad.html)**
* **[tva.html](tva.html)**
* **[urbania.html](urbania.html)**

Chaque page réunit toutes les vidéos TikTok diffusées jusqu'à maintenant par ces médias. Pour chaque vidéo, on a un décompte du nombre de vues dans le coin inférieur droit. Le script **[tiktok.py](tiktok.py)** fait la somme de ces vues et du nombre de vidéos pour chacun des huit médias diffusant sur TikTok. Le tableau ci-dessous vous présente le résultat du décompte effectué par ce script.

| **_Média_**   | **Nombre de vidéos** | **Nombre d’abonnés** | **Nombre de j’aime** | **Somme des vues** |  **Vues/vidéo** |
|------|-------:|-------:|-------:|-------:|----:|
| _MAJ_ | 15 | 10&nbsp;100 | 64&nbsp;600 | 809&nbsp;895 | **53&nbsp;993,0** |
| _24heures_ | 39 |  4&nbsp;218 | 50&nbsp;500 |   1&nbsp;396&nbsp;852 | **35&nbsp;816,7** |
| _Rad_ | 30 |  8&nbsp;113 | 43&nbsp;500 | 728&nbsp;403 | **24&nbsp;280,1** |
| _URBANIA_   | 62 |  4&nbsp;930 | 42&nbsp;300 |   1&nbsp;210&nbsp;622 | **19&nbsp;526,2** |
| _Noovo.info_  | 54 |  1&nbsp;915 | 17&nbsp;100 | 326&nbsp;443 |  **6&nbsp;045,2** |
| _TVA Nouvelles_ | 82 |  5&nbsp;801 | 27&nbsp;300 | 481&nbsp;957 |  **5&nbsp;877,5** |
| _Le Devoir_ | 16 |   660 |  2&nbsp;221 |  23&nbsp;582 |  **1&nbsp;473,9** |
| _La Tribune_ | 13 | 57 | 75 |   5&nbsp;754 |   **442,6** |

<hr>

[^coops]: Les données sur les six journaux des Coopératives de l'information ont été jumelées.
