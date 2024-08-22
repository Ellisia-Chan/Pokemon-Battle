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
    
    def ShowBattleScore(self, playerPower, computerPower):
        if playerPower == computerPower:
            print("====== Tie! ======")
            return "Tie!"
        elif playerPower > computerPower:
            print("====== You Win! ======")
            return "Win!"
        else:
            print("====== You Lose! ======")
            return "Lose!"

    def SetRecordStats(self, battleNumber, playerPokemon, playerPower, computerPokemon, computerPower, gameStatus):
        self.battleNumber = battleNumber
        self.playerPokemonList.append(playerPokemon)
        self.playerPowerList.append(playerPower)
        self.computerPokemonList.append(computerPokemon)
        self.computerPowerList.append(computerPower)
        self.gameStatusList.append(gameStatus)

    def ShowBattleStats(self):
        print("\n-------------------------------------- Battle Summary -------------------------------------------\n")
        print("{:<15}{:<16}{:<15}{:<18}{:<17}{:<0}".format(
            "Battle Number",
            "Player Pokemon",
            "Player Power",
            "Computer Pokemon",
            "Computer Power",
            "Status"
            ))
        
        for battleIndex in range(0, self.battleNumber):
            print("{:<5}{:<13}{:<18}{:<12}{:<21}{:<12}{:<0}".format(
                "",  
                str(battleIndex + 1),
                self.playerPokemonList[battleIndex], 
                str(self.playerPowerList[battleIndex]),
                self.computerPokemonList[battleIndex],
                str(self.computerPowerList[battleIndex]),
                self.gameStatusList[battleIndex]
                ))
            
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
                print("{:<8}{:<10}{:<10}".format(
                    "",
                    "Name",
                    "Base Power"
                    ))

                count = 0
                for pokemon, basevalue in pokemonsName.items():
                    count += 1
                    print("{:<1}{:<5}{:<15}{:<0}".format(
                        "",
                        str(count) + ". ",
                        pokemon,
                        str(basevalue)
                        ))

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

            gameStatus = self.gameManager.ShowBattleScore(playerPower, computerPower)
            self.gameManager.SetRecordStats(self.battleNumber, self.selectedPokemon[0] ,playerPower, self.computerPokemon[0], computerPower, gameStatus)

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
                self.gameManager.ShowBattleStats()
                break
            
if __name__ == "__main__":
    game = GamePlay()