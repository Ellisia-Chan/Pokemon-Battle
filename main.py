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
        
        self.battleNumber = 0
        self.playerPokemonList = []
        self.playerPowerList = []
        self.computerPokemonList = []
        self.computerPowerList = []
        self.gameStatusList = []

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
            print("====== Tie! ======")
            return "Tie!"
        elif playerPower > computerPower:
            print("====== You Win! ======")
            return "Win!"
        else:
            print("====== You Lose! ======")
            return "Lose!"

    def RecordStats(self, battleNumber, playerPokemon, playerPower, computerPokemon, computerPower, gameStatus):
        self.battleNumber = battleNumber
        self.playerPokemonList.append(playerPokemon)
        self.playerPowerList.append(playerPower)
        self.computerPokemonList.append(computerPokemon)
        self.computerPowerList.append(computerPower)
        self.gameStatusList.append(gameStatus)

    def ShowStats(self):
        print("\n------------------------------------------- Battle Summary -------------------------------------------\n")
        print(" " * 2 + "Battle Number" +
              " " * 4 + "Player Pokemon" +
              " " * 6 + "Player Power" +
              " " * 6 + "Computer Pokemon" +
              " " * 5 + "Computer Power" +
              " " * 7 + "Status")
        
        for battleIndex in range(0, self.battleNumber):
            print(" " * 8 + f"{battleIndex + 1}" +
                  " " * 14 + f"{self.playerPokemonList[battleIndex]}" + 
                  " " * 14 + f"{self.playerPowerList[battleIndex]}" +
                  " " * 14 + f"{self.computerPokemonList[battleIndex]}" +
                  " " * 16 + f"{self.computerPowerList[battleIndex]}" +
                  " " * 15 + f"{self.gameStatusList[battleIndex]}")
        print("")

class GamePlay:
    def __init__(self):
        self.gameManager = GameManager()
        self.selectedPokemon = []
        self.computerPokemon = []
        self.battleNumber = 1


        self.CharacterSelection()

    def CharacterSelection(self):
        while True:
            try:
                print("\n--------------- Pokemon Battle ---------------\n")
                
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
                

    def BattleSimulation(self):
        breakOuterLoop = False
        optionInput = ""
        
        while True:        
            self.computerPokemon = self.gameManager.GetComputerPokemon()
            playerPower = self.gameManager.GetFinalPower(self.selectedPokemon[1])
            computerPower = self.gameManager.GetFinalPower(self.computerPokemon[1])

            print(f"\n--------------- Battle {self.battleNumber} ---------------")
            print("Your Pokemon: " + str(self.selectedPokemon[0]) + "  Power: " + str(playerPower))
            print("Computer Pokemon: " + str(self.computerPokemon[0]) + "  Power: ???")
            print("\nPress Enter to Start Battle \n")
            input("")
            print(f"Your Power: {playerPower}  ComputerPower: {computerPower}\n")

            gameStatus = self.gameManager.FinalScore(playerPower, computerPower)
            self.gameManager.RecordStats(self.battleNumber, self.selectedPokemon[0] ,playerPower, self.computerPokemon[0], computerPower, gameStatus)

            self.battleNumber += 1
            

            while True:
                print("")
                print("1. Continue?")
                print("2. Select New Pokemon?")
                print("[X] Quit")

                optionInput = str(input("Enter Number or X to Quit: "))

                if optionInput == "1":
                    break
                elif optionInput == "2":
                    breakOuterLoop = True
                    break
                elif optionInput == "x" or optionInput == "X":
                    breakOuterLoop = True
                    break
                else:
                    print("Invalid Input. Try Again!\n")
                    time.sleep(1)
                    continue
            
            if optionInput == "2" and breakOuterLoop:
                self.CharacterSelection()               
                break           
            elif breakOuterLoop:
                breakOuterLoop = False
                self.gameManager.ShowStats()
                break
            
if __name__ == "__main__":
    game = GamePlay()