import random
import abc

"""
@Class: Dice
@Description: 
    Represents a single "die" with X number of sides.
@Methods:
    Roll - Rolls the dice and returns a value between 1 and "number of sides" 
"""
class Dice(object):
    def __init__(self,num_sides=6):
        self.NumSides = num_sides

    def Roll(self):
        return random.randint(1,self.NumSides)  

##############################################################################
##############################################################################

"""
@Class: Pig
@Description: 
    Represents the game of pig (dice game)
@Methods:
    Roll - Rolls the "die" or "dice" and returns a list of rolled values
"""
class Pig(object):
    def __init__(self,num_dice=1,dice_sides=6,skunk_value=1):
        self.NumDice = num_dice
        self.DiceSides = dice_sides
        self.DiceList = []
        self.SkunkValue = skunk_value
        for i in range(self.NumDice):
            self.DiceList.append(Dice(self.DiceSides))
    """
    @Method: Roll
    @Description: 
        One roll in a pig game, with 1 to NumDice per roll
    @Returns: int: [0=skunk value occured, total of all dice otherwise]
    """ 
    def Roll(self):
        scores = []
        for d in self.DiceList:
            scores.append(d.Roll())
            if self.SkunkValue in scores:
                return 0 
        return sum(scores)

##############################################################################
##############################################################################

class Player(object):
    def __init__(self,name,stw,num_dice=1,strategy=('Random',7)):
        self.Name = name        # My name
        self.TotalScore = 0     # Total score
        self.stw = stw          # score to win
        self.LastScore = 0      # Score on last turn
        self.LastNumRolls = 0   # Last number of rolls
        self.Opponents = {}     # Dict of opponents
        self.NumDice = num_dice
        self.Strategy = strategy[0]
        self.pig = Pig(num_dice)# init pig game 
        self.Strategies = {
                'Target_Score':0,
                'Target_Rolls':0,
                'Sprint_To_Finish':0,
                'Mimic_Opponent':0,
                'Situational':0,
                'Random':0
            }
        self.Strategies[strategy[0]] = strategy[1]

    """
    @Method: AddOpponents
    @Description: Adds an opponent, or list of opponents (as long as it's not me) to a dictionary with name and score.
        Example: {
                   'bob':0.
                   'sue':0
                 }
    
    @Params: [] - Opponents
    @Returns: None
    """
    def AddOpponents(self,opponent):
            for op in opponent:
                if not op.Name == self.Name:
                    self.Opponents[op.Name] = op


    """
    @Method: __str__
    @Description: Prints out a nice version of self
    @Returns: string representation
    """
    def __str__(self):
        tmp = " "
        for k,v in self.Opponents.items():
            tmp = tmp + "[" + k + " " + str(v.TotalScore) + "," + str(v.LastScore) + "," + str(v.LastNumRolls) + "] "
        return "Name: %s, TotScore: %s, LastScore: %s, LastNumRolls: %s, Opponents: %s" % (self.Name,self.TotalScore,self.LastScore,self.LastNumRolls,tmp)
        
    """
    @Method: __repr__
    @Description: Calls __str__
    @Returns: a call to __str__
    """
    def __repr__(self):
        return self.__str__()
        

    """
    @Method: SetStrategy
    @Description: Sets the current strategy for the player
    @Params:
        strategy: string 
        value: int    
    @Returns: None
    @Usage:
            SetStrategy('Target_Score',20)
            SetStrategy('Target_Rolls',5)     
            SetStrategy('Sprint_To_Finish',72)    
    """
    def SetStrategy(self,strategy,value):
        if strategy in self.Strategies:
            self.Strategies[strategy] = value
        else:
            raise ValueError('The strategy does not exist!')

    """
    @Method: PlayerRoll
    @Description: Implements a turn for a player. If the player rolls a 1 at any time zero is returned, 
                  otherwise the total of the rolls is returned.
    @Params:
        string: player
        int: max rolls 
    @Returns: int: total
    """
    def Roll(self):
        if self.TotalScore / self.TargetScore >= .8:
            self.Strategy = 'SprintToFinish'
        if self.Strategy == 'Random':
            Score,NumRolls = self.RandomRoll()
        elif self.Strategy == 'Aggressive':
            Score,NumRolls = self.Target_Roll(8)
        elif self.Strategy == 'Cautious':
            Score,NumRolls = self.Target_Roll(4)
        elif self.Strategy == 'Robust':
            pass
        elif self.Strategy == 'CopyCat':
            pass
        
        self.TotalScore += Score
        self.LastScore = Score
        self.LastNumRolls = NumRolls
        
        
    def RandomRoll(self):
        Score = 0
        NumRolls = 0
        #Variable to use as a means to see if current turns score and the previous total score beat the stw
        tem_s = self.TotalScore                
        for i in range(random.randint(1,7)):
            NumRolls += 1
            roll = self.pig.Roll()
            if roll == 0:
                break
            Score += roll
            #if the score breaks the stw print the "woot they won" message and return the score and number of rolls used.
            if (Score + tem_s) >= self.stw:
                print('%s has just reached %d points and is stopping' % (self.Name, self.TotalScore)) 
                return (Score,NumRolls)
        return (Score,NumRolls)

            
    def Target_Score(self):
        pass

    """
    @Method: Target_Roll
    @Description: Implements a target number of rolls for the player to attempt. If rolls to attempt are achieved
    			player has the score of the rolls added to their total, if the player rolls a 1 their score is not
    			adjusted.
    @Params:
        string: player
        int: max rolls 
    @Returns: int: Score int: NumRolls
    """        
    def Target_Roll(self, Rolls):
        Score = 0
        NumRolls = 0
        self.rolls = rolls
        tem_s = self.TotalScore
        for i in range(rolls)
            NumRolls += 1
            roll = self.pig.Roll()
            if roll == 0:
                break
            Score += roll
            if (score + tem_s) <= self.stw:
                print('%s has just reached %d points and is stopping' % (self.Name, self.TotalScore)) 
                return (Score,NumRolls)
        return (Score,NumRolls)

    """
    @Method: Sprint_To_Finish
    @Description: Implements a rush to the target score when the players score is within 80% of the target Score.
    			Player rolls untill either they roll a 1 and end up having to wait till their next turn or they reach 
    			the Score to Win.
    @Params:
        string: player
    @Returns: int: Score int: NumRolls
    """  
    def Sprint_To_Finish(self):
        Score = 0
        NumRolls = 0
        self.rolls = rolls
        tem_s = self.TotalScore
        while score + tem_s not stw:
            NumRolls += 1
            roll = self.pig.Roll()
            if roll == 0:
                break
            Score += roll
            if (score + tem_s) <= self.stw:
                print('%s has just reached %d points and is stopping' % (self.Name, self.TotalScore)) 
                return (Score,NumRolls)
        return (Score,NumRolls)
        
        
    def Mimic_Opponent(self):
        pass

    def Situational(self):
        pass
        
    def Combination(self):
        pass


##############################################################################
##############################################################################

"""
This Class represents one instance of a game with X players rolling X dice playing to a score of X.
"""
class Game(object):
    """
    @Method: Init
    @Description: Initializes a pig game instance
    @Params:
        list: Players - A list of player names
        int: NumDice - Number of dice per roll
        int: RandomRolls - Top value of random range for rolls
        int: TargetScore - Target score to trigger a winner
    @Returns: None
    """
    def __init__(self, **kwargs):
        self.Players = {}                           # player dictionary
        self.NumDice = kwargs['num_dice']           # number of dice per roll
        self.RandomRolls = kwargs['random_roles']   # max num random rolls
        self.TargetScore = kwargs['target_score']   # game winning score
        self.WinnerName = None                      # no winner yet
        
        # initialize all players
        self.AddPlayers(kwargs['players'])
            
        self.StartGame()
        
    def __str__(self):
        string = ""
        for name,obj in self.Players.items():
            string += obj.__str__() + "\n"
        return string
        
    """
    @Method: AddPlayers
    @Description: Adds a new player or players to the game
        Example: {
                   'bob':<player_object>
                   'sue':<player_object>
                 }
    
    @Params: [] - players
    @Returns: None
    """
    def AddPlayers(self,players):
        if not type(players) == list:
            self.Players[players.Name] = players
        else:
            for p in players:
                self.Players[p.Name] = p
                    
    """
    @Method: WinnerExists
    @Description: Checks to see if a player has acheived the target score.
    @Params:None
    @Returns: bool
    """         
    def StartGame(self):

        self.UpdatePlayerOpponents()
        
        # Main game loop
        while not self.WinnerExists():
            print(self)
            for name,PlayerObj in self.Players.items():
                PlayerObj.Roll()
       
    """
    @Method: WinnerExists
    @Description: Checks to see if a player has acheived the target score.
    @Params:None
    @Returns: bool
    """
    def WinnerExists(self):
        for name,PlayerObj in self.Players.items():
            if PlayerObj.TotalScore >= self.TargetScore:
                self.WinnerName = PlayerObj.Name
                return True
        self.WinnerName = None
        return False

    """
    @Method: Winner
    @Description: Returns the winner, if there is one.
    @Params:None
    @Returns: [string,None]: Players name or None
    """
    def Winner(self):
        return self.WinnerName
        
    """
    @Method: UpdatePlayerOpponents
    @Description: Gives a copy of each player in the game, to every other player in the game. 
    @Params:None
    @Returns: None
    """   
    def UpdatePlayerOpponents(self):

        for name,PlayerObj in self.Players.items():
            PlayerObj.AddOpponents(self.Players.values())

##############################################################################
##############################################################################



def main():
    #Score to Win variable to set the stw in Player Class and for the Target_Score inside of the Pig Class
    stw = 100               
    p1 = Player('ann', stw)
    p2 = Player('bob', stw)
    p3 = Player('sue', stw)
    p4 = Player('dax', stw)
    
    AllPlayers = [p1,p2,p3,p4]
    
    # Param values to initialize a pig game instance
    kwargs = {'num_dice':1,'random_roles':9,'target_score':stw,'players':AllPlayers}

    g = Game(**kwargs)
    
    print(g)
    
    
main()
