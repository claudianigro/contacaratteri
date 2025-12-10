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



from ui.console import print_risultato
from data.services import (get_caratteri_len, get_text_len_no_space,get_words_number, get_phrase_number)
from data.repository import get_file_content

def main() -> None:
    try:
        content : str = get_file_content("text.txt") 
        print_risultato(get_caratteri_len(content), "caratteri")
        print_risultato(get_text_len_no_space(content), "caratteri senza spazi")
        print_risultato(get_words_number(content), "parole")
        print_risultato(get_phrase_number(content), "frasi")    
   

    except ValueError as e:
        print(f"{e}")

    except FileNotFoundError as e:
        print(f"{e}")

    except Exception as e:
        print(f"{e}")
#Si controllano prima le eccezioni più specifiche e poi quelle più generiche

    

if __name__ == "__main__":
    main()

