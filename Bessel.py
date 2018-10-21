import sympy

#Se encarga de realizar el polinomio de Bessel de manera recursiva y solo es necesario darle el orden
def PoliBessel (N):
    s=sympy.Symbol('s')
    B1=s+1
    B2=(s**2)+(3*s)+3
    if N==1:
        B= B1
    elif N==2:
        B= B2
    else:
        B=sympy.expand ( (2*N-1)*PoliBessel(N-1)+(s**2)*PoliBessel(N-2))
    return B

#Se encarga de realizar la normalizacion para bessel
def NormaBessel(Retardo,Wrg):
    #Normalizo la frecuencia de paso
    Wrgn=Retardo*Wrg
    return Wrgn

'''Se encarga de devolver los coeficientes de la funcion tranferencia de Bessel
Recibe el Retardo de grupo querido, la frecuencia a la cual el retardo de grupo
debe superar una cierta tolerancia y la tolerancia es Porcentaje/100
Por ultimo,el Nmax por predeterminado es 15 para evitar un fitro muy grande'''
def AproxBessel(Retardo,Wrg,Tol,N=0,Nmin=0,Nmax=15):
    s=sympy.Symbol('s')
    Wn=NormaBessel(Retardo,Wrg)
    if N == 0:
        #Trato de obtener la funcion de bessel que cumpla con lo pedido
        N=1
        #Si tengo un valor de Nmin voy a empezar desde ahi
        if Nmin != 0:
            N=Nmin
        while (N < Nmax) and (Nmin<=N):
            Polinomio = PoliBessel(N)
            Tranferencia = Polinomio.subs(s,0)/Polinomio.subs(s,1j*Wn)
            Temp= ( ( Wn**(2*N) ) * (abs(Tranferencia)**2) )/ (Polinomio.subs(s,0)**2)
            if (Temp<Tol):
                print(Temp)
                break
            else:
                N+=1
        #Chequeo para ver si estoy en el Nmax
        if N == Nmax:
            Polinomio = PoliBessel(N)
            Tranferencia = Polinomio.subs(s,0)/Polinomio.subs(s,1j*Wn)
            print("Se alcanzo el limite")
        elif N == Nmin:
            print("Se alconzo el minimo")
    else:
        Polinomio = PoliBessel(N)
        Tranferencia = Polinomio.subs(s,0)/Polinomio.subs(s,1j*Wn)
    return N,Polinomio

def main():
    print(AproxBessel(10e-03,600,0.20,6,2,7))

if __name__ == "__main__":
    main()