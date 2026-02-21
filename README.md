# 🛡️ PyPassword Generator (Lambda Edition)
Un generatore di password sicuro e veloce che sfrutta le potenzialità della programmazione funzionale in Python per creare stringhe alfanumeriche casuali.

🚀 Caratteristiche Tecniche
Questo script non è il solito generatore di password; utilizza un approccio più avanzato:

Lambda Functions: Utilizzo di funzioni anonime per rendere il codice più snello e leggibile.

Random Sampling: Invece di semplici cicli, usa random.sample per estrarre campioni unici di caratteri.

In-place Shuffling: Massima sicurezza rimescolando la lista finale con random.shuffle() prima della generazione della stringa.

Standard Library: Pieno utilizzo del modulo string per includere simboli, numeri e lettere senza doverli scrivere a mano.

🛠️ Come Funziona il Codice
Il cuore del programma è questa istruzione:

Python
formula = lambda x, y : random.sample(x, y)
Questa "formula" permette di estrarre esattamente il numero di caratteri richiesti dall'utente dalle tre liste principali (lettere, numeri, simboli). Successivamente, i risultati vengono concatenati e "shakerati" per evitare che la password segua uno schema prevedibile (es. prima solo lettere, poi solo numeri).

📦 Requisiti
Python 3.x

Nessuna libreria esterna richiesta (usa i moduli standard random e string).

🖥️ Esempio di Output
Plaintext
Welcome to the PyPassword Generator!
How many letters would you like in your password? 6
How many numbers would you like? 2
How many symbols would you like? 2

Your password is: 4&kLp9!sAz
