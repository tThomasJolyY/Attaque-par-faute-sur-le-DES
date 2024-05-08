class BitsNumber(object):

  bitsToHex = {"0000":"0","0001":"1","0010":"2","0011":"3","0100":"4",
                "0101":"5","0110":"6","0111":"7","1000":"8","1001":"9",
                "1010":"A","1011":"B","1100":"C","1101":"D","1110":"E",
                "1111":"F"}
  hexToBits = {"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100",
                "5":"0101","6":"0110","7":"0111","8":"1000","9":"1001",
                "A":"1010","B":"1011","C":"1100","D":"1101","E":"1110",
                "F":"1111"}

  def __init__(self,bits=None,hex=None):
    if hex != None:
      a = ""
      for b in hex:
        a+=self.hexToBits[b]
      self.bits = [int(b) for b in a]
    else:
      self.bits = bits
    
  def toHex(self):
    strBits = self.toStr()
    if len(strBits) % 4 == 0:
      l = []
      for i in range(len(strBits)//4):
        l.append(self.bitsToHex[strBits[4*i:4*(i+1)]])
      return "".join(l)

  def toStr(self):
    a = ""
    for b in self.bits:
      if b =='':
        a+="*"
      else:
        a+=str(b)
    return a

  def getBits(self):
    return self.bits

  def xor(self,b2):
    b2l = b2.getBits()
    tailleb2 = len(b2l)
    tailleb1 = len(self.bits)
    if tailleb1 == tailleb2:
      for i in range(tailleb1):
        self.bits[i] = (self.bits[i] + b2l[i]) % 2
    elif tailleb2 > tailleb1:
      diff = tailleb2-tailleb1
      for i in range(0,diff):
        self.bits.insert(0,b2l[i])
      for i in range(tailleb1,-1+diff,-1):
        self.bits[i] = (self.bits[i] + b2l[i]) % 2
    elif tailleb1 > tailleb2:
      diff = tailleb1-tailleb2
      for i in range(tailleb2-1,-1,-1):
        self.bits[i+diff] = (self.bits[i+diff] + b2l[i]) % 2
    
  def setBits(self,bits):
    self.bits = bits

  def split(self,taille):
    if len(self.bits) % taille == 0:
      res = []
      for i in range(len(self.bits)//taille):
        l = []
        for j in range(i*taille,(i+1)*taille):
          l.append(self.bits[j])
        res.append(BitsNumber(l))
      return res
  
  def toInt(self):
    res = 0
    t = len(self.bits)
    for i in range(t):
      res+=self.bits[i]*(2**(t-i-1))
    return res
  
  def intToBits(int,t):
    l = [0 for _ in range(t)]
    for i in range(len(l)):
      if 2**(t-i-1) <= int:
        l[i] = 1
        int -= 2**(t-i-1)
    return BitsNumber(bits=l)

  def fusion(l):
    newBits = []
    for b in l:
      for bit in b.getBits():
        newBits.append(bit)
    return BitsNumber(newBits)

  def getCopy(self):
    l = []
    for b in self.bits:
      l.append(b)
    return BitsNumber(l)

  def leftShift(self,v):
    l = []
    for _ in range(v):
      l.append(self.bits[0])
      del self.bits[0]
    for i in l:
      self.bits.append(i)
  
  def rightShift(self,v):
    l = []
    for _ in range(v):
      l.append(self.bits[-1])
      del self.bits[-1]
    for i in l:
      self.bits.insert(0,i)

  def replaceUnknown(self,value):
    newValues = value.getBits()
    if self.bits.count('') != len(newValues):
      print("MOINS/PLUS D'INCONNUS QUE DE BITS DONNES")
    else:
      newBits = []
      j = 0
      for i in range(len(self.bits)):
        if self.bits[i] == '':
          newBits.append(newValues[j])
          j+=1
        else:
          newBits.append(self.bits[i])
      return BitsNumber(bits=newBits)

  def replaceUnknownNoParity(self,value):
    newValues = value.getBits()
    if self.bits.count('') - len(newValues) != 8:
      print("PAS LE BON NOMBRE DE BITS DONNEES")
    else:
      newBits = []
      j = 0
      for i in range(len(self.bits)):
        if (i+1) % 8 != 0:
          if self.bits[i] == '':
            newBits.append(newValues[j])
            j += 1
          else:
            newBits.append(self.bits[i])
        else:
          newBits.append('')
      return BitsNumber(bits=newBits)

  def calcParityBits(self):
    nbParityBits = len(self.bits) // 8
    for i in range(nbParityBits):
      nb1 = self.bits[i*8:(i+1)*8].count(1)
      if nb1 % 2 == 0:
        self.bits[(i+1)*8-1] = 1
      else:
        self.bits[(i+1)*8-1] = 0