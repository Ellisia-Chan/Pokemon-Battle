import random
import time

class GameManager:
    def __init__(self):
        self.pokemons = {
            "Pikachu": 50,
            "Charmander": 55,
            "Bulbasaur": 60,
            "Squirtle": 58,
            "Jigglypuff": 45,
            "Eevee": 52,
            "Snorlax": 80,
            "Gengar": 70,
            "Machamp": 75,
            "Mewtwo": 90
        }

    def GetComputerPokemon(self):
        pokemoneList = list(self.pokemons.items())
        pokemonIndex = random.randrange(0, len(self.pokemons) - 1)
        computerPokemon = pokemoneList[pokemonIndex]
        return computerPokemon

    def GetPokemons(self):
        return self.pokemons

    def GetFinalPower(self, basePower):
        randomNum = random.randrange(10, 20)
        finalPower = basePower + randomNum
        return finalPower
    
    def FinalScore(self, playerPower, computerPower):
        if playerPower == computerPower:
            print("----- Tie! -----")
        elif playerPower > computerPower:
            print("----- You Win! -----")
        else:
            print("----- You Lose! -----")

    def RecordStats(self, ):
        pass

class GamePlay:
    def __init__(self):
        self.gameManager = GameManager()
        self.selectedPokemon = []
        self.computerPokemon = []
        self.battle = 1


        self.CharacterSelection()

    def CharacterSelection(self):
        while True:
            try:
                print("------ Pokemon Battle ------\n")
                
                pokemonsName = self.gameManager.GetPokemons()

                print("Select a Pokemon: \n")
                print(f" " * 8 + "Name" + " " * 5 + "Base Power")

                count = 0
                for pokemon, basevalue in pokemonsName.items():
                    count += 1
                    print(f" " * 3 + str(count) + ". " + pokemon + " " * 8 + str(basevalue))

                pokemonIndex = int(input("\nEnter Pokemon Number: "))

                if pokemonIndex > len(pokemonsName) or pokemonIndex < 0:
                    print("Number is Out of Range. Try Again \n")
                    time.sleep(1)
                    continue
                else:
                    pokemonList = list(pokemonsName.items())
                    self.selectedPokemon = pokemonList[pokemonIndex -1]
                    break
            except ValueError:
                print("Invalid Input. Please Try Again \n")
                time.sleep(1)
                continue
        self.BattleSimulation()          
                

    def  BattleSimulation(self):
        breakOuterLoop = False

        while True:        
            self.computerPokemon = self.gameManager.GetComputerPokemon()
            playerPower = self.gameManager.GetFinalPower(self.selectedPokemon[1])
            computerPower = self.gameManager.GetFinalPower(self.computerPokemon[1])

            print(f"\n-------- Battle {self.battle} --------")
            print("Your Pokemon: " + str(self.selectedPokemon[0]) + "  Power: " + str(playerPower))
            print("Computer Pokemon: " + str(self.computerPokemon[0]) + "  Power: ???")
            print("\nPress Enter to Start Battle \n")
            input("")
            print(f"Your Power: {playerPower}  ComputerPower: {computerPower}")

            self.gameManager.FinalScore(playerPower, computerPower)

            self.battle += 1

            while True:
                print("")
                print("1. Continue?")
                print("2. Select New Pokemon?")
                print("[X] Quit")

                optionInput = str(input("Enter Number or X to Quit: "))

                if optionInput == "1":
                    break
                elif optionInput == "2":
                    self.CharacterSelection()
                    breakOuterLoop = True
                    break
                elif optionInput == "x" or optionInput == "X":
                    breakOuterLoop = True
                    break
                else:
                    print("Invalid Input. Try Again!\n")
                    time.sleep(1)
                    continue

            if breakOuterLoop:
                breakOuterLoop = False
                break

        


        

if __name__ == "__main__":
    game = GamePlay()