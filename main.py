import random
import time

# Author: Villaber, Christian Jude
# J2S

class GameManager:
    def __init__(self):
        self.pokemons_Dict = {
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
        
        self.battle_Number: int = 0
        self.total_Wins: int = 0
        self.total_Loses: int = 0
        self.total_Ties: int = 0
        self.player_Pokemon_List: list = []
        self.player_Power_List: list = []
        self.computer_Pokemon_List: list = []
        self.computer_Power_List: list = []
        self.game_Status_List: list = []
  
    def ShowBattleScore(self, player_Power: int, computer_Power: int) -> str:
        if player_Power == computer_Power:
            print(" " * 22 + "|==================|")
            print(" " * 22 + "|       Tie!       |")
            print(" " * 22 + "|==================|\n")
            self.total_Ties += 1
            return "Tie!"
        elif player_Power > computer_Power:
            print(" " * 22 + "|==================|")
            print(" " * 22 + "|     You Win!     |")
            print(" " * 22 + "|==================|\n")
            self.total_Wins +=1
            return "Win!"
        else:
            print(" " * 22 + "|==================|")
            print(" " * 22 + "|    You Lose!     |")
            print(" " * 22 + "|==================|\n")
            self.total_Loses += 1
            return "Lose!"

    def ShowBattleStartInformation(self, battle_Number: int, selected_Pokemon: list, computer_Pokemon: list, player_BasePower: int, computer_BasePower: int, player_Enhanced_Power: int, player_Final_Power: int):
    # Battle number(#) Information
        # Player Stats
        print("\n" + "-" * 40 + f" Battle {battle_Number} " + "-" * 40 + "\n")
        print("{:<31}{:<20}{:<25}{:<0}".format(
            "Your Pokemon: " + str(selected_Pokemon[0]), 
            "Base Power: " + str(player_BasePower),
            "Enhanced Power: +" + str(player_Enhanced_Power),
            "Final Power: " + str(player_Final_Power)))
        
        # Computer Stats
        print("{:<30}{:<20}{:<25}{:<0}".format(
            "Computer Pokemon: " + str(computer_Pokemon[0]), 
            " Base Power: " + str(computer_BasePower),
            " Enhanced Power: +???",
            " Final Power: ???"))
        
        print("\nPress Enter to Start Battle \n")
        input("")
        return
    
    def ShowBattleResultInformation(self, player_Selected_Pokemon: list, computer_Pokemon: list, player_BasePower: int, computer_BasePower: int, player_Enhanced_Power: int, computer_Enhanced_Power: int, player_Final_Power: int, computer_Final_Power: int):
        # Battle number(#) Result Stats Table
            print("{:<5}{:<30}{:<0}".format(
                "",
                "Your Pokemon: " + str(player_Selected_Pokemon[0]),
                "Computer Pokemon: " + str(computer_Pokemon[0])))
            
            print("{:<5}{:<30}{:<0}".format(
                "",
                "Base Power: " + str(player_BasePower),
                "Base Power: " + str(computer_BasePower)))
            
            print("{:<5}{:<30}{:<0}".format(
                "",
                "Enhanced Power: +" + str(player_Enhanced_Power),
                "Enhanced Power: +" + str(computer_Enhanced_Power)))
            
            print("{:<5}{:<30}{:<0}".format(
                "",
                "Final Power: " + str(player_Final_Power),
                "Final Power: " + str(computer_Final_Power)))
    
    def ShowBattleSummary(self):
        print("\n" + "-" * 40 + " Battle Summary " + "-" * 40 + "\n")
        
        # Show Totals of Wins, Loses and Ties
        print("{:<5}{:<20}{:<20}{:<0}".format(
            "",
            "Total Wins = " + str(self.total_Wins),
            "Total Loses = " + str(self.total_Loses),
            "Total Ties = " + str(self.total_Ties)
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
        for battle_Index in range(0, self.battle_Number):
            print("{:<5}{:<13}{:<18}{:<12}{:<21}{:<12}{:<0}".format(
                "",  
                str(battle_Index + 1),
                self.player_Pokemon_List[battle_Index], 
                str(self.player_Power_List[battle_Index]),
                self.computer_Pokemon_List[battle_Index],
                str(self.computer_Power_List[battle_Index]),
                self.game_Status_List[battle_Index]
                ))     
        print("")
    
    def ShowFatigueInfo(self, target_Opponent: str):
        print("{:<5}".format("\n" + "-" * 15 + " Pokemon Fatigue " + "-" * 15))
        print("{:<12}{:<0}".format("\n", f"{target_Opponent} Pokemon is Tired"))
        print("{:<14}{:<0}".format("", "Power is Reduced"))
        
    def ValidatePokemonSelection(self, pokemon_Index: int) -> bool:
        if pokemon_Index > len(self.pokemons_Dict) or pokemon_Index < 0:
            print("Number is Out of Range. Try Again \n")
            time.sleep(1)
            self.ClearConsole()                 
            return False
        else:
            return True
    
    # Records all information for battle summary
    def SetRecordStats(self, battle_Number: int, player_Pokemon: str, player_Power: int, computer_Pokemon: str, computer_Power: int, game_Status: str):
        self.battle_Number = battle_Number
        self.player_Pokemon_List.append(player_Pokemon)
        self.player_Power_List.append(player_Power)
        self.computer_Pokemon_List.append(computer_Pokemon)
        self.computer_Power_List.append(computer_Power)
        self.game_Status_List.append(game_Status)
  
    def SetSelectPokemon(self, pokemon_Index: int) -> list:
        selected_Pokemon = list(self.pokemons_Dict.items())[pokemon_Index - 1]
        return selected_Pokemon 
    
    def GetComputerPokemon(self) -> list:
        return random.choice(list(self.pokemons_Dict.items()))

    def GetPokemonList(self):
        return self.pokemons_Dict

    def GetFinalPower(self, base_Power: int) -> int:
        random_Num = 100
        random_Range = random.randrange(0, random_Num)      
        final_Power = base_Power + random_Range
        return final_Power, random_Range

    def GetPowerDecay(self, base_Power: int) -> int:
        return (
            base_Power - 800000 if base_Power > 1000000 else
            base_Power - 10500 if base_Power > 20000 else
            base_Power - 8000 if base_Power > 10000 else
            base_Power - 4500  if base_Power > 5000  else
            base_Power - 1500  if base_Power > 2000  else
            base_Power - 800  if base_Power > 1000  else
            base_Power - 300  if base_Power > 500  else
            base_Power - 100
        )
           
    def GetBasePowerIncrease(self, base_Power: int) -> int:
        result = int(base_Power * 0.3)
        return result
    
    def ClearConsole(self):
        # Clear printed lines in console for cleaner
        # and readable texts
        print("\033c", end="")                       
        

class GamePlay:
    def __init__(self):
        self.game_Manager = GameManager()
        self.player_Selected_Pokemon = []
        self.computer_Pokemon = []
        self.battle_Number = 1
        self.player_Main_PowerBase = 0
        self.computer_Main_PowerBase = 0
        
        self.computer_Wins = 0
        self.player_Wins = 0
        self.is_Character_Selection = False

        self.CharacterSelection()

    def CharacterSelection(self):
        while True:
            try:
                print("\n" + "-" * 15 + " Pokemon Battle " + "-" * 15 + "\n")
                
                pokemon_Name_List = self.game_Manager.GetPokemonList()

                # Pokemon Selection Table Header
                print("Select a Pokemon: \n")
                print("{:<8}{:<10}{:<10}".format(
                    " #",
                    "Name",
                    "Base Power"
                    ))
                
                # Pokemon Selection Table Contents
                count = 0
                for pokemon, basevalue in pokemon_Name_List.items():
                    count += 1
                    print("{:<1}{:<5}{:<15}{:<0}".format(
                        "",
                        str(count),
                        pokemon,
                        str(basevalue)
                        ))

                pokemon_Index = int(input("\nEnter Pokemon Number: "))
                
                # Checks input index if the index is within the length range of the pokemonList
                # if True => Exit Loop and set target pokemon index to selectedPokemon
                # if False => Continue Loop
                if self.game_Manager.ValidatePokemonSelection(pokemon_Index):
                    self.player_Selected_Pokemon = self.game_Manager.SetSelectPokemon(pokemon_Index)
                    break
                    
            except ValueError:
                print("Invalid Input. Please Try Again \n")
                time.sleep(1)
                self.game_Manager.ClearConsole()                                     
                continue
        
        self.game_Manager.ClearConsole()      
        self.BattleSimulation()          
                
    def BattleSimulation(self):
        break_OuterLoop = False
        show_Summary = False
        option_Input = ""
        
        while True:        
            self.computer_Pokemon = self.game_Manager.GetComputerPokemon()
            
            player_BasePower = self.player_Selected_Pokemon[1]
            computer_BasePower = self.computer_Pokemon[1]
            
            # Checks the Main Power Base of this game instance
            if self.player_Main_PowerBase != 0 and self.is_Character_Selection == False:
                player_BasePower += self.player_Main_PowerBase
                
            if self.computer_Main_PowerBase != 0 and self.is_Character_Selection == False:
                computer_BasePower += self.computer_Main_PowerBase
            
            # Calculation of Final Power
            player_Final_Power, player_Enhanced_Power = self.game_Manager.GetFinalPower(player_BasePower)
            computer_Final_Power, computer_Enhanced_Power = self.game_Manager.GetFinalPower(computer_BasePower)

            # Show Battle Pokemon stats at start
            self.game_Manager.ShowBattleStartInformation(
                self.battle_Number,
                self.player_Selected_Pokemon, 
                self.computer_Pokemon,
                player_BasePower,
                computer_BasePower,
                player_Enhanced_Power,
                player_Final_Power)
            
            game_Battle_Status = self.game_Manager.ShowBattleScore(player_Final_Power, computer_Final_Power)
            
            # Increase the Base Power of Winners with the opponents Final Power
            if game_Battle_Status == "Win!":
                self.player_Wins += 1
                self.player_Main_PowerBase += computer_Final_Power
                self.computer_Main_PowerBase += self.game_Manager.GetBasePowerIncrease(computer_BasePower)
                
            elif game_Battle_Status == "Lose!":
                self.computer_Wins += 1
                self.computer_Main_PowerBase += player_Final_Power
                self.player_Main_PowerBase += self.game_Manager.GetBasePowerIncrease(player_BasePower)
                
            player_Fatigue = False
            computer_Fatigue = False
            
            # Condition for Win Streaks
            if self.computer_Wins >= 3:
                self.computer_Main_PowerBase = self.game_Manager.GetPowerDecay(computer_BasePower)
                computer_Fatigue = True
                self.computer_Wins = 0
                
            elif self.player_Wins >= 3:
                self.player_Main_PowerBase = self.game_Manager.GetPowerDecay(player_BasePower)
                player_Fatigue = True
                self.player_Wins = 0
                
            # Shows Battle Results
            self.game_Manager.ShowBattleResultInformation(
                self.player_Selected_Pokemon,
                self.computer_Pokemon,
                player_BasePower,
                computer_BasePower,
                player_Enhanced_Power,
                computer_Enhanced_Power,
                player_Final_Power,
                computer_Final_Power)
            
            # Set is_Character_Seletion to False after Character Selection occur
            if self.is_Character_Selection:
                self.is_Character_Selection = False
            
            # Show Fatigue Information        
            if player_Fatigue:
                self.game_Manager.ShowFatigueInfo("Player")
                player_Fatigue = False
            elif computer_Fatigue:
                self.game_Manager.ShowFatigueInfo("Computer")
                computer_Fatigue = False
                
            # Record Battle Result to Battle Summary
            self.game_Manager.SetRecordStats(self.battle_Number, self.player_Selected_Pokemon[0] ,player_Final_Power, self.computer_Pokemon[0], computer_Final_Power, game_Battle_Status)
            
            self.battle_Number += 1
            
            # Option Selection after every battle
            while True:
                print("")
                print("1. Continue?")
                print("2. Select New Pokemon?")
                print("[X] Quit")

                option_Input = str(input("Enter Number or X to Quit: "))

                if option_Input == "1":
                    self.game_Manager.ClearConsole()  
                    break
                elif option_Input == "2":
                    self.game_Manager.ClearConsole()  
                    break_OuterLoop = True
                    self.CharacterSelection()   
                    break
                elif option_Input == "x" or option_Input == "X":
                    self.game_Manager.ClearConsole()  
                    break_OuterLoop = True
                    show_Summary = True
                    break
                else:
                    print("Invalid Input. Try Again!\n")
                    time.sleep(1)
                    self.game_Manager.ClearConsole()  
                    continue
            
            if break_OuterLoop:
                if show_Summary:
                    self.game_Manager.ShowBattleSummary()            
                break           
    
if __name__ == "__main__":
    start_Game = GamePlay()