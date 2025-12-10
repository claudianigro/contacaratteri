"""
- dove si trova il testo?
    viene preso da un file
    i file vengono mostrati a video dal terminale
- voglio contare i caratteri di un testo
    con spazi e senza spazi
    le parole
    le frasi
    i paragrafi
    tempo di lettura
    ripetizioni della parola e della lettera

"""

# ================================================
# Repository
#===============================================

from typing import TextIO

def get_file_content(file_path: str) -> str:
    if not file_path:
        raise ValueError("Il file path non può essere vuoto")
    
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError("Il file non è stato trovato")

"Si controllano due eccezioni: file vuoto e file non trovato, entrambe figlie delle eccezioni Exception"

#======================
# Services 
#===============================================

def stampa_testo_input(text: TextIO) -> None:
    with text as f:
        content = f.read()
        print(content)


import re
def get_text_len_no_space(text: str) -> int:
    print(len(re.sub(r"\s+", "",  text)))


def main() -> None:
    try:
        content : str = get_file_content("text.txt") 
        print(content)

    except ValueError as e:
        print(f"{e}")

    except FileNotFoundError as e:
        print(f"{e}")

    except Exception as e:
        print(f"{e}")
#Si controllano prima le eccezioni più specifiche e poi quelle più generiche
    finally:
        print("fine try catch")
    

main()



