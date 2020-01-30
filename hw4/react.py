class Particle:
    
    def __init__(self, sym, chg, massNumber):
        self.sym = sym
        self.chg = chg
        self.massNumber = massNumber
    
    #this is code for extra marks (part1)
    def __add__(self,*other):
        return (self,*other)
    
    def __radd__(self, y):
        return self.__add__(*y)
    
    def __rmul__(self,other):
        i=0
        a=[]
        while(i<other):
            a.append(self)
            i=i+1
        return tuple(a)
    
    def __str__(self):
        return self.sym

    def __repr__(self):
        return self.sym


class Nucleus(Particle):
        
    def __str__(self):
        return "({}){}".format(self.massNumber, self.sym)
    
    def __repr__(self):
        return "({}){}".format(self.massNumber, self.sym)
    

class UnbalancedNumber(Exception):
    def __init__(self, diffMass):
        self.diffMass=diffMass
        print("diff masses=%s"% self.diffMass)
        pass

        
class UnbalancedCharge(Exception):
    def __init__(self, diffCharge):
        self.diffCharge=diffCharge
        print("diff charge=%s"% self.diffCharge)
        pass
class Reaction(Nucleus):
    
    def __init__(self, t1, t2):
        self.leftTuple=t1
        self.rightTuple=t2
        self.leftelements=[]
        self.rightelements=[]
        
        i=0
        while(i<len(self.leftTuple)):
            self.leftelements.append(self.leftTuple[i])
            i=i+1
            
        i=0
        while(i<len(self.rightTuple)):
            self.rightelements.append(self.rightTuple[i])
            i=i+1
        
        massLeft=0
        chargeLeft=0
        i=0
        while(i<len(self.leftTuple)):
            massLeft=massLeft+self.leftTuple[i].massNumber
            chargeLeft=chargeLeft+self.leftTuple[i].chg
            i=i+1
        massRight=0
        chargeRight=0
        i=0
        while(i<len(self.rightTuple)):
            massRight=massRight+self.rightTuple[i].massNumber
            chargeRight=chargeRight+self.rightTuple[i].chg
            i=i+1
        diffMass=massLeft-massRight
        
        if (diffMass!=0):
            raise UnbalancedNumber(diffMass)
        diffCharge=chargeLeft-chargeRight
        if (diffCharge!=0):
            raise UnbalancedCharge(diffCharge)
        
    def __str__(self):
        i=0
        a=removeMul(self.leftelements)
        b=removeMul(self.rightelements)
        return a + " -> " +b
    
#this function below is code for extra credit (part2) 
def removeMul(duplicate): 
    final_list = [] 
    s=""
    i=0
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num)
            count=duplicate.count(duplicate[i])
            if(count>1):
                s=s+str(count)+" "+'%s '%duplicate[i]
            else:
                s=s+'%s '%duplicate[i]
            length=len(duplicate)
            if(i<length-1):
                s=s+" + "
        i=i+1
    if(s[-1]=='+' or s[-2]=='+'):
        s=s[:-3]
    return s
        
def removeDupli(list1,list2):
    list1.reverse()
    list2.reverse()
    i=0
    while(i<len(list1)):
            
        j=0
        while(j<len(list2)):
            if(list1[i]==list2[j]):
                del list2[j]
                del list1[i]
                break
            j=j+1
        i=i+1
    list1.reverse()
    list2.reverse()
    
class ChainReaction:
    
    def __init__(self,name):
        self.name=name
        self.addreactions=[]
        self.netleft=[]
        self.netright=[]


    def addReaction(self,other):
        self.addreactions.append(other)
        self.netleft=self.netleft+other.leftelements
        self.netright=self.netright+other.rightelements
        
    def __str__(self):
        removeDupli(self.netleft,self.netright)
        removeDupli(self.netright,self.netleft)
        s=""
        s=s+self.name+" chain:"
        i=0
        
        while(i<len(self.addreactions)):
            s=s+"\n"+ str(self.addreactions[i])
            i=i+1
        a=removeMul(self.netleft)
        b=removeMul(self.netright)
        s=s+"\nnet \n"+str(a) +" -> "+ str(b)
        return s
    
    
if __name__=="__main__":
    
    em = Particle("e-", -1, 0)       # an electron
    ep = Particle("e+", 1, 0)        # a positron
    p = Particle("p", 1, 1)          # a proton
    n = Particle("n", 0, 1)          # a neutron
    nu_e = Particle("nu_e", 0, 0)    # a neutrino
    gamma = Particle("gamma", 0, 0)  # a gamma particle

    d = Nucleus("H", 1, 2)    # hydrogen
    li6 = Nucleus("Li", 3, 6) # lithium
    he4 = Nucleus("He", 2, 4) # helium
    he3 = Nucleus ("He", 2, 3)


    print(Reaction((li6, d), (he4, he4)))
    print(Reaction(li6 + d, he4 + he4))
    print(Reaction(li6 + d + he4, he4 + he4 + he4))
    print(Reaction(li6 + d, 2* he4))
    chnPP = ChainReaction ("proton - proton ( branch I)")
    for rctn in ( Reaction ((p, p), (d, ep , nu_e )),
            Reaction ((p, p), (d, ep , nu_e )),
            Reaction ((d, p), (he3 , gamma )),
            Reaction ((d, p), (he3 , gamma )),
            Reaction (( he3 , he3), (he4 , p, p ))):
        chnPP . addReaction ( rctn )
    print(chnPP)
    
    
    
