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

##To run this program, OpenCV must be installed##

directory = "/users/mjortberg521/desktop/" #Replace this line with the file path to the directory that you are using
template_file_path = directory+"SetCards/resizedphotos716x464/" #Replace this line with the file path to the folder of template images downloaded from GitHub

twelve_cards_image_name = "gameImg1.jpg" #Replace this with the name of the image containing the 12 card SET you want to solve. 
										 #The image must be cropped with 3 cards going across horizontally and 4 cards going down vertically

twelve_cards_image_path = directory + twelve_cards_image_name
twelve_cards_image = cv2.imread(twelve_cards_image_path)

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


img = Image.open(twelve_cards_image_path) #Open the image from the path entered at the beginning of the program
img = img.resize((2148, 1856), PIL.Image.ANTIALIAS) #Resize this image to make it crop into nice boxes for each card well

#bounding boxes
bboxes = {
'1':(50,50,666,414),
'2':(766,50,1382,414),
'3':(1482,50,2098,414),

'4':(50,514,666,878),
'5':(766,514,1382,878),
'6':(1482,514,2098,878),

'7':(50,978,666,1342),
'8':(766,978,1382,1342),
'9':(1482,978,2098,1342),

'10':(50,1442,666,1806),
'11':(766,1442,1382,1806),
'12':(1482,1442,2098,1806)
}

#Crop the game image to the just the cards and save all 12 to directory
def cropBBoxes(): 
	for n in range(1,13,1):
		cardName = "card" + str(n)
		cardName = img.crop(bboxes[str(n)])

		cardName.save(os.path.join(directory, "setslices/slice_" + str(n) + ".jpg"))

cropBBoxes()

def makeGameCardList():
	gameCards = {}
	#Make a dict with all of the game card paths from the cropped images

	for n in range(1,13,1): #from 1 to 12 by 1
		gameCardPath = directory+"setslices/slice_"+str(n)+".jpg"
		gameCards[n] = gameCardPath #Adds to the gamecards dict with key=n and value=gameCardPath

	return gameCards

def findColors(path):
	
	image = cv2.imread(path)

	redboundaries = [
	([14, 15, 215], [60, 60, 255]) ####RED
	]

	##BGR boundaries for each of the colors##

	purpleboundaries = [
	([100, 20, 75], [130, 60, 150]) ####PURPLE
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

	ret, thresh = cv2.threshold(imgray, 180, 255, 0) #180,255 specifies the range to look for contours in
	im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	y = len(contours)

	#print contours
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
	
		gameCardImg = cv2.imread(path)

		color = findColors(path)

		print 'Color:', color

		y = findContours(path)
		print 'Contours:',y

		if color == "Green": #Green
			if 25<y<58: #If it is one shaded card (y is the number of contours)
				#This will template match the current gameCard against all cards in the specific color/shade dict

				matchIndexDict = templateMatch(GreenCards['OneGreenShaded'], path) #Generate a dictionary with key=template name and value=similarity score when comparing the currect green, 1 shaded shape card against all possible green 1 shape shaded
				mostSimilarImg = max(matchIndexDict, key = matchIndexDict.get) #Gets the key corresponding to the card with the maximum similarity index-this is the template name (e.g. "[0,0,0,0].jpg")

				seq = GreenCards['OneGreenShaded'][mostSimilarImg] #Get the most similar template attribute code using the key mostSimilarImg (file name) from matchIndexDict
				matchedCards.append(seq)

			elif 60<y<80: 
				matchIndexDict = templateMatch(GreenCards['TwoGreenShaded'], path) 
				mostSimilarImg = max(matchIndexDict, key = matchIndexDict.get) 

				seq = GreenCards['TwoGreenShaded'][mostSimilarImg] 
				matchedCards.append(seq)

			elif 95<y<120:
				matchIndexDict = templateMatch(GreenCards['ThreeGreenShaded'], path)
				mostSimilarImg = max(matchIndexDict, key = matchIndexDict.get) 

				seq = GreenCards['ThreeGreenShaded'][mostSimilarImg] 
				matchedCards.append(seq)

			else:
				matchIndexDict = templateMatch(GreenCards['GreenOpenAndSolids'], path) 
				mostSimilarImg = max(matchIndexDict, key = matchIndexDict.get) 

				seq = GreenCards['GreenOpenAndSolids'][mostSimilarImg] 
				matchedCards.append(seq)


		if color == "Purple": #Purple
			if 25<y<58: 
				matchIndexDict = templateMatch(PurpleCards['OnePurpleShaded'], path) 
				mostSimilarImg = max(matchIndexDict, key = matchIndexDict.get) 

				seq = PurpleCards['OnePurpleShaded'][mostSimilarImg] 
				matchedCards.append(seq)

			elif 60<y<80: 
				matchIndexDict = templateMatch(PurpleCards['TwoPurpleShaded'], path) 
				mostSimilarImg = max(matchIndexDict, key = matchIndexDict.get) 

				seq = PurpleCards['TwoPurpleShaded'][mostSimilarImg] 
				matchedCards.append(seq)

			elif 95<y<120:
				matchIndexDict = templateMatch(PurpleCards['ThreePurpleShaded'], path)
				mostSimilarImg = max(matchIndexDict, key = matchIndexDict.get) 

				seq = PurpleCards['ThreePurpleShaded'][mostSimilarImg] 
				matchedCards.append(seq)

			else:
				matchIndexDict = templateMatch(PurpleCards['PurpleOpenAndSolids'], path)
				mostSimilarImg = max(matchIndexDict, key = matchIndexDict.get) 

				seq = PurpleCards['PurpleOpenAndSolids'][mostSimilarImg] 
				matchedCards.append(seq)

		if color == "Red": #Red
			if 25<y<58: 
				matchIndexDict = templateMatch(RedCards['OneRedShaded'], path)
				mostSimilarImg = max(matchIndexDict, key = matchIndexDict.get)

				seq = RedCards['OneRedShaded'][mostSimilarImg] 
				matchedCards.append(seq)

			elif 60<y<80: 
				matchIndexDict = templateMatch(RedCards['TwoRedShaded'], path) 
				mostSimilarImg = max(matchIndexDict, key = matchIndexDict.get) 

				seq = RedCards['TwoRedShaded'][mostSimilarImg] 
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

gameCards = makeGameCardList() #returns dict of game card paths
print gameCards

cards = matchCards()
print cards #This is a list of the card attribute codes

cardsNoSpaces = []

for card in cards:
	newCard = ''.join(str(i) for i in card) #Remove all spaces from the filenames-Python added spaces when creating C3
	cardsNoSpaces.append(newCard)

print cardsNoSpaces #Dict key must be tuple so all names have been changed to 4 digs now, not lists

#Used to look up the coordinate to put the text and draw the rectangle
cardBoxPositions1 = {
	cardsNoSpaces[0]: (50,50),
	cardsNoSpaces[1]: (766, 50),
	cardsNoSpaces[2]: (1482, 50),
	cardsNoSpaces[3]: (50, 514),
	cardsNoSpaces[4]: (766, 514),
	cardsNoSpaces[5]: (1482, 514),
	cardsNoSpaces[6]: (50,978),
	cardsNoSpaces[7]: (766, 978),
	cardsNoSpaces[8]: (1482, 978),
	cardsNoSpaces[9]: (50, 1442),
	cardsNoSpaces[10]: (766, 1442),
	cardsNoSpaces[11]: (1482, 1442)
}

cardBoxPositions2 = {
	cardsNoSpaces[0]: (666,414),
	cardsNoSpaces[1]: (1382, 414),
	cardsNoSpaces[2]: (2098, 414),
	cardsNoSpaces[3]: (666, 878),
	cardsNoSpaces[4]: (1382, 878),
	cardsNoSpaces[5]: (2098, 878),
	cardsNoSpaces[6]: (666,1342),
	cardsNoSpaces[7]: (1382, 1342),
	cardsNoSpaces[8]: (2098, 1342),
	cardsNoSpaces[9]: (666, 1806),
	cardsNoSpaces[10]: (1382, 1806),
	cardsNoSpaces[11]: (2098, 1806)

}

#print "Cards:", len(cards)

def findCards(trials): #0, 1, 2, 3 to represent the position of T in the list
	
	C3 = []
	trialCount = trials #n is the trial variable iterated when running the program

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

		print trialCount
		cards.remove(C3)
		print "you need to select", C3Description
		print len(cards), 'cards remaining'
		print(cards)

		C3 = ''.join(str(i) for i in C3) #Remove all spaces from the filenames-Python added spaces when creating C3 
		C2 = ''.join(str(i) for i in C2)
		C1 = ''.join(str(i) for i in C1)

		#While there are no spaces in the card names temporarily, use them to draw boxes around the cards on the original image

		cv2.rectangle(twelve_cards_image, cardBoxPositions1[C1], cardBoxPositions2[C1], (255,0,0), 6)
		cv2.putText(twelve_cards_image, "Card 1, Trial: "+str(trials), cardBoxPositions1[C1], cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
		cv2.rectangle(twelve_cards_image, cardBoxPositions1[C2], cardBoxPositions2[C2], (0,255,0), 6)
		cv2.putText(twelve_cards_image, "Card 2, Trial: "+str(trials), cardBoxPositions1[C2], cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
		cv2.rectangle(twelve_cards_image, cardBoxPositions1[C3], cardBoxPositions2[C3], (0,0,255), 6)
		cv2.putText(twelve_cards_image, "Card 3, Trial: "+str(trials), cardBoxPositions1[C3], cv2.FONT_HERSHEY_SIMPLEX, 2, 255)


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
	findCards(trials) #Run the findCards function and pass the current trial count to it

	cv2.waitKey(1) 

	if trials > 100:
		print "No more sets to be found!"
		time.sleep(10000)
		break

	cv2.imshow("Original Game",twelve_cards_image)
	cv2.imwrite("/users/mjortberg521/desktop/SET_game_results.jpg", twelve_cards_image)
	
	time.sleep(.01)
