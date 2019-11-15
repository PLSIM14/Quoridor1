import requests


def lister_parties(idul):

    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'
    rep = requests.get(url_base+'lister/', params={'idul': idul})
    if rep.status_code == 200:
    
        rep = rep.json()
        print(rep)
    
    else:
        print(f"Le GET sur {url_base+'lister'} a produit le code d'erreur {rep.status_code}.")
        raise RuntimeError(str(idul))

def débuter_partie(idul):
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'
    rep = requests.post(url_base+'débuter/', data={'idul': idul})
    rep.json()


def jouer_coup(id_partie, type_coup, position):
    raise RuntimeError('')

