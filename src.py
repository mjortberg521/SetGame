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

##All of these lists were generated using Excel
GreenCards = {
	
'OneGreenShaded': { #All of the cards with one shaded object are in the range 25-45
'[0,0,1,0].jpg': [0,0,1,0], 
'[0,0,1,1].jpg': [0,0,1,1], 
'[0,0,1,2].jpg': [0,0,1,2], 
},

'TwoGreenShaded': { #All of the cards with two shaded objects are in the range 60-80
'[0,1,1,0].jpg': [0,1,1,0], 
'[0,1,1,1].jpg': [0,1,1,1], 
'[0,1,1,2].jpg': [0,1,1,2], 
},

'ThreeGreenShaded': {
'[0,2,1,0].jpg': [0,2,1,0], 
'[0,2,1,1].jpg': [0,2,1,1], 
'[0,2,1,2].jpg': [0,2,1,2], 
},

'GreenOpenAndSolids': {
'[0,0,0,0].jpg': [0,0,0,0], 
'[0,0,0,1].jpg': [0,0,0,1], 
'[0,0,0,2].jpg': [0,0,0,2], 
'[0,0,2,0].jpg': [0,0,2,0], 
'[0,0,2,1].jpg': [0,0,2,1], 
'[0,0,2,2].jpg': [0,0,2,2], 
'[0,1,0,0].jpg': [0,1,0,0], 
'[0,1,0,1].jpg': [0,1,0,1], 
'[0,1,0,2].jpg': [0,1,0,2], 
'[0,1,2,0].jpg': [0,1,2,0], 
'[0,1,2,1].jpg': [0,1,2,1], 
'[0,1,2,2].jpg': [0,1,2,2], 
'[0,2,0,0].jpg': [0,2,0,0], 
'[0,2,0,1].jpg': [0,2,0,1], 
'[0,2,0,2].jpg': [0,2,0,2], 
'[0,2,2,0].jpg': [0,2,2,0], 
'[0,2,2,1].jpg': [0,2,2,1], 
'[0,2,2,2].jpg': [0,2,2,2], 
}
}

PurpleCards = {

'OnePurpleShaded': {
'[1,0,1,0].jpg': [1,0,1,0], 
'[1,0,1,1].jpg': [1,0,1,1], 
'[1,0,1,2].jpg': [1,0,1,2], 
},

'TwoPurpleShaded': {
'[1,1,1,0].jpg': [1,1,1,0], 
'[1,1,1,1].jpg': [1,1,1,1], 
'[1,1,1,2].jpg': [1,1,1,2], 
},

'ThreePurpleShaded': {
'[1,2,1,0].jpg': [1,2,1,0], 
'[1,2,1,1].jpg': [1,2,1,1], 
'[1,2,1,2].jpg': [1,2,1,2], 
},

'PurpleOpenAndSolids': {
'[1,0,0,0].jpg': [1,0,0,0], 
'[1,0,0,1].jpg': [1,0,0,1], 
'[1,0,0,2].jpg': [1,0,0,2], 
'[1,0,2,0].jpg': [1,0,2,0], 
'[1,0,2,1].jpg': [1,0,2,1], 
'[1,0,2,2].jpg': [1,0,2,2], 
'[1,1,0,0].jpg': [1,1,0,0], 
'[1,1,0,1].jpg': [1,1,0,1], 
'[1,1,0,2].jpg': [1,1,0,2], 
'[1,1,2,0].jpg': [1,1,2,0], 
'[1,1,2,1].jpg': [1,1,2,1], 
'[1,1,2,2].jpg': [1,1,2,2], 
'[1,2,0,0].jpg': [1,2,0,0], 
'[1,2,0,1].jpg': [1,2,0,1], 
'[1,2,0,2].jpg': [1,2,0,2], 
'[1,2,2,0].jpg': [1,2,2,0], 
'[1,2,2,1].jpg': [1,2,2,1], 
'[1,2,2,2].jpg': [1,2,2,2], 
}
}

RedCards = {

'OneRedShaded': {
'[2,0,1,0].jpg': [2,0,1,0], 
'[2,0,1,1].jpg': [2,0,1,1], 
'[2,0,1,2].jpg': [2,0,1,2], 
},

'TwoRedShaded': {
'[2,1,1,0].jpg': [2,1,1,0], 
'[2,1,1,1].jpg': [2,1,1,1], 
'[2,1,1,2].jpg': [2,1,1,2], 
},

'ThreeRedShaded': {
'[2,2,1,0].jpg': [2,2,1,0], 
'[2,2,1,1].jpg': [2,2,1,1], 
'[2,2,1,2].jpg': [2,2,1,2], 
},

'RedOpenAndSolids': {
'[2,0,0,0].jpg': [2,0,0,0], 
'[2,0,0,1].jpg': [2,0,0,1], 
'[2,0,0,2].jpg': [2,0,0,2], 
'[2,0,2,0].jpg': [2,0,2,0], 
'[2,0,2,1].jpg': [2,0,2,1], 
'[2,0,2,2].jpg': [2,0,2,2], 
'[2,1,0,0].jpg': [2,1,0,0], 
'[2,1,0,1].jpg': [2,1,0,1], 
'[2,1,0,2].jpg': [2,1,0,2], 
'[2,1,2,0].jpg': [2,1,2,0], 
'[2,1,2,1].jpg': [2,1,2,1], 
'[2,1,2,2].jpg': [2,1,2,2], 
'[2,2,0,0].jpg': [2,2,0,0], 
'[2,2,0,1].jpg': [2,2,0,1], 
'[2,2,0,2].jpg': [2,2,0,2], 
'[2,2,2,0].jpg': [2,2,2,0], 
'[2,2,2,1].jpg': [2,2,2,1], 
'[2,2,2,2].jpg': [2,2,2,2], 
}
}

out_directory = "/users/mjortberg521/desktop/"

image_path = "/users/mjortberg521/desktop/set12cards.png"
img = Image.open(image_path)
#width, height = img.size
#verticalSlices = 4 #int(math.ceil(height/450)) #Each card 450 pixels tall
#horizontalSlices = 3 #int(math.ceil(width/700)) #Each card is 700 or so pixels wide
#countVertical = 1

#bounding boxes
bbox1=(50,50,666,414)
bbox2=(766,50,1382,414)
bbox3=(1482,50,2098,414)

bbox4=(50,514,666,878)
bbox5=(766,514,1382,878)
bbox6=(1482,514,2098,878)

bbox7=(50,978,666,1342)
bbox8=(766,978,1382,1342)
bbox9=(1482,978,2098,1342)

bbox10=(50,1442,666,1806)
bbox11=(766,1442,1382,1806)
bbox12=(1482,1442,2098,1806)

#Crop the game image to the just the cards and save all 12 to out_directory
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

card1.save(os.path.join(out_directory, "slice_" + "1.jpg"))
card2.save(os.path.join(out_directory, "slice_" + "2.jpg"))
card3.save(os.path.join(out_directory, "slice_" + "3.jpg"))

card4.save(os.path.join(out_directory, "slice_" + "4.jpg"))
card5.save(os.path.join(out_directory, "slice_" + "5.jpg"))
card6.save(os.path.join(out_directory, "slice_" + "6.jpg"))

card7.save(os.path.join(out_directory, "slice_" + "7.jpg"))
card8.save(os.path.join(out_directory, "slice_" + "8.jpg"))
card9.save(os.path.join(out_directory, "slice_" + "9.jpg"))

card10.save(os.path.join(out_directory, "slice_" + "10.jpg"))
card11.save(os.path.join(out_directory, "slice_" + "11.jpg"))
card12.save(os.path.join(out_directory, "slice_" + "12.jpg"))

def makeGameCardList():
	gameCards = {}
	#Make a dict with all of the game card paths

	for n in range(1,13,1): #from 1 to 12 by 1
		gameCardPath = out_directory+"slice_"+str(n)+".jpg"
		gameCards[n] = gameCardPath #Adds to the gamecards dict with the number of the game img followed by its path

	return gameCards

def findColors(path):
	image = cv2.imread(path)

	redboundaries = [
	([14, 15, 215], [60, 60, 255]) ####RED
	]

	purpleboundaries = [
		([100, 20, 75], [130, 60, 150]) ####PURPLE
	]

	greenboundaries = [
		([60, 170, 25], [80, 200, 40]) ####GREEN 
	]

	for (lower, upper) in redboundaries:
		# create NumPy arrays from the boundaries
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")
	 
		# find the colors within the specified boundaries and apply the mask
		mask = cv2.inRange(image, lower, upper)
		redoutput = cv2.bitwise_and(image, image, mask = mask)

		if np.count_nonzero(mask) > 0:
			x = 2 #RED
			#print "red found"

	for (lower, upper) in purpleboundaries:
		# create NumPy arrays from the boundaries
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")
	 
		# find the colors within the specified boundaries and apply the mask
		mask = cv2.inRange(image, lower, upper)
		purpleoutput = cv2.bitwise_and(image, image, mask = mask)

		if np.count_nonzero(mask) > 0:
			#print "purple found"
			x = 1 #PURPLE

	for (lower, upper) in greenboundaries:
		# create NumPy arrays from the boundaries
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")
	 
		# find the colors within the specified boundaries and apply the mask
		mask = cv2.inRange(image, lower, upper)
		greenoutput = cv2.bitwise_and(image, image, mask = mask)

		if np.count_nonzero(mask) > 0:
			#print "green found"
			x = 0 #GREEN

	return x

	#cv2.imshow("images", np.hstack([image, redoutput, purpleoutput, greenoutput]))
	#cv2.waitKey(0)

def findContours(path):
	im = cv2.imread(path)
	imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

	ret, thresh = cv2.threshold(imgray, 180, 255, 0) ###############THESE VALUES ARE FOR THE SHADED DIAMOND################
	im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	#cv2.drawContours(im2, contours, -1, (0,255,0), 3)

	#cv2.imshow("im2", im2)
	y = len(contours)

	#print contours
	return y

def templateMatch(cardDict, gameCardPath): #path is the path of the gameCardImg
	matchIndexDict = {}

	for key in cardDict: #Compare the current game img against all  templates in cardDict to find the most similar
		templatePath = out_directory+'SetCards/ResizedPhotos716x464/'+key
		templateImg = cv2.imread(templatePath)
		gameCardImg = cv2.imread(gameCardPath)

		matchIndex = cv2.matchTemplate(gameCardImg, templateImg, cv2.TM_CCOEFF_NORMED)
		min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(matchIndex)

		matchIndexDict[key] = max_val #Add the template name and its similarity score to the dict

	return matchIndexDict

def matchCards(): #template will be the one being compared against
	matchedCards = []
	matchIndexDict = {}

	for path in gameCards.values(): #For each of the paths in the gameCards dict, load the image
		gameCardImg = cv2.imread(path)

		x = findColors(path)
		print x
		y = findContours(path)
		print y

		if x == 0: #Green
			if 25<y<58: #If it is one shaded card

				matchIndexDict = templateMatch(GreenCards['OneGreenShaded'], path) #Generate a dictionary of the match index vals
				mostSimilarImg = max(matchIndexDict, key = matchIndexDict.get) #Gets the key corresponding to the maximum similarity index

				seq = GreenCards['OneGreenShaded'][mostSimilarImg] #Get the most similar template attribute code
				matchedCards.append(seq)

			elif 60<y<80: 
				matchIndexDict = templateMatch(GreenCards['TwoGreenShaded'], path) #Generate a dictionary of the match index vals
				mostSimilarImg = max(matchIndexDict, key = matchIndexDict.get) #Gets the key corresponding to the maximum similarity index

				seq = GreenCards['TwoGreenShaded'][mostSimilarImg] #Get the most similar template attribute code
				matchedCards.append(seq)

			elif 95<y<120:
				matchIndexDict = templateMatch(GreenCards['ThreeGreenShaded'], path) #Generate a dictionary of the match index vals
				mostSimilarImg = max(matchIndexDict, key = matchIndexDict.get) #Gets the key corresponding to the maximum similarity index

				seq = GreenCards['ThreeGreenShaded'][mostSimilarImg] #Get the most similar template attribute code
				matchedCards.append(seq)

			else:
				matchIndexDict = templateMatch(GreenCards['GreenOpenAndSolids'], path) #Generate a dictionary of the match index vals
				mostSimilarImg = max(matchIndexDict, key = matchIndexDict.get) #Gets the key corresponding to the maximum similarity index

				seq = GreenCards['GreenOpenAndSolids'][mostSimilarImg] #Get the most similar template attribute code
				matchedCards.append(seq)


		if x == 1: #Purple
			if 25<y<58: #If it is one shaded card
				matchIndexDict = templateMatch(PurpleCards['OnePurpleShaded'], path) #Generate a dictionary of the match index vals
				mostSimilarImg = max(matchIndexDict, key = matchIndexDict.get) #Gets the key corresponding to the maximum similarity index

				seq = PurpleCards['OnePurpleShaded'][mostSimilarImg] #Get the most similar template attribute code
				matchedCards.append(seq)

			elif 60<y<80: 
				matchIndexDict = templateMatch(PurpleCards['TwoPurpleShaded'], path) #Generate a dictionary of the match index vals
				mostSimilarImg = max(matchIndexDict, key = matchIndexDict.get) #Gets the key corresponding to the maximum similarity index

				seq = PurpleCards['TwoPurpleShaded'][mostSimilarImg] #Get the most similar template attribute code
				matchedCards.append(seq)

			elif 95<y<120:
				matchIndexDict = templateMatch(PurpleCards['ThreePurpleShaded'], path) #Generate a dictionary of the match index vals
				mostSimilarImg = max(matchIndexDict, key = matchIndexDict.get) #Gets the key corresponding to the maximum similarity index

				seq = PurpleCards['ThreePurpleShaded'][mostSimilarImg] #Get the most similar template attribute code
				matchedCards.append(seq)

			else:
				matchIndexDict = templateMatch(PurpleCards['PurpleOpenAndSolids'], path) #Generate a dictionary of the match index vals
				mostSimilarImg = max(matchIndexDict, key = matchIndexDict.get) #Gets the key corresponding to the maximum similarity index

				seq = PurpleCards['PurpleOpenAndSolids'][mostSimilarImg] #Get the most similar template attribute code
				matchedCards.append(seq)

		if x ==2: #Red
			if 25<y<58: #If it is one shaded card
				matchIndexDict = templateMatch(RedCards['OneRedShaded'], path) #Generate a dictionary of the match index vals
				mostSimilarImg = max(matchIndexDict, key = matchIndexDict.get) #Gets the key corresponding to the maximum similarity index

				seq = RedCards['OneRedShaded'][mostSimilarImg] #Get the most similar template attribute code
				matchedCards.append(seq)

			elif 60<y<80: 
				matchIndexDict = templateMatch(RedCards['TwoRedShaded'], path) #Generate a dictionary of the match index vals
				mostSimilarImg = max(matchIndexDict, key = matchIndexDict.get) #Gets the key corresponding to the maximum similarity index

				seq = RedCards['TwoRedShaded'][mostSimilarImg] #Get the most similar template attribute code
				matchedCards.append(seq)

			elif 95<y<120:
				matchIndexDict = templateMatch(RedCards['ThreeRedShaded'], path) 
				mostSimilarImg = max(matchIndexDict, key = matchIndexDict.get) 

				seq = RedCards['ThreeRedShaded'][mostSimilarImg] 
				matchedCards.append(seq)

			else:
				matchIndexDict = templateMatch(RedCards['RedOpenAndSolids'], path) 
				mostSimilarImg = max(matchIndexDict, key = matchIndexDict.get) 

				seq = RedCards['RedOpenAndSolids'][mostSimilarImg] 
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
