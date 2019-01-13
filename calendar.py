
#This first loop is going to keep the program running or exit from the program depending on their choice.
userChoice = "yes"
while (userChoice != "no"):
	# This helps the user decide a choice.
  userMode = input("Please choose which option you would like to access: Create a new entry = a, View Entries = b or Edit an existing entry = c: ")
  # The choice needs to repeat until an acceptable answer is give A, B or C
  while (userMode != 'a') and (userMode != 'b') and (userMode != 'c'):
    userMode = input("Please input a b or c: ")
	#Creating the option to add to the file
  if userMode == ('a'):
    print ("You have selected to create a new entry")
    f = open('view.txt','a')
    f.write(input()+'\n')

    #This is creating a view only entry.
  elif userMode == ('b'):
    print ("You have selected to view entries")
    f= open('view.txt','r')
    print(f.read())
    #This is going to allow the user to view and edit an entry in the file.
  elif userMode == ("c"):
    print("You have selected edit an entry")
    f= open('view.txt','r+')
    i = 0
    for line in list(f):
      i += 1
      print(str(i) + '. ' + line, end='')
	# Determining which line the user wants to edit.
    userLine = int(input("\nWhich line would you like to edit: "))
    f.seek(0)
    fileContents = list(f)
    print(fileContents[userLine-1], end='')
    fileContents[userLine-1] = input() + '\n'
    f.seek(0)
    f.writelines(fileContents)
 # If th user doesn't input one of the correct values an error message will appear.
  else:
    print ("Please input a correct value")
#Part of the first loop, it will either run the program again or exit from it.
  userChoice = input("Do you want to continue using the calendar? ")
  while (userChoice != "no") and (userChoice != "yes"):
      userChoice = input("Please input yes or no: ")

f.close()
