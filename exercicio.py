#Crie um dicionário para armazenar informações de um livro, 
#incluindo título, autor e ano de publicação. Imprima cada informação.

from typing import Dict, Any

livro: Dict[str, any] = {
    "titulo": "game of thrones",
    "autor" : "Igor",
    "ano": 2025 
}

lista_de_elementos: list = livro.items()
for elemento in lista_de_elementos:
    print(elemento)