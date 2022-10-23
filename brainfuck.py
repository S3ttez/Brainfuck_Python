from enum import Enum

class BrainfuckMachineStates:
    Open = "["
    Closed = "]"   

class BrainfuckMachine(Exception):

 class HeadOverflow(Exception):
              pass
 class BracketMismatch(Exception):
              pass


 def __init__(self, MAX_tape):
        self.tape = [0]*MAX_tape
        self.code = ""
        self.head = 0
        self.loop = []
        self.currentPos = 0
        self.commands = {
            "+": self.ADD,
            "-": self.REMOVE,
            ">": self.RIGHT,
            "<": self.LEFT,
            "[": self.JumpStateNOTEqualZero,
            "]": self.JumpStateEQUALZero,
        }

 def ADD(self):
        self.tape[self.head] += 1
        print("\nAdded +!")
        if self.tape[self.head] > 255:
                self.tape[self.head] = 0
 def REMOVE(self):
        self.tape[self.head] -= 1
        print("\nRemoved -!")
        if self.tape[self.head] < 0:
                self.tape[self.head] = 255

 def RIGHT(self):
        self.head += 1
        print("\Moved DX!")
        if self.head > 64:
               raise BrainfuckMachine.HeadOverflow("Headoverflow")

 def LEFT(self):
        self.head -= 1
        print("\Moved SX!")
        if self.head < 0:
                print(self.head)
                raise BrainfuckMachine.HeadOverflow("Headoverflow")  

 def JumpStateNOTEqualZero(self):
        self.loop.append(self.currentPos)
        if self.tape[self.head] == 0:
                self.currentPos +=1
        while self.tape[self.head] == 0 and self.currentPos < len(self.code) and self.loop:
            self.el = self.code[self.currentPos]
            if  self.el == BrainfuckMachineStates.Open or self.el == BrainfuckMachineStates.Closed:
                    self.commands[self.el]()
            self.currentPos += 1

 def JumpStateEQUALZero(self):
        if self.tape[self.head] == 0:
                self.loop.pop()
                return
        self.currentPos = self.loop[-1]
 
 def run(self):
        self.currentPos = 0
        self.head = self.tape[0]
        while self.currentPos < len(self.code):
            self.el = self.code[self.currentPos]
            if self.el in self.commands:
                self.commands[self.el]()
                self.currentPos+=1
            print("\ncode: " + self.code)
            print("\nelemento: " + self.el)            
        if self.loop:
                raise BrainfuckMachine.BracketMismatch




