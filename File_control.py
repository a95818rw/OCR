def write(text):
    f = open("out.txt", 'w')
    f.write(text)

def read(address):
    f = open(address, 'r')
    text = f.read()
    return text