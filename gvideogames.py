class usuario:
    def __init__(self, nombre): 
        self.nombre = nombre
        self.__biblioteca = []

    def agregar_juego(self, juego):
        self.__biblioteca.append(juego)
        print(f"El juego {juego.titulo} fue agregado con éxito")
    
    def jugar(self, titulo_buscado, tiempo):

        encontrado = False
        for juego in self.__biblioteca:
            if juego.titulo == titulo_buscado:
                juego.horas_jugadas += tiempo 
                print(f"{self.nombre} ha jugado {tiempo} horas al juego {juego.titulo}")
                encontrado = True
                break
        
        if not encontrado:
            print(f"'{titulo_buscado}' no se ha encontrado en la biblioteca de Steam. compralo careverga")

    def top_3_mas_jugados(self):
        lista_ordenada = sorted(self.__biblioteca, key=lambda juego: juego.horas_jugadas, reverse=True)

        print("--- TOP 3 ---")

        for juego in lista_ordenada[:3]:
            print(f"{juego.titulo}: {juego.horas_jugadas} horas")



class videojuego:
     def __init__(self, titulo, genero, horas_jugadas):
         self.titulo = titulo
         self.genero = genero
         self.horas_jugadas = horas_jugadas

mi_usuario = usuario("Jose")
mi_juego1 = videojuego("Valorant", "Shooter", 500)
mi_juego2 = videojuego("Minecraft", "Mundo abierto", 1000)       
mi_juego3 = videojuego("Roblox", "Multisexo", 200)

mi_usuario.agregar_juego(mi_juego1)
mi_usuario.agregar_juego(mi_juego2)
mi_usuario.agregar_juego(mi_juego3)

mi_usuario.jugar("Valorant", 200)
mi_usuario.jugar("Minecraft", 100)
mi_usuario.jugar("Roblox", 300)

mi_usuario.top_3_mas_jugados()