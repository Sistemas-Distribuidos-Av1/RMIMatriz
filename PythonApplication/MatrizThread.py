from multiprocessing import Process, Pool, Queue
from typing import Iterable
from base import Matriz
import numpy as np
import time

if __name__ == "__main__":                
    A = Matriz.carregaMatriz(Matriz, "matA.txt")
    B = Matriz.carregaMatriz(Matriz, "matB.txt")        
    matrizFinal = np.ndarray([len(A), len(B[0])], dtype='float')    
    #matrizFinal = []    
    #processos = []

    #queue = Queue()
    start_timer = time.time()

    with Pool() as pool:
        for i in range (8):
            #matrizFinal.append(pool.starmap(Matriz.mul, [(Matriz, A[i * 512 : i * 512 + 512,], B[:])]))
            #matrizFinal.append(pool.starmap(Matriz.mul, [(Matriz, A[i * 4 : i * 4 + 4,], B[:])]))
            matrizFinal[i * 512: i * 512 + 512,] = pool.starmap(Matriz.mul, [(Matriz, A[i * 512 : i * 512 + 512,], B[:])]).pop()            
            #matrizFinal[i * 4: i * 4 + 4,] = pool.starmap(Matriz.mul, [(Matriz, A[i * 4 : i * 4 + 4,], B[:])]).pop()            
        #for result in pool.starmap(Matriz.mul, [(Matriz, A[i : i + 512,], B[:])]):
        #    print()
    """
    for x in range(8):
        t = x * 512
        processo = Process(target = Matriz.mul, args = (Matriz, A[t : t + 512,], B[:]))
        processo.start()
        processos.append(processo)

    [processos[x].join() for x in range(8)]    
    #[processos[x].close() for x in range(8)]
    """
    end_timer = time.time() - start_timer   
    print("Passou")
    #print(matrizFinal)
    """
    for x in range(8):
        t = x * 512
        matrizFinal[t: t + 512, :] = queue.get()        
    """
    Matriz.salvarCronometro(Matriz, end_timer)
    Matriz.salvaMatriz(Matriz, "matC.txt" ,matrizFinal)      