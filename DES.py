from Bit import BitsNumber

class DES(object):

  PC1C = [56, 48, 40, 32, 24, 16, 8, 0, 57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35]

  PC1D = [62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 60, 52, 44, 36, 28, 20, 12, 4, 27, 19, 11, 3]

  PC2 = [13, 16, 10, 23, 0, 4, 2, 27, 14, 5, 20, 9, 22, 18, 11, 3, 25, 7, 15, 6, 26, 19, 12, 1, 40, 51, 30, 36, 46, 54, 29, 39, 50, 44, 32, 47, 43, 48, 38, 55, 33, 52, 45, 41, 49, 35, 28, 31]

  PC1CINV = [7, 15, 23, '', '', '', '', '', 6, 14, 22, '', '', '', '', '', 5, 13, 21, '', '', '', '', '', 4, 12, 20, '', '', '', '', '', 3, 11, 19, 27, '', '', '', '', 2, 10, 18, 26, '', '', '', '', 1, 9, 17, 25, '', '', '', '', 0, 8, 16, 24, '', '', '', '']

  PC1DINV = ['', '', '', 27, 23, 15, 7, '', '', '', '', 26, 22, 14, 6, '', '', '', '', 25, 21, 13, 5, '', '', '', '', 24, 20, 12, 4, '', '', '', '', '', 19, 11, 3, '', '', '', '', '', 18, 10, 2, '', '', '', '', '', 17, 9, 1, '', '', '', '', '', 16, 8, 0, '']

  PC2INV = [4, 23, 6, 15, 5, 9, 19, 17, '', 11, 2, 14, 22, 0, 8, 18, 1, '', 13, 21, 10, '', 12, 3, '', 16, 20, 7, 46, 30, 26, 47, 34, 40, '', 45, 27, '', 38, 31, 24, 43, '', 36, 33, 42, 28, 35, 37, 44, 32, 25, 41, '', 29, 39]

  Sbox = {1: [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
              [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8], 
              [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0], 
              [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
          2: [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10], 
              [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5], 
              [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15], 
              [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
          3: [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8], 
              [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1], 
              [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7], 
              [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
          4: [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15], 
              [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9], 
              [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4], 
              [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
          5: [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9], 
              [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6], 
              [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14], 
              [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
          6: [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11], 
              [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8], 
              [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6], 
              [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
          7: [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1], 
              [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6], 
              [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2], 
              [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
          8: [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7], 
              [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2], 
              [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8], 
              [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]}

  def __init__(self,input,key):
    self.input = input
    self.key = key
    self.l = None
    self.r = None
    self.kis = []

  def ip(self,bits):
    input = bits.getBits()
    l = [input[57],input[49],input[41],input[33],
        input[25],input[17],input[9],input[1],
        input[59],input[51],input[43],input[35],
        input[27],input[19],input[11],input[3],
        input[61],input[53],input[45],input[37],
        input[29],input[21],input[13],input[5],
        input[63],input[55],input[47],input[39],
        input[31],input[23],input[15],input[7],
        input[56],input[48],input[40],input[32],
        input[24],input[16],input[8],input[0],
        input[58],input[50],input[42],input[34],
        input[26],input[18],input[10],input[2],
        input[60],input[52],input[44],input[36],
        input[28],input[20],input[12],input[4],
        input[62],input[54],input[46],input[38],
        input[30],input[22],input[14],input[6]]
    bits.setBits(l)

  def ipInv(self,bits):
    output = bits.getBits()
    l = [output[39],output[7],output[47],output[15],
        output[55],output[23],output[63],output[31],
        output[38],output[6],output[46],output[14],
        output[54],output[22],output[62],output[30],
        output[37],output[5],output[45],output[13],
        output[53],output[21],output[61],output[29],
        output[36],output[4],output[44],output[12],
        output[52],output[20],output[60],output[28],
        output[35],output[3],output[43],output[11],
        output[51],output[19],output[59],output[27],
        output[34],output[2],output[42],output[10],
        output[50],output[18],output[58],output[26],
        output[33],output[1],output[41],output[9],
        output[49],output[17],output[57],output[25],
        output[32],output[0],output[40],output[8],
        output[48],output[16],output[56],output[24]]
    bits.setBits(l)

  def p(self,bits):
    e = bits.getBits()
    l = [e[15],e[6],e[19],e[20],
        e[28],e[11],e[27],e[16],
        e[0],e[14],e[22],e[25],
        e[4],e[17],e[30],e[9],
        e[1],e[7],e[23],e[13],
        e[31],e[26],e[2],e[8],
        e[18],e[12],e[29],e[5],
        e[21],e[10],e[3],e[24]]
    bits.setBits(l)

  def expension(self,bits):
    e = bits.getBits()
    l = [e[31],e[0],e[1],e[2],
        e[3],e[4],e[3],e[4],
        e[5],e[6],e[7],e[8],
        e[7],e[8],e[9],e[10],
        e[11],e[12],e[11],e[12],
        e[13],e[14],e[15],e[16],
        e[15],e[16],e[17],e[18],
        e[19],e[20],e[19],e[20],
        e[21],e[22],e[23],e[24],
        e[23],e[24],e[25],e[26],
        e[27],e[28],e[27],e[28],
        e[29],e[30],e[31],e[0]]
    bits.setBits(l)

  def round(self,i):
    if i != 15:
      oldr = self.r.getCopy()
      self.expension(self.r)
      self.r.xor(self.kis[i])
      self.SFunction(self.r)
      self.p(self.r)
      self.r.xor(self.l)
      self.l.setBits(oldr.getBits())
    else:
      oldr = self.r.getCopy()
      self.expension(self.r)
      self.r.xor(self.kis[i])
      self.SFunction(self.r)
      self.p(self.r)
      self.l.xor(self.r)
      self.r.setBits(oldr.getBits())

  def SFunction(self,input):
    boites = input.split(6)
    res = []
    for b in range(len(boites)):
      bits = boites[b].getBits()
      r = 2*bits[0] + bits[5]
      cAsBits = BitsNumber([bits[1],bits[2],bits[3],bits[4]])
      c = cAsBits.toInt()
      newVal = self.Sbox[b+1][r][c]
      newBitVal = BitsNumber.intToBits(newVal,4)
      res.append(newBitVal)
    input.setBits(BitsNumber.fusion(res).getBits())

  def keySchedule(self):
    e1 = [1,2,9,16]
    kbits = self.key.getBits()
    cbits = [kbits[ind] for ind in self.PC1C]
    dbits = [kbits[ind] for ind in self.PC1D]
    c = BitsNumber(bits=cbits)
    d = BitsNumber(bits=dbits)
    for i in range(1,17):
      if i in e1:
        vi = 1
      else:
        vi = 2
      c.leftShift(vi)
      d.leftShift(vi)
      conc = BitsNumber.fusion([c,d])
      concBits = conc.getBits()
      kibits = [concBits[ind] for ind in self.PC2]
      ki = BitsNumber(bits=kibits)
      self.kis.append(ki)
  
  def pc2TestFunc(self,cd):
    cdbits = cd.getBits()
    kibits = [cdbits[ind] for ind in self.PC2]
    cd.setBits(kibits)

  def pc1cTestFunc(self,cd):
    cbits = cd.getBits()
    newcbits = [cbits[ind] for ind in self.PC1C]
    cd.setBits(newcbits)

  def pc1dTestFunc(self,cd):
    dbits = cd.getBits()
    newdbits = [dbits[ind] for ind in self.PC1D]
    cd.setBits(newdbits)

  def cypher(self):
    self.keySchedule()
    self.ip(self.input)
    leftRight = self.input.split(32)
    self.l = leftRight[0].getCopy()
    self.r = leftRight[1].getCopy()
    for i in range(16):
      self.round(i)
    output = BitsNumber.fusion([self.l,self.r])
    self.ipInv(output)
    return output
  
  def pInv(self,output):
    input = output.getBits()
    l = [input[8], input[16], input[22], input[30], 
    input[12], input[27], input[1], input[17], 
    input[23], input[15], input[29], input[5], 
    input[25], input[19], input[9], input[0], 
    input[7], input[13], input[24], input[2], 
    input[3], input[28], input[10], input[18], 
    input[31], input[11], input[21], input[6], 
    input[4], input[26], input[14], input[20]]
    output.setBits(l)
  
  def invIpInv(self,bits):
    e = bits.getBits()
    l = [e[57], e[49], e[41], e[33], e[25], e[17], e[9], 
        e[1], e[59], e[51], e[43], e[35], e[27], e[19],
        e[11], e[3], e[61], e[53], e[45], e[37], e[29], 
        e[21], e[13], e[5], e[63], e[55], e[47], e[39], 
        e[31], e[23], e[15], e[7], e[56], e[48], e[40], 
        e[32], e[24], e[16], e[8], e[0], e[58], e[50], 
        e[42], e[34], e[26], e[18], e[10], e[2], e[60], 
        e[52], e[44], e[36], e[28], e[20], e[12], e[4], 
        e[62], e[54], e[46], e[38], e[30], e[22], e[14], e[6]]
    bits.setBits(l)

  def att15TH(self,ogBits,lFaute):
    res = []
    og = BitsNumber(hex=ogBits)
    self.ip(og)
    l = og.split(32)
    r = l[1].getCopy()
    self.expension(r)
    eqr = r.split(6)
    lrf = []
    for bits in lFaute:
      tmp = og.getCopy()
      faute = BitsNumber(hex=bits)
      self.ip(faute)
      lf = faute.split(32)
      rf = lf[1].getCopy()
      self.expension(rf)
      eqrf = rf.split(6)
      lrf.append(eqrf)
      tmp.xor(faute)
      self.pInv(tmp)
      restmp = tmp.getCopy()
      res.append(restmp.split(4))
    print("Les 32 systèmes obtenus :")
    for i in range(len(res)):
      print("P-1(L16+L16F"+str(i+1)+") = ",)
      for j in range(len(res[i])):
        print("   ",res[i][j].toStr(),"= S(K16 + "+eqr[j].toStr()+") + S(K16 + "+lrf[i][j].toStr()+")")
    print("computing k16...")
    k16Bits = []
    for bloci in range(8):
      for k in range(2**6):
        pot = True
        k16pot = BitsNumber.intToBits(k,6)
        for j in range(len(lrf)):
          tmp1 = k16pot.getCopy()
          tmp1.xor(eqr[bloci])
          res1 = self.SFunction6bits(tmp1,bloci)
          tmp2 = k16pot.getCopy()
          tmp2.xor(lrf[j][bloci])
          res2 = self.SFunction6bits(tmp2,bloci)
          res1.xor(res2)
          if res[j][bloci].getBits() != res1.getBits():
            pot = False
        if pot==True:
          k16Bits.append(k16pot)
    return BitsNumber.fusion(k16Bits)

  def SFunction6bits(self,bloc,i):
    o = bloc.getCopy()
    bits = o.getBits()
    r = 2*bits[0] + bits[5]
    cAsBits = BitsNumber([bits[1],bits[2],bits[3],bits[4]])
    c = cAsBits.toInt()
    newVal = self.Sbox[i+1][r][c]
    newBitVal = BitsNumber.intToBits(newVal,4)
    return newBitVal
  
  def pc1CDInv(self,bloc):
    blocCop = bloc.getCopy()
    blocCop2 = bloc.getCopy()
    bits = blocCop.getBits()
    bits2 = blocCop2.getBits()
    l = []
    for i in range(len(self.PC1CINV)):
      if self.PC1CINV[i] != '':
        l.append(bits[self.PC1CINV[i]])
      elif self.PC1DINV[i] != '':
        l.append(bits2[self.PC1DINV[i]+28])
      else:
        l.append('')    
    bloc.setBits(l)
  
  def pc2Inv(self,bloc):
    bits = bloc.getBits()
    l = ['']*56
    for i in range(len(self.PC2INV)):
      if self.PC2INV[i] != '':
        l[i] = bits[self.PC2INV[i]]
    res = BitsNumber(bits=l)
    return res

  def findKFromK16(self,k16,expectedOutput,input):
    e1 = [1,2,9,16]
    cd = self.pc2Inv(k16)
    l = cd.split(28)
    c = l[0].getCopy()
    d = l[1].getCopy()
    for i in range(16,0,-1):
      if i in e1:
        vi = 1
      else:
        vi = 2
      c.rightShift(vi)
      d.rightShift(vi)
    k = BitsNumber.fusion([c,d])
    self.pc1CDInv(k)
    print("Voici les 48 bits de la clé maître : ",k.toStr())
    print("brutforcing des 8 bits manquants...")
    for missingBits in range(2**8):
      m = input.getCopy()
      potBits = BitsNumber.intToBits(missingBits,8)
      keyPot = k.replaceUnknownNoParity(potBits)
      keyPot.calcParityBits()
      desTry = DES(m,keyPot)
      res = desTry.cypher()
      if res.getBits() == expectedOutput.getBits():
        print("!!!!!\nclé trouvée")
        print("Voici k : ",keyPot.toHex())
        print("k en base 2 :",keyPot.toStr())
        print("!!!!!")
        return keyPot
      
"""
#EXEMPLE D'UTILISATION DU PROGRAMME

cFautes = ['E80EFDC4947D5960', 
          'BC0EB9C4CD7D1142', 
          'BC0EEA80CC5D5963', 
          'E80AF9C44D355D67', 
          '385EECD6DD7C5D63', 
          'A85EE5C79C6C5963', 
          'A82EF9C4C87D5022', 
          '388EE8C4CD7D1963', 
          'A95BE984DE7D59F7', 
          'E90EE9C4D83D4B6B', 
          'E80E79D4CC355D63', 
          'AD0EECC4EC7F4923', 
          'C80AF954C97D0872', 
          'A80AEB10CD7D1973', 
          'A906E9C49C695B63', 
          'C82EF9C4CC7D5862', 
          'BC0AA9D44C7D1947', 
          'A80BEDC59C6DD961', 
          'A90ECDC4C87F4963', 
          'E80FF9C584E95972', 
          'B10EA8E49C795823', 
          'B80E28F4CC7D5C23', 
          'A809E984CC7CD963', 
          'A106E9C5DC795963', 
          'EC0EE8C4E83D592B', 
          'A80BA8C0CC7C79F7', 
          'A80FE1C58CED5973', 
          'BD4EE880DE5D5963', 
          'AA1FF989CC295972', 
          'A80ED9CDC8294962', 
          'A88EA8D4CD7D7963', 
          'AA1DE9C4CC7D5973']

cJuste = "A80EE9C4CC7D5963"

messageClair = "68BC76C7F198AE83"

des = DES([],[])
k16 = des.att15TH(cJuste,cFautes)
print("Voici k16  : ",k16.toHex())

m = BitsNumber(hex=messageClair)
c = BitsNumber(hex=cJuste)
des = DES([],[])
cle_maitre = des.findKFromK16(k16,c,m)
"""