import argparse


def analyser_commande():
    parser = argparse.ArgumentParser(description="Jeu Quoridor - phase 1")
    parser.add_argument('idul', type=str, help='IDUL du joueur.')
    parser.add_argument('-l', '--lister', metavar='', help='Lister les identificatios de vos 20 dernières parties.')
    args = parser.parse_args()
    return args


print(analyser_commande())

if __name__ == '__main__':
    analyser_commande()