from ConnectFour import *
from tkinter import *
import winsound

#GUI class
class ConnectFourGUI():
  def __init__(self):
    self.__model=Connect()

    self.__mainWindow=Tk()
    

    self.__connectFourLabel=Label(self.__mainWindow,\
                                  text="Welcome to Connect Four!",\
                                  font=('utopia', 32, 'bold')).grid(row=0)
    self.__moveEntry=Entry(self.__mainWindow,width=10)
    self.__moveEntry.grid(row=1)
    self.__moveEntry.bind('<Return>', self.moveEntryFilled)

    self.__moveButton=Button(self.__mainWindow, text='Move to',\
                             command=self.__moveHere)
    self.__moveButton.grid(row=2)
    self.__moveButton.configure(state='disabled')

    self.__currentPlayerChange=StringVar()
    self.__currentPlayerChange.set('Current Player:X')
    self.__currentPlayerLabel = Label(self.__mainWindow,\
                                      textvariable=self.__currentPlayerChange)\
                                      .grid(row=3)
    
    self.__canvas = Canvas(self.__mainWindow, width=350, height=325)
    self.__canvas.grid(row=4)
    self.__canvas.config(width=50*self.__model.getColumns(),\
                         height=60*self.__model.getRows())
    
    self.drawBoard()  

    self.__newGameButton=Button(self.__mainWindow, text='Start New Game',\
                                command=self.newGame)
    self.__newGameButton.grid(row=5)
      
    mainloop()
  #Event Handler--------------------------------------------------------------
  #draw Board
  def drawBoard(self):
    #print (self.__model.getRows())
    for row in range(1, self.__model.getRows()+1):
      y=row*50
      self.__canvas.create_line(0,y,350,y, fill='blue')
  
    for columns in range(0,self.__model.getColumns()):
      x=columns*50
      self.__canvas.create_line(x,0,x,300, fill='blue')
      self.__canvas.create_text(x+25,325, text=columns,\
                                font=('utopia', 32, 'bold'))
  #Contstruct piece on given column
  def __constructPieces(self):
    col=int(self.__moveEntry.get())
    for rows in range(self.__model.getRows()-1,-1,-1):
      #starts from row 5(bottom row)
      x0=col*50
      y0=rows*50
      x1=(col+1)*50
      y1=(rows+1)*50
      if 'O' == self.__model.board[rows][col]:
        self.__currentPlayerChange.set('Current Player:'+\
                                       self.__model.getTurn())          
        self.__canvas.create_oval(x0,y0,x1,y1, fill='yellow')
      elif 'X' == self.__model.board[rows][col]:
        self.__currentPlayerChange.set('Current Player:'+\
                                       self.__model.getTurn())         
        self.__canvas.create_oval(x0,y0,x1,y1, fill='red')

  #get Entry, resume button            
  def moveEntryFilled(self,event):
    if self.__moveEntry.get():
      self.__moveButton.configure(state='normal')

  def __moveHere(self):
    #drops the piece down into the board and draws it
    if self.isDigit(self.__moveEntry.get()):
      self.__model.dropPiece(int(self.__moveEntry.get()))
      #print (self.__model.board)
      self.__constructPieces()
      winsound.PlaySound("dropsound.wav", winsound.SND_FILENAME)
      if not self.__model.isGame():
        self.__canvas.create_text(175,150, text='Player '+\
                                  self.__model.getTurn() + ' Won!',\
                                  font=('utopia', 32, 'bold'))
        winsound.PlaySound("gamewinner.wav", winsound.SND_FILENAME)
      elif self.__model.isTieGame():
        self.__canvas.create_text(175,150, text=" TIE!",\
                                  font=('utopia', 32, 'bold'))
      self.__moveEntry.delete(0,END)
    else:
      messagebox.showwarning("Invalid move!",\
                             "Please enter a column from 0 to 6!")
      
   
  def newGame(self):
    #clears board and starts a new game
    self.__canvas.delete(ALL)
    self.__model=Connect()
    self.__currentPlayerChange.set('Current Player:X')
    self.drawBoard()
#help methods-----------------------------------------------------------------
  #params: value-value of entry(str)
  def isDigit(self,value):
    if value.isdigit():
      return int(value)>=0 and int(value)<7



ConnectFourGUI()
                                  
                                 

