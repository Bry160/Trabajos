import re

class AnalyzeData:

    def __init__(self, filename, word):
        self.__filename = filename
        self.__word = word

    def getFilename(self):
        return self.__filename

    def getWord(self):
        return self.__word

    def processData(self):
        try:
            with open(self.getFilename(), 'r') as file:
                lines = file.readlines()
                total_palabras = 0

                for line in lines:
                    res = re.split(r"\s+", line.strip())
                    for palabra in res:
                        if palabra == self.getWord():
                            total_palabras += 1

                print(f'La palabra "{self.getWord()}" se encontró {total_palabras} veces')

        except FileNotFoundError:
            print(f'El archivo {self.getFilename()} no se encuentra.')
        except Exception as e:
            print(f'Ocurrió un error: {e}')



ad = AnalyzeData('data.txt', 'leche')
ad.processData()
