import random
import time

# Author: Villaber, Christian Jude
# J2S

class GameManager:
    def __init__(self):
        self.pokemonsDict = {
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
        
        self.battleNumber: int = 0
        self.totalWins: int = 0
        self.totalLoses: int = 0
        self.totalTies: int = 0
        self.playerPokemonList: list = []
        self.playerPowerList: list = []
        self.computerPokemonList: list = []
        self.computerPowerList: list = []
        self.gameStatusList: list = []
  
    def ShowBattleScore(self, playerPower: int, computerPower: int) -> str:
        if playerPower == computerPower:
            print(" " * 22 + "|==================|")
            print(" " * 22 + "|       Tie!       |")
            print(" " * 22 + "|==================|\n")
            self.totalTies += 1
            return "Tie!"
        elif playerPower > computerPower:
            print(" " * 22 + "|==================|")
            print(" " * 22 + "|     You Win!     |")
            print(" " * 22 + "|==================|\n")
            self.totalWins +=1
            return "Win!"
        else:
            print(" " * 22 + "|==================|")
            print(" " * 22 + "|    You Lose!     |")
            print(" " * 22 + "|==================|\n")
            self.totalLoses += 1
            return "Lose!"

    def ShowBattleStartInformation(self, battleNumber: int, selectedPokemon: list, computerPokemon: list, playerBasePower: int, computerBasePower: int, playerEnhancedPower: int, playerFinalPower: int):
    # Battle number(#) Information
        # Player Stats
        print("\n" + "-" * 40 + f" Battle {battleNumber} " + "-" * 40 + "\n")
        print("{:<31}{:<20}{:<25}{:<0}".format(
            "Your Pokemon: " + str(selectedPokemon[0]), 
            "Base Power: " + str(playerBasePower),
            "Enhanced Power: +" + str(playerEnhancedPower),
            "Final Power: " + str(playerFinalPower)))
        
        # Computer Stats
        print("{:<30}{:<20}{:<25}{:<0}".format(
            "Computer Pokemon: " + str(computerPokemon[0]), 
            " Base Power: " + str(computerBasePower),
            " Enhanced Power: +???",
            " Final Power: ???"))
        
        print("\nPress Enter to Start Battle \n")
        input("")
        return
    
    def ShowBattleResultInformation(self, playerSelectedPokemon: list, computerPokemon: list, playerBasePower: int, computerBasePower: int, playerEnhancedPower: int, computerEnhancedPower: int, playerFinalPower: int, computerFinalPower: int):
        # Battle number(#) Result Stats Table
            print("{:<5}{:<30}{:<0}".format(
                "",
                "Your Pokemon: " + str(playerSelectedPokemon[0]),
                "Computer Pokemon: " + str(computerPokemon[0])))
            
            print("{:<5}{:<30}{:<0}".format(
                "",
                "Base Power: " + str(playerBasePower),
                "Base Power: " + str(computerBasePower)))
            
            print("{:<5}{:<30}{:<0}".format(
                "",
                "Enhanced Power: +" + str(playerEnhancedPower),
                "Enhanced Power: +" + str(computerEnhancedPower)))
            
            print("{:<5}{:<30}{:<0}".format(
                "",
                "Final Power: " + str(playerFinalPower),
                "Final Power: " + str(computerFinalPower)))
    
    def ShowBattleSummary(self):
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
           
    def ValidatePokemonSelection(self, pokemonIndex: int) -> bool:
        if pokemonIndex > len(self.pokemonsDict) or pokemonIndex < 0:
            print("Number is Out of Range. Try Again \n")
            time.sleep(1)
            self.ClearConsole()                 
            return False
        else:
            return True
    
    # Records all information for battle summary
    def SetRecordStats(self, battleNumber: int, playerPokemon: str, playerPower: int, computerPokemon: str, computerPower: int, gameStatus: str):
        self.battleNumber = battleNumber
        self.playerPokemonList.append(playerPokemon)
        self.playerPowerList.append(playerPower)
        self.computerPokemonList.append(computerPokemon)
        self.computerPowerList.append(computerPower)
        self.gameStatusList.append(gameStatus)
  
    def SetSelectPokemon(self, pokemonIndex: int) -> list:
        selectedPokemon = list(self.pokemonsDict.items())[pokemonIndex - 1]
        return selectedPokemon 
    
    def GetComputerPokemon(self) -> list:
        return random.choice(list(self.pokemonsDict.items()))

    def GetPokemonList(self):
        return self.pokemonsDict

    def GetFinalPower(self, basePower: int) -> int:
        randomNum = 50
        randomRange = random.randrange(0, randomNum)      
        finalPower = basePower + randomRange
        return finalPower, randomRange

    def GetPowerDecay(self, basePower: int) -> int:
        return (
            basePower - 800000 if basePower > 1000000 else
            basePower - 10500 if basePower > 20000 else
            basePower - 8000 if basePower > 10000 else
            basePower - 4500  if basePower > 5000  else
            basePower - 1500  if basePower > 2000  else
            basePower - 800  if basePower > 1000  else
            basePower - 300  if basePower > 500  else
            basePower - 100
        )
           
    def GetBasePowerIncrease(self, basePower: int) -> int:
        result = int(basePower * 0.3)
        return result
    
    def ClearConsole(self):
        # Clear printed lines in console for cleaner
        # and readable texts
        print("\033c", end="")                       
        

class GamePlay:
    def __init__(self):
        self.gameManager = GameManager()
        self.playerSelectedPokemon = []
        self.computerPokemon = []
        self.battleNumber = 1
        self.playerMainPowerBase = 0
        self.computerMainPowerBase = 0
        
        self.computerWins = 0
        self.playerWins = 0

        self.CharacterSelection()

    def CharacterSelection(self):
        while True:
            try:
                print("\n" + "-" * 15 + " Pokemon Battle " + "-" * 15 + "\n")
                
                pokemonsNameList = self.gameManager.GetPokemonList()

                # Pokemon Selection Table Header
                print("Select a Pokemon: \n")
                print("{:<8}{:<10}{:<10}".format(
                    " #",
                    "Name",
                    "Base Power"
                    ))
                
                # Pokemon Selection Table Contents
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
                    self.playerSelectedPokemon = self.gameManager.SetSelectPokemon(pokemonIndex)
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
        showSummary = False
        optionInput = ""
        
        while True:        
            self.computerPokemon = self.gameManager.GetComputerPokemon()
            
            playerBasePower = self.playerSelectedPokemon[1]
            computerBasePower = self.computerPokemon[1]
            
            # Checks the Main Power Base of this game instance
            if self.playerMainPowerBase != 0:
                playerBasePower += self.playerMainPowerBase
                
            if self.computerMainPowerBase != 0:
                computerBasePower += self.computerMainPowerBase
            
            # Calculation of Final Power
            playerFinalPower, playerEnhancedPower = self.gameManager.GetFinalPower(playerBasePower)
            computerFinalPower, computerEnhancedPower = self.gameManager.GetFinalPower(computerBasePower)

            # Show Battle Pokemon stats at start
            self.gameManager.ShowBattleStartInformation(
                self.battleNumber,
                self.playerSelectedPokemon, 
                self.computerPokemon,
                playerBasePower,
                computerBasePower,
                playerEnhancedPower,
                playerFinalPower)
            
            gameBattleStatus = self.gameManager.ShowBattleScore(playerFinalPower, computerFinalPower)
            
            # Increase the Base Power of Winners with the opponents Final Power
            if gameBattleStatus == "Win!":
                self.playerWins += 1
                self.playerMainPowerBase += computerFinalPower
                self.computerMainPowerBase += self.gameManager.GetBasePowerIncrease(computerBasePower)
                
            elif gameBattleStatus == "Lose!":
                self.computerWins += 1
                self.computerMainPowerBase += playerFinalPower
                self.playerMainPowerBase += self.gameManager.GetBasePowerIncrease(playerBasePower)
                
            
            # Condition for Win Streaks
            if self.computerWins >= 2:
                self.computerMainPowerBase = self.gameManager.GetPowerDecay(computerBasePower)
                self.computerWins = 0
            elif self.playerWins >= 2:
                self.playerWins = 0
                self.playerMainPowerBase = self.gameManager.GetPowerDecay(playerBasePower)
                
            # Shows Battle Results
            self.gameManager.ShowBattleResultInformation(
                self.playerSelectedPokemon,
                self.computerPokemon,
                playerBasePower,
                computerBasePower,
                playerEnhancedPower,
                computerEnhancedPower,
                playerFinalPower,
                computerFinalPower)

            # Record Battle Result to Battle Summary
            self.gameManager.SetRecordStats(self.battleNumber, self.playerSelectedPokemon[0] ,playerFinalPower, self.computerPokemon[0], computerFinalPower, gameBattleStatus)
            
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
                    self.CharacterSelection()   
                    break
                elif optionInput == "x" or optionInput == "X":
                    self.gameManager.ClearConsole()  
                    breakOuterLoop = True
                    showSummary = True
                    break
                else:
                    print("Invalid Input. Try Again!\n")
                    time.sleep(1)
                    self.gameManager.ClearConsole()  
                    continue
            
            if breakOuterLoop:
                if showSummary:
                    self.gameManager.ShowBattleSummary()            
                break           
    
if __name__ == "__main__":
    startGame = GamePlay()