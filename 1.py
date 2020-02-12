global xx
xx=0
def bian(x):
    sum1=0
    sum2=0
    sum3=0
    sum4=0
    sum5=0
    sum6=0
    
    global xx
    if x[0]=='十' and xx==0:
        x='一'+x
        xx+=1
    for i in range(0,len(x)):
        if x[i]=='十' or x[i]=='百' or x[i]=='千' or x[i]=='万' or x[i]=='亿':
            sum1=1
    for i in range(0,len(x)):
        if x[i]=='零':
            sum4=1
    if x[0]=='负':
        return (-1)*bian(x[1:])
    else:
        if len(x)==1:
            if x=='十':
                return 10
            elif x=='九':
                return 9
            elif x=='八':
                return 8
            elif x=='七':
                return 7
            elif x=='六':
                return 6
            elif x=='五':
                return 5
            elif x=='四':
                return 4
            elif x=='三':
                return 3
            elif x=='二':
                return 2
            elif x=='一':
                return 1
            elif x=='零':
                return 0
            elif x=='百':
                return 100
            elif x=='千':
                return 1000
            elif x=='万':
                return 10000
            elif x=='亿':
                return 100000000
            else:
                return x
        elif len(x)==2 :
            if x[len(x)-1]=='十':
                return int(bian(x[0]))*int(bian(x[1]))
            elif x[len(x)-1]=='百':
                return int(bian(x[0]))*int(bian(x[1]))
            elif x[len(x)-1]=='万':
                return int(bian(x[0]))*int(bian(x[1]))
            elif x[len(x)-1]=='千':
                return int(bian(x[0]))*int(bian(x[1]))
            elif x[len(x)-1]=='亿':
                return int(bian(x[0]))*int(bian(x[1]))
            elif x[0]=='十':
                return int(bian(x[0]))+int(bian(x[1]))
            else:
                return bian(x[0])*10+bian(x[1])
        elif len(x)==3 and x[1]=='十':

            if danwei(x[2])==0:
                return bian(x[0])*10+bian(x[2])
            elif danwei(x[2])==1:
                return bian(x[0])*10*bian(x[2])
        elif len(x)>2 and sum1==0 :
            sum3=len(x)
            for i in range(0,len(x)):
                sum2+=bian(x[i])*(10**(sum3-1))
                sum3-=1
            return sum2
        elif sum4==0:
            for i in range(0,len(x)-1,2):
                if danwei(x[i+1])==1:
                    if bian(x[i])*bian(x[i+1])<sum5:
                        sum5+=bian(x[i])*bian(x[i+1])
                    else:
                        sum5=(sum5+bian(x[i]))*bian(x[i+1])
            if len(x)%2!=0:
                if bian(x[len(x)-1])<sum5:
                    sum5+=bian(x[len(x)-1])
                else:
                    sum5*=bian(x[len(x)-1])
            return sum5
        elif sum4==1:
            for i in range(1,len(x),2):
                if danwei(x[i])==1:
                    if bian(x[i-1])*bian(x[i])<sum6:
                        sum6+=bian(x[i-1])*bian(x[i])
                        i=i+2
                    else:
                        sum6=(sum6+bian(x[i-1]))*bian(x[i])
                        i=i+2
                elif danwei(x[i])==2 and i==len(x)-1:
                    sum6*=bian(x[i-1])
                elif danwei(x[i-1])==2 :
                    i+=1
                elif danwei(x[i-1])!=2 and danwei(x[i])==2:
                    sum6=sum6*bian(x[i-1])
                elif danwei(x[i])==0:
                    sum6+=x[i]
                i=i-1
            if i==len(x)-1:
                sum6+=bian(x[i])
            if i<len(x)-1:
                sum6+=bian(x[len(x)-1])
            
            return sum6

def danwei(x):
    if x=='十' or x=='百' or x=='千' or x=='万' or x=='亿':
        return 1
    elif x=='零':
        return 2
    else:
        return 0
def jisuan(a,x,y):
    if a=='增加':
        return x+y
    elif a=='加':
        return x+y
    elif a=='减':
        return x-y
    elif a=='减少':
        return x-y
    elif a=='乘':
        return x*y
    elif a=='乘以':
        return x*y
    elif a=='除':
        return x/y
    elif a=='除以':
        return x/y
    elif a=='等于':
        return y
    elif a=='取余':
        return x%y

        
def bijiao(a,x,y):
    x=bian(x)
    y=bian(y)
    if a=='大于':
        return x>y
    if a=='小于':
        return x<y
    if a=='等于':
        return x==y
    if a=='小于等于':
        return x<=y
    if a=='大于等于':
        return x>=y
    if a=='不等于':
        return x!=y
def bian2(x):
    a=''
    a1=0
    a2=0
    sum1=''
    sum2=0
    sum3=''
    sum4=0
    for i in range(0,len(x)):
        if x[i]=='0':
            a1=1
    for i in range(1,len(x)):
        if x[i]!='0':
            a2=1
    
    if x[0]=='-':
        return'负'+bian2(x[1:])
    elif x[0]=='一' or x[0]=='二' or x[0]=='三'or x[0]=='四' or x[0]=='五' or x[0]=='六' or x[0]=='七' or x[0]=='八' or x[0]=='九' or x[0]=='十' or x[0]=='零' or x[0]=='负':
        return x
    else:
        if len(x)==1:
            if x=='10':
                return '十'
            elif x=='9':
                return '九'
            elif x=='8':
                return '八'
            elif x=='7':
                return '七'
            elif x=='6':
                return '六'
            elif x=='5':
                return '五'
            elif x=='4':
                return '四'
            elif x=='3':
                return '三'
            elif x=='2':
                return '二'
            elif x=='1':
                return '一'
            elif x=='0':
                return '零'
            else:
                return x
        elif len(x)==2:
            for i in range(0,len(x)):
                a+=bian2(x[i])
            return zheng(a)
        elif len(x)>2 and a1==0:
            sum2=len(x)
            for i in range(0,len(x)):
                if i!=len(x)-1:
                    sum2-=1
                    sum1+=bian2(x[i])+danwei2(sum2)
                else:
                    sum1+=bian2(x[i])
            return danwei3(sum1)
        elif len(x)>2 and a1==1:
            sum2=len(x)-1
            if a2==0:
                return danwei3(bian2(x[0])+danwei2(sum2))
            else:
                sum4=len(x)-1
                sum4=int(sum4)
                for i in range(0,len(x)-1):
                    if bian2(x[i])!='零':
                        sum3=sum3+bian2(x[i])+danwei2(sum4)
                    elif bian2(x[i-1])=='零'and bian2(x[i])=='零':
                        sum3=sum3
                    else:
                        sum3=sum3+bian2(x[i])
                    sum4=sum4-1
                sum3+=bian2(x[len(x)-1])
                if sum3[len(sum3)-1]=='零':
                    sum3=sum3[0:len(sum3)-1]
                return danwei3(sum3)
def danwei3(x):
    if x[len(x)-1]=='零':
        x=x[0:len(x)-1]
    a=x.split('万')
    c=x.split('亿')
    sum0=''
    sum1=''
    if len(a)>=3 or len(c)>=3:
        if len(a)>=3:
            for i in range(0,len(a)-1):
                sum0+=a[i]
            sum0+='万'+a[len(a)-1]
            sum1=sum0
        elif len(c)>=3:
            sum0=x
            b=sum0.split('亿')
            for i in range(0,len(b)-1):
                sum1+=b[i]
            sum1+='亿'+b[len(b)-1]
        return sum1
    else:
        return x
def danwei2(x):
    if x==3:
        return '千'
    elif x==2:
        return '百'
    elif x==1:
        return '十'
    elif x==4:
        return '万'
    elif x==5:
        return '十万'
    elif x==6:
        return '百万'
    elif x==7:
        return '千万'
    elif x==8:
        return '亿'
    elif x==9:
        return '十亿'
    elif x==10:
        return '百亿'
        
def zheng(x):
    a=0
    sum1=0
    
    for i in range(0,len(x)):
        if x[i]!='零':
            a=1
        else:
            sum1+=1   
    if a==0:
        if sum1==1:
            return '十'
        elif sum1==2:
            return x[0]+'百'
        elif sum1==3:
            return x[0]+'千'
        elif sum1==4:
            return x[0]+'万'
        elif sum1==5:
            return x[0]+'十万'
        elif sum1==6:
            return x[0]+'百万'
        elif sum1==7:
            return [0]+'千万'
        elif sum1==8:
            return x[0]+'亿'
        elif sum1==9:
            return x[0]+'十亿'
        elif sum1==10:
            return x[0]+'百亿'
        elif sum1==11:
            return x[0]+'千亿'
        elif sum1==12:
            return x[0]+'万亿'
    elif x[0]=='零':
        return bian2(x[1:])
    elif len(x)==2 and x[0]!='十':
        if x[0]!='一':
            if x[1]!='零':
                return x[0]+'十'+x[1]
            else:
                return x[0]+'十'
        else:
            if x[1]!='零':
                return '十'+x[1]
            else:
                return '十'
    else:
        
        return x
    
            
global zz
zz=0
def shuru(a):
    z1=0
    z2=0
    z3=1
    z4=0
    z5=0
    z6=0
    z7=0
    z8=''
    z9=len(a)
    z10=0
    z11=''
    global zz
    for i in range(0,z9):
        z9=len(a)
        for j in range(0,z9):
            if a[j]=='':
                a.pop(j)
                break
    if a[0]== '整数':
        if zz==0:
            zz=1
        elif zz!=0:
            for x in range(0,len(b)):
                if b[x]==a[1]:
                    print("变量已存在")
                    z6=1
                    break;
        if z6==0:
            b.append(a[1])
            if a[2]== '等于':
                c.append(bian2(a[3]))
                
    elif a[0]== '看看':
        for i in range(len(b)):
            if b[i]==a[1]:
                print(bian2(c[i]))
                z1=1
                break
        if a[1][0]=='“':
            while a[1][z3]!='”': 
                print(a[1][z3],end='')
                z3+=1
        elif z1==0:
            print(a[1]+'不存在')     
    elif a[0]=='如果':
        for i in range(len(b)):
            if b[i]==a[1]:
                for j in range(len(b)):
                    if b[j]==a[3]:
                        z7=1
                if z7==0:
                    z8=a[3]
                else:
                    z8=c[j]
                if bijiao(a[2],c[i],z8)==True:
                    if a[4]=='则':
                        for x in range(5,len(a)):
                            if a[x]=='否则':
                                z2=1
                                break
                        if z2==1:
                            shuru(a[5:x])
                        else:
                            shuru(a[5:])
                elif bijiao(a[2],c[i],z8)==False:
                    
                    for x in range(4,len(a)):
                        if a[x]=='否则':
                            z4=1
                            break       
                    if z4==1:
                        shuru(a[x+1:])
    elif a[0]=='无':
        z5+=1
    else:
        
        for i in range(len(b)):
            if b[i]==a[2]:
                z10=1
                break
        if z10==1:
            z11=c[i]
        else:
            z11=a[2]
        for i in range(len(b)):
            if b[i]==a[0]:
                c[i]=bian2(str(int(jisuan(a[1],int(bian(c[i])),int(bian(z11))))))
b=[]
c=[]
a=(input().split(' '))
while len(a)!=1:
    shuru(a)
    a= (input().split(' '))
    
