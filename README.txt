README.TXT
INTRO:
Hello! And welcome to Position of the Sun Calculator!
With this program you can determine the position of the Sun relative to any location on all eight planets within the solar system as well as Pluto at any time and date.
STARTING PROGRAM:
In order to run the program, execute the python script entitled "position_of_sun.py" found within the same folder as this readme document. (position_of_class.py is the class of functions called to run position_of_sun.py)

DETERMINING SOLAR POSITION:
Once "position_of_sun.py" has started, you will see the following screen:
     	
	Welcome to The Position of the Sun Calculator!       
	Can be used for any Planet in the System!   ...and Pluto!
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Let's input the necessary information...

	Make sure to fill in values associated with time and location for when
	and where you wish to determine solar position and not current values
	for time and location, unless you wish to determine solar
	position for your current time and location... or you could
	just look out the window, up to you.

	What is the year (based on Gregorian Calendar)? 

Enter the year as a four digit inetger-- 2017

	What is the month (based on Gregorian Calendar)?

Enter the month as a two digit integer-- 03

	What is the day of the month (based on Gregorian
	Calendar)?

Enter the day as a two digit integer-- 07

	What is the hour?

	----Input as military time: example - 1:00 pm = 13, 0 for Midnight
	----Does not account for Daylight Savings
	----If not on Earth, will automatically use UTC

Enter the hour as a two digit integer-- 17

	What is the minute (0 through 59)?

Enter the minute as a two digit integer-- 42

	What planet are we observing the Sun from?

This is where the program goes one of two ways, I will first go through "Earth" and then later go through a ny of the eight other celestial bodies (Earth's process is the only unique one). So we will enter the name of the planet, first letter capitalized-- Earth

	What is the location's latitude (negative for south example: 45 degrees south 	equals -45)?

Enter the latitude as a two digit integer-- 45

	How many hours off of GMT (Greenwich Mean Time) is this
	location?

	----Denote negative value for west of GMT
	----For example, CST would be input as: -6
	----Does not account for Daylight Savings Time
	----Not sure of the timezone? Go here...
	----https://www.timeanddate.com/time/map/

Enter hours off as negative or positive integer-- -6

	Ahh, I see we are in the Western Hemisphere, what degree west?

Program will determine if you are in the western or eastern hemisphere for Earth, Enter longitude as a three digit integer-- 092

	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	Let's see what we got...

	On   3 / 7 / 2017   at   17 : 42  at 45 degrees latitude and 92 degrees west of the 	longitudinal meridian on Earth 

	The center of the Sun is 3.05748481814 degrees above the horizon and 259.792807526 	degrees east of north

And  there you have it, solar position for the Earth now moving back to select another planet.

	What planet are we observing the Sun from?

Enter name with first letter capitalized-- Mars

	What is the location's latitude (negative for south example: 45 degrees south 	equals -45)?

Enter latitude as two digit integer-- 45

	Longitudinal degrees on planets other than Earth
	increase to 360 west of the meridian. What are the
	degrees west of the meridian?

Enter longitude as 3 digit integer-- 092

	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	Let's see what we got...

	On   3 / 17 / 2017   at   17 : 42  at 45 degrees latitude and 92 degrees west of the 	longitudinal meridian on Mars 

	The center of the Sun is 25.7233486185 degrees above the horizon and 140.295973037 	degrees east of north 


And there you have it! Now you can calculate the position of the sun relative to any location on the eight planets of our solar system as well as Pluto for any given time and date! Have fun!

	

	


