class Encoder:
    
    def __init__(self):
        pass
    
    def binaryToChar(self,inp):
        return chr(round(int(inp,2)/42))
            
    def charToBinary(self,inp):
        return "{0:b}".format(ord(inp)*42)
    
    def encode(self, origin):
        encoded = "*&*"
        for letter in origin:
            encodedLetter = self.charToBinary(letter)
            encoded += encodedLetter + "*&*"
        return encoded
    
    def decode(self,encoded):
        decoded = ""
        decodeIt = ""
        for digit in encoded:
            if (digit=="*" or digit=="&"):
                if(decodeIt!=""):
                    decoded += self.binaryToChar(decodeIt)
                    decodeIt = ""                    
            else:
                decodeIt += digit
        return decoded

