class Roman:
    
    def __init__(self,number):
        if isinstance(number,str)==True:
            romanList=[ 'I', 'V' , 'X' , 'L' , 'C' , 'D' , 'M' ]
            m=0
            for i in range(len(number)):
                if number[i] not in romanList:
                    m=1
            if m==1:
                raise ValueError("not a roman number")
        elif not (number<2000000):
            raise ValueError('value is too big in absolute value to represent')
        elif number<0:
            Pnumber=-number
            b= self.romanConvertor(Pnumber)
            self.romanNum="-"+b
            self.integer = number
        else:
            self.romanNum = self.romanConvertor(number)
            self.integer= number
        
    def __repr__(self):
        return "Roman('%s')" % self.romanNum

    def __str__(self):
        return self.romanNum
    
    def __add__(self,other):
        if isinstance(other, Roman):
            return Roman(self.integer+other.integer)
        if isinstance(other,int):
            return Roman(self.integer+other)
            
    
    def __sub__(self,other):
        if isinstance(other,Roman):
            return Roman(self.integer-other.integer)
        if isinstance(other,int):
            return Roman(self.integer-other)
    
    def __mul__(self,other):
        if isinstance(other,Roman):
            return Roman(self.integer*other.integer)
        if isinstance(other,int):
            return Roman(self.integer*other)
    
    def __truediv__(self,other):
        if isinstance(other, Roman):
            return Roman(self.integer//other.integer),(self.integer%other.integer)
        if isinstance(other,int):
            return Roman(self.integer//other),(self.integer%other)
        
    def __floordiv__(self,other):
        if isinstance(other,Roman):
            return Roman(self.integer//other.integer)
        if isinstance(other,int):
            return Roman(self.integer//other)
    
    def __pow__(self,other):
        if isinstance(other,Roman):
            return Roman(self.integer**other.integer)
        if isinstance(other,int):
            return Roman(self.integer**other)
    
    def __eq__(self,other):
        if isinstance(other,Roman):
            return Roman(self.integer==other.integer)
        if isinstance(other,int):
            return Roman(self.integer==other)
    
    def __ne__(self,other):
        if isinstance(other,Roman):
            return Roman(self.integer!=other.integer)
        if isinstance(other,int):
            return Roman(self.integer!=other)
    
    def __lt__(self,other):
        if isinstance(other,Roman):
            return Roman(self.integer<other.integer)
        if isinstance(other,int):
            return Roman(self.integer<other)
    
    def __le__(self,other):
        if isinstance(other,Roman):
            return Roman(self.integer<=other.integer)
        if isinstance(other,int):
            return Roman(self.integer<=other)
    
    def __ge__(self,other):
        if isinstance(other,Roman):
            return Roman(self.integer>=other.integer)
        if isinstance(other,int):
            return Roman(self.integer>=other)
    
    def __gt__(self,other):
        if isinstance(other,Roman):
            return Roman(self.integer>other.integer)
        if isinstance(other,int):
            return Roman(self.integer>other)
    
    def __neg__(self):
        return Roman(-self.integer)
    
    def romanLogic(self,num):
        decimal=[1,   5,    10,   50,  100,  500,  1000]
        roman=[ 'I', 'V' , 'X' , 'L' , 'C' , 'D' , 'M' ]
        num2=[]
        i=-1
        rNumber=""
        while num!=0:
            i=i+1
            num2.append(num%10)
            num=num//10
            if(num2[i]<4):
                rNumber=num2[i]*roman[i*2]+rNumber
            elif(num2[i]==4):
                rNumber=roman[i*2]+roman[i*2+1]+rNumber
            elif(num2[i]<9):
                rNumber=roman[i*2+1]+(num2[i]%5)*roman[i*2]+rNumber
            elif(num2[i]==9):
                rNumber=roman[i*2]+roman[i*2+2]+rNumber
        return rNumber


    def romanConvertor(self, num):
        if num== 0:
            return 'N'
        elif num>3999:
            a=self.romanLogic(num// 1000)
            b="("+a+")"
            c=self.romanLogic(num% 1000)
            return b+c
        else:
            a= self.romanLogic(num)
            return a

j=0
while(j<1001):
    globals()[str(Roman(j))]=Roman(j)
    j=j+1
