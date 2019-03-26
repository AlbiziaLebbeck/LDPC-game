import numpy as np
import random

MAX_RUN=1000
T= np.arange(0, MAX_RUN)

Q = np.zeros(MAX_RUN)

for run in range(0,MAX_RUN):
    H = np.zeros((4,8))
    for m in range (0,4):
        for n in range (0,8):
            H[m][n]= random.randint(0,1)
    print(H)
    n_2 = 0
    for i in range (0,4):
        for i1 in range (i,4):
            h = H[i,:]+H[i1,:]
            for k in range (0, h.shape[0]):
                if h[k]==2:
                    n_2=n_2+1

    if n_2>=2:
        
        Q[run]=1
    else  :
        
        Q[run]=0
print(Q)
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.gca()
ax.set_xticks(np.arange(0, MAX_RUN, 50))
#ax.set_yticks(numpy.arange(0.001, 0.1, 0.1))
plt.plot(T,Q,marker='o')
#plt.semilogy(EbN0dB,ber_uncoded_theory,marker='x')
##plt.semilogy(EbN0dB,ber_ldpc15,marker='s')
plt.grid()
#plt.axis('scaled')
plt.show(block=False)
