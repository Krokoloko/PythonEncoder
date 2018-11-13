from Classes import Encoder

encoder = Encoder.Encoder()

inp = input()

binary = encoder.encode(inp)
print("Encoded\n")
print(binary + "\n")

string = encoder.decode(binary)
print("Decoded\n")
print(string)
