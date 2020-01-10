# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 12:14:17 2020

@author: MORAD
"""

import requests
import json

#1- requete de l'api
requete = requests.get('https://demo.api-platform.com/books?order%5BpublicationDate%5D=desc')
#print(test.content()) voir le contenu
#2 - transformer en json
requete_json = json.loads(requete.content)


""" Lister les 10 derniers livres par leur date de publication"""
#3 Tri des 10 1er livre
ten_first_books = requete_json['hydra:member'][0:9]
#test:print(ten_first_books)
""" plus joli en présentation """
print(("LES 10 1er LIVRES SONT: ").center(50))
for book in ten_first_books:
    print("Le livre", book['title'].upper(), "a été publié le:", book['publicationDate'][0:10])
    





""" Lister le livre écrit par l’auteur « Dr. Kaitlyn Ratke »"""
requete_auteur = requests.get('https://demo.api-platform.com/books?order[publicationDate]=desc&author=Dr.%20Kaitlyn%20Ratke&page=1')
auteur = json.loads(requete_auteur.content)
auteur_book = auteur['hydra:member']
for y in auteur_book:
    print("Le livre écrit par Dr. Kaitlyn Ratke est: ", y['title'].upper())


""" Lister tous les commentaires du livre dont l’id est 
 « 1d52ba85-97c8-4cc3-b81a-40582f3aff64 »"""
 
requete_id = requests.get('https://demo.api-platform.com/books/1d52ba85-97c8-4cc3-b81a-40582f3aff64/reviews')
req_id = json.loads(requete_id.content)
asked_id = req_id['hydra:member']
for comment in asked_id:
    print(comment['body'])



""" Fonction qui va regarder tous les commentaires # ATTENTION C'EST QUE LA 1ere PAGE """
def liste_comm():
    requete_id = requests.get('https://demo.api-platform.com/books/1b08c9ab-6254-4015-ad14-bac3e5c008df/reviews')
    req_id = json.loads(requete_id.content)
    asked_id = req_id['hydra:member']
    for comment in asked_id:
        print("Les commentaires sont: ", comment['body'])
liste_comm()



""" Fonction qui va regarder tous les commentaires # QUE LA 1ERE  """
def list_all_comments(id='1d52ba85-97c8-4cc3-b81a-40582f3aff64'):
    requete = requests.get('https://demo.api-platform.com/books/1b08c9ab-6254-4015-ad14-bac3e5c008df/reviews')
    requete_content = requete.json()
    print(requete_content)
list_all_comments()

# Boucle sur les pages
url = 'https://demo.api-platform.com/books/1b08c9ab-6254-4015-ad14-bac3e5c008df/reviews?page='
p = 41
for i in range(p) :
    p = str(p)
    concat = url + p
    p = int(p)
    p -= 1
    print(concat)
    
    
    

"""Créer un nouveau commentaire avec le texte et la note de votre choix pour le livre
dont l’id est « 1b08c9ab-6254-4015-ad14-bac3e5c008df » """

new_post = {
     "author": "Morad5",
     "body": "test5",
     "rating": 2,
     "book":"books/1b08c9ab-6254-4015-ad14-bac3e5c008df"
     }
requests.post('https://demo.api-platform.com/reviews', json = new_post)


def post_comment():
    new_post = {
     "author": "Morad4",
     "body": "test3",
     "rating": 6,
     "book":"books/1b08c9ab-6254-4015-ad14-bac3e5c008df"
     }
    requests.post('https://demo.api-platform.com/reviews', json = new_post)
post_comment()




"""Modifier votre nouveau commentaire en utilisant l’id qui vous a été fourni 
lors de sa création"""

def edit_comment():
    edit_post = {
            "author": "Morad",
            "body": "Commentaire modifié"
    }

    headers_review = {'Content-Type':'application/merge-patch+json'}

    requests.patch('https://demo.api-platform.com/reviews/37ed3395-39ed-4a53-bdba-169a0c1a2f05', json=edit_post, headers=headers_review)
edit_comment()