import random
import curses
import sys
import random

class player():
	def __init__(self):
		self.name='Player_1'
		self.life=100
		self.xpos=4
		self.ypos=4

class enemy():
	def __init__(self):
		self.name='Enemy'+str(random.randrange(1,10))
		self.life=96
		self.xpos=random.randrange(2,49)
		self.ypos=random.randrange(2,14)
		self.onenemy=0

class environment():
	def __init__(self):
		self.screen1=curses.initscr()
		self.error=0
		self.screen = curses.newwin(20,60,1,1)
		curses.start_color()
		curses.noecho()
		curses.cbreak()
		self.screen.keypad(True)
		self.p=[]
		self.pl=player()
		self.playerpoint=0
		self.numenemies=0
		for i in range(2,49):
			for j in range(2,14):
				try:
					self.screen.addch(j,i, ord(' '))
				except curses.error:
					pass
		self.screen.refresh()
		self.pointandlife()
		self.drawpadold()
		self.drawpadnew()
	
	def startgame(self):
		while True:
			p=self.initscreen()
			if p==1:
				self.callonexit()
				break
			elif p==2:
				self.playing()
				self.endscreen()
			else:
				self.screen.addstr(15,3,"Invalid Option Entered")
					
	def playing(self):
		self.numenemies=0
		self.playerpoint=0
		for i in range(0,59):
			for j in range(0,19):
				try:
					self.screen.addch(j,i, ord(' '))
				except curses.error:
					pass
		for i in range(1,50):
			try:
				self.screen.addch(1,i, ord('*'))
			except curses.error:
				pass
		for i in range(1,50):
			try:
				self.screen.addch(15,i, ord('*'))
			except curses.error:
				pass
		for j in range(1,15):
			try:
				self.screen.addch(j,1, ord('*'))
			except curses.error:
				pass
		for j in range(1,16):
			try:
				self.screen.addch(j,50, ord('*'))
			except curses.error:
				pass
		self.screen.addstr(0,3,"Simple Python Game")
		try:
			while True:
				char = self.screen.getch()
				self.drawpadold()
				if char == ord('q'):
					break
				elif char == curses.KEY_RIGHT:
					self.pl.xpos=self.pl.xpos+1
					if self.pl.xpos>49:
						self.pl.xpos=49
				elif char == curses.KEY_LEFT:
					self.pl.xpos=self.pl.xpos-1
					if self.pl.xpos<2:
						self.pl.xpos=2
				elif char == curses.KEY_UP:
					self.pl.ypos=self.pl.ypos-1
					if self.pl.ypos<2:
						self.pl.ypos=2
				elif char == curses.KEY_DOWN:
					self.pl.ypos=self.pl.ypos+1
					if self.pl.ypos>14:
						self.pl.ypos=14
				q=self.pointandlife()
				if q==1:
					break
				self.drawpadnew()
		except curses.error:
			self.error=1
    
	def pointandlife(self):
		for i in self.p:
			if i.xpos==self.pl.xpos and i.ypos==self.pl.ypos:
				self.playerpoint=self.playerpoint-1
				self.pl.life=self.pl.life-12
				i.onenemy=1
				if self.pl.life==0:
					break
				i.life=i.life-12
				if i.life==0:
					self.playerpoint=self.playerpoint+40
					self.pl.life=self.pl.life+96
					self.p.remove(i)
					self.numenemies=self.numenemies+1
					if not self.p:
						return 1
			else:
				i.onenemy=0
		if self.pl.life<=0:
			self.pl.life=100
			self.playerpoint=self.playerpoint-10
		self.screen.addstr(17,0,"           ")
		self.screen.addstr(17,0,"Points: "+str(self.playerpoint))
		self.screen.addstr(17,12,"                ")
		self.screen.addstr(17,12,"Player Life: "+str(self.pl.life))
		return 0
						
	def drawpadnew(self):
		try:
			self.screen.addch(self.pl.ypos,self.pl.xpos,ord('@'))
		except curses.error:
			pass
		for i in self.p:
			if i.onenemy==1:
				try:
					self.screen.addch(i.ypos,i.xpos,ord('%'))
				except curses.error:
					pass
			else:
				try:
					self.screen.addch(i.ypos,i.xpos,ord('#'))
				except curses.error:
					pass
		self.screen.refresh()
		
	def drawpadold(self):
		try:
			self.screen.addch(self.pl.ypos,self.pl.xpos,ord(' '))
		except curses.error:
			pass
	
	def initscreen(self):
		for i in range(0,59):
			for j in range(0,19):
				try:
					self.screen.addch(j,i, ord(' '))
				except curses.error:
					pass
		self.screen.addstr(5,3,"Simple Python Game")
		self.a=25
		while self.a>20:
			curses.echo()
			self.screen.addstr(8,3,"Welcome")
			self.screen.addstr(10,3,"Enter Number of Enemies [or q to quit]: ")
			str1=self.screen.getstr()
			curses.noecho()
			if 'q' not in str1:
				self.a=int(str1)
			else:
				return 1
		for i in range(0,self.a):
			self.en=enemy()
			self.p.append(self.en)
		self.screen.addstr(12,3,"To start press \'s\' and then any key")
		self.screen.addstr(13,3,"To quit press \'q\'")
		char = self.screen.getch()
		if char == ord('q'):
			return 1
		elif char==ord('s'):
			return 2
		else:
			return 3
	
	def endscreen(self):
		for i in range(0,59):
			for j in range(0,19):
				try:
					self.screen.addch(j,i, ord(' '))
				except curses.error:
					pass
		self.screen.addstr(5,3,"Simple Python Game")
		self.screen.addstr(8,3,"Player Statistics")
		self.screen.addstr(10,3,"Life: "+str(self.pl.life))
		self.screen.addstr(11,3,"Points: "+str(self.playerpoint))
		self.screen.addstr(12,3,"Enemies killed: "+str(self.numenemies))
		self.screen.addstr(15,3,"Press \'c\' to continue")
		char=ord('e')
		while char!=ord('c'):
			char = self.screen.getch()
			
		
	def callonexit(self):
		curses.nocbreak()
		self.screen.keypad(0)
		curses.echo()
		curses.endwin()


if __name__=="__main__":
	env=environment()
	env.startgame()
