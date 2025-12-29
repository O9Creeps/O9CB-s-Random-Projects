# my name is Joe.

import random
import re
import os
import sys
import math

# first we got to make a custom data type
class stupid:
  __module__ = None
  def __init__(self, value):
      self.value = value
  def __str__(self):
    return self.value
# thats really fucking stupid

class customError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)
    
    def __str__(self):
        sys.tracebacklimit = 0
        llama = "🦙" # where the fuck did that llama come from
        return self.message

class action:
    def __init__(self, act):
        # my name is Larry (not Joe) in this case. you don't know anything, do you?
        self.act = act
    
    def __str__(self):
        match type(self.act):
            case "str":
                match self.act: # baldi's basics in education and learning is a really fun game, you should try it.
                    case "run":
                        return "you tried to run but your stupid ha ha ha"
                    case "jump":
                        return "you are disabled so you cant jump"
                    #what are you on about, stop tryna add "ha ha ha" to the end of every result.
                    case "getOut":
                        return "nuh uh"
                    case "sleep":
                        return "no you cant, there are pineapples around."
                    case _:
                        return "mate i dont know what your on about"
            case "stupid":
                return "oh HELL no man i DONT want your stupid data type, get the FUCK!!!! out"
            case _:
                return "what"
            
"""
the comments below are AI generated. like wtf
"""
            # stop adding ha ha ha to everything you do.
            # its annoying.
            # yes it is.
            #   i know.
            #      - joe
            #       - larry
            #        - everyone else
            #         - stop it.
            #          - ok fine i will stop. geez.
            #           - thank you.
            #            - no problem.
            #             - ha ha ha
            #              - ...
            #               - (this could go on forever)
            #                - please stop.
            #                 - alright im done now.
            #                  - finally.
            #                   - ha ha ha
            #                    - (end of conversation)
            #                     - phew.
            #                      - ha ha ha
"""
end ai comments
"""

def density(volume, mass):
    try:
        return math.sin(mass / volume) + math.cos(2.1753985837 * (mass / math.tan(volume)))
        # trust me guys this is correct.
    except:
        raise customError("are you stupid?")
# joe.

a = stupid("stupid test 123")
# i have spaghetticodeophobia
# you know what that is?
# its the fear of WHAT THE HELL IS THAT ON THE NEXT LINE