"""
AQA Assembly Language Interpreter
James W. and Michal W. 2021
"""

class MemoryException(Exception):
    
    def __init__(self,exNum):
        self.__exList = ["0: Unknown memory exception occurred.","1: Memory Location not found."]
        super().__init__(self.exList[exNum])
        
class ProcessorException(Exception):
    
    def __init__(self,exNum):
        self.__exList = ["0: Unknown processor exception occurred.","1: General Register not found."]
        super().__init__(self.exList[exNum])

class Memory(object):
    """Class that stores things in main memory"""
    def __init__(self):
        #memory can store 256 bytes from location 0 to 256
        self.__memoryList = [0]*256
    
    def getFromLocation(self, index):
        try:
            output = self.__memoryList[index]
            return output
        except:
            raise memoryException(1)
        
    
    def storeToLocation(self, index, item):
        try:
            self.__memoryList[index] = item
        except:
            raise MemoryException(1)

class LabelTable(object):
    """Stores labels with their index in a dictionary"""
    
    def __init__(self):
        self.__labelTable = {}
    
    def addLabel(self, lineNum, labelName):
        """Adds a label to the table"""
        self.__labelTable[lineNum] = labelName
    
    def getLine(self, labelName):
        """Gets the line number for a label"""
        

        
class Processor(object):
    
    def __init__(self):
        #general purpose registers
        self.__register = [0] * 16
        
        #special purpose registers
        self.__programCounter = 0
        self.__currentInstructionRegister = 0
        self.__memoryAddressRegister = 0
        self.__memoryBufferRegister = 0
        self.__errorHasOccurred = False
    
    def parseInput(self,)
    
    def getFromRegister(self, index):
        output = self.__register[index]
        return output

    def storeToRegister(self, index, value):
        self.__register[index] = value
        
    def addToRegister(self, outputIndex, inputIndex, value):
        registerVal = self.getFromRegister(inputIndex)

        if value[0] == "#":
            #use decimal value
            value = int(value[1:])
        elif value[0] == "R":
            #use value from register
            inputIndex = int(value[1:])
            value = self.getFromRegister(inputIndex)

        
        output = registerVal + value
        self.storeToRegister(outputIndex, output)
    
    def subtractFromRegister(self, outputIndex, inputIndex, value):
        registerVal = self.getFromRegister(inputIndex)
        if value[0] == "#":
            #use decimal value
            value = int(value[1:])
        elif value[0] == "R":
            #use value from register
            inputIndex = int(value[1:])
            value = self.getFromRegister(inputIndex)
        
        output = registerVal - value
        self.storeToRegister(outputIndex, output)

            
    def moveToRegister(self, outputIndex, value):
        if value[0] == "#":
            #use decimal value
            value = int(value[1:])
            
            self.storeToRegister(outputIndex, value)
            
        elif value[0] == "R":
            #use value in register
            inputIndex = int(value[1:])
            value = self.getFromRegister(inputIndex)
            
            self.storeToRegister(outputIndex, value)
    
    
        
        
    
    
        


while True:
    pass