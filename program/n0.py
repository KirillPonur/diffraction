import numpy as np
from numpy import sin,pi
# import matplotlib
# matplotlib.use('Agg')
from matplotlib import pyplot as plt 
sint=np.linspace(-0.01,0.01,100000);

la=640

b=0.52
N=1
plt.xlim([-2000,2000])

plt.ylim(ymin=10**-4,ymax=(N**2)*1.5)



la=la*10**(-9)
k=2*pi/la
b=b*10**(-3)
# d=d*10**(-3)

I0=1
DM=(sin(k*b*sint/2)/((k*b*sint/2)))**2


# x = np.arange(1,11) 
# y = 2 * x + 5 
plt.title("N="+str(N)+", b="+str(b*1000)+" мм, длина волны "+str(la*10**9)+' нм') 
plt.xlabel(r'Угол, в угловых секундах') 
plt.ylabel(r'Интенсивность, I')
# plt.ylabel("y axis caption"
P=180/pi*3600
# for i in [0,1,2,3,4,5,6,-1,-2,-3,-4,-5,-6]: 
	# plt.axvline(x=la*i/d*P,c='blue',linestyle='-.',alpha=0.5,lw=1)
# for i in [1,2,-1,-2]: 
	# plt.axvline(x=la*i/b*P,c='red',linestyle='--',alpha=0.5,lw=1)


# plt.plot(sint*P,RM,c='blue',linestyle='-',alpha=0.5,lw=1) 
# plt.plot(sint*P,DM,c='red',linestyle='-',alpha=0.5,lw=1) 
plt.yscale('log')
plt.plot(sint*P,DM,c='black',linestyle='-',alpha=1,lw=1.4) 
# plt.xticks([la/d],["1"])
# plt.show()
plt.savefig('../plot/N1.png', dpi=300, format='png')

# x=np.array([1,2,3])
# y=np.array([1,2,3])
# z=x*2;
# a=np.vstack((sint*P,RM,DM,RM*DM)).T
# a = np.array([ [1,2,3], [4,5,6], [7,8,9] ])
# print(a)
# columns=['theta','RM','DM','I']
# header='	'.join(columns)
# np.savetxt("../data/N15t.tsv", a,header=header,comments='',delimiter="	")