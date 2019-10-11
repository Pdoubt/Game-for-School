# -*- coding: utf-8 -*-
# IMPORTES



import time
import random



# GLOBALS



HEALTH, ATK, DEF, C_CLASS, B_S_B = None, None, None, None, 0

def clear():
    print(u'\033[H\033[J')

# GAME
              


def main():
    intro()
    character_class = choose_class()
    
    print("[+] You chose %s." % character_class)
    
    assign_stats(character_class)
    
    time.sleep(2)
    
    clear()
    
    print_lore()
    
    time.sleep(1)
    
    clear()
    
    ask_for_guide()
    
    clear()



# GAME OPENING



def intro():
    
    clear()
    
    print (c)
    
    time.sleep(1)
    
    clear()
    
    print (a)
    
    time.sleep(1)



# CREATE CLASS



def choose_class():
    clear()
    character_class = None
    classes = ["Knight", "Mage", "Paladin"]

    while character_class not in classes:
        clear()
        print(b)
        character_class = raw_input("[*] Class: ")
        
        if character_class not in classes:
            print("\n[-] %s class does not exist!\n[-] Try again.\n" % character_class)
            time.sleep(2)
            
    return character_class

def assign_stats(character_class):
    
    class_stats = {"Knight": [150, 10, 10],
                   "Mage": [100, 15, 5],
                   "Paladin": [200, 5, 15]}
               
    if character_class in class_stats:
        
        global HEALTH
        global ATK
        global DEF
        global C_CLASS
        
        HEALTH = class_stats[character_class][0]
        ATK = class_stats[character_class][1]
        DEF = class_stats[character_class][2]
        C_CLASS = character_class 
        
def print_lore():
    
    character_lores = {"Knight": "[+] You have joined the King's side. The King has gifted you with 'The Diamond Sword.' This sword was crafted by the hands of heaven's greatest blacksmithes and sent down to Earth during the crucifiction of Jesus. This sword deals a whooping 10dmg. You have taken upon the duty to remove evil from the Kingdom of Fortknight.\n[+] Now go forth young soldier, and begin your quest of greatness." ,
                       "Mage": "[+] You have joined the Brotherhood of Mages. You do not fight for fame or glory. You simply fight for the satisifaction of seeing the blood of your enemies spill. From the bones of Dragons you've slayed with bare hands, you crafted the 'Staff.' This staff deals a whooping 15 dmg. You have decicded to use your powers to enforce your will upon the weak.\n[+] Fly foward and vaporize your enemies.",
                       "Paladin": "[+] You have joined the Pope's order in the defense of Forknight. The Pope has seen the forces of man fight over these lands for many years. He has prayed for guidence from God and through his inspiration, wants to re-establish the presence of religion. The mightiest archangle Michael has granted you his hammer of war, 'The Crucifier.' You are being sent off to clease the land of demons and other evil creatures.\n[+] Don't forget to say your prayers, and begin your crusade of rightousness for the Holy Church of Fortknight."}
                       
    if C_CLASS in character_lores:
        print(character_lores[C_CLASS])

    
    
    raw_input("[*] Press enter to continue...")



# TUTORIAL



def print_guide():
    print("[+] This is a text-based battle simulator. You will go on adventures and fight the forces of evil in the land of Fortknight. If you stumble upon an enemy you will enter the battle sequence. Within this sequence you will have three optinons, Attack, Defend, or Heal.\n[+] If you choose attack your damage will be based on the item you have equipped and the enemey's defense.\n[+] If you choose defend you have a chance to block a percentage of the enemy's attack based on your defense.\n[+] If you choose heal,you will still be vunerable to being attack but you'll have a chance to heala random percentage of your health.\n[+] After the battle sequence you can chooseeither rest or to keep adventuring.\n[+] If you rest you will be at a stand stillfor thirty seconds and back to full health.\n[+] If you choose to keep adventuring you will enter the battle sequence again.\n[+] After 10 battles you will encounter a boss. Bosses have increased health and damage.\n[+] Whithin the world of Fortknight there are multiple item tiers. Common, Uncommon, Rare, Epic, and Legendary. Common's, Uncommon's, and Rare's are dropped from regular battles, while Uncommon's, Rare's, Epic's, and Legendary's are dropped from boss battles.\n[+] Good luck and have fun.")
    raw_input("[*] Press enter to continue...")
   
def ask_for_guide():
    
    answer = None
    answers = ["Y", "N"]
    yes = ["Y"]
    no = ["N"]
    
    while answer not in answers:
        
        print("[+] Would you like to read a game tutorial before going into battle? (Y/N)")
        answer = raw_input("[*] Answer: ")
        print(answer)
        
        if answer not in answers:
            print("[-] Invalid answer. Please try again...")
       
        elif answer in yes:
            clear()
            print_guide()
            clear()
            print("[+] Prepare to begin your adventure...")
            time.sleep(1)
        
        elif answer in no:
            clear()
            print("[+] Prepare to begin your adventure...")
            time.sleep(1)



# BATTLE
 
   
    
# def start_battle()

   



# CREATING ENEMY



def get_race(races):
    
    return random.choice(range(0, 5))

def get_class(classes):
    
    if B_S_B is 10:
        return 4
    
    return random.choice(range(0, 4))

# def get_enemy_stats(races, classes):

                
            
def create_enemy():
                     # HP, ATK, DEF 

    races = [{"Goblin":[25, 25, 30]},
             {"Hound":[30, 20, 25]},
             {"Zombie":[35, 15, 20]},
             {"Vampire":[45, 10, 15]},
             {"Evil Jester":[50, 5, 10]}]
   
    classes = [{"Archer":[-10, 15, 15]},
               {"Witch":[-15, 10, 0]},
               {"Barbarian":[10, 10, 10]},
               {"Grunt":[50, 5, 10]},
               {"Boss":[100, 100, 100]}]


    enemy = [races[get_race(races)], classes[get_class(classes)]]
    
    return enemy



# TESTING FUNCTIONS
    


def test_stats():
    print HEALTH, ATK, DEF
    
def test_edit():
    
    global HEALTH
    HEALTH += 999
    
    print HEALTH
    


# ASCII ART



a = '''                                                                                                                                
     ***** **                                           *****                                                   *                 
  ******  **** *                             *       ******                               *                   **            *     
 **   *  *  ***                             **      **   *  *    **                      ***                  **           **     
*    *  *    *                              **     *    *  *   **** *                     *                   **           **     
    *  *            ****    ***  ****     ********     *  *     ****                                          **         ******** 
   ** **           * ***     **** ****   ********     ** **    * **        ***  ****    ***         ****      **  ***   ********  
   ** **          *   ****    **   ****     **        ** **   *             **** ****    ***       *  ***  *  ** * ***     **     
   ** ******     **    **     **            **        ** *****               **   ****    **      *    ****   ***   ***    **     
   ** *****      **    **     **            **        ** ** ***              **    **     **     **     **    **     **    **     
   ** **         **    **     **            **        ** **   ***            **    **     **     **     **    **     **    **     
   *  **         **    **     **            **        *  **    ***           **    **     **     **     **    **     **    **     
      *          **    **     **            **           *       ***         **    **     **     **     **    **     **    **     
  *****           ******      ***           **       ****         ***        **    **     **     **     **    **     **    **     
 *  *****          ****        ***           **     *  *****        ***  *   ***   ***    *** *   ********    **     **     **    
*    ***                                           *    ***           ***     ***   ***    ***      *** ***    **    **           
*                                                  *                                                     ***         *            
 **                                                 **                                             ****   ***       *             
                                                                                                 *******  **       *              
                                                                                                *     ****        *                                                                                                                                         
'''



b = '''+----------------------------+
|      Choose your class     |
+--------+-------+-----------+
| Knight |  Mage |  Paladin  |
+--------+-------+-----------+
|  150hp | 100hp |   200hp   |
+--------+-------+-----------+
|  10dmg | 15dmg |    5dmg   |
+--------+-------+-----------+
|  10def |  5def |   15def   |
+--------+-------+-----------+\n
'''



c = '''                                                                                                                                   
     ***** *    **   ***              ***                                                           ****           *                  
  ******  *  *****    ***              ***                                                         *  *************                   
 **   *  *     *****   ***              **                                                        *     *********                     
*    *  **     * **      **             **                                                        *     *  *                          
    *  ***     *         **             **                  ****                                   **  *  **            ****          
   **   **     *         **    ***      **       ****      * ***  * *** **** ****       ***           *  ***           * ***  *       
   **   **     *         **   * ***     **      * ***  *  *   ****   *** **** ***  *   * ***         **   **          *   ****        
   **   **     *         **  *   ***    **     *   ****  **    **     **  **** ****   *   ***        **   **         **    **         
   **   **     *         ** **    ***   **    **         **    **     **   **   **   **    ***       **   **         **    **         
   **   **     *         ** ********    **    **         **    **     **   **   **   ********        **   **         **    **         
    **  **     *         ** *******     **    **         **    **     **   **   **   *******          **  **         **    **         
     ** *      *         *  **          **    **         **    **     **   **   **   **                ** *      *   **    **         
      ***      ***      *   ****    *   **    ***     *   ******      **   **   **   ****    *          ***     *     ******          
       ******** ********     *******    *** *  *******     ****       ***  ***  ***   *******            *******       ****     o o o
         ****     ****        *****      ***    *****                  ***  ***  ***   *****               ***                                                                                                                                                                                                                  
'''



# EXTRA FUNCTIONS



if __name__ == "__main__":
    main()
           
