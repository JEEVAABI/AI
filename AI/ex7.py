from utils import *
from logic import *
char=['P','B','W','S']
abc=''
ind=[1,2,3,4]
for i in char:
    for x in ind:
        for y in ind:
            abc= abc+(str(i)+str(x)+str(y))+','
abc= abc[0:-1]
abc
wumpus_kb = PropKB()
P11,P12,P13,P14,P21,P22,P23,P24,P31,P32,P33,P34,P41,P42,P43,P44,B11,B12,B13,B14,B21,B22,B23,B24,B31,B32,B33,B34,B41,B42,B43,B44,W11,W12,W13,W14,W21,W22,W23,W24,W31,W32,W33,W34,W41,W42,W43,W44,S11,S12,S13,S14,S21,S22,S23,S24,S31,S32,S33,S34,S41,S42,S43,S44= expr('P11,P12,P13,P14,P21,P22,P23,P24,P31,P32,P33,P34,P41,P42,P43,P44,B11,B12,B13,B14,B21,B22,B23,B24,B31,B32,B33,B34,B41,B42,B43,B44,W11,W12,W13,W14,W21,W22,W23,W24,W31,W32,W33,W34,W41,W42,W43,W44,S11,S12,S13,S14,S21,S22,S23,S24,S31,S32,S33,S34,S41,S42,S43,S44')
wumpus_kb.tell(~P11)
wumpus_kb.tell(~S11)
wumpus_kb.tell(~W11)
wumpus_kb.tell(~B11)
wumpus_kb.tell(~S12)
wumpus_kb.tell(~B12)
wumpus_kb.tell(~P12)
wumpus_kb.tell(~W12)
wumpus_kb.tell(~P13)
wumpus_kb.tell(~S13) 
wumpus_kb.tell(~W13)
wumpus_kb.tell(~B13)
wumpus_kb.tell(~S14)
wumpus_kb.tell(~B14)
wumpus_kb.tell(~P14)
wumpus_kb.tell(~W14)
wumpus_kb.clauses
wumpus_kb.ask_if_true(P21)
wumpus_kb.tell(~S24)
wumpus_kb.tell(~B24)
wumpus_kb.tell(~P24)
wumpus_kb.tell(~W24)
wumpus_kb.clauses
wumpus_kb.ask_if_true(W23)
wumpus_kb.tell(~S21)
wumpus_kb.tell(~B21)
wumpus_kb.tell(~P21)
wumpus_kb.tell(~W21)
wumpus_kb.clauses
wumpus_kb.ask_if_true(B21)
wumpus_kb.tell(~S22)
wumpus_kb.tell(~B22)
wumpus_kb.tell(~P22)
wumpus_kb.tell(~W22)
wumpus_kb.clauses
wumpus_kb.ask_if_true(B22)
wumpus_kb.tell(B34)
wumpus_kb.tell(B23)
wumpus_kb.tell(B31)
wumpus_kb.tell(B32)
wumpus_kb.tell(B44)
wumpus_kb.tell(B42)
wumpus_kb.tell(S12 | '<=>' | ((W22 | W13)))
wumpus_kb.tell(~B12 | '<=>' | ((~P22 | ~P13)))
wumpus_kb.tell(B23 | '<=>' | ((P33 | P34)))

wumpus_kb.tell(B31 | '<=>' | ((P41| P23)))
wumpus_kb.tell(B32 | '<=>' | ((P33| P42)))
wumpus_kb.tell(B34 | '<=>' | ((P33| P44)))
wumpus_kb.clauses
wumpus_kb.ask_if_true(~P41)