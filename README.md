# BJTK
Black Jack TKinter avec la contraite d'utiliser des objets, nous n'avons pas utilisé de dictionnaires car ces derniers sont impertinents face aux listes dans ce cas d'utilisation. Cependant ils sont toujours existants dans le dossier alpha.


### Problèmes connus
Même après avoir gagné ou perdu le joueur peut continuer de reprendre des czrtes ou laisser le casino en reprendre si il n'a pas encore dépassé 17 points.

Les images des cartes ne peuvent changer de taille nous avons donc prévu le dossier `_cards` pour les plus grosses résolutions et le `cards` utilisé par défaut pour alterner, changez le code en ajoutant le `_` manquant

La limite de 17 avant que le casino ne se couche peut être discutée, certains préfèrent 18 d'autres 19, nous avons préferré garder une limite facile à battre. 

Le bouton Mélanger ne devrait pas exister, lors d'une partie de blackjack on ne doit jamais mélanger les cartes, afin de permettre aux meilleurs joueurs de les deviner, par question d’authenticité nous avons permis de jouer ainsi, mais il nous a été demandé de faire une fonction mélanger_cartes et nous l'avons laissé.
