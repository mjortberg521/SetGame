from __future__ import division
import random
from random import randint
import time
import PIL
from PIL import Image
import math
import os
import cv2
import numpy as np
import imutils

##To run this program, OpenCV must be installed##

directory = "/users/mjortberg521/desktop/" #Replace this line with the file path to the directory that you are using
template_file_path = directory+"SetCards/resizedphotos716x464/" #Replace this line with the file path to the folder of template images downloaded from GitHub

twelve_cards_image_name = "gameImg8.jpeg" #Replace this with the name of the image containing the 12 card SET you want to solve. 
										 #The image must be cropped with 3 cards going across horizontally and 4 cards going down vertically
resultsPath = directory+"SET_game_results.jpg"

twelve_cards_image_path = directory + twelve_cards_image_name
twelve_cards_image = cv2.imread(twelve_cards_image_path)

##All of these lists were generated using Excel
GreenCards = {

'GreenShadedAndThreeOpen': { #All of the cards with two shaded objects are in the range 60-80
'[0,1,1,0].jpg': [0,1,1,0], 
'[0,1,1,1].jpg': [0,1,1,1], 
'[0,1,1,2].jpg': [0,1,1,2], 
'[0,0,1,0].jpg': [0,0,1,0],
'[0,0,1,1].jpg': [0,0,1,1], 
'[0,0,1,2].jpg': [0,0,1,2],
'[0,2,0,0].jpg': [0,2,0,0], #Begin 3 open
'[0,2,0,1].jpg': [0,2,0,1], 
'[0,2,0,2].jpg': [0,2,0,2]
},

'ThreeGreenShaded': {
'[0,2,1,0].jpg': [0,2,1,0], 
'[0,2,1,1].jpg': [0,2,1,1], 
'[0,2,1,2].jpg': [0,2,1,2],
'[0,1,1,0].jpg': [0,1,1,0], 
'[0,1,1,1].jpg': [0,1,1,1], 
'[0,1,1,2].jpg': [0,1,1,2]
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
'[0,2,2,2].jpg': [0,2,2,2] ###Start one shaded below
#'[0,0,1,0].jpg': [0,0,1,0], 
#'[0,0,1,1].jpg': [0,0,1,1], 
#'[0,0,1,2].jpg': [0,0,1,2], 
}
}

PurpleCards = {

'PurpleShadedAndThreeOpen': {
'[1,1,1,0].jpg': [1,1,1,0], 
'[1,1,1,1].jpg': [1,1,1,1], 
'[1,1,1,2].jpg': [1,1,1,2], 
'[1,0,1,0].jpg': [1,0,1,0], 
'[1,0,1,1].jpg': [1,0,1,1], 
'[1,0,1,2].jpg': [1,0,1,2],
'[1,2,0,0].jpg': [1,2,0,0], #Begin 3 open
'[1,2,0,1].jpg': [1,2,0,1], 
'[1,2,0,2].jpg': [1,2,0,2]
},

'ThreePurpleShaded': {
'[1,2,1,0].jpg': [1,2,1,0], 
'[1,2,1,1].jpg': [1,2,1,1], 
'[1,2,1,2].jpg': [1,2,1,2],
'[1,1,1,0].jpg': [1,1,1,0], 
'[1,1,1,1].jpg': [1,1,1,1], 
'[1,1,1,2].jpg': [1,1,1,2]
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
'[1,2,2,2].jpg': [1,2,2,2] ###Begin one shaded below
#'[1,0,1,0].jpg': [1,0,1,0], 
#'[1,0,1,1].jpg': [1,0,1,1], 
#'[1,0,1,2].jpg': [1,0,1,2]
}
}

RedCards = {

'RedShadedAndThreeOpen': {
'[2,1,1,0].jpg': [2,1,1,0], 
'[2,1,1,1].jpg': [2,1,1,1], 
'[2,1,1,2].jpg': [2,1,1,2], 
'[2,0,1,0].jpg': [2,0,1,0], 
'[2,0,1,1].jpg': [2,0,1,1], 
'[2,0,1,2].jpg': [2,0,1,2],
'[2,2,0,0].jpg': [2,2,0,0], #Begin 3 open
'[2,2,0,1].jpg': [2,2,0,1], 
'[2,2,0,2].jpg': [2,2,0,2]
},

'ThreeRedShaded': {
'[2,2,1,0].jpg': [2,2,1,0], 
'[2,2,1,1].jpg': [2,2,1,1], 
'[2,2,1,2].jpg': [2,2,1,2],
'[2,1,1,0].jpg': [2,1,1,0], 
'[2,1,1,1].jpg': [2,1,1,1], 
'[2,1,1,2].jpg': [2,1,1,2]
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
'[2,2,2,2].jpg': [2,2,2,2] ###Begin one shaded below
#'[2,0,1,0].jpg': [2,0,1,0], 
#'[2,0,1,1].jpg': [2,0,1,1], 
#'[2,0,1,2].jpg': [2,0,1,2]
}
}

img = Image.open(twelve_cards_image_path) #Open the image from the path entered at the beginning of the program
img = img.resize((2148, 1856), PIL.Image.ANTIALIAS) #Resize this image to make it crop into nice boxes for each card well

img.save(twelve_cards_image_path, 'JPEG') #save the newly resized image at twelve_cards_image_path, replacing it

twelve_cards_image = cv2.imread(twelve_cards_image_path) #read the newly resized image for use with the openCV functions

####FIND THE BOUNDING BOXES####

bboxesNew = []

gray = cv2.cvtColor(twelve_cards_image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5,5), 0)
thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)[1] #Creates img of shapes in white fg on black bg

#Find contours
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #Returns the set of outlines for the white shapes
cnts = cnts[0] if imutils.is_cv2() else cnts[1] #Gets the appropriate val based on cv version

displayBboxesP1 = [] #dict for first point of bounding rect
displayBboxesP2 = []

for c in cnts:
	if cv2.contourArea(c) > 1000: #Only get the large contours
		cv2.drawContours(twelve_cards_image, [c], -1, (0, 255, 0), 2) #Outline each contour in green

		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.04*peri, True)

		if len(approx) == 4: #only get the rectangles
			(x, y, w, h) = cv2.boundingRect(approx) #find the bounding box
			bboxesNew.append((x,y,w+x,h+y)) #Add coordinates to new list

			displayBboxesP1.append((x,y))  #Add the 1st pt
			displayBboxesP2.append((w+x,y+h))  #Add 2nd point

print "Card locations: ", bboxesNew
#Crop the game image to the just the cards and save all 12 to directory
def cropBBoxes(): 
	for n in range(0,12,1):
		cardName = "card" + str(n)
		cardName = img.crop(bboxesNew[n]) #crop the original image down to the individual card bbox

		cardName = cardName.resize((716,464)) #resize cropped card to correct dimensions

		cardName.save(os.path.join(directory, "setslices/slice_" + str(n) + ".jpg"))

cropBBoxes()

def makeGameCardList():
	gameCards = {}
	#Make a dict with all of the game card paths from the cropped images

	for n in range(0,12,1): #from 1 to 12 by 1
		gameCardPath = directory+"setslices/slice_"+str(n)+".jpg"
		gameCards[n] = gameCardPath #Adds to the gamecards dict with key=n and value=gameCardPath

	return gameCards

def findColors(path):
	
	image = cv2.imread(path)

	redboundaries = [
	([14, 15, 150], [95, 90, 255]) ####RED
	]

	purpleboundaries = [
	([60, 20, 50], [130, 65, 150]) ####PURPLE
	]

	greenboundaries = [
	([60, 120, 30], [120, 255, 100]) ####GREEN 
	]

	x = None #Put these here to prevent the "ref before assignment error"
	color = None

	for (lower, upper) in redboundaries:
		# create NumPy arrays from the boundaries
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")
	 
		# find the colors within the specified boundaries and apply the mask
		redMask = cv2.inRange(image, lower, upper)
		redoutput = cv2.bitwise_and(image, image, mask = redMask)

		x = np.count_nonzero(redMask)
			
	for (lower, upper) in purpleboundaries:
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")
	 
		# find the colors within the specified boundaries and apply the mask
		purpleMask = cv2.inRange(image, lower, upper)
		purpleoutput = cv2.bitwise_and(image, image, mask = purpleMask)

		y = np.count_nonzero(purpleMask) 

	for (lower, upper) in greenboundaries:
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")
	 
		# find the colors within the specified boundaries and apply the mask
		greenMask = cv2.inRange(image, lower, upper)
		greenoutput = cv2.bitwise_and(image, image, mask = greenMask)

		z = np.count_nonzero(greenMask) 


	maximum = max(x, y, z) #Find the maximum of the red, purple, green masks 

	if maximum == x: 
		c = 2
		color = 'Red'

	elif maximum == y: 
		c = 0
		color = 'Purple'

	elif maximum == z: 
		c = 1
		color = 'Green'


	return color

def findContours(path):
	im = cv2.imread(path)
	imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	#blurred = cv2.GaussianBlur(imgray, (7,7), 0)

	edged = cv2.Canny(imgray, 100, 200) ####May change to blurred
	y = np.count_nonzero(edged)

	return y

def templateMatch(cardDict, gameCardPath): 
	matchIndexDict = {}

	#For dictionary keys in a for loop, use "for n in d"
	#For dictionary values in a for loop, use "for n in d.values"

	for key in cardDict: #Compare the current game img against all templates in cardDict
		templatePath = directory+'SetCards/ResizedPhotos716x464/'+key #Templates must be the resized ones because for matchTemplate to work, they have to be the same size as the gameCardPath
		#The key of cardDict looks like "[0,0,0,0].jpg"		
		templateImg = cv2.imread(templatePath)
		gameCardImg = cv2.imread(gameCardPath)

		matchIndex = cv2.matchTemplate(gameCardImg, templateImg, cv2.TM_CCOEFF_NORMED) #matchTemplate returns an array ## args = (imgpath, templatepath, method)
		min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(matchIndex) #Gets the min value, max value, min position, and max position

		matchIndexDict[key] = max_val #Add the template name and its similarity score (how similar it is to the gameCardImg) to the dict

		#Return a dictionary with key = template file name (e.g. "[0,0,0,0].jpg") and value = similarity score

	return matchIndexDict


def matchCards(): #Method to find the filename (and thus attribute code) of the cards in the image
	matchedCards = [] #Initialize empty list that will contain a list of cards later (e.g. [0,0,0,0], [1,0,1,0], [2,0,0,0])
	matchIndexDict = {}
	
	#MakeGameCards is called before matchCards
	#You need a list of all the gameCard paths to run the color, contour, and comparison functions
	for path in gameCards.values(): #For each of the paths in the gameCards dict
		print path
		gameCardImg = cv2.imread(path)

		color = findColors(path)

		print 'Color:', color

		y = findContours(path)
		print 'Contours:',y

		if color == "Green": #Green
			if 5000<y<16000: #If it is a shaded card (y is the number of contours)
				#This will template match the current gameCard against all cards in the specific color/shade dict

				matchIndexDict = templateMatch(GreenCards['GreenShadedAndThreeOpen'], path) #Generate a dictionary with key=template name and value=similarity score when comparing the currect green, 1 shaded shape card against all possible green 1 shape shaded
				mostSimilarImg = max(matchIndexDict, key = matchIndexDict.get) #Gets the key corresponding to the card with the maximum similarity index-this is the template name (e.g. "[0,0,0,0].jpg")
				print matchIndexDict
				print mostSimilarImg
				print '--------------------------------'

				seq = GreenCards['GreenShadedAndThreeOpen'][mostSimilarImg] #Get the most similar template attribute code using the key mostSimilarImg (file name) from matchIndexDict
				matchedCards.append(seq)

				del GreenCards['GreenShadedAndThreeOpen'][mostSimilarImg] #After the most similar img is found, remove from dict to prevent repeats

				if mostSimilarImg in GreenCards['GreenOpenAndSolids']: #If it's a one shaded card, remove all instances
					del GreenCards['GreenOpenAndSolids'][mostSimilarImg]
			
			elif y>16000:
				matchIndexDict = templateMatch(GreenCards['ThreeGreenShaded'], path) #Generate a dictionary with key=template name and value=similarity score when comparing the currect green, 1 shaded shape card against all possible green 1 shape shaded
				mostSimilarImg = max(matchIndexDict, key = matchIndexDict.get) #Gets the key corresponding to the card with the maximum similarity index-this is the template name (e.g. "[0,0,0,0].jpg")
				print matchIndexDict
				print mostSimilarImg
				print '--------------------------------'

				seq = GreenCards['ThreeGreenShaded'][mostSimilarImg] #Get the most similar template attribute code using the key mostSimilarImg (file name) from matchIndexDict
				matchedCards.append(seq)

				del GreenCards['ThreeGreenShaded'][mostSimilarImg] #After the most similar img is found, remove from dict to prevent repeats

			else:
				matchIndexDict = templateMatch(GreenCards['GreenOpenAndSolids'], path) 
				mostSimilarImg = max(matchIndexDict, key = matchIndexDict.get) 
				print matchIndexDict
				print mostSimilarImg
				print '--------------------------------'

				seq = GreenCards['GreenOpenAndSolids'][mostSimilarImg] 
				matchedCards.append(seq)

				del GreenCards['GreenOpenAndSolids'][mostSimilarImg]

				if mostSimilarImg in GreenCards['GreenShadedAndThreeOpen']: #If it's a one shaded card, remove all instances
					del GreenCards['GreenShadedAndThreeOpen'][mostSimilarImg]


		if color == "Purple": #Purple
			if 5000<y<16000: 
				matchIndexDict = templateMatch(PurpleCards['PurpleShadedAndThreeOpen'], path) 
				mostSimilarImg = max(matchIndexDict, key = matchIndexDict.get) 
				print matchIndexDict
				print mostSimilarImg
				print '--------------------------------'

				seq = PurpleCards['PurpleShadedAndThreeOpen'][mostSimilarImg] 
				matchedCards.append(seq)

				del PurpleCards['PurpleShadedAndThreeOpen'][mostSimilarImg]

				if mostSimilarImg in PurpleCards['PurpleOpenAndSolids']:
					del PurpleCards['PurpleOpenAndSolids'][mostSimilarImg]

			elif y>16000:
				matchIndexDict = templateMatch(PurpleCards['ThreePurpleShaded'], path) 
				mostSimilarImg = max(matchIndexDict, key = matchIndexDict.get) 
				print matchIndexDict
				print mostSimilarImg
				print '--------------------------------'

				seq = PurpleCards['ThreePurpleShaded'][mostSimilarImg] 
				matchedCards.append(seq)

				del PurpleCards['ThreePurpleShaded'][mostSimilarImg]

			else:
				matchIndexDict = templateMatch(PurpleCards['PurpleOpenAndSolids'], path)
				mostSimilarImg = max(matchIndexDict, key = matchIndexDict.get) 
				print matchIndexDict
				print mostSimilarImg
				print '--------------------------------'

				seq = PurpleCards['PurpleOpenAndSolids'][mostSimilarImg] 
				matchedCards.append(seq)

				del PurpleCards['PurpleOpenAndSolids'][mostSimilarImg]

				if mostSimilarImg in PurpleCards['PurpleShadedAndThreeOpen']:
					del PurpleCards['PurpleShadedAndThreeOpen'][mostSimilarImg]


		if color == "Red": #Red
			if 5000<y<16000: 
				matchIndexDict = templateMatch(RedCards['RedShadedAndThreeOpen'], path)
				mostSimilarImg = max(matchIndexDict, key = matchIndexDict.get)
				print matchIndexDict
				print mostSimilarImg
				print '--------------------------------'

				seq = RedCards['RedShadedAndThreeOpen'][mostSimilarImg] 
				matchedCards.append(seq)

				del RedCards['RedShadedAndThreeOpen'][mostSimilarImg] 

				if mostSimilarImg in RedCards['RedOpenAndSolids']:
					del RedCards['RedOpenAndSolids'][mostSimilarImg]

			elif y>16000:
				matchIndexDict = templateMatch(RedCards['ThreeRedShaded'], path)
				mostSimilarImg = max(matchIndexDict, key = matchIndexDict.get)
				print matchIndexDict
				print mostSimilarImg
				print '--------------------------------'

				seq = RedCards['ThreeRedShaded'][mostSimilarImg] 
				matchedCards.append(seq)

				del RedCards['ThreeRedShaded'][mostSimilarImg] 

			else:
				matchIndexDict = templateMatch(RedCards['RedOpenAndSolids'], path) 
				mostSimilarImg = max(matchIndexDict, key = matchIndexDict.get) 
				print matchIndexDict
				print mostSimilarImg
				print '--------------------------------'

				seq = RedCards['RedOpenAndSolids'][mostSimilarImg] 
				matchedCards.append(seq)

				del RedCards['RedOpenAndSolids'][mostSimilarImg]

				if mostSimilarImg in RedCards['RedShadedAndThreeOpen']:
					del RedCards['RedShadedAndThreeOpen'][mostSimilarImg]

	return matchedCards

gameCards = makeGameCardList() #returns dict of game card paths
print gameCards

cards = matchCards()
print cards #This is a list of the card attribute codes

cardsNoSpaces = []

for card in cards:
	newCard = ''.join(str(i) for i in card) #Remove all spaces from the filenames
	cardsNoSpaces.append(newCard)

print cardsNoSpaces #Dict key must be tuple so all names have been changed to 4 digs now, not lists

#Used to look up the coordinate to put the text and draw the rectangle
cardBoxPositionsP1 = {}
cardBoxPositionsP2 = {}

for n in range (0,12):
	cardBoxPositionsP1[cardsNoSpaces[n]] = displayBboxesP1[n] #Associate nth card with nth p1 position from earlier list
	cardBoxPositionsP2[cardsNoSpaces[n]] = displayBboxesP2[n] #This returns the cards with associated positions correct but out of order, fyi

print cardBoxPositionsP1
print cardBoxPositionsP2

foundSets = 0

def findCards(trials): #0, 1, 2, 3 to represent the position of T in the list
	
	C3 = []
	trialCount = trials #trials is the variable iterated when running the program


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
		C1 = cards[randint(0,len(cards)-1)] #Select card 1 out of the list of cards. Need to subtract 1 because the list has 12 items but are accessed with digits 0-11
		cards.remove(C1)
		return C1

	C1 = chooseCardOne()
	C1Description = decodeAttributes(C1)
	print 'C1:', C1
	print C1Description

	def chooseCardTwo():
		C2 = cards[randint(0,len(cards)-1)] #Select card 2 out of 11 cards remaining
		cards.remove(C2)
		return C2

	C2 = chooseCardTwo()
	C2Description = decodeAttributes(C2)
	print 'C2:', C2
	print C2Description
   
	#CREATING THE THIRD CARD
	for n in [0,1,2,3]: 
		if C1[n] == C2[n]:
			i = C1[n]
			C3.append(i)

		else: 
			for i in [0,1,2]: 
				if i!=C1[n] and i!=C2[n]: #If the nth atribute in the first two cards are different
			 		C3.append(i) #Add the attribute to the list for C3

	C3Description = decodeAttributes(C3) #Get the description statement for C3
	print "C3:", C3
	print C3Description
	
	if C3 in cards:
		global foundSets
		foundSets+=1
		print "foundsets: ", foundSets

		print trialCount
		cards.remove(C3)
		print "you need to select", C3Description
		print len(cards), 'cards remaining'
		print(cards)
		print '--------------------------------'

		C3 = ''.join(str(i) for i in C3) #Remove all spaces from the filenames-Python added spaces when creating C3 
		C2 = ''.join(str(i) for i in C2)
		C1 = ''.join(str(i) for i in C1)

		#While there are no spaces in the card names temporarily, use them to draw boxes around the cards on the original image
		#Color changes for each set
		if foundSets == 1: 
			cv2.rectangle(twelve_cards_image, cardBoxPositionsP1[C1], cardBoxPositionsP2[C1], (255,0,0), 12)
			cv2.putText(twelve_cards_image, "Card 1, Trial: "+str(trials), cardBoxPositionsP1[C1], cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
			cv2.rectangle(twelve_cards_image, cardBoxPositionsP1[C2], cardBoxPositionsP2[C2], (255,0,0), 12)
			cv2.putText(twelve_cards_image, "Card 2, Trial: "+str(trials), cardBoxPositionsP1[C2], cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
			cv2.rectangle(twelve_cards_image, cardBoxPositionsP1[C3], cardBoxPositionsP2[C3], (255,0,0), 12)
			cv2.putText(twelve_cards_image, "Card 3, Trial: "+str(trials), cardBoxPositionsP1[C3], cv2.FONT_HERSHEY_SIMPLEX, 2, 255)

		if foundSets == 2: 
			cv2.rectangle(twelve_cards_image, cardBoxPositionsP1[C1], cardBoxPositionsP2[C1], (0,255,0), 12)
			cv2.putText(twelve_cards_image, "Card 1, Trial: "+str(trials), cardBoxPositionsP1[C1], cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
			cv2.rectangle(twelve_cards_image, cardBoxPositionsP1[C2], cardBoxPositionsP2[C2], (0,255,0), 12)
			cv2.putText(twelve_cards_image, "Card 2, Trial: "+str(trials), cardBoxPositionsP1[C2], cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
			cv2.rectangle(twelve_cards_image, cardBoxPositionsP1[C3], cardBoxPositionsP2[C3], (0,255,0), 12)
			cv2.putText(twelve_cards_image, "Card 3, Trial: "+str(trials), cardBoxPositionsP1[C3], cv2.FONT_HERSHEY_SIMPLEX, 2, 255)

		if foundSets == 3:
			cv2.rectangle(twelve_cards_image, cardBoxPositionsP1[C1], cardBoxPositionsP2[C1], (0,0,255), 12)
			cv2.putText(twelve_cards_image, "Card 1, Trial: "+str(trials), cardBoxPositionsP1[C1], cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
			cv2.rectangle(twelve_cards_image, cardBoxPositionsP1[C2], cardBoxPositionsP2[C2], (0,0,255), 12)
			cv2.putText(twelve_cards_image, "Card 2, Trial: "+str(trials), cardBoxPositionsP1[C2], cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
			cv2.rectangle(twelve_cards_image, cardBoxPositionsP1[C3], cardBoxPositionsP2[C3], (0,0,255), 12)
			cv2.putText(twelve_cards_image, "Card 3, Trial: "+str(trials), cardBoxPositionsP1[C3], cv2.FONT_HERSHEY_SIMPLEX, 2, 255)

		if foundSets == 4:
			cv2.rectangle(twelve_cards_image, cardBoxPositionsP1[C1], cardBoxPositionsP2[C1], (200,0,255), 12)
			cv2.putText(twelve_cards_image, "Card 1, Trial: "+str(trials), cardBoxPositionsP1[C1], cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
			cv2.rectangle(twelve_cards_image, cardBoxPositionsP1[C2], cardBoxPositionsP2[C2], (200,0,255), 12)
			cv2.putText(twelve_cards_image, "Card 2, Trial: "+str(trials), cardBoxPositionsP1[C2], cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
			cv2.rectangle(twelve_cards_image, cardBoxPositionsP1[C3], cardBoxPositionsP2[C3], (200,0,255), 12)
			cv2.putText(twelve_cards_image, "Card 3, Trial: "+str(trials), cardBoxPositionsP1[C3], cv2.FONT_HERSHEY_SIMPLEX, 2, 255)

		"""
		Code to show each individual card from key files
		C3 = str('['+C3[0]+','+C3[1]+','+C3[2]+','+C3[3]+']') #Correctly format the names of the cards to access from the downloaded template files
		C2 = str('['+C2[0]+','+C2[1]+','+C2[2]+','+C2[3]+']') 
		C1 = str('['+C1[0]+','+C1[1]+','+C1[2]+','+C1[3]+']')
		
		C3TemplatePath = template_file_path+str(C3)+".jpg"
		C3UXimg = cv2.imread(C3TemplatePath)
		C3name = str(C3)+"; Trial: "+str(trialCount) #this is the name of the image for the template card displayed when a SET is found
		cv2.imshow(C3name, C3UXimg)
		
		C2TemplatePath = template_file_path+str(C2)+".jpg"
		C2UXimg = cv2.imread(C2TemplatePath)
		C2name = str(C2)+"; Trial: "+str(trialCount)
		cv2.imshow(C2name,C2UXimg)
		C1TemplatePath = template_file_path+str(C1)+".jpg"
		C1UXimg = cv2.imread(C1TemplatePath)
		C1name = str(C1)+"; Trial: "+str(trialCount)
		cv2.imshow(C1name,C1UXimg)
		#time.sleep(5000)
		print '--------------------------------'
		"""
		
	else: 
		print "No card found"
		cards.append(C1)
		cards.append(C2) #Put first two cards back
		print len(cards), 'cards remaining'
		print '--------------------------------'

	return C3


trials = 0
while True:
	trials += 1 
	print 'Trial: ',trials

	if len(cards) == 0:
		result = cv2.imread(resultsPath)
		cv2.imshow("Set Game Array",result)
		cv2.waitKey(1)
		time.sleep(10)
		break

	findCards(trials) #Run the findCards function and pass the current trial count to it
	cv2.waitKey(1) 

	if trials > 100:
		print "No more sets to be found!"
		time.sleep(10)
		break

	cv2.imshow("Original Game",twelve_cards_image)
	cv2.imwrite(resultsPath, twelve_cards_image)
	
	time.sleep(.01)
