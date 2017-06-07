from __future__ import division
import random
from random import randint
import time
from PIL import Image
import math
import os
import cv2
import numpy as np


"""
Make the set using data from the image
1. Make a dictionary with image files and their attribute code lists DONE
2. Identify each card of the 12 by comparing it to all stored files in the program. When a match is found, save the attribute code list of the found image 
3. Add the attribute code list to the list of cards
"""

images = {
'[0,0,0,0].jpg': [0,0,0,0], '[0,0,0,1].jpg': [0,0,0,1], '[0,0,0,2].jpg': [0,0,0,2], '[0,0,1,0].jpg': [0,0,1,0], 
'[0,0,1,1].jpg': [0,0,1,1], '[0,0,1,2].jpg': [0,0,1,2], '[0,0,2,0].jpg': [0,0,2,0], '[0,0,2,1].jpg': [0,0,2,1], 
'[0,0,2,2].jpg': [0,0,2,2], '[0,1,0,0].jpg': [0,1,0,0], '[0,1,0,1].jpg': [0,1,0,1], '[0,1,0,2].jpg': [0,1,0,2], 
'[0,1,1,0].jpg': [0,1,1,0], '[0,1,1,1].jpg': [0,1,1,1], '[0,1,1,2].jpg': [0,1,1,2], '[0,1,2,0].jpg': [0,1,2,0], 
'[0,1,2,1].jpg': [0,1,2,1], '[0,1,2,2].jpg': [0,1,2,2], '[0,2,0,0].jpg': [0,2,0,0], '[0,2,0,1].jpg': [0,2,0,1], 
'[0,2,0,2].jpg': [0,2,0,2], '[0,2,1,0].jpg': [0,2,1,0], '[0,2,1,1].jpg': [0,2,1,1], '[0,2,1,2].jpg': [0,2,1,2], 
'[0,2,2,0].jpg': [0,2,2,0], '[0,2,2,1].jpg': [0,2,2,1], '[0,2,2,2].jpg': [0,2,2,2], '[1,0,0,0].jpg': [1,0,0,0], 
'[1,0,0,1].jpg': [1,0,0,1], '[1,0,0,2].jpg': [1,0,0,2], '[1,0,1,0].jpg': [1,0,1,0], '[1,0,1,1].jpg': [1,0,1,1], 
'[1,0,1,2].jpg': [1,0,1,2], '[1,0,2,0].jpg': [1,0,2,0], '[1,0,2,1].jpg': [1,0,2,1], '[1,0,2,2].jpg': [1,0,2,2], 
'[1,1,0,0].jpg': [1,1,0,0], '[1,1,0,1].jpg': [1,1,0,1], '[1,1,0,2].jpg': [1,1,0,2], '[1,1,1,0].jpg': [1,1,1,0], 
'[1,1,1,1].jpg': [1,1,1,1], '[1,1,1,2].jpg': [1,1,1,2], '[1,1,2,0].jpg': [1,1,2,0], '[1,1,2,1].jpg': [1,1,2,1], 
'[1,1,2,2].jpg': [1,1,2,2], '[1,2,0,0].jpg': [1,2,0,0], '[1,2,0,1].jpg': [1,2,0,1], '[1,2,0,2].jpg': [1,2,0,2], 
'[1,2,1,0].jpg': [1,2,1,0], '[1,2,1,1].jpg': [1,2,1,1], '[1,2,1,2].jpg': [1,2,1,2], '[1,2,2,0].jpg': [1,2,2,0], 
'[1,2,2,1].jpg': [1,2,2,1], '[1,2,2,2].jpg': [1,2,2,2], '[2,0,0,0].jpg': [2,0,0,0], '[2,0,0,1].jpg': [2,0,0,1], 
'[2,0,0,2].jpg': [2,0,0,2], '[2,0,1,0].jpg': [2,0,1,0], '[2,0,1,1].jpg': [2,0,1,1], '[2,0,1,2].jpg': [2,0,1,2], 
'[2,0,2,0].jpg': [2,0,2,0], '[2,0,2,1].jpg': [2,0,2,1], '[2,0,2,2].jpg': [2,0,2,2], '[2,1,0,0].jpg': [2,1,0,0], 
'[2,1,0,1].jpg': [2,1,0,1], '[2,1,0,2].jpg': [2,1,0,2], '[2,1,1,0].jpg': [2,1,1,0], '[2,1,1,1].jpg': [2,1,1,1], 
'[2,1,1,2].jpg': [2,1,1,2], '[2,1,2,0].jpg': [2,1,2,0], '[2,1,2,1].jpg': [2,1,2,1], '[2,1,2,2].jpg': [2,1,2,2], 
'[2,2,0,0].jpg': [2,2,0,0], '[2,2,0,1].jpg': [2,2,0,1], '[2,2,0,2].jpg': [2,2,0,2], '[2,2,1,0].jpg': [2,2,1,0], 
'[2,2,1,1].jpg': [2,2,1,1], '[2,2,1,2].jpg': [2,2,1,2], '[2,2,2,0].jpg': [2,2,2,0], '[2,2,2,1].jpg': [2,2,2,1], 
'[2,2,2,2].jpg': [2,2,2,2], 
}


"""slice an image into parts slice_size tall"""
out_directory = "/users/mjortberg521/desktop/"

image_path = "/users/mjortberg521/desktop/set12cards.png"
img = Image.open(image_path)
#width, height = img.size
#verticalSlices = 4 #int(math.ceil(height/450)) #Each card 450 pixels tall
#horizontalSlices = 3 #int(math.ceil(width/700)) #Each card is 700 or so pixels wide
#countVertical = 1

#bounding boxes

bbox1 = (0, 0, 716, 464)
bbox2 = (716, 0, 1432, 464)
bbox3 = (1432, 0, 2148, 464)

bbox4 = (0, 464, 716, 928)
bbox5 = (716, 464, 1432, 928)
bbox6 = (1432, 464, 2148, 928)

bbox7 = (0, 928, 716, 1392)
bbox8 = (716, 928, 1432, 1392)
bbox9 = (1432, 928, 2148, 1392)

bbox10 = (0, 1392, 716, 1856)
bbox11 = (716, 1392, 1432, 1856)
bbox12 = (1432, 1392, 2148, 1856)

card1 = img.crop(bbox1)
card2 = img.crop(bbox2)
card3 = img.crop(bbox3)

card4 = img.crop(bbox4)
card5 = img.crop(bbox5)
card6 = img.crop(bbox6)

card7 = img.crop(bbox7)
card8 = img.crop(bbox8)
card9 = img.crop(bbox9)

card10 = img.crop(bbox10)
card11 = img.crop(bbox11)
card12 = img.crop(bbox12)

card1.save(os.path.join(out_directory, "slice_" + "1.png"))
card2.save(os.path.join(out_directory, "slice_" + "2.png"))
card3.save(os.path.join(out_directory, "slice_" + "3.png"))

card4.save(os.path.join(out_directory, "slice_" + "4.png"))
card5.save(os.path.join(out_directory, "slice_" + "5.png"))
card6.save(os.path.join(out_directory, "slice_" + "6.png"))

card7.save(os.path.join(out_directory, "slice_" + "7.png"))
card8.save(os.path.join(out_directory, "slice_" + "8.png"))
card9.save(os.path.join(out_directory, "slice_" + "9.png"))

card10.save(os.path.join(out_directory, "slice_" + "10.png"))
card11.save(os.path.join(out_directory, "slice_" + "11.png"))
card12.save(os.path.join(out_directory, "slice_" + "12.png"))


img1 = cv2.imread("/users/mjortberg521/desktop/SetCards/ResizedPhotos716x464/[0,0,2,1].jpg") #Template/standard
img2 = cv2.imread("/users/mjortberg521/desktop/slice_8.png") #Test


result = cv2.matchTemplate(img2, img1, cv2.TM_CCOEFF_NORMED)
print result
#cv2.imshow("result",result)

def makeGameCardList():
	gameCards = {}

	for n in range(1,13,1): #from 1 to 12 by 1
		gameCardPath = out_directory+"slice_"+str(n)+".png"
		gameCards[n] = gameCardPath #Adds to the gamecards dict with the number of the game img followed by its path

	return gameCards

def matchCards(): #template will be the one being compared against
	matchedCards = []
	matchIndexDict = {}

	for path in gameCards.values():
		gameCardImg = cv2.imread(path)
		print path

		for key in images:
			templatePath = out_directory+'SetCards/ResizedPhotos716x464/'+key
			print templatePath
			templateImg = cv2.imread(templatePath)

			matchIndex = cv2.matchTemplate(gameCardImg, templateImg, cv2.TM_CCOEFF_NORMED)
			print matchIndex

			matchIndexDict[key] = matchIndex
			#print matchIndexDict

		mostSimilarImg = max(matchIndexDict, key = matchIndexDict.get) #Gets the key corresponding to the maximum similarity index

		seq = images[mostSimilarImg] #Get the most similar template attribute code
		matchedCards.append(seq)

	return matchedCards


"""
def makeManualCards():
	cards = [[1, 2, 1, 2], [1, 1, 0, 2], [2, 1, 1, 1], [0, 2, 0, 1], [2, 2, 1, 1], [0, 0, 1, 2], [2, 0, 1, 1], [0, 1, 0, 0], [0, 2, 1, 1], [1, 0, 1, 0], [1, 0, 1, 1], [0, 1, 1, 2]]
	#ABOVE IS A SET ENTERED FROM A REAL WORLD SCENARIO
	#BELOW IS THE METHOD TO GENERATE A RANDOM SET. 

	for n in range (50): #This allows it to hit 12 cards and remove duplicates for max amount of duplicated (40.5)
		if len(cards)<12:
			T0 = randint(0,2) #Color
			T1 = randint(0,2) #Number
			T2 = randint(0,2) #Shade
			T3 = randint(0,2) #Shape

			seq = [T0, T1, T2, T3]

			if seq not in cards: #if the card has not already been found
				cards.append(seq)

	return cards

cards = makeManualCards()
"""
#########################################################################

gameCards = makeGameCardList() #returns gameCard paths. This must run for matchCards to work
print gameCards

cards = matchCards()
print cards

#print "Cards:", len(cards)

def findCards(): #0, 1, 2, 3 to represent the position of T in the list
	C3 = []

	def decodeAttributes(c): #c is C3 or the card you are working with
		colorDig = c[0] 
		colors = {0: 'green', 1: 'purple', 2: 'red'}
		cardColor = colors[colorDig]

		numberDig = c[1]
		numbers = {0: 'one', 1: 'two', 2: 'three'}
		cardNumber = numbers[numberDig]

		shadeDig = c[2]
		shades = {0: 'open', 1: 'shaded', 2: 'solid'}
		shadeValue = shades[shadeDig]

		shapeDig = c[3]
		shapes = {0: 'round', 1: 'diamond', 2: 'curvy'}
		shapeValue = shapes[shapeDig]

		statement = str(cardNumber) + ' ' + str(shadeValue) + ' ' + str(cardColor) + ' ' + str (shapeValue) #two solid purple diamond card
		return statement

	def chooseCardOne():
		C1 = cards[randint(0,len(cards))] #Select card 1 out of the list of cards
		cards.remove(C1)
		return C1

	C1 = chooseCardOne()
	C1Description = decodeAttributes(C1)
	print 'C1:', C1
	print C1Description

	def chooseCardTwo():
		C2 = cards[randint(0,len(cards))] #Select card 2 out of 11 cards remaining
		cards.remove(C2)
		return C2

	C2 = chooseCardTwo()
	C2Description = decodeAttributes(C2)
	print 'C2:', C2
	print C2Description
   
	#SELECTING THE THIRD CARD
	for n in range (4): 
		if C1[n] == C2[n]:
			i = C1[n]
			C3.append(i)

		else:
			for i in [0,1,2]: 
				if i!=C1[n] and i!=C2[n]:
			 		C3.append(i)

	C3Description = decodeAttributes(C3)
	print "C3:", C3
	print C3Description
	
	if C3 in cards:
		cards.remove(C3)
		print "you need to select", C3Description
		print len(cards), 'cards remaining'
		print(cards)
		print '--------------------------------'
		
	else: 
		print "No card found"
		cards.append(C1)
		cards.append(C2) #Put first two cards back
		print len(cards), 'cards remaining'
		print '--------------------------------'

	#for n in range (30): #This allows it to hit 12 cards and remove duplicates for max amount of duplicated (40.5)
		#while len(cards)<12:
			#T0 = randint(0,2)
			#T1 = randint(0,2)
			#T2 = randint(0,2)
			#T3 = randint(0,2)

			#seq = [T0, T1, T2, T3]

			#if seq not in cards: #if the card has not already been found
				#cards.append(seq)

	return C3

def playGame(): 
	
	C3 = findCards()

trials = 0
while True:
	trials += 1 
	print 'Trial: ',trials
	playGame()

	time.sleep(.25)
