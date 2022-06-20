#              0               1         2               3               4            5          6          7
pontos=['Rio de Janeiro','V.Redonda','Resende','Aparecida do Norte','S.J.Campos','São Paulo','Jundiai','Campinas']

trebrigatorio=['Rio de Janeiro / São Paulo','Rio de Janeiro / V.Redonda','Rio de Janeiro / S.J.Campos','Rio de Janeiro / Campinas','V.Redonda / S.J.Campos','V.Redonda / São Paulo','V.Redonda / Campinas','S.J.Campos / São Paulo','S.J.Campos / Campinas','São Paulo / Campinas' ]

passageiros=[7308,2198,210,483,85,280,43,8995,1449,12581]

indexobrig=[[0,4],[0,0],[0,3],[0,6],[1,3],[1,4],[1,6],[4,4],[4,6],[5,6]]


km=[[113,167,270,353.4,445.8,499.2,537.8],       #Rio de Janeiro
    [113,54,157,240.4,332.4,385.8,424.8],        #V.Redonda
    [167,54,103,186.4,278.8,332.2,370.8],        #Resende
    [270,157,103,83.4,175.8,229.2,267.8],        #Aparecida do Norte
    [353.4,240.4,186.4,83.4,92.4,145.8,184.4],   #S.J.Campos
    [445.8,332.8,278.8,175.8,92.4,53.4,92],      #São Paulo
    [499.2,386.2,332.2,229.2,145.8,53.4,38.6],   #Jundiai
    [537.8,424.8,370.8,267.8,184.4,92,38.6]]     #Campinas

porcentagem=[]

vale=[]

def viabilidade():
    print("\n")
    for i in range(len(trebrigatorio)):
        t=indexobrig[i]
        km2=float(km[t[0]][t[1]])
        tarifa=0.49*km2
        custo=1250000*km2
        receita=tarifa*passageiros[i]
        porcent=(receita/custo)*100

        if porcent >= 10:
            print("\nO trecho",trebrigatorio[i],"é viavel, lucro estimado de R$","%.2f" % (receita-custo))
            print("Tarifa","%.2f" % tarifa)
            print("Custo anual: R$","%.2f" % custo)
            print("Receita anual: R$","%.2f" % receita)
            print("Kilometragem:","%.2f" % km2,"km")
            vale.append(trebrigatorio[i])
        else:
            print("\nO trecho",trebrigatorio[i],"não é viavel, prejuizo estimado de R$","%.2f" % (receita-custo))
            print("Tarifa: R$","%.2f" % tarifa)
            print("Custo anual: R$","%.2f" %  custo)
            print("Receita anual: R$","%.2f" % receita)
            print("Kilometragem:","%.2f" % km2,"km")
 
    if len(vale) >= 8: 
        print("\nFerrovia viável como um todo")
    else:
        print("\nFerrovia inviável como um todo")
    vale.clear()


  
def trechobrigatorio(r):
    print("\nQual das opções você deseja calcular?")
    for i in range(len(trebrigatorio)):
        print(i,"para o trecho",trebrigatorio[i])

    n=int(input())

    if n > 9:
        print("\nCaractere invalido, retornando..")
        return

    t=indexobrig[n]

    km2=float(km[t[0]][t[1]])

    global tarifa
    tarifa=0.49*km2

    if r == 3:
        pa=passageiros[n]
        custo=1250000*km2
        pessoas=custo/tarifa
        pessoas10=pessoas*1.10
        receita=pessoas10*tarifa
        por=(pessoas10/pa)*100

        return pessoas10,custo,receita,n,por,pa
    
    if r == 2:
        p=passageiros[n]
        c=30
        h=0
        for h in range(4):
            porcentagem.append("%.2f" % float(p*(c/100)))
            c+=10
        return tarifa,n,p

    if r == 1:
        custo=1250000*km2
        return custo,n,km2

    return tarifa,n,km2

def tarifasimulada(r):
    print("\nQual a estação de partida?")
    for i in range (len(pontos)):
        print(i,"para",pontos[i])

    p = int(input())

    if p > 7:
        print("\nCaractere invalido, retornando..\n")
        return

    global opcoes
    opcoes = [x for x in pontos if pontos.index(x) != p]

    print("Qual a estação de destino?")
    for i in range (len(opcoes)):
        print(i,"para", opcoes[i])

    d=int(input())

    if d > 6:
        print("\nCaractere invalido, retornando..\n")
        return

    km2=float(km[p][d])
  
    tarifa=0.49*km2

    if r == 2:
        custo=1250000*km2
        pessoas=custo/tarifa
        pessoas10=pessoas*1.10
        receita=pessoas10*tarifa
        return pessoas10,custo,receita,p,d


    if r == 1:
        custo=1250000*km2
        return custo,p,d,km2

    return tarifa,p,d,km2
        

print("\nSelecione o que deseja:")

while True:
    a=int(input("1 para Cálculo da tarifa ao passageiro por trecho\n2 para Cálculo do custo operacional anual por trecho\n3 para Cálculo da projeção anual de receitas\n4 para calcular a quantidade minima de passageiros\n5 para verificar a viabilidade de cada trecho "))
    
    if a == 1:
        d=int(input("\n1 para calcular opções de trechos obrigatórios\n2 para simular qualquer uma das estações "))

        if d == 1:
            r=0
            t=trechobrigatorio(r)
            print("\nA tarifa para o trecho",trebrigatorio[t[1]],"é de: R$","%.2f" % t[0])
            print("A distância para esse trecho é de",t[2],"km")
        elif d == 2:
            r=0
            t=tarifasimulada(r)
            print("\nA tarifa para o trecho",pontos[t[1]],"/",opcoes[t[2]],"é de: R$","%.2f" % t[0])
            print("A distância para esse trecho é de",t[3],"km")
            opcoes.clear()
        else:
            print("\nOpção invalida, retornando..\n")

    elif a == 2:
        d=int(input("\n1 para calcular opções de trechos obrigatórios\n2 para simular qualquer uma das estações "))

        if d == 1:
            r=1
            c=trechobrigatorio(r)
            print("\nO custo para o trecho",trebrigatorio[c[1]],"é de: R$","%.2f" % c[0])
            print("A distância para esse trecho é de",c[2],"km")

        elif d == 2:
            r=1
            c=tarifasimulada(r)
            print("\nO custo para o trecho",pontos[c[1]],"/",opcoes[c[2]],"é de: R$","%.2f" % c[0])
            print("A distância para esse trecho é de",c[3],"km")
            opcoes.clear()
        else:
            print("\nOpção invalida, retornando..\n")    

    elif a == 3:
        r=2
        r=trechobrigatorio(r)
        print("\nPara essa projeção de receitas tomamos como referencia",r[2],"pessoas.\n")
        
        nu = 30
    
        print("A receita anual para o trecho",trebrigatorio[r[1]],"é de:")
        for i in range(4):
            print("R$","%.2f" % (tarifa*float(porcentagem[i])),"para",nu,"%","dos passageiros.")
            nu+=10
        
        porcentagem.clear()
    elif a == 4:

        d=int(input("\n1 para calcular opções de trechos obrigatórios\n2 para simular qualquer uma das estações "))
        if d == 1:
            r=3
            qtd=trechobrigatorio(r)
            print("\nSão necessarias pelo menos",int(qtd[0]),"pessoas para o trecho",trebrigatorio[qtd[3]],"ter 10","%","de lucro")
            print(int(qtd[0]),"pessoas equivale a um aumento de",int(qtd[4]),"%","em relação ao total de passageiros desse trecho")
            print("Com",int(qtd[0]),"pessoas a receita é R$","%.2f" % qtd[2],"\nO custo anual para esse trecho é R$",qtd[1])
            print("Lucro estimado de R$","%.2f" % (qtd[2]-qtd[1]))
            print("Como referencia tomamos como base",qtd[5],"passageiros")


        elif d == 2:
            r=2
            q=tarifasimulada(r)
            print("\nSão necessarias pelo menos",int(q[0]),"pessoas para o trecho",pontos[q[3]],"/",opcoes[q[4]],"ter 10","%","de lucro")
            print("Com",int(q[0]),"pessoas a receita é R$","%.2f" % q[2],"\nO custo anual para esse trecho é R$",q[1])
            print("Lucro estimado de R$","%.2f" % (q[2]-q[1]))
            opcoes.clear()
    
    elif a == 5:
        viabilidade()

    else:
        print("\nEscolha invalida.")
    
    x=int(input("\nQuer fazer outra consulta? 1 para sim, qualquer outro numero para não "))

    if x!=1:
        print("\nFim")
        break
    