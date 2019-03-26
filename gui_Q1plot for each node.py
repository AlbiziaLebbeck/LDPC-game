import tkinter
def plot():
    import math
    import random
    import numpy 
    #random.seed(1206701)
    import time
    
    start_time = time.clock()
    H = [[1,1,0,0,1,1,1,0],
         [0,1,1,1,0,0,0,0],
         [0,0,1,0,1,0,1,1],
         [0,0,0,1,0,1,1,1]]
    M = len(H)
    N = len(H[0])
    R = (N-M)/N
    print('R',R)
    snr = float(snr1.get())
    MAX_RUN = 1000
    MAX_ITERATION = 15
    MaxValue = 0.999999999
    MinValue = 0.000000001
    #print('H',H)

    EbN0dB = list(range(0,9))

    ber_uncoded = []
    ber_ldpc = []
    Q0_plot= numpy.zeros((MAX_ITERATION,N))
    Q1_plot= numpy.zeros((MAX_ITERATION,N))
    print('SNR:',snr)
    Eb = 1
    noise_variance       = 0.5*Eb*10**(-snr/10)
    print("noise",noise_variance)
    noise_variance_coded = 0.5/R*Eb*10**(-snr/10) #Watid
    print('Variance_uncoded',noise_variance)
    print('Variance_coded',noise_variance_coded)
    cnt_error_uncoded = 0
    cnt_error_ldpc = [0]*MAX_ITERATION
    for run in range(MAX_RUN):
        #data = [random.randint(0,1) for k in range(N)]
        #print('Data',data)
        data = [0, 0, 0, 0, 0, 0, 0, 0]
        bpsk = [2*k-1 for k in data]
        noise = [random.gauss(mu=0, sigma = math.sqrt(noise_variance))  for k in range(len(data))]
        noise_coded = [random.gauss(mu=0, sigma = math.sqrt(noise_variance_coded))  for k in range(len(data))] #Watid
        receive = [bpsk[k] + noise[k]  for k in  range(len(data))]
        receive_coded = [bpsk[k] + noise_coded[k]  for k in  range(len(data))] #Watid
        detect = [1 if k>0 else 0 for k in receive]
        uncode_error = [1 if detect[k]!=data[k] else 0 for k in range(N-M)] #Watid
        cnt_error_uncoded += sum(uncode_error)
        #print('Uncoded error',uncode_error)
        P0 = [1/(1+math.exp(2*r/noise_variance_coded)) for r in receive_coded] #Watid
        P1 = [1-p for p in P0]
        #print('P0',P0)
        #print('P1',P1)

        qij0 = []
        qij1 = []
        for m in range(M):
            qij0.append([])
            qij1.append([])
            for n in range(N):
                qij0[m].append(P0[n]*H[m][n])
                qij1[m].append(P1[n]*H[m][n])
        #print('qij0',qij0)
        #print('qij1',qij1)
                
        rij0 = []
        rij1 = []
        for m in range(M):
            rij0.append([])
            rij1.append([])
            for n in range(N):
                rij0[m].append(0)
                rij1[m].append(0)
        #print('rij0',rij0)
        #print('rij1',rij1)

        Q0 = []
        Q1 = []
        for n in range(N):
            Q0.append(0)
            Q1.append(0)
        
        for itr in range(MAX_ITERATION):
        #    print('Itr ---------',itr)
            for m in range(M):      
                prod_term = 1
                for k in range(N):
                    if H[m][k] != 0:
                        if qij1[m][k]>MaxValue:    #Watid
                            qij1[m][k] = MaxValue  #Watid
                        if qij1[m][k]<MinValue:    #Watid
                            qij1[m][k] = MinValue  #Watid
                            
                        prod_term *= 1-2*qij1[m][k]
                for n in range(N):
                    if H[m][n] != 0:
                            
                        rij0[m][n] = 0.5 + 0.5*prod_term/(1-2*qij1[m][n]);
                        rij1[m][n] = 1 - rij0[m][n];
            #print('rij0 = ',rij0)
            #print('rij1 = ',rij1)
                        
            for n in range(N):
                prod_rij0 = 1
                for m in range(M):
                    if H[m][n]!=0:
                        prod_rij0 *= rij0[m][n]
                Q0[n] = P0[n]*prod_rij0
                
                prod_rij1 = 1
                for m in range(M):
                    if H[m][n]!=0:
                        prod_rij1 *= rij1[m][n]
                Q1[n] = P1[n]*prod_rij1
            #print('Q0 = ',Q0)
            #print('Q1 = ',Q1)
                
            for m in range(M):
                for n in range(N):
                    if H[m][n]!=0:
                        
                        qij0[m][n] = Q0[n]/rij0[m][n]
                        qij1[m][n] = Q1[n]/rij1[m][n]

                        K = qij0[m][n] + qij1[m][n]
                        
                        qij0[m][n] /= K
                        qij1[m][n] /= K                      
            #print('qij0 =',qij0)
            #print('qij1 =',qij1)
            
            for n in range(N):
                K = Q0[n] + Q1[n]
                Q0[n] /= K
                Q1[n] /= K
            #print('Q0 = ',Q0)
            #print('Q1 = ',Q1)
                Q0_plot[itr][n]=Q0[n]
                Q1_plot[itr][n]=Q1[n]
            detect = [1 if Q1[k]>Q0[k] else 0 for k in range(N-M)]    #Watid
            error = [1 if detect[k]!=data[k] else 0 for k in range(N-M)]    #Watid
            
            #cnt_error_ldpc[itr] += sum(error)
            #print('Itr',itr,'error= ',error)
    #ber_ldpc.append([k/(MAX_RUN*(N-M)) for k in cnt_error_ldpc])    #Watid
    #ber_uncoded.append(cnt_error_uncoded/(MAX_RUN*(N-M)))    #Watid

    #ber_ldpc15 = [k[13] for k in ber_ldpc]
    EbN0 = [10**(k/10) for k in EbN0dB]
    #ber_uncoded_theory = [0.5*math.erfc(math.sqrt(k)) for k in EbN0]
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.gca()
    ax.set_xticks(numpy.arange(0, MAX_ITERATION+1, 1))
    #ax.set_yticks(numpy.arange(0.001, 0.1, 0.1))
    #plt.semilogy(EbN0dB,ber_uncoded,marker='o')
    #plt.semilogy(EbN0dB,ber_uncoded_theory,marker='x')
##    for n in range(N):
##     plt.plot(range(MAX_ITERATION),Q0_plot[:,n],marker='s')
##     plt.grid()
##     #plt.axis('scaled')
##     plt.show(block=False)
    for n in range(N):
     tmp = numpy.copy(Q1_plot[:,n])
     tmp = numpy.insert(tmp,0,P1[n])
     print('Tmp',tmp)
     plt.plot(range(MAX_ITERATION+1),tmp,marker='x')
     #print(Q1_plot)
     plt.grid()
     #plt.axis('scaled')
     plt.show(block=False)
    #plt.plot(range(MAX_ITERATION),P1,marker='s')

    
root = tkinter.Tk()
root.title("BER vs SNR plot")
bt = tkinter.Button(root, text="run", command=plot,bg='sky blue')
bt.place(x=6,y=6)
bt.config(height=4,width=8)
snr1= tkinter.StringVar()
snr_text=tkinter.Entry(root, width=10,textvariable=snr1)
snr_text.place(x=80,y=6)
