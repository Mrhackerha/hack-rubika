Import libraryArsein.Arsein
from libraryArsein.Arsein import Robot_Rubika

mrhacker = Robot_Rubika("Auth")
MRHACKER = mrhacker.getMessages("s0B0e8da28a4fde394257f518e64e800","0")
for g in MRHACKER:
    if len(g["text"]) == 6:
    	print("---",g["text"])
    	
    	
    	
    	
    print("---",g["text"])
