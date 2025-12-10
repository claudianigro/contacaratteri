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


#============================================
# CONFIGURAZIONI E COSTANTI
#============================================
REGEX_TUTTI_CARATTERI = r'.'           # Tutti i caratteri (usare con re.DOTALL)
REGEX_SENZA_SPAZI = r'\S'              # Caratteri esclusi gli spazi
REGEX_SOLO_LETTERE = r'[a-zA-ZÀ-ÿ]'   # Solo lettere, incluse accentate
REGEX_PAROLE = r'\w+'                  # Parole (lettere, numeri, underscore)
REGEX_PAROLE_LETTERE = r'[a-zA-ZÀ-ÿ]+' # Parole composte solo da lettere
REGEX_FRASI = r'[^.!?]+[.!?]+'         # Frasi terminate da . ! ?

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

def get_caratteri_len(text: str) -> int:
    if not text:
        return 0
    return len(text)


import re
def get_text_len_no_space(text: str) -> int:
    if not text:
        return 0
    print(len(re.sub(REGEX_SENZA_SPAZI, "",  text)))

def get_words_number(text: str) -> int:
    if not text:
        return 0
    return len(re.findall(REGEX_PAROLE_LETTERE, text))


def main() -> None:
    try:
        content : str = get_file_content("text.txt") 
        print(get_caratteri_len(content))
        print(get_text_len_no_space(content))

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



