#Gustavo Coradin Guadagnin
file = open("arquivo1.txt", "r") #ler arquivo
vetor = [] #manipulações para colocar em matriz
matriz = []
vetor = file.readlines() 
for i in range(len(vetor)):     
    matriz.append(vetor[i].split())

operacoes=['U','I','D','C']#vetor para verificar qual a próxima operação

for j in range(len(matriz)):#verificação for no vetor operações
        if matriz[j][0] in operacoes:
            calculo=matriz[j][0]
            if calculo=='U':#verificando se é operação do tipo união
                a=matriz[j+1]
                b=matriz[j+2]
                c=a

                conjuntoAU=[]#for para tirar virgula do conjunto 1 
                for conjA in range(len(a)):
                    listaconjA=a[conjA]
                    conjA=listaconjA.replace(",","")
                    conjuntoAU.append(conjA)

                conjuntoBU=[]#for para tirar virgula do conjunto 2 
                for conjB in range(len(b)):
                    listaConjB=b[conjB]
                    conjB=listaConjB.replace(",","")
                    conjuntoBU.append(conjB)

                for item in b: #for para preencher o vetor do resultado (c) e tirar a repetição
                    if item not in a:
                        c.append(item)

                uniaoFinal=[] #for para tirar virgula
                for semV in range(len(c)):
                    lista=c[semV]
                    semVirgula=lista.replace(",","")
                    uniaoFinal.append(semVirgula)  
                print('Uniao: conjunto 1' ,'{',','.join(conjuntoAU),"}"",", 'conjunto 2' ,'{',','.join(conjuntoBU),"}"".", 'Resultado:;{',','.join(uniaoFinal),"}")#join para adicionar elementos necessários para apresentação final
                print("\n")

            elif calculo=='I':#verificando se e operação do tipo interseção
                aI=matriz[j+1]
                bI=matriz[j+2]
                d=[]
  
                conjunto_aI=[]#for para tirar virgula 
                for conj_aI in range(len(aI)):
                    listaconj_aI=aI[conj_aI]
                    conj_aI=listaconj_aI.replace(",","")
                    conjunto_aI.append(conj_aI)

                conjunto_bI=[]#for tirar virgula
                for conj_bI in range(len(bI)):
                    listaconj_bI=bI[conj_bI]
                    conj_bI=listaconj_bI.replace(",","")
                    conjunto_bI.append(conj_bI)
                

                for inter in aI:#for para para preencher o vetor do resultado (d) e tirar a repetição
                    if inter in bI:
                        d.append(inter)

                intersecao=[]#for para tirar virgula
                for semV2 in range(len(d)):
                    listaInter=d[semV2]
                    semVirgula2=listaInter.replace(",","")
                    intersecao.append(semVirgula2)
                print('Intersecao: conjunto 1' ,'{',','.join(conjunto_aI),"}"",", 'conjunto 2' ,'{',','.join(conjunto_bI),"}"".", 'Resultado:{',','.join(intersecao),"}")#join para adicionar elementos necessários para apresentação final
                print("\n")    


            elif calculo=='D':#verificando se e operação do tipo diferença
                aD=matriz[j+1]
                bD=matriz[j+2]
                e=[]

                conjunto_aD=[]#for para tirar virgula
                for conj_aD in range(len(aD)):
                    listaconj_aD=aD[conj_aD]
                    conj_aD=listaconj_aD.replace(",","")
                    conjunto_aD.append(conj_aD)
                
                conjunto_bD=[]#for para tirar virgula
                for conj_bD in range(len(bD)):
                    listaconj_bD=bD[conj_bD]
                    conj_bD=listaconj_bD.replace(",","")
                    conjunto_bD.append(conj_bD)

                for dif in aD:#for para para preencher vetor de resultado (e) e tirar repetição
                    if dif not in bD:
                        e.append(dif)

                diferencaFinal=[]#for para tirar virgula
                for semV3 in range(len(e)):
                    listaDif=e[semV3]
                    semVirgula3=listaDif.replace(",","")
                    diferencaFinal.append(semVirgula3)
                print('Diferenca: conjunto 1'  ,'{',','.join(conjunto_aD),"}"",", 'conjunto 2'  ,'{',','.join(conjunto_bD),"}"".", 'Resultado:{',','.join(diferencaFinal),"}")#join para adicionar elementos necessários para apresentação final
                print("\n")
            else:#em caso de não se encaixar em nenhuma das operações acima cai em produto cartesiano
                aC=matriz[j+1]
                bC=matriz[j+2]
                f=[]
                
                conjunto_aC=[]
                for conj_aC in range(len(aC)):#for tirar virgula
                    listaconj_aC=aC[conj_aC]
                    conj_aC=listaconj_aC.replace(",","")
                    conjunto_aC.append(conj_aC)
                
                conjunto_bC=[]
                for conj_bC in range(len(bC)):#for tirar virgula
                    listaconj_bC=bC[conj_bC]
                    conj_bC=listaconj_bC.replace(",","")
                    conjunto_bC.append(conj_bC)
                for x in aC:#for para preencher vetor de resultado (f) e tirar repeticao
                    for y in bC:
                        if (x+y) not in f:
                            f.append(x+y)

                pcFinal=[]#for para tirar virgula de pcFinal(resultado)
                for semV4 in range(len(f)):
                    listaPc=f[semV4]
                    semVirgula4=listaPc.replace(",","")
                    pcFinal.append(semVirgula4)

                print('Produto cartesiano: conjunto 1'  ,'{',','.join(conjunto_aC),"}"",", 'conjunto 2'  ,'{',','.join(conjunto_bC),"}"".", 'Resultado:{(',')'';''('.join(pcFinal),')'"}")#join para adicionar elementos necessários para apresentação final