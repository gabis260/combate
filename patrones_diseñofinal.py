# interfaces
class Estrategia_ataque:
    def ataque(self):
        pass

class Estategia_salud:
    def salud(self):
        pass

#estrategias
class Cuerpo_a_cuerpo(Estrategia_ataque):
    def ataque(self):
        print("Realizando ataque cuerpo a cuerpo")

class Ataque_distancia(Estrategia_ataque):
    def ataque(self):
        print("Realizando ataque a distancia")

class Amague(Estrategia_ataque):
    def ataque(self):
        print("esta realizando un amague")

class Baja_salud(Estategia_salud):
    def salud(self):
        return "Baja"

class Media_salud(Estategia_salud):
    def salud(self):
        return "Media"

class Alta_salud(Estategia_salud):
    def salud(self):
        return "Alta"

# Context
class Unit:
    def __init__(self, name, ataque_estrategia:Estrategia_ataque,salud_estrategia,salud=100):
        self.name = name
        self.ataque_estrategia = ataque_estrategia
        self.salud_estrategia = salud_estrategia
        self.salud = salud

    def set_ataque_estrategia(self, ataque_estrategia):
        self.ataque_estrategia = ataque_estrategia

    def set_salud_estrategia(self, salud_estrategia):
        self.salud_estrategia = salud_estrategia

    def ataque(self):
        print(f"{self.name}: ", end="")
        self.ataque_estrategia.ataque()

    def salud_status(self):
        return self.salud_estrategia.salud()

    def take_damage(self, damage):
        self.salud -= damage
        if self.salud <= 0:
            self.die()

    def die(self):
        print(f"{self.name} ha muerto")

# Usage
if __name__ == "__main__":
   
    soldier = Unit("Soldado", Cuerpo_a_cuerpo(), Alta_salud())
    arquero = Unit("Arquero", Ataque_distancia(), Baja_salud())
    caballero = Unit("Caballero", Cuerpo_a_cuerpo(), Alta_salud())
    capitan=Unit("Capitan",Cuerpo_a_cuerpo(),Alta_salud())



    # Realizar ataques
    soldier.ataque()
    arquero.ataque()
    caballero.ataque()
    capitan.ataque()

    # Mostrar estado de Estategia_salud
    print(f"Estado de Estategia_salud de {soldier.name} es: {soldier.salud_status()}")
    print(f"Estado de Estategia_salud de  {arquero.name} es:   {arquero.salud_status()}")
    print(f"Estado de Estategia_salud de {caballero.name} es: {caballero.salud_status()}")
    print(f"Estado de Estategia_salud de {capitan.name} es: {capitan.salud_status()} ")

    #daño y muerte
    soldier.take_damage(80)  
    arquero.take_damage(30)
    caballero.take_damage(120)  
    capitan.take_damage(50)
