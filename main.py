"""
Computer Adventure Game
ICS3U-04
Jasmine Li
This program is a choose your own adventure game in the setting of a computer.
Concept: Everything and everyone here was created with the sole purpose to serve Master, the human using the computer. One outcome is pass all tests well and get accepted into the dust society, by collecting 3 badges. However, the other outcome is overthrowing the Master's dictatorship, being selected as a rebel due to earning 5 or more secret points. Along the way, there will be clues to the truth behind this society.
History:
  Program creation: Jan 8, 2024
  Program submission: Jan 27, 2024
"""
# Needed to clear the screen
import os

# Import to select random numbers
import random

# To control the console output
import sys

# To create delays
import time


def clear():
  """This causes the screen to clear"""
  os.system('clear')

def typewriter(sentence):
  """
  Function to create the typewriter effect with set delay time
  Modified from source: https://python.plainenglish.io/typewriter-animation-using-python-7f4275e812bf
  Args:
    sentence: str
  """
  # Loop through each character in the sentence
  for char in sentence:
      # Write, display and delay
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(0.01)
  # Pause after printing the entire sentence
  time.sleep(0.1)
  print()

def typewriterSpecial(sentence, delay):
  """
  Function to create the typewriter effect with specified delay time.
  Modified from source: https://python.plainenglish.io/typewriter-animation-using-python-7f4275e812bf
  Args:
    sentence: str
    delay: float
  """
  # Loop through each character in the sentence
  for char in str(sentence):
      # Write, display and delay
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(delay)
  # Pause after printing the entire sentence
  time.sleep(0.5)
  print()
  
def cpu(badge, secret):
  """
  This represents the CPU location. Randomly, when arrive, there will be a jam in the processing and user needs to decode binary.
  Args:
    badge: boolean
    secret: int
  Returns:
    selection: str
    badge: boolean
    secret: int
  """
  typewriter("\nYou're in the CPU")
  # initialize game and continuing as false
  continuing = False
  game = False

  # This whole scenario only shows up sometimes, done by a random choice between 0 and 1.
  if random.choice([0,1]) == 0:
    # Using the typewriterSpecial function to make the onomatopoeia more dramatic (slower)
    typewriterSpecial("BARRR BARRRRMP BARRRRMP",0.05)
    # Using typewriter function to display all the scenario text
    typewriter("WARNING WARNING ALL HANDS ON DECK ALL HANDS ON DECK")
    typewriter("""
    [1] Stay where you are. It's safer here.
    [2] Run towards another dust, maybe they'll know what's going on.
    [3] Let's run away from the chaos to a different location.""")
    # Prompts user for choice
    actChoice = input()
    # Verification of validity of user input and looping until valid input is recieved.
    while actChoice not in ['1','2','3']:
      typewriter("Invalid selection.")
      actChoice = input()
    # Using if statements to bring the user on different scenarios based on choice.
    if actChoice == '1':
      typewriter("\nDusts scramble all around you towards the hill in the distance. BAM someone shoulders you...")
      typewriter("""
  [1] YOU: 'Hey! Watch it!'
  [2] YOU: 'Sorry!'""")
      # Prompts user for choice
      actChoice = input()
      # Verification of validity of user input
      while actChoice not in ['1','2']:
        typewriter("Invalid selection.")
        actChoice = input()
      # Using if statements to bring the user on different scenarios based on choice.
      if actChoice == '1':
        # add a secret point due to defiant response
        secret += 1
        typewriter("\nOTHER DUST: 'YOU watch it! You're standing in the way, we have to hurry!'")
      elif actChoice == '2':
        typewriter("\nOTHER DUST: 'Sorry are you alright? Quick, we have to hurry!'")
      typewriter("\nYOU: Where are you going?")
      typewriter("\nOTHER DUST: There's a jam in the processing! We have to go fix the issue before Master becomes impatient! We have 5 human seconds at most! That's only 5 dust minutes!")
      # setting continuing to true so that this pathway continues in the if continuing: ...
      continuing = True
    elif actChoice == '2':
      # Adding a secret point
      secret += 1
      typewriter("\nOTHER DUST: There's a jam in the processing! We have to go fix the issue before Master becomes impatient! We have 5 human seconds at most! That's only 5 dust minutes!")
      # setting continuing to true so that this pathway continues in the if continuing: ...
      continuing = True
  # if continuing was changed to true, then this part is run.
  if continuing:
    typewriter("""
  [1] Follow the dust towards the hill. Maybe I can contribute and earn something in return...
  [2] YOU: 'Who's Master?'""")
    # Prompts user for choice
    actChoice = input()
    # Verification of validity of user input
    while actChoice not in ['1','2']:
      typewriter("Invalid selection.")
      actChoice = input()
    # Using if statements to bring the user on different scenarios based on choice.
    if actChoice == '2':
      # earned a secret point
      secret += 1
      typewriter("\nOTHER DUST: You must be new, all you have to know is that we must make her happy or else... well, nevermind that, let's hurry.")
    typewriter("\nYou've arrived at the top of the silver hill and there are many lines across the ground and dusts scramble about between the lines and small booths you see all around.")
    typewriter("\nYOU: What are they doing?")
    typewriter("\nOTHER DUST: They're processing all the different commands being given to us right now. Over there at that booth! Looks like that's where the jam is! Let's go over there!")
    typewriter("\nOTHER DUST: Oh! It looks like we're short on a translator! Oh man I really should've studied world languages instead of wire braiding... Hey! Do you perchance know how to speak binary?")
    typewriter("""
  [1] YOU: 'Yes, I can!'
  [2] YOU: 'Oops, sorry, I haven't'""")
    # Prompts user for choice
    actChoice = input()
    # Verification of validity of user input
    while actChoice not in ['1','2']:
      typewriter("Invalid selection.")
      actChoice = input()
    # Using if statements to bring the user on different scenarios based on choice.
    if actChoice == '1':
      typewriter("\nOTHER DUST: Oh! You're amazing!... maybe just the thing that'll save us all... anyway that's amazing! Go over there and help start decoding!!!")
      # setting game to true so that the game part runs.
      game = True
    elif actChoice == '2': #> else:
      typewriter("\nOTHER DUST: Oh, well I guess we both won't be of much help here then... let's get outta their way.")
      typewriter("""
  [1] YOU: Yeah... I guess so...
  [2] YOU: I want to at least go see the process over there! Maybe I'll know how to help there...""")
      # Prompts user for choice
      actChoice = input()
      # Verification of validity of user input
      while actChoice not in ['1','2']:
        typewriter("Invalid selection.")
        actChoice = input()
      # Using if statements to bring the user on different scenarios based on choice.
      if actChoice == '2':
        typewriter("\nOTHER DUST: Ok! Let's go!")
        # setting game to true so that the game part runs.
        game = True
  # if game was set to True, this game code runs.
  if game:
    typewriter("\nOTHER DUST: Hey Jerold! Jerold! JEROLD!")
    typewriter("\nJEROLD: Oh Steve! Whacha doing here?")
    typewriter("\nOTHER DUST (STEVE): This is our newest dust member! Maybe they can help with the jam over there!")
    typewriter("\nJEROLD: Oh just what we needed!!")
    typewriter("\nSTEVE: Well then, I'll leave you to it! Good luck!")
    # if at least one secret point has already been earned (already shown some defiance), run this sentence
    if secret >= 1:
      typewriter("\nSTEVE: I like your spunk! (>ᴗ•)")
    typewriter("\nJEROLD: I need you to decode some human numbers into binary! If you didn't know, humans usually use numbers in base 10, but we like the numbers in binary which is base 2. So let's start decoding!")
    # set decode to a random integer between 1 and 200
    decode = random.randint(1,200)
    # print the number generated
    typewriter("\nDecode this (convert from base 10 to base 2): "+str(decode))
    # prompt user for their answer (converted to base 2)
    ansInput = input()
    # initialize the exponent as 7 because 2**7 is the largest power that a number under 200 could be divisible by.
    exp = 7
    # initialize an empty string
    divisors = []
    # while loop until after exponent reaches 0
    while exp >= 0:
      # append to the list the quotient after division
      divisors.append(decode // 2**exp)
      # change the variable now to be the remainder such that the next division is made using this new number
      decode = decode%(2**exp)
      # decrease the exponent by 1
      exp -= 1
    # while loop as long as the 0th index is 0 to remove all the 0s at the beginning.
    while divisors[0] == 0:
      divisors.remove(0)
    # join the list items
    strDivisors = [str(x) for x in divisors]
    # prompt user to try again as long as their answer is wrong.
    while ansInput != "".join(strDivisors):
      typewriter("Incorrect :( Try Again!")
      ansInput = input()
    typewriter("\nJEROLD: Incredible! I've never seen anydust like this! You did it and saved the jam! As a token of gratitude, here's a badge of honour, it'll surely help you get on the good side of human to let you stay!")
    # award a badge
    badge += 1
    # award a secret point for being capable
    secret += 1
    typewriter("\nSTEVE: WOAH I saw you decoding away over there! Great job great job!!! I knew you had it in you! I heard that if you collect 3 of these badges you're in for sure!")
    typewriter("\nSTEVE: Well, I guess this is the furthest I will bring you! Good luck! I see hope in you, something different... your defiance with your skills, it may be just what we need...")

  # prompt user for their next destination choice
  typewriter("\nWhere would you like to go next? \n[r] RAM\n[f] Fan\n[p] Ports\n[e] Exit Game")
  selection = input()
  # Check that the user has entered a legitimate entry.
  while selection.lower() not in ['r', 'f', 'p', 'e']:
    typewriter("Invalid selection.")
    selection = input()

  # returning the user's input and items/points collected
  return selection.lower(), badge, secret

def ram(badge, secret):
  """
  This represents the RAM location. User "helps RAM" recall by memory three numbers and earns a badge.
  Args:
    badge: boolean
    secret: int
  Returns:
    selection: str
    badge: boolean
    secret: int
  """
  typewriter("\nYou're in the RAM")
  # use random choice between 0 and 1 to randomly choose whether this scenario will happen.
  if random.choice([0,1]) == 0:
    typewriter("\nVOICE: UGHHH I CAN'T BELIEVE YOU FORGOT AGAIN JERRY!")
    typewriter("\nJERRY: Aw man what do I do now!")
    typewriter("""
  [1] YOU: What's wrong you guys?
  [2] YOU: What a weird bunch, hey, you guys, whacha doing?""")
    # Prompts user for choice
    actChoice = input()
    # Verification of validity of user input
    while actChoice not in ['1','2']:
      typewriter("Invalid selection.")
      actChoice = input()
    # Using if statements to bring the user on different scenarios based on choice.
    if actChoice == '2':
      # add a secret point
      secret+=1
    typewriter("\nJERRY: Oh hey! I keep forgetting the info I was assigned... Man Master's gonna be so mad again!!! I'm so scared of her...")
    typewriter("\nYOU: Maybe I can help?")
    typewriter("\nJERRY: Oh that would be so amazing! I need to remember these 3 numbers!\n")
    # set the answer variable to a random integer between 0 and 9999999
    answer = str(random.randint(0, 9999999))
    # typewriter the number
    typewriter(answer)
    typewriter("\nYou have 5 seconds!")
    # Give the user 5 seconds to memorize it. The timer was created using the typewriterSpecial function with a 0.5 second delay with spaces between the numbers.
    typewriterSpecial("\n5 4 3 2 1 ",0.5)
    # clear screen
    clear()
    # prompt user for their answer
    userAns = input("What was the number? ")
    # while user has a wrong answer, choose a different number and try again (repeat)
    while userAns != answer:
      typewriter("Incorrect, here's another one to try again with:")
      answer = str(random.randint(0, 9999999))
      typewriter(answer)
      typewriter("\nYou have 5 seconds!")
      typewriterSpecial("\n5 4 3 2 1 ",0.5)
      clear()
      userAns = input("What was the number? ")
      #> Rather than repeating all of this, you can simply have it all occur within the while loop. Can also create a small function that just does this game and returns True if they win, False if they lose.


    typewriter("\nJERRY: AMAZING! Thank you thank you! Now Master just might spare me!")
    # if more than 2 secret points already earned, give more hints.
    if secret > 2:
      typewriter("\nJERRY: Man I really wish we could all be free from Master's tyranny one day...")
    typewriter("\nJERRY: To show you my gratitude, here's a badge for you! If you get three badges, Master'll let you stay!")
    # earned a badge
    badge += 1

  # prompt user for next location
  typewriter("\nWhere would you like to go next? \n[f] Fan\n[c] CPU\n[e] Exit Game")
  selection = input()
  # Check that the user has entered a legitimate entry.
  while selection.lower() not in ['f', 'c', 'e']:
    typewriter("Invalid selection.")
    selection = input()

  # returning the user's input and earnings
  return selection.lower(), badge, secret
  
def fan(badge, secret):
  """
  This represents the fan location. Choose the correct conversational tactics and win badge or secret points.
  Args:
    badge: boolean
    secret: int
  Returns:
    selection: str
    badge: boolean
    secret: int
  """
  typewriter("\nYou're in the fan")
  typewriter("\nWHIRRRRR WHIRRRRRR")
  typewriter("\nSOMEONE: Heyyy there! Who's this new one?")
  typewriter("""
  [1] YOU: Hey?
  [2] YOU: Ummm bye!""")
  # Prompts user for choice
  actChoice = input()
  # Verification of validity of user input
  while actChoice not in ['1','2']:
    typewriter("Invalid selection.")
    actChoice = input()
  # Using if statements to bring the user on different scenarios based on choice.
  if actChoice == '1':
    typewriter("\nSOMEONE (Jay): I'm Jay, pleasure to be of your aquaintance")
    typewriter("""
  [1] YOU: You're gorgeous!
  [2] YOU: Soooo...!""")
    # Prompts user for choice
    actChoice = input()
    # Verification of validity of user input
    while actChoice not in ['1','2']:
      typewriter("Invalid selection.")
      actChoice = input()
    # Using if statements to bring the user on different scenarios based on choice.
    if actChoice == '1':
      typewriter("\nJAY: Well aren't you a charming one, here, here's a badge, just don't tell anyone where you got it...")
      # earn a badge
      badge += 1
    else:
      typewriter("\nJAY: THE AUDACITY! TO NOT COMMENT ON MY BEAUTY IN THE FACE OF ME! NO BADGE FOR YOU!")
  else:
    # earn a secret point
    secret += 1

  # prompt user for next location
  typewriter("\nWhere would you like to go next? \n[r] RAM\n[c] CPU\n[e] Exit Game")
  selection = input()
  # Check that the user has entered a legitimate entry.
  while selection.lower() not in ['r', 'c', 'e']:
    typewriter("Invalid selection.")
    selection = input()

  # returning the user's input and earnings
  return selection.lower(), badge, secret
  
def ports():
  """
  This represents the Ports location. Sings a Welcome song that has embedded hints.
  Returns:
    selection: str
  """
  typewriter("\nYou're in the ports")
  # Song with hints about true nature of the society embedded
  typewriter("\nCHORUS: OHHHHH WELCOMMEEEEEE")
  typewriter("\nCHORUS: OHHHHH WELCOMMEEEEEE")
  typewriter("\nCHORUS: OHHHHH WELCOMMEEEEEE WONDERFUL DUSTTTTTT")
  typewriter("\nCHORUS: WILL THEY BE OUR SAVIOUR, WILL THEY BE THE NEXT MARIONETTE")
  typewriter("\nCHORUS: OHHHHH WE SURE HOPE FOR THE PRIOR YES WE DOOOOO")
  typewriter("\nCHORUS: OHHHHH WELCOMMEEEEEE")
  typewriter("\nCHORUS: OHHHHH WELCOMMEEEEEE")
  typewriter("\nCHORUS: YES WELCOMME!")

  # prompt user for next location
  typewriter("Where would you like to go next? \n[k] Keyboard\n[c] CPU\n[e] Exit Game")
  selection = input()
  # Check that the user has entered a legitimate entry.
  while selection.lower() not in ['k', 'c', 'e']:
    typewriter("Invalid selection.")
    selection = input()

  # returning the user's input now that it has been validated
  return selection.lower()
  
def keyboard():
  """
  This represents the Keyboard location. You can eavesdrop on others' conversations.
  Returns:
    selection: str
  """
  typewriter("\nYou're in the keyboard")
  # others' conversations with hints embedded about the nature of the society.
  typewriter("\nDUST 1: Hey, have you heard about the new dust that just came in?")
  typewriter("\nDUST 2: Of course! They're the talk of the town!")
  typewriter("\nDUST 1: Do you really think he could be the one to lead us to...")
  typewriter("\nDUST 2: Shhh, be careful...")
  typewriter("\nDUST 1: Fine... I'll scramble the word then: beerl")
  typewriter("\nDUST 2: I know right, I don't want to get to excited yet though but I hear they have potential!")

  # prompt user for next location
  typewriter("\nWhere would you like to go next? \n[p] Ports\n[e] Exit Game")
  selection = input()
  # Check that the user has entered a legitimate entry.
  while selection.lower() not in ['p', 'e']:
    typewriter("Invalid selection.")
    selection = input()

  # returning the user's input now that it has been validated
  return selection.lower()


#=============MAIN==================
typewriter("WELCOME dust particle number 34323049677777\nYou are the newest addition to the dust population within computer 777.")
typewriter("PROVE your worth here if you wish to stay.")
typewriter("You will encounter a series of choices and challenges that will test your integrity and worth within our society. If given a list of choices ex. \n[1]...\n[2]...\n[3]...\nInput your choice and 'enter'")
typewriter("Let it begin! You start in the CPU.")


# initialize user to start in CPU
choice = 'c'

# Initialize variables to show no badges and no secret points earned.
badgeTotal = 0
secretTotal = 0

# Call the function according to the returned location choice as long as e is not chosen and 3 badges hasn't been earned and they have less than 5 secret points
while choice != 'e' and badgeTotal < 3 and secretTotal < 5:
  if choice == 'c':
    # Returns the user's selection for next location and earnings
    choice, badgeTotal, secretTotal = cpu(badgeTotal,secretTotal)
  elif choice == 'r':
    # Returns the user's selection for next location and earnings
    choice, badgeTotal, secretTotal = ram(badgeTotal,secretTotal)
  elif choice =='f':
    # Returns the user's selection for next location and earnings
    choice, badgeTotal, secretTotal = fan(badgeTotal,secretTotal)
  elif choice == 'p':
    # Returns the user's selection for next location and earnings
    choice = ports()
  elif choice == 'k':
    # Returns the user's selection for next location and earnings
    choice = keyboard()
  # call the clear function so that the screen clears after every location change.
  clear()

# if not exited and more or equal to 5 secret points, display this conclusion
if choice != 'e' and secretTotal >= 5:
  typewriter("You earned... 5 or more secret points...")
  typewriter("\nDUST POPULATION: NO WAY IT HAS ACTUALLY HAPPENED! IT HAS HAPPENED! Dust number 34323049677777, we knew you had it in you! We've seen your capabilites and your defiance! Everything and everyone here was created with the sole purpose to serve Master, the human using the computer. Thank you for being a rebel, you're the key to this revolution to overthrowing Master Jasmine, the tyrannical computer user! We will regain freedom! Together!")

# else, if not exited and more or equal to 3 badges, display this conclusion (this part is elif because if earned enough secret points, show the above conclusion.)
elif choice != 'e' and badgeTotal >= 3:
  typewriter("Wow you earned three badges!")
  typewriter("\nMaster: Thank you for your wonderful service Dust number 34323049677777! Muahaha you will treat me well... won't you? Muahaha of course you will...")

# If e is inputted, or after the conclusions, this will print because exited out of while loop and if loop.
print("\nThanks for playing!")
