import random

# ---------------- CLASSES ---------------- #
class Personagem:
    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe
        self.lv = 1
        self.exp = 0
        self.inventario = {"Poção": 2}
        self.cooldown_habilidade = 0

        # Atributos base por classe
        if classe == "Guerreiro":
            self.hp_max = 70
            self.hp = 70
            self.atk = 7
        elif classe == "Mago":
            self.hp_max = 50
            self.hp = 50
            self.atk = 5
        elif classe == "Arqueiro":
            self.hp_max = 60
            self.hp = 60
            self.atk = 6

    def atacar(self, alvo):
        crit_chance = 0.2 if self.classe == "Arqueiro" else 0.1
        if random.random() < crit_chance:
            dano = self.atk * 2
            print(f"⚡ CRÍTICO! {self.nome} causou {dano} de dano!")
        else:
            dano = self.atk
            print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano!")
        alvo.hp -= dano

    def habilidade_especial(self, alvo):
        if self.cooldown_habilidade > 0:
            print("Habilidade em recarga!")
            return

        if self.classe == "Guerreiro":
            dano = self.atk * 3
            print(f"🔥 {self.nome} usou Golpe Poderoso! Dano: {dano}")
            alvo.hp -= dano
        elif self.classe == "Mago":
            dano = self.atk * 2
            print(f"✨ {self.nome} lançou Bola de Fogo! Dano: {dano}")
            alvo.hp -= dano
            if random.random() < 0.3:
                print("🔥 O inimigo foi queimado e perdeu 5 HP extra!")
                alvo.hp -= 5
        elif self.classe == "Arqueiro":
            dano = self.atk * 2
            print(f"🏹 {self.nome} usou Tiro Preciso! Dano: {dano}")
            alvo.hp -= dano

        self.cooldown_habilidade = 3

    def usar_item(self):
        if self.inventario.get("Poção", 0) > 0:
            cura = 20
            self.hp = min(self.hp + cura, self.hp_max)
            self.inventario["Poção"] -= 1
            print(f"{self.nome} usou uma Poção e recuperou {cura} HP!")
        else:
            print("Sem poções disponíveis!")

    def ganhar_exp(self, quantidade):
        self.exp += quantidade
        print(f"{self.nome} ganhou {quantidade} XP!")
        if self.exp >= self.lv * 10:
            self.subir_nivel()

    def subir_nivel(self):
        self.lv += 1
        self.hp_max += 10
        self.hp = self.hp_max
        self.atk += 2
        print(f"🎉 {self.nome} subiu para o nível {self.lv}!")
        print(f"Novo HP: {self.hp_max}, Novo ATK: {self.atk}")

    def status(self):
        print(f"\n{self.nome} | Classe: {self.classe} | LV: {self.lv} | HP: {self.hp}/{self.hp_max} | ATK: {self.atk} | XP: {self.exp}")
        print(f"Inventário: {self.inventario}")

class Inimigo:
    def __init__(self, nome, nivel_base):
        self.nome = nome
        self.lv = random.randint(nivel_base, nivel_base + 3)
        self.atk = random.randint(3, 8)
        self.hp = 30 + (self.lv * 5)

    def atacar(self, alvo):
        if random.random() < 0.15:
            print(f"{alvo.nome} esquivou do ataque!")
            return
        dano = self.atk
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano!")
        alvo.hp -= dano

    def status(self):
        print(f"{self.nome} | LV: {self.lv} | HP: {self.hp} | ATK: {self.atk}")

# ---------------- LOOT ---------------- #
def gerar_loot(jogador):
    itens_possiveis = ["Poção", "Espada (+2 ATK)", "Armadura (+10 HP)"]
    chance = random.random()
    if chance < 0.5:
        item = random.choice(itens_possiveis)
        print(f"🎁 Você encontrou: {item}!")
        if item == "Poção":
            jogador.inventario["Poção"] = jogador.inventario.get("Poção", 0) + 1
        elif "Espada" in item:
            jogador.atk += 2
        elif "Armadura" in item:
            jogador.hp_max += 10
            jogador.hp = jogador.hp_max

# ---------------- BATALHA ---------------- #
def batalha(jogador, inimigo):
    print(f"\n⚔️ Um {inimigo.nome} apareceu!")
    while jogador.hp > 0 and inimigo.hp > 0:
        jogador.status()
        inimigo.status()
        print("\nEscolha sua ação:")
        print("1 - Atacar")
        print("2 - Habilidade Especial")
        print("3 - Usar Poção")
        escolha = input("> ")

        if escolha == "1":
            jogador.atacar(inimigo)
        elif escolha == "2":
            jogador.habilidade_especial(inimigo)
        elif escolha == "3":
            jogador.usar_item()
        else:
            print("Opção inválida!")

        if inimigo.hp <= 0:
            print(f"\n✅ Você derrotou {inimigo.nome}!")
            jogador.ganhar_exp(inimigo.lv * 5)
            gerar_loot(jogador)
            return True

        inimigo.atacar(jogador)
        if jogador.hp <= 0:
            print("\n❌ Você foi derrotado!")
            return False

        if jogador.cooldown_habilidade > 0:
            jogador.cooldown_habilidade -= 1

# ---------------- MENU ---------------- #
def menu():
    nome = input("Escolha o nome do seu personagem: ")
    print("Escolha sua classe:")
    print("1 - Guerreiro")
    print("2 - Mago")
    print("3 - Arqueiro")
    escolha_classe = input("> ")
    classe = "Guerreiro" if escolha_classe == "1" else "Mago" if escolha_classe == "2" else "Arqueiro"

    jogador = Personagem(nome, classe)

    while True:
        print("\n--- MENU ---")
        print("1 - Status")
        print("2 - Inventário")
        print("3 - Batalhar")
        print("4 - Sair")
        opcao = input("> ")

        if opcao == "1":
            jogador.status()
        elif opcao == "2":
            print(f"Inventário: {jogador.inventario}")
        elif opcao == "3":
            inimigo = Inimigo("Goblin", jogador.lv)
            resultado = batalha(jogador, inimigo)
            if not resultado:
                break
        elif opcao == "4":
            print("Saindo do jogo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()