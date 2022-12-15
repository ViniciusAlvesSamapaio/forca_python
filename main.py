import random

print("****************** JOGO DA FORCA********************")
print("")
forc = ['''

+----+
|    |
     |
     |
     |
     |
===========  
''',
        '''
+----+
|    |
O    |
     |
     |
     |
===========         
''',
        '''

+----+
|    |
O    |
|    |
     |
     |
===========  
''',
        '''
 +----+
 |    |
 O    |
/|    |
      |
      |
 ===========         
''',
        '''
 +----+
 |    |
 O    |
/|\   |
      |
      |
 ===========         
''',
        '''
 +----+
 |    |
 O    |
/|\   |
/     |
      |
 ===========         
''',
        '''
 +----+
 |    |
 O    |
/|\   |
/ \   |
      |
 ===========         
'''
        ]


class forca:

    def __init__(self, palavra):
        self.palavra = palavra
        self.errada = []
        self.certa = []

    def guess(self, letra):
        if letra in self.palavra and letra not in self.certa:
            self.certa.append(letra)
        elif letra not in self.palavra and letra not in self.errada:
            self.errada.append(letra)
        else:
            return False
        return True

    def forca_final(self):
        return self.forca_vence() or (len(self.errada) == 6)

    def forca_vence(self):
        if '_' not in self.esconder_palavra():
            return True
        return False

    def esconder_palavra(self):
        r = ""
        for letra in self.palavra:
            if letra not in self.certa:
                r += "_"
            else:
                r += letra
        return r

    def status_jogo(self):
        print(forc[len(self.errada)])
        print('\nPalavra', self.esconder_palavra())
        print('\nLetras erradas:', )
        for letra in self.errada:
            print(letra)
        print("")
        print('\nLetras certas:', )
        for letra in self.certa:
            print(letra)


def rand_palavra():
    with open("palavras.txt", "rt") as f:
            bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


def main():

    game = forca(rand_palavra())

    while not game.forca_final():
        game.status_jogo()
        joga = input("\n digite uma letra\n")
        game.guess(joga)

    game.status_jogo()

    if game.forca_vence():

        print("vc venceu, parabens")
    else:
        print("")
        print('vc perdeu')


if __name__ == "__main__":
    main()
