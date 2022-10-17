import Pyro5.api
import numpy as np

@Pyro5.api.expose
class Matriz(object):
    def salvaMatriz(self, arquivo, matriz):    
        """
        gravar = open(arquivo, '+w')
    
        matrix.write(str(matriz[0]).removeprefix('[').removesuffix(']').replace(',', ' '))
        linha = len(matriz)
        coluna = len(matriz[0])
        for i in range(linha):
            gravar.write('\n')
            for j in range(coluna):
                gravar.write(matriz[i][j])
                
        for row in range(1, len(matriz)):
            gravar.write(str(matriz[row]).removeprefix('[').removesuffix(']').replace(',', ' '))        
        gravar.close()
        """
        np.savetxt(arquivo, matriz, fmt="%.4f")        

    def salvarCronometro(self, tempo):
        arquivo = open("cronometro.txt", 'a+')
        arquivo.write("//" + str(tempo))        
        arquivo.close()     

    def carregaMatriz(self, arquivo):    
        """
        i = 0
        j = 0
        temp = ""
        matriz = np.ndarray([n, m], dtype="float")   
        for o in open(arquivo, "r"):        
            for q in o:
                if q != '\t' and q != '\n' and q != ' ' and q != '\r\n':  
                    temp += q    
                else:
                    matriz[i][j] = float(temp)
                    temp = ""
                    j += 1
            i+=1
            j = 0
        matriz[i - 1][i - 1] = float(temp)
        """
        matriz = np.loadtxt(fname=arquivo, dtype=float)
        return matriz

    def mul(self, A, B):
        linha = len(A)
        coluna = len(B[0])

        matrizFinal = np.ndarray([len(A), len(B[0])], dtype='float')
        for i in range(linha):
            for j in range(coluna):                
                matrizFinal[i, j] = np.dot(A[i], B[:, j])                                                                
                #matrizFinal[i + inicio, j] = sum([x * y for (x, y) in zip(A[i], B[:, j])])
                #[row[1] for row in A]                              
        return matrizFinal 

    def mulThread(self, A, B, queue):
        linha = len(A)
        coluna = len(B[0])

        matrizFinal = np.ndarray([len(A), len(B[0])], dtype='float')
        for i in range(linha):
            for j in range(coluna):                
                matrizFinal[i, j] = np.dot(A[i], B[:, j])                                                                
                #matrizFinal[i + inicio, j] = sum([x * y for (x, y) in zip(A[i], B[:, j])])
                #[row[1] for row in A]                              
        queue.put(matrizFinal)