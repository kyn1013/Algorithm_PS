table =[('A', '.-'),    ('B', '-...'),  ('C', '-.-.'),  ('D', '-..'),
        ('E', '.'),     ('F', '..-.'),  ('G', '--.'),   ('H', '....'),
        ('I', '..'),    ('J', '.---'),  ('K', '-.-'),   ('L', '.-..'),
        ('M', '--'),    ('N', '-.'),    ('O', '---'),   ('P', '.--.'),
        ('Q', '--.-'),  ('R', '.-.'),   ('S', '...'),   ('T', '-'),
        ('U', '..-'),   ('V', '...-'),  ('W', '.--'),   ('X', '-..-'),
        ('Y', '-.--'),  ('Z', '--..') ]

class TNode:
    def __init__(self, elem, left, right):
        self.data = elem
        self.left = left
        self.right = right

def encode(ch):
    idx = ord(ch.upper()) - ord('A')
    return table[idx][1]

def make_morse_tree():
    root = TNode(None, None, None)
    for tp in table:
        code = tp[1] #모스코드
        node = root
        for c in code:
            if c == '.' :
                if node.left == None:
                    node.left = TNode(None, None, None)
                node = node.left
            elif c == '-':
                if node.right == None:
                    node.right = TNode(None, None, None)
                node = node.right

        node.data = tp[0]
    return root

def decode(root, code):
    node = root
    for c in code:
        if c == '.' :
            node = node.left
        elif c == '-' :
            node = node.right
    return node.data

tree = make_morse_tree()
str = input("입력 문장 : ")
mlist = []
for ch in str:
    code = encode(ch)
    mlist.append(code)
print("Morse Code: ", mlist)
print("Decoding  : ", end='')
for code in mlist:
    ch = decode(tree, code)
    print(ch, end='')
print()
