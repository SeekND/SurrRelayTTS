from time import *
from surrortg import Game  # First we need import the Game
from surrortg.inputs import LinearActuator  # and our preferred input(s)
from surrortg.inputs import Switch
from surrortg.inputs import Joystick, Directions
import pigpio
import logging
import asyncio
import time
import os
import RPi.GPIO as GPIO


speech=""
voice="m"
playername = ""
winlose = 0

P6_PIN = 19
P5_PIN = 13
P4_PIN = 6
P3_PIN = 20
P2_PIN = 16
P1_PIN = 12

PW_PIN = 26
PL_PIN = 5

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(P1_PIN, GPIO.OUT)
GPIO.setup(P2_PIN, GPIO.OUT)
GPIO.setup(P3_PIN, GPIO.OUT)
GPIO.setup(P4_PIN, GPIO.OUT)
GPIO.setup(P5_PIN, GPIO.OUT)
GPIO.setup(P6_PIN, GPIO.OUT)


GPIO.output(P1_PIN, GPIO.HIGH)
GPIO.output(P2_PIN, GPIO.HIGH)
GPIO.output(P3_PIN, GPIO.HIGH)
GPIO.output(P4_PIN, GPIO.HIGH)
GPIO.output(P5_PIN, GPIO.HIGH)
GPIO.output(P6_PIN, GPIO.HIGH)


GPIO.setup(PW_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #WIN
GPIO.setup(PL_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #LOSE



def playerwon(channel):  
    global winlose
    winlose = 1
    logging.info(f"Player won")
    os.system('espeak -ven+f5 -s130 "win" --stdout |aplay  2>/dev/null')

def playerlost(channel):  
    global winlose
    winlose = 2
    logging.info(f"Player lost")
    os.system('espeak -ven+f5 -s130 "loss" --stdout |aplay  2>/dev/null')

GPIO.add_event_detect(PW_PIN, GPIO.FALLING, callback=playerwon, bouncetime=2000)
GPIO.add_event_detect(PL_PIN, GPIO.FALLING, callback=playerlost, bouncetime=2000)



class Left(Switch):

    def __init__(self, pin, io):
        # Store and initialize pigpio for the control pin
        self.io = io
        self.pin = pin

    async def on(self, seat=0):
      
        if (winlose == 1 or winlose == 2 ):
            self.io.disable_inputs()
            self.io.send_playing_ended()
        else:
            GPIO.output(self.pin, GPIO.LOW)

    async def off(self, seat=0):
         GPIO.output(self.pin, GPIO.HIGH)



class Right(Switch):

    def __init__(self, pin, io):
        # Store and initialize pigpio for the control pin
        self.io = io
        self.pin = pin

    async def on(self, seat=0):
      
        if (winlose == 1 or winlose == 2 ):
            self.io.disable_inputs()
            self.io.send_playing_ended()
        else:
            GPIO.output(self.pin, GPIO.LOW)

    async def off(self, seat=0):
         GPIO.output(self.pin, GPIO.HIGH)

class Up(Switch):

    def __init__(self, pin, io):
        # Store and initialize pigpio for the control pin
        self.io = io
        self.pin = pin

    async def on(self, seat=0):
      
        if (winlose == 1 or winlose == 2 ):
            self.io.disable_inputs()
            self.io.send_playing_ended()
        else:
            GPIO.output(self.pin, GPIO.LOW)

    async def off(self, seat=0):
         GPIO.output(self.pin, GPIO.HIGH)


class Down(Switch):

    def __init__(self, pin, io):
        # Store and initialize pigpio for the control pin
        self.io = io
        self.pin = pin

    async def on(self, seat=0):
      
        if (winlose == 1 or winlose == 2 ):
            self.io.disable_inputs()
            self.io.send_playing_ended()
        else:
            GPIO.output(self.pin, GPIO.LOW)

    async def off(self, seat=0):
         GPIO.output(self.pin, GPIO.HIGH)


class AH(Switch):

    def __init__(self, pin, io):
        # Store and initialize pigpio for the control pin
        self.io = io
        self.pin = pin

    async def on(self, seat=0):
      
        if (winlose == 1 or winlose == 2 ):
            self.io.disable_inputs()
            self.io.send_playing_ended()
        else:
            GPIO.output(self.pin, GPIO.LOW)

    async def off(self, seat=0):
         GPIO.output(self.pin, GPIO.HIGH)



class AL(Switch):

    def __init__(self, pin, io):
        # Store and initialize pigpio for the control pin
        self.io = io
        self.pin = pin

    async def on(self, seat=0):
      
        if (winlose == 1 or winlose == 2 ):
            self.io.disable_inputs()
            self.io.send_playing_ended()
        else:
            GPIO.output(self.pin, GPIO.LOW)

    async def off(self, seat=0):
         GPIO.output(self.pin, GPIO.HIGH)



# MAKES PLAYER QUIT

class ForceQuit(Switch):
    def __init__(self,io):
        self.io = io

    async def on(self, seat=0): 
        self.io.disable_inputs()
        self.io.send_playing_ended()
        logging.info(f"player was force kicked")


    async def off(self, seat=0):
        return



# TTS switches


class SwitchSend(Switch):
    def __init__(self,io):
        self.io = io

    async def on(self, seat=0):
        global speech
        if voice == "m":
            os.system('espeak -ven+m5 -s130 "'+speech +'" --stdout |aplay  2>/dev/null')
        elif voice == "f":
            os.system('espeak -ven+f5 -s130 "'+speech +'" --stdout |aplay  2>/dev/null')

        logging.info(f"Speech ------ {speech} - by {seat}")
        speech = ""

    async def off(self, seat=0):
        return


class SwitchVoice(Switch):
    async def on(self, seat=0):
        global voice
        if voice == "m":
            voice = "f"
        elif voice == "f":
            voice = "m"

    async def off(self, seat=0):
        logging.info(f"voice is now {voice} for {seat}")



class SwitchDel(Switch):
    async def on(self, seat=0):
        global speech
        logging.info(f"erased - {speech} - for {seat}")
        speech = ""

    async def off(self, seat=0):
        return

class SwitchSpc(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+" "

    async def off(self, seat=0):
        return

class SwitchA(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"a"

    async def off(self, seat=0):
        return

class SwitchB(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"b"

    async def off(self, seat=0):
        return

class SwitchC(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"c"

    async def off(self, seat=0):
        return

class SwitchD(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"d"

    async def off(self, seat=0):
        return

class SwitchE(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"e"

    async def off(self, seat=0):
        return

class SwitchF(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"f"

    async def off(self, seat=0):
        return

class SwitchG(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"g"

    async def off(self, seat=0):
        return

class SwitchH(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"h"

    async def off(self, seat=0):
        return

class SwitchI(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"i"

    async def off(self, seat=0):
        return

class SwitchJ(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"j"

    async def off(self, seat=0):
        return

class SwitchK(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"k"

    async def off(self, seat=0):
        return


class SwitchL(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"l"

    async def off(self, seat=0):
        return

class SwitchM(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"m"

    async def off(self, seat=0):
        return

class SwitchN(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"n"

    async def off(self, seat=0):
        return

class SwitchO(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"o"

    async def off(self, seat=0):
        return

class SwitchP(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"p"

    async def off(self, seat=0):
        return


class SwitchQ(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"q"

    async def off(self, seat=0):
        return


class SwitchR(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"r"

    async def off(self, seat=0):
        return


class SwitchS(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"s"

    async def off(self, seat=0):
        return


class SwitchT(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"t"

    async def off(self, seat=0):
        return


class SwitchU(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"u"

    async def off(self, seat=0):
        return


class SwitchV(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"v"

    async def off(self, seat=0):
        return

class SwitchW(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"w"

    async def off(self, seat=0):
        return


class SwitchX(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"x"

    async def off(self, seat=0):
        return


class SwitchY(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"y"

    async def off(self, seat=0):
        return


class SwitchZ(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"z"

    async def off(self, seat=0):
        return


class Switch1(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"1"

    async def off(self, seat=0):
        return

class Switch2(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"2"

    async def off(self, seat=0):
        return

class Switch3(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"3"

    async def off(self, seat=0):
        return

class Switch4(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"4"

    async def off(self, seat=0):
        return

class Switch5(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"5"

    async def off(self, seat=0):
        return

class Switch6(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"6"

    async def off(self, seat=0):
        return

class Switch7(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"7"

    async def off(self, seat=0):
        return

class Switch8(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"8"

    async def off(self, seat=0):
        return

class Switch9(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"9"

    async def off(self, seat=0):
        return

class Switch0(Switch):
    async def on(self, seat=0):
        global speech
        speech = speech+"0"

    async def off(self, seat=0):
        return









class RCGame(Game):

    async def on_init(self):
        #self.pi = pigpio.pi()
        #if not self.pi.connected:
        #    raise RuntimeError("Could not connect to pigpio")


        self.io.register_inputs({"left": Left( P1_PIN, self.io)})   
        self.io.register_inputs({"right": Right( P2_PIN, self.io) })
        self.io.register_inputs({"up": Up(P3_PIN, self.io)})   
        self.io.register_inputs({"down": Down(  P4_PIN, self.io)})  
        self.io.register_inputs({"attackhigh": AH(  P5_PIN, self.io)})  
        self.io.register_inputs({"attacklow": AL( P6_PIN, self.io)})  


        self.io.register_inputs({"force_quit": ForceQuit(self.io)})


        self.io.register_inputs({"switch_send": SwitchSend(self.io)})
        self.io.register_inputs({"switch_voice": SwitchVoice()})
        self.io.register_inputs({"switch_del": SwitchDel()})
        self.io.register_inputs({"switch_spc": SwitchSpc()})
        self.io.register_inputs({"switch_a": SwitchA()})
        self.io.register_inputs({"switch_b": SwitchB()})
        self.io.register_inputs({"switch_c": SwitchC()})
        self.io.register_inputs({"switch_d": SwitchD()})
        self.io.register_inputs({"switch_e": SwitchE()})
        self.io.register_inputs({"switch_f": SwitchF()})
        self.io.register_inputs({"switch_g": SwitchG()})
        self.io.register_inputs({"switch_h": SwitchH()})
        self.io.register_inputs({"switch_i": SwitchI()})
        self.io.register_inputs({"switch_j": SwitchJ()})
        self.io.register_inputs({"switch_k": SwitchK()})
        self.io.register_inputs({"switch_l": SwitchL()})
        self.io.register_inputs({"switch_m": SwitchM()})
        self.io.register_inputs({"switch_n": SwitchN()})
        self.io.register_inputs({"switch_o": SwitchO()})
        self.io.register_inputs({"switch_p": SwitchP()})
        self.io.register_inputs({"switch_q": SwitchQ()})
        self.io.register_inputs({"switch_r": SwitchR()})
        self.io.register_inputs({"switch_s": SwitchS()})
        self.io.register_inputs({"switch_t": SwitchT()})
        self.io.register_inputs({"switch_u": SwitchU()})
        self.io.register_inputs({"switch_v": SwitchV()})
        self.io.register_inputs({"switch_w": SwitchW()})
        self.io.register_inputs({"switch_x": SwitchX()})
        self.io.register_inputs({"switch_y": SwitchY()})
        self.io.register_inputs({"switch_z": SwitchZ()})
        self.io.register_inputs({"switch_1": Switch1()})
        self.io.register_inputs({"switch_2": Switch2()})
        self.io.register_inputs({"switch_3": Switch3()})
        self.io.register_inputs({"switch_4": Switch4()})
        self.io.register_inputs({"switch_5": Switch5()})
        self.io.register_inputs({"switch_6": Switch6()})
        self.io.register_inputs({"switch_7": Switch7()})
        self.io.register_inputs({"switch_8": Switch8()})
        self.io.register_inputs({"switch_9": Switch9()})
        self.io.register_inputs({"switch_0": Switch0()})



        #self.io.register_inputs({"X": SwitchJoystick(self.io, self.pi, PWM5_PIN, PWM6_PIN)})


    async def on_countdown(self):
        global speech
        global speech
        global playername
        global winlose

        self.io.enable_inputs()

        speech = ""
        voice = "m"
        winlose = 0


        playername = str(self.players)
        
        cropname = playername.find("username")
        if len(playername) > cropname :
            playername = playername[0: 0:] + playername[cropname+11 + 1::]

        cropname = playername.find("}")
        end = playername.find("]")
        if len(playername) > cropname :
            playername = playername[0: cropname-1:] + playername[end + 1::]

        logging.info(f"----- player is: {playername}")

        os.system('espeak -ven+f5 -s130 "'+playername +' has joined"  --stdout |aplay  2>/dev/null')



    async def on_finish(self):

        self.io.disable_inputs()
        os.system('espeak -ven+f5 -s130 "'+playername +' has left"  --stdout |aplay  2>/dev/null')
        
        if winlose == 1:
        	self.io.send_score(score=1, seat=0, final_score=True)
        elif winlose == 2:
        	self.io.send_score(score=0, seat=0, final_score=True)



    async def on_exit(self, reason, exception):
        self.pi.stop()


# And now you are ready to play!
if __name__ == "__main__":
    RCGame().run()
