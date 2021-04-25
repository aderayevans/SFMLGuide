*** Guide to use SFML in commandline without any IDE:
> Download SFML MinGW
> Then save all SFML files in the folder at D:\Programs\SFML (or whatever folder you would like, just remember it)
> Create main.cpp (the main file of your project)
> Copy all dll-files in your SFML/bin to the same folder containning your project files
> Paste this command in CMD:
###################
g++ -c main.cpp -o main.o -I D:/Programs/SFML/include -g -m64 -Wall && g++ main.o -o main.exe -L D:/Programs/SFML/lib -lsfml-audio -lsfml-graphics -lsfml-system -lsfml-network -lsfml-window
###################
Explain a little bit: 
	-o main.o is your output file after run the command, 
	-I D:/Programs/SFML/include link to SFML/include 
	-g -m64 -Wall are what I haven't known yet
	-o main.exe is your execute file,
	-L D:/Programs/SFML/lib link to SFML/lib
		-lsfml-audio
		-lsfml-graphics
		-lsfml-system 
		-lsfml-network 
		-lsfml-window	these are the specific what libraries that you'd wish to use in your project
Then
> Paste this command in CMD:
###################
g++ -c main.cpp -o main.o -I D:/Programs/SFML/include -O3 -m64 && g++ main.o -o main.exe -L D:/Programs/SFML/lib -lsfml-audio -lsfml-graphics -lsfml-system -lsfml-network -lsfml-window -mwindows
###################	
Explain 2 different plot in the command:
	-O3 -m64 are what I also haven't known yet (remember o3 not 03)
	-mwindows is whatever it is, fuck it

> After this you can run by double click your fucking execute file. Peace.