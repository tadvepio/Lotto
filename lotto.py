import random
import time

def lotto():
	
	#Säännöt
	def rules():
		print("\nHow Lottery works:\nPlayer must have atleast one ticket to enter the lottery. One Ticket contains 7 numbers and an optional extra number.")
		print("\nTicket prices: One ticket containing 7 numbers costs 1 euro and an optional extra number costs 0.5 euros in addition")
		print("\nBuying:\n 1.Player can either choose his own numbers or generate a random ticket.\n 2. After the ticket is bought, it cannot be modified anymore and the payment will be deducted from players balance.\n 3.Extra numbers cannot be bought separately.")
		print("\nExtra number: If the player has bought an extra number, he will win more if:\n  -The extra number is right\n  -Either 3 or 6 numbers were right in the pre-existing numbers")
		print("\nOnce the player has entered the upcoming lottery, the lottery will be held and buying new tickets will not be possible untill it's over.")
		print("\nAfter the lottery, player will or will not be rewarded with the amount of prizemoney depending on how many numbers he got right and all pre-existing tickets will be deleted.")
		print("\nPrize-chart:\n")
		print("""			1| 0 euros 
			2| 0.5 euros
			3| 1 euros (With extra number: 2 euros) 
			4| 10 euros
			5| 50 euros
			6| 2000 euros (With extra number 550 000 euros)
			7| 1 000 000 euros
			""")
	def extraNumber(ticket):
		i = 1
		while i == 1:
			try:
				choise = int(input("\n1.Choose yourself\n2.Random\n"))
				if choise == 1:
					choosing = True
					while choosing:
						try:
							uInp = int(input("\nNumber between 1-40: "))
							if uInp < 1 or uInp > 40:
								print("\nNumber out of range")
							else:
								if uInp in ticket:
									print("\nNumber already in use.")
								elif uInp not in ticket:
									extra = uInp
									choosing = False
									i -= 1
						except ValueError:
							pass

				elif choise == 2:
					r1 = random.randint(1,40)
					if r1 in ticket:
						continue
					elif r1 not in ticket:
						extra = r1
						i -= 1
				else:
					pass
			except ValueError:
				pass
		return extra


	#Funktio luo 7 numeroisen lottorivin lista-muodossa
	def lottoNumberGenerator():
		generating = True
		while generating:
			officialNumbers = random.sample(range(1,41),7)
			officialNumbers.sort()
			break
		return officialNumbers
	
	#Funktio luo lottorivin käyttäjän syötteen mukaan
	def userNumberGen():
		userNumbers = []
		uInput = 0
		noDuplicates = set()
		for i in range(7):
			inputting = True
			while inputting:
				try:
					uInput = int(input("\nType in a number between 1 and 40: "))
					if uInput < 1 or uInput > 40:
						print("\nOnly numbers between 1 and 40")
					else:
						break
				except ValueError:
					print("\nNumbers only")

			if i >= 1:
				if uInput in noDuplicates:
					replacing = True
					while replacing:
						try:
							uInput = int(input("\nNumber already in use, pick another: "))
							if uInput in noDuplicates:
								continue
							elif uInput < 1 or uInput > 40:
								print("\nOnly numbers between 1 and 40")
							else:
								userNumbers.append(uInput)
								noDuplicates.add(uInput)
								break
						except ValueError:
							print("\nNumbers only")
				else:
					userNumbers.append(uInput)
					noDuplicates.add(uInput)

			else:
				userNumbers.append(uInput)
				noDuplicates.add(uInput)
		userNumbers.sort()
		return userNumbers
	

	#Funktio vertaa pelaajan ja arvottua riviä keskenään
	#ja luo niistä uuden listan joka jakaa yhteiset numerot 
	def checkResults(player,lotto):
		matches = []
		for i in range(len(player)):
			if player[i] in lotto:
				matches.append(player[i])
			else:
				continue
		return matches

	#Voittokertoimet
	def lottoMultiplier(n):
		#Lottokertoimet ovat niin surullisia, että lisäsin 2 osumaan 0,5 kertoimen
		hitsAndMult = {0:0,1:0,2:0.5,3:1,3.5:2,4:10,5:50,6:2000,6.5:550000,7:1000000}
		return hitsAndMult[n]
	#menu-funktio toimii jatkuvana ympäristönä ohjelman aikana. Se kutsuu yllä määritellyt funktiot.
	def menu():
		devilDeal = False
		balance = 1.0
		userRows = []
		extras = []
		print("Welcome to lotto! We have added 20 euros to your balance.")
		playing = True
		while playing:
			print("\n1.Buy a ticket\n2.Show tickets\n3.Show balance\n4.Play with current tickets\n5.Rules\n6.Quit")
			try:
				choose = int(input())
				if choose == 1:
					buying = True
					while buying:
						try:
							buyOrnot = int(input("\nTicket price: 1.0 euro\n1.Choose your own numbers\n2.Generate a ticket\n3.Back\n"))
							if buyOrnot == 1 and balance >= 1:
								betweener = []
								betweener.append(userNumberGen())
								payment = 1
								confirming = True
								while confirming:
									try:
										print("\nYour ticket:",*betweener[0])
										doExtra = True
										while doExtra:
											extraBetween = []
											try:
												accept = int(input("\nDo you want an extra number for 0.5 euros?(1.Yes/2.No):"))
												if accept == 1 and (balance-payment) >= 0.5:
													extraBetween.append(extraNumber(betweener))
													payment += 0.5
													doExtra = False
												elif accept == 2:
													doExtra = False
												elif balance-payment <= 0.5:
													print("\nNot enough money")
													doExtra = False
													confirming = False
												else:
													pass
											except ValueError:
												pass

										print("\nYour ticket:",*betweener[0],"Extra:",*extraBetween)
										sure = int(input("\nConfirm purchase?(1.Yes/2.No) "))
										if sure == 1 and (balance-payment) >= 0:
											userRows.append(betweener[0])
											extras.append(extraBetween)
											balance -= payment
											confirming = False

										elif sure == 2:
											payment -= 0.5
											confirming = False
										else:
											payment -= 0.5


									except ValueError:
										payment -= 0.5
										break

							elif buyOrnot == 2 and balance >= 1:
								betweener = []
								betweener.append(lottoNumberGenerator())
								payment = 1
								confirming = True
								while confirming:
										print("\nYour ticket:",*betweener[0])
										doExtra = True
										while doExtra:
											extraBetween = []
											try:
												accept = int(input("\nDo you want an extra number for 0.5 euros?(1.Yes/2.No):"))
												if accept == 1 and (balance-payment) >= 0.5:
													extraBetween.append(extraNumber(betweener))
													payment += 0.5
													doExtra = False
												elif accept == 2:
													doExtra = False
												else:
													if (balance-payment) < 0.5:
														print("\nYou don't have enough money")
														doExtra == False
													else:
														doExtra == False
											except ValueError:
												pass
											try:
												print("\nYour ticket:",*betweener[0],"Extra:",*extraBetween)
												sure = int(input("\nConfirm purchase?(1.Yes/2.No) "))
												if sure == 1 and balance-payment >= 0:
													userRows.append(betweener[0])
													extras.append(extraBetween)
													balance -= payment
													confirming = False
													doExtra = False
												elif sure == 2:
													payment -= 0.5
													doExtra = False
													confirming = False
												else:
													print("Not enough money")
													doExtra = False
													confirming = False
													pass
											except ValueError:
												payment -= 0.5
												break

							elif buyOrnot == 3:
								buying = False
							elif balance < 1 and len(userRows) > 0:
								print("\nNot enough money in balance")
								buying = False
							#Lotto on ylivoimaisesti huonoin peli, joten lisäsin pelaajalle
							#mahdollisuuden tehdä sopimuksen paholaisen kanssa, sitten
							#kun pelaaja ei pysty enää ostamaan lippuja ja pelaajalla ei
							#ole entuudestaan pelattavia lottolipukkeita. Joko pelaaja
							#hyväksyy sopimuksen tai voi lopettaa pelin päävalikosta.
							elif balance < 1 and len(userRows) < 1:
								buying = False
								print("\nAs you walk out of the shop pennyless, a stranger in a old fashioned suit and a cigar in his mouth in a dark alley waves you to come over")
								destinyAwaits = True
								while destinyAwaits:
									try:
										goOrNot = int(input("\nWhat do you do?\n1.Approach the stranger\n2.Walk away\n"))
										if goOrNot == 1:
											print("\nYou approach the strange old fashioned mobster with unease",end="")
											time.sleep(1.5)
											print(".",end="")
											time.sleep(1.5)
											print(".",end="")
											time.sleep(1.5)
											print(".",end="")
											time.sleep(4.0)
											print('\nStranger:"Hello friend. I see you are in trouble. What if I told you, that with my help you could win the lottery?" he says with a friendly, yet intimidating voice.')
											time.sleep(3.0)
											print('\n"What do you mean?" you ask with hesitation.')
											time.sleep(4.0)
											print('\nStranger:"Lets just say that I can give you the ticket to win tonights lottery. No payment. Take it as an act of good will, my friend.\nHe picks up a ticket from his pocket and offers it to you.')
											time.sleep(3.0)
											
											lastQuestion = True
											while lastQuestion:
												try:
													chooseDestiny = int(input("\nWhat do you do?\n1.Take the ticket\n2.Refuse\n"))
													if chooseDestiny == 1:
														print("\nYou take the ticket and as soon as you do it, the stranger vanishes into thin air.\nThat was weird...")
														userRows.append(lottoNumberGenerator())
														extras.append([])
														destinyAwaits = False
														lastQuestion = False
														devilDeal = True
													elif chooseDestiny == 2:
														print("\nYou thank the stranger and walk away with nothing.")
														lastQuestion = False
														goOrNot = False

													else:
														pass				
												except ValueError:
													pass
										elif goOrNot == 2:
											print("\nYou walk away like there was no-one there")
											destinyAwaits = False
										else:
											pass
									except ValueError:
										pass

							else:
								pass
						except ValueError:
							pass
				elif choose == 2:
					#Näyttää ostetut liput käyttäjälle
					if len(userRows) >= 1:
						for i in range(len(userRows)):
							print("\nTicket "+str(i+1)+":",*userRows[i],"Extra:",*extras[i])
					else:
						print("\nYou do not have any tickets")

				elif choose == 3:
					#Saldon tarkistus
					print("\nYour balance:",balance,"euros.")
				
				elif choose == 4:
					#Lotto peli: Ohjelma arpoo ensin itselleen viralliset lottonumerot
					#jonka jälkeen vertaa niitä käyttäjän numeroihin lippu kerrallaan.
					#Voittojen tarkistusta varten hyödynnetään aliohjelmia lottoMultiplier
					#ja checkresults. Lopuksi ohjelma kertoo käyttäjälle onko voittanut tai
					#ei ja voiton määrä, sekä osumat omissa lottolipuissa. Vanhat liput poistetaan
					#ja peli pääättyy.
					if len(userRows) >= 1:
						try:
							playforsure = int(input("Are you ready?(1.Yes 2.No): "))
							if playforsure == 1 and devilDeal != True:
								lotteryNumbers = lottoNumberGenerator()
								print("**********************************************************")
								print("** Welcome to tonights lottery! No more buying tickets! **")
								print("**********************************************************")
								time.sleep(2.0)
								print("Let's begin!")
								for i in range(len(lotteryNumbers)):
									time.sleep(2.0)
									print("!",lotteryNumbers[i],"!")
								hits = []
								extrahits = []
								winnings = 0
								winnings2 = 0
								for i in range(len(userRows)):
									myTicket = userRows[i]
									hits.append(checkResults(myTicket,lotteryNumbers))
								for i in range(len(extras)):
									myExtras = extras[i]
									extrahits.append(checkResults(myExtras,lotteryNumbers))
								for i in range(len(hits)):
									if len(extrahits[i]) > 0 and len(hits[i]) == 3 or len(extrahits[i]) > 0 and len(hits[i]) == 6:
										winnings = lottoMultiplier(len(hits[i]+0.5))
										balance += winnings
										winnings2 += winnings
									else:
										winnings = lottoMultiplier(len(hits[i]))
										balance += winnings
										winnings2 += winnings
								if winnings2 > 0:
									time.sleep(2.0)
									print("\nWinning tickets:")
									for i in range(len(userRows)):
										if len(hits[i]) > 1:
											print("\nTicket "+str(i+1)+":",*userRows[i],"Extra:",*extras[i],"-",len(hits[i])+len(extrahits[i]),"hit(s)!")
										else:
											continue
									print("\nYou won",winnings2,"euro(s)! All winnings are added to your balance! Thank you for playing!")
									del userRows[:]
									del extras[:]
									input()
								else:
									time.sleep(2.0)
									print("\nSorry, you didn't win anything this time. Thank you for playing!")
									for i in range(len(userRows)):
										print("\nTicket "+str(i+1)+":",*userRows[i],"Extra:",*extras[i],"-",len(hits[i])+len(extrahits[i]),"hit(s)")
									del userRows[:]
									del extras[:]
									input("Press any key to continue")

							elif playforsure == 2:
								pass
							#Paholaisen kanssa on tehty sopimus ja päävoitto on taattu.
							elif playforsure == 1 and devilDeal == True:
								lotteryNumbers = userRows[0]
								print("**********************************************************")
								print("** Welcome to tonights lottery! No more buying tickets! **")
								print("**********************************************************")
								time.sleep(2.0)
								print("Let's begin!")
								for i in range(len(lotteryNumbers)):
									time.sleep(2.0)
									print("!",lotteryNumbers[i],"!")
								hits = []
								extrahits = []
								winnings = 0
								winnings2 = 0
								for i in range(len(userRows)):
									myTicket = userRows[i]
									hits.append(checkResults(myTicket,lotteryNumbers))
								for i in range(len(extras)):
									myExtras = extras[i]
									extrahits.append(checkResults(myExtras,lotteryNumbers))
								for i in range(len(hits)):
									if len(extrahits[i]) > 0 and len(hits[i]) == 3 or len(extrahits[i]) > 0 and len(hits[i]) == 6:
										winnings = lottoMultiplier(len(hits[i]+0.5))
										balance += winnings
										winnings2 += winnings
									else:
										winnings = lottoMultiplier(len(hits[i]))
										balance += winnings
										winnings2 += winnings
								print("\nYou got",len(hits[0]),"hits!!!\nYou won",winnings2,"euros!!!! Congratulations!! Youre a millionaire!!")
								del userRows[:]
								del extras[:]
								print(('\n...You hear a dreadful whisper in the air: '))
								time.sleep(2.0)
								print('"Your soul...."')
								time.sleep(2.0)
								print('"belongs...."')
								time.sleep(2.0)
								print('"to me..."')
								time.sleep(2.0)
								input("\n(Press any key to continue)")

							else:
								pass

						except ValueError:
							pass
					else:
						print("\nYou don't have any tickets to play with")
				elif choose == 5:
					#Näyttää säännöt pelin pelaamiseen
					rules()
				
				elif choose == 6:
					#Lopettaa koko ohjelman. Pelistä ei löydy tallenusmekanismia.
					confirming = True
					while confirming:
						try:
							areYouSure = int(input("\nAre you sure?(1.Yes/2.No)"))
							if areYouSure == 1:
								playing = False
								break
							elif areYouSure == 2:
								break
							else:
								pass
						except ValueError:
							pass
				else:
					pass
			except ValueError:
				pass
	
	menu()

lotto()
