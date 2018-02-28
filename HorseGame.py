import random
import time 
from builtins import input

horse_dic = {}
registered_horses = []
wild_horses = []
    
class Horses(): 
    def __init__(self): # An instance of the horse class, with some stats.
        self.color = random.choice(['black', 'white', 'brown', 'blue', 'tan', 'beige', 'gray'])
        self.pattern = random.choice(['solid', 'speckled', 'patchy'])
        self.strength = random.randint(1,5)
        self.speed = random.randint(1,5)
        self.stamina = random.randint(1,5)
        self.temperament = random.choice(['wild', 'gentle', 'stubborn', 'shy'])
    
    def display_stats(self): # Displays horse stats
        print("Here are your horse's stats: ")
        print(self.pattern, self.color)
        print('Strength: ' + str(self.strength))
        print('Speed: ' + str(self.speed))
        print('Stamina: ' + str(self.stamina))
        print('Temperament: ' + self.temperament)

def welcome(): # Starts the game off in the ranch.
    print('Ranch Hand: \nWelcome to the stable. You currently have %d registered horses.' % len(registered_horses))
    if len(registered_horses) == 0:
        adv = input('\nDo you want to try to tame one? (y/n)')
        if adv == 'y': # Starts horse catching game
            print('\nRanch Hand: \nGood luck out there!')
            beginning()
        else:
            print('Ok. Game over.')
    else:
        print('Here are all your horses:\n')
        for r in registered_horses:
            print('-' + r)
        yn = input('\nWould you like to take out a horse? (y/n)')
        if yn == 'y':
            horse_select()
        else:
            pass
        what = input('\nDo you want to tame more horses? (y/n)')
        if what == 'y':
            beginning()
        else:
            welcome()
    
def horse_select():
    choice = input('Which horse would you like to take out? (Enter a number from 1 to %d.)\n' % len(registered_horses))
    try:
        choice = int(choice)-1
        if choice <= len(registered_horses):
            if registered_horses[choice] not in horse_dic:
                print('\nSomething went wrong.\n')
            else:
                print('Ok. Taking out %s. Here are his stats:\n' % registered_horses[choice])
                output_selected_horse_stat(horse_dic.get(registered_horses[choice])) #prints out the stat of selected horse , horse_dic.get(registered_horses[choice]) extracts the stat list of selected horse
        else:
            print('Unregistered horse.')
    except ValueError:
        print('Please enter a number.')
        
def output_selected_horse_stat(l):
    '''print out the stat of horse from extracted list'''
    print(l[0],l[1])
    print("Strenth: %s" %str(l[2]))
    print("Speed: %s" %str(l[3]))
    print("Stamina: %s" %str(l[4]))
    print("Temperament: %s" %str(l[5]))

def beginning(): # Horse catching game
    new_horse()
    print('\nIn the distance you see a %s %s horse.\n' % (wild_horses[-1].pattern, wild_horses[-1].color))
    time.sleep(1)
    yn = input('Would you like to try to tame it? (y/n)')
    if yn == 'y':
        horse_roll()
    else:
        stable = input('Go back to stable? (y/n)')
        if stable == 'y':
            welcome()
        else:
            beginning()

def new_horse():
    wild_horses.append(1)
    wild_horses[-1] = Horses()
    

def register():
    # Upon successful horse catching, and adds a horse to list if desired.
    reg = input('\nWould you like to register this horse? (y/n)')
    if reg == 'y':
        name = input('\nWhat would you like to name it?')
        registered_horses.append(name.title())
        if name not in horse_dic:
            horse_dic[name.title()] = [wild_horses[-1].pattern, wild_horses[-1].color, wild_horses[-1].strength, wild_horses[-1].speed, wild_horses[-1].stamina, wild_horses[-1].temperament]
        print('\nOk. You named your horse %s. Going back to the stable.\n' % registered_horses[-1])
        time.sleep(1)
        
        welcome()
    else:
        print('Ok. Back to the wild.\n')
        beginning()

def horse_roll(): 
    # Determines whether a horse is caught. 70% chance of success. 
    while True:
        hr = random.randint(1, 10)
        if hr >= 4:
            print('\nAttempting to catch a %s %s horse.' % (wild_horses[-1].pattern, wild_horses[-1].color))
            time.sleep(1)
            print('\nSuccess!\n')
            wild_horses[-1].display_stats()
            register()
            break
        else:
            time.sleep(1)
            print('\nDamn. He got away.\n')
            time.sleep(1)
            ag = input('Try again? (y/n)')
            new_horse()
            if ag == 'n':
                break

def main():
    welcome()               


if __name__ == '__main__':
    main()

