import argparse
import json


def analyser_commande():
    parser = argparse.ArgumentParser(description="Jeu Quoridor - phase 1")
    parser.add_argument('idul', type=str, help='IDUL du joueur.')
    parser.add_argument('-l', '--lister', metavar='', help='Lister les identificatios de vos 20 dernières parties.')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    analyser_commande()

def afficher_damier_ascii(etat):

    json.loads(etat)

    dessus = f'Légende: 1={etat["joueurs"][0]["nom"]}, 2=automate' + '\n'
    dessus += '   -----------------------------------' + '\n'
    dessous = '--|-----------------------------------' + '\n'
    dessous += '  | 1   2   3   4   5   6   7   8   9'

    damier_vide = []

    for i in range(18, 1, -1):

        damier_pair = list(f'{i//2} | .   .   .   .   .   .   .   .   . |')
        damier_impair = list('  |                                   |')
        
        if i%2 == 0:
            damier_vide.append(damier_pair) 
        else:
              damier_vide.append(damier_impair) 

    for i in range(2):
        damier_vide[18-2*etat["joueurs"][i]["pos"][1]][4*etat["joueurs"][i]["pos"][0]] = f'{i+1}'

    for i in range(len(etat["murs"]["horizontaux"])):
        for j in range(7):

            damier_vide[19-2*etat["murs"]["horizontaux"][i][1]][4*etat["murs"]["horizontaux"][i][0]+j-1] = '-'

    for i in range(len(etat["murs"]["verticaux"])):
        for j in range(3):
            damier_vide[18-2*etat["murs"]["horizontaux"][i][1]-j][4*etat["murs"]["horizontaux"][i][0]-2] = '|'


    bon_affichage = []

    for ligne in damier_vide:
        bon_affichage += ligne + ['\n']

        yeet = ''.join(bon_affichage)

    print(dessus + yeet + dessous)

afficher_damier_ascii(etat)

