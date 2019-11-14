import argparse


def analyser_commande():
    parser = argparse.ArgumentParser(description="Jeu Quoridor - phase 1")
    parser.add_argument('idul', type=str, help='IDUL du joueur.')
    parser.add_argument('-l', '--lister', metavar='', help='Lister les identificatios de vos 20 dernières parties.')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    analyser_commande()


def afficher_damier_ascii(etat):

    dessus = f'Légende: 1=idul, 2=automate' + '\n'
    dessus += '   -----------------------------------' + '\n'
    dessous = '--|-----------------------------------' + '\n'
    dessous += '  | 1   2   3   4   5   6   7   8   9'

    damier_vide = []


    print(dessus + dessous)
