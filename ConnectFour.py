"""
Aleck Lu and Jun Hua Chen
jchen249@binghamton.edu alu2@binghamton.edu
cs110
Python Final Project
"""

"""
This class represents a connect four game.
A connect four game has board and win conditions
input from keyboard:
  column number(int)
output to monitor:
  Updated game board with pieces drawn

"""



#python final project





class Connect:

  #Class Varibales____________________________________________________________
  MAX_MOVE=42
  ROW_TWO=2
  ROW_THREE=3
  ROW_FOUR=4
  ROW_FIVE=5
  NUM_COLUMNS=7
  NUM_ROWS=6

#Constructor------------------------------------------------------------------
  def __init__(self):
  #initialize: self.players(List) to list of X and O ,self.__turn(str) to first player, self.__winCondition to False,
  #   self.__columns to 7, self.__rows to 6, self.board to list with 7 columns and 6 rows, self.count to empty list
    self.players=['X','O']
    self.__turn=self.players[0]
    self.__winCondition=False
    self.__columns = self.NUM_COLUMNS
    self.__rows=self.NUM_ROWS
    self.board = [['' for i in range(7)] for y in range(6)]
    self.count=[] #keep track of the occurence of the same column entry

    
#--Accessors------------------------------------------------------------------
  #returns: current player turn(str)
  def getTurn(self):
    return self.__turn
  # returns: number of columns(str)
  def getColumns(self):
    return self.__columns
  # returns: number of rows(str)
  def getRows(self):
    return self.__rows

#predicates____________________________________________________________________
  #True if board is filled but win condition hasn't been met
  def isTieGame(self):
    return len(self.count) == self.MAX_MOVE
  #True if player X turn
  def isTurn(self):
    return self.__turn == self.players[0]
  #True if no one has made a Connect 4 yet
  def isGame(self):
    return self.__winCondition == False

#mutators---------------------------------------------------------------------
  
  #Switches turn between PLayer X and Player O
  #invokes: isTurn()
  def switchTurn(self):
    if self.isTurn():
      self.__turn = self.players[1]
    else:
      self.__turn = self.players[0]

  #Drops a piece into the game board.
  #Ends the game if win condition has been met
  #params: column-column entry(int)
  #invokes: isGame(), win(), switchTurn(), getTurn()
  def dropPiece(self, column):
    self.count.append(column)
    if self.isGame():
      if 0 <= column < (self.getColumns()) and\
           self.count.count(column)<7:
        #print (0 <= int(column) < (self.getColumns()))
          if self.board[self.ROW_FIVE][column] == '':
            self.board[self.ROW_FIVE][column]=self.getTurn()
          elif self.board[self.ROW_FOUR][column] == '':
            self.board[self.ROW_FOUR][column]=self.getTurn()
          elif self.board[self.ROW_THREE][column] == '':
            self.board[self.ROW_THREE][column]=self.getTurn()
          elif self.board[self.ROW_TWO][column] == '':
            self.board[self.ROW_TWO][column]=self.getTurn()
          elif self.board[1][column] == '':
            self.board[1][column]=self.getTurn()
          elif self.board[0][column] == '':
            self.board[0][column]=self.getTurn()
          self.win()
          if self.__winCondition==False:
            self.switchTurn()

  #All possible win conditions
  #invokes: getTurn()
          
  def win(self):
    for row in range(self.NUM_ROWS-3):#vertical
      for column in range(self.NUM_COLUMNS):
          ##print(self.board[column][row])
          ##print (self.board)
          ##print (self.board[3][0])
        if self.board[row][column]==self.getTurn() and\
           self.board[row+1][column]==self.getTurn() and\
           self.board[row+2][column]==self.getTurn() and\
           self.board[row+3][column]==self.getTurn():
            
            self.__winCondition=True

    for row in range(self.NUM_ROWS):#horizontal
      for column in range(self.NUM_COLUMNS-3):
       if self.board[row][column]==self.getTurn() and\
           self.board[row][column+1]==self.getTurn() and\
           self.board[row][column+2]==self.getTurn() and\
           self.board[row][column+3]==self.getTurn():
          self.__winCondition=True

    for row in range(self.NUM_ROWS-3,self.NUM_ROWS):#up right
      for column in range(self.NUM_COLUMNS-3):
         if self.board[row][column]==self.getTurn() and\
           self.board[row-1][column+1]==self.getTurn() and\
           self.board[row-2][column+2]==self.getTurn() and\
           self.board[row-3][column+3]==self.getTurn():
          self.__winCondition=True

    for row in range(self.NUM_ROWS-3):#down right
      for column in range(self.NUM_COLUMNS-3):
        if self.board[row][column]==self.getTurn() and\
           self.board[row+1][column+1]==self.getTurn() and\
           self.board[row+2][column+2]==self.getTurn() and\
           self.board[row+3][column+3]==self.getTurn():
          self.__winCondition=True
      

                                    
               
                    
              
                                
            
                 
          
          

    
    
      
        
    
                   
    
  
        
        

      
    
        

  
      
      

    
      
      
