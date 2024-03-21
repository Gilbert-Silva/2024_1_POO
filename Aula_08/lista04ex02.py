class PlayList:
    def __init__(self, nome, desc):
        self.__nome = nome
        self.__descricao = desc
        self.__musicas = []
    def set_nome(self, nome):
        self.__nome = nome
    def set_descricao(self, descricao):
        self.__descricao = descricao
    def get_nome(self):
        return self.__nome
    def get_descricao(self):
        return self.__descricao
    def inserir(self, m):
        self.__musicas.append(m)
    def listar(self):
        return self.__musicas
    def __str__(self):
        return f"PlayList {self.__nome} possui {len(self.__musicas)} música(a)"    

class Musica:
    def __init__(self, titulo, artista, album):
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album
    def set_titulo(self, titulo):
        self.__titulo = titulo
    def set_artista(self, artista):
        self.__artista = artista
    def set_album(self, album):
        self.__album = album
    def get_titulo(self):
        return self.__titulo
    def get_artista(self):
        return self.__artista
    def get_album(self):
        return self.__album
    def __str__(self):
        return f"Música: {self.__titulo} do álbum {self.__album} - {self.__artista}"

class UI:
    def main():
      play = None
      op = 0
      while op != 9:
          op = UI.menu()
          if op == 1: 
              play = UI.nova_playlist()
          if op == 2: 
              if play == None: 
                  print("Crie uma nova playlist antes!")
              else:
                  musica = UI.nova_musica()
                  play.inserir(musica)
          if op == 3: 
              if play == None: 
                  print("Crie uma nova playlist antes!")
              else:
                  for musica in play.listar():
                      print(musica)     
    
    def nova_playlist():
      nome = input("Informe o nome da playlist: ")
      desc = input("Informe uma descrição: ")
      playlist = PlayList(nome, desc)
      return playlist
    
    def nova_musica():
      titulo = input("Informe o título da música: ")
      artista = input("Informe o artista ou banda: ")
      album = input("Informe o álbum: ")
      musica = Musica(titulo, artista, album)
      return musica

    def menu():
        print("1 - Nova PlayList")
        print("2 - Inserir música")
        print("3 - Listar músicas")
        print("9 - fim")
        return int(input("Opção: "))

UI.main()

"""
a = Musica("Easy", "Ivete Sangalo", "Ao Vivo")
b = Musica("Transilvania", "Iron Maiden", "Iron Maiden")
print(a)
print(b)
"""

        


