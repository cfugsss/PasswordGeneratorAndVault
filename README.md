# PasswordGeneratorAndVault
This program generates a random 12 digit/character password (upper and lowercase) and stores it in a file along with your username and app/website.

# Description

  2/22/22
Made this because I cant remember a password for more than 3 minutes. Functionality I want to add in the future is saving the password,
username, and app as a list in a new file so the program can retrieve your information without you going to the file. For now you get a
nice sentance including your password, username, and sitename/app in the text file. Passwords are also not encryped so. 

  2/23/22
  currently working on it || 8pm now and still currently working on it || (later that night) made a lot of headway today, basically threw away the whole first script and rewrote
  it using tkinter so its a gui. Excited for the finished product, unitl next time (probably tomorrow) || Well update, i remade this code and played csgo all day. I remade this 
  original code in gui using tkinter, so far i only 90% finished the generating password portion. I just need to figure how how to store a list of [username, sitename, password] 
  inot a seperate file and ill be done with half of the project; But thats for another day. Until tomorrow.
  
  2/24/22
  Yesterday I didnt log anything but spent some time trying to figure out how to store the data to a seperate file without overwriting it everytime. I watched some videos and
  did some research. I decided to go with a sql table using sqlite3. I also decided to create a new code because in passGen.py I was learning tkinter and how it works, now i 
  think i could make it better and more streamline. I only have a little bit of time today but im going to start the new code either setting up the new gui or starting building
  the database with sqlite.
  
  3/1/22
  watched some tutorials on how to use variables in sqlite3, so i can add the values from variables username, site, and password to the sql table. Once i figure that 
  out ill implement it into the code in the generation portion and a function to retrieve it, and then it should be finished for now. Until i come back
  at some point to work on it again but after this its onto the next project.
  
  3/15/22
  
  So I covered all the basics of python by this point and have started taking some intermediate courses and completly understand easier concepts to do this project. Im going
  continue more with the course but im also slowly editing this code when I have time. I will update it fully once its completly working. I am now using pandas to store the
  data and to retrieve it later. Im excited to finally "finish" (by that I mean have it wokring. For the future I either want to make the gui look way better or convert the whole
  thing over to a web app using django or flask. Well see what happens.
