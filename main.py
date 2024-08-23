import random
import time

# Author: Villaber, Christian Jude
# J2S

class GameManager:
    def __init__(self):
        self.pokemonsList = {
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
        self.totalWins = 0
        self.totalLoses = 0
        self.totalTies = 0
        self.playerPokemonList = []
        self.playerPowerList = []
        self.computerPokemonList = []
        self.computerPowerList = []
        self.gameStatusList = []

    def GetComputerPokemon(self):
        pokemoneList = list(self.pokemonsList.items())
        pokemonIndex = random.randrange(0, len(self.pokemonsList) - 1)
        computerPokemon = pokemoneList[pokemonIndex]
        return computerPokemon

    def GetPokemonList(self):
        return self.pokemonsList

    def GetFinalPower(self, basePower):
        randomNum = random.randrange(10, 20)
        finalPower = basePower + randomNum
        return finalPower, randomNum
    
    def ShowBattleScore(self, playerPower, computerPower):
        if playerPower == computerPower:
            print("====== Tie! ======")
            self.totalTies += 1
            return "Tie!"
        elif playerPower > computerPower:
            print("====== You Win! ======")
            self.totalWins +=1
            return "Win!"
        else:
            print("====== You Lose! ======")
            self.totalLoses += 1
            return "Lose!"

    # Records all information for battle summary
    def SetRecordStats(self, battleNumber, playerPokemon, playerPower, computerPokemon, computerPower, gameStatus):
        self.battleNumber = battleNumber
        self.playerPokemonList.append(playerPokemon)
        self.playerPowerList.append(playerPower)
        self.computerPokemonList.append(computerPokemon)
        self.computerPowerList.append(computerPower)
        self.gameStatusList.append(gameStatus)

    def ShowBattleStats(self):
        print("\n" + "-" * 40 + " Battle Summary " + "-" * 40 + "\n")
        
        # Show Totals of Wins, Loses and Ties
        print("{:<5}{:<20}{:<20}{:<0}".format(
            "",
            "Total Wins = " + str(self.totalWins),
            "Total Loses = " + str(self.totalLoses),
            "Total Ties = " + str(self.totalTies)
            ))
        print("")
        
        # Battle Summary Table Header
        print("{:<15}{:<16}{:<15}{:<18}{:<17}{:<0}".format(
            "Battle Number",
            "Player Pokemon",
            "Player Power",
            "Computer Pokemon",
            "Computer Power",
            "Status"
            ))
        
        # Battle Summary Table Contents
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
        
    def ValidatePokemonSelection(self, pokemonIndex):
        if pokemonIndex > len(self.pokemonsList) or pokemonIndex < 0:
            print("Number is Out of Range. Try Again \n")
            time.sleep(1)
            self.ClearConsole()                 
            return False
        else:
            return True
    
    def SetSelectPokemon(self, pokemonIndex):
        selectedPokemon = list(self.pokemonsList.items())[pokemonIndex - 1]
        return selectedPokemon   
    
    def ClearConsole(self):
        # Clear printed lines in console for cleaner
        # and readable texts
        print("\033c", end="")                       
        

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
                print("\n" + "-" * 15 + " Pokemon Battle " + "-" * 15 + "\n")
                
                pokemonsNameList = self.gameManager.GetPokemonList()

                # Table Header
                print("Select a Pokemon: \n")
                print("{:<8}{:<10}{:<10}".format(
                    " #",
                    "Name",
                    "Base Power"
                    ))
                
                # Shows a table of pokemons for selections
                count = 0
                for pokemon, basevalue in pokemonsNameList.items():
                    count += 1
                    print("{:<1}{:<5}{:<15}{:<0}".format(
                        "",
                        str(count),
                        pokemon,
                        str(basevalue)
                        ))

                pokemonIndex = int(input("\nEnter Pokemon Number: "))
                
                # Checks input index if the index is within the length range of the pokemonList
                # if True => Exit Loop and set target pokemon index to selectedPokemon
                # if False => Continue Loop
                if self.gameManager.ValidatePokemonSelection(pokemonIndex):
                    self.selectedPokemon = self.gameManager.SetSelectPokemon(pokemonIndex)
                    break
                    
            except ValueError:
                print("Invalid Input. Please Try Again \n")
                time.sleep(1)
                self.gameManager.ClearConsole()                                     
                continue
        
        self.gameManager.ClearConsole()      
        self.BattleSimulation()          
                
    def BattleSimulation(self):
        breakOuterLoop = False
        optionInput = ""
        
        while True:        
            self.computerPokemon = self.gameManager.GetComputerPokemon()
            playerBasePower = self.selectedPokemon[1]
            computerBasePower = self.computerPokemon[1]
            playerFinalPower, playerEnhancedPower = self.gameManager.GetFinalPower(playerBasePower)
            computerFinalPower, computerEnhancedPower = self.gameManager.GetFinalPower(computerBasePower)

            # Battle number(#) Information
            # Player Stats
            print("\n" + "-" * 40 + f" Battle {self.battleNumber} " + "-" * 40 + "\n")
            print("{:<31}{:<20}{:<25}{:<0}".format(
                "Your Pokemon: " + str(self.selectedPokemon[0]), 
                "Base Power: " + str(playerBasePower),
                "Enhanced Power: +" + str(playerEnhancedPower),
                "Final Power: " + str(playerFinalPower)))
            
            # Computer Stats
            print("{:<30}{:<20}{:<25}{:<0}".format(
                "Computer Pokemon: " + str(self.computerPokemon[0]), 
                " Base Power: " + str(computerBasePower),
                " Enhanced Power: +???",
                " Final Power: ???"))
            
            print("\nPress Enter to Start Battle \n")
            input("")
            print(f"Your Power: {playerFinalPower}  ComputerPower: {computerFinalPower}\n")

            gameStatus = self.gameManager.ShowBattleScore(playerFinalPower, computerFinalPower)
            self.gameManager.SetRecordStats(self.battleNumber, self.selectedPokemon[0] ,playerFinalPower, self.computerPokemon[0], computerFinalPower, gameStatus)

            self.battleNumber += 1
            
            # Option Selection after every battle
            while True:
                print("")
                print("1. Continue?")
                print("2. Select New Pokemon?")
                print("[X] Quit")

                optionInput = str(input("Enter Number or X to Quit: "))

                if optionInput == "1":
                    self.gameManager.ClearConsole()  
                    break
                elif optionInput == "2":
                    self.gameManager.ClearConsole()  
                    breakOuterLoop = True
                    break
                elif optionInput == "x" or optionInput == "X":
                    self.gameManager.ClearConsole()  
                    breakOuterLoop = True
                    break
                else:
                    print("Invalid Input. Try Again!\n")
                    time.sleep(1)
                    self.gameManager.ClearConsole()  
                    continue
            
            if optionInput == "2" and breakOuterLoop:
                self.CharacterSelection()               
                break           
            elif breakOuterLoop:
                breakOuterLoop = False
                self.gameManager.ShowBattleStats()
                break
    
if __name__ == "__main__":
    startGame = GamePlay()