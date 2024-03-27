k= .23 #speed constatn min^-1
Vol0=600 #vol flow rate  dm^3/min

def dcadv(ca):
    ra = -k*ca 
    return  ra/Vol0

def RK4(v0,ca0,v,h):
    n=(int)((v-v0)/h)
    ca=ca0
    for i in range(1,n-1):
        k1=dcadv(ca)                 
        k2=dcadv(ca+h*k1*0.5)                 
        k3=dcadv(ca+h*k2*0.5)                 
        k4=dcadv(ca+h*k3)                 
        ca=ca+h*(k1+2*k2+2*k3+k4)/6
    return ca
h=0.0001
ca0=10 #initile concenteration mole/dm^3
v=100 #volume After the procces dm^3
print(f"the value of ca at v=100 is {RK4(0,ca0,v,h)}")

