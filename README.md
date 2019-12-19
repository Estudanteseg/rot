# rot

Baseado no site rot13.com decidi criar um programa que realiza a criptografia ou decriptografia de uma frase. Com isso ao 

realizar um CTF poderei ter agilidade para decifrar algum texto baseado em posição do alfabeto.


# A seguir exemplos de como criptografar um texto 

# Aplicando CRIPTOGRAFIA ROT13 na frase "O rato roeu a roupa do rei de Roma."

estudante:~/Documents/estudo/py/crypt$ ./rot.py -i -p 13 -v "O rato roeu a roupa do rei de Roma."

******************************************************************

* O resultado é: B engb ebrh n ebhcn qb erv qr Ebzn.

******************************************************************


# Aplicando DECRIPTOGRAFIA ROT13 na frase "Cnenoraf ibpr qrpvsebh n fraun [Cnffjbeq1]."


estudante:~/Documents/estudo/py/crypt$ ./rot.py -d -p 13 -v "Cnenoraf ibpr qrpvsebh n fraun [Cnffjbeq1]."

******************************************************************

* O resultado é: Parabens voce decifrou a senha [Password1].

******************************************************************


