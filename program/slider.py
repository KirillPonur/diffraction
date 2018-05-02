import numpy as np
from numpy import sin,cos,pi
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

la=640

la=la*10**(-9)
k=2*pi/la
N=15


phi=0
b0=1*10**(-3)
h=1*10**(-3)
d0=2*10**(-3)
theta=phi/180*pi
b=b0*cos(theta)-h*sin(theta)
d=d0*cos(theta)



fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.25)
# t = np.arange(0.0, 1.0, 0.001)
sint=np.linspace(-0.003,0.003,100000);
P=180/pi*3600
s = (sin(N*k*d*sint/2)/sin(k*d*sint/2))**2*(sin(k*b*sint/2)/((k*b*sint/2)))**2
l, = plt.plot(sint*P, s, c='red',linestyle='-',alpha=0.7,lw=1.4)
plt.yscale('log')
plt.axis([-500, 500, 10**-3, (N**2)*10])

axcolor = 'lightgoldenrodyellow'
# axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axphi = plt.axes([0.1, 0.15, 0.8, 0.03], facecolor=axcolor)

# sfreq = Slider(axfreq, 'Freq', 0.1, 30.0, valinit=f0, valstep=delta_f)
PHI = Slider(axphi, 'Phi', 0, 89, valinit=0)
# plt.xlim([-500,500])
# plt.ylim(ymin=10**-3,ymax=(N**2)*1.5)

def update(val):
	theta = PHI.val/180*pi
	# b0=1*10**(-3)
	# h=1*10**(-3)
	# d0=2*10**(-3)
	# theta=phi/180*pi
	b=b0*cos(theta)-h*sin(theta)
	d=d0*cos(theta)
	s = (sin(N*k*d*sint/2)/sin(k*d*sint/2))**2*(sin(k*b*sint/2)/((k*b*sint/2)))**2
	l.set_ydata(s)
	l.set_xdata(sint*P)
	fig.canvas.draw_idle()
# sfreq.on_changed(update)
PHI.on_changed(update)

# resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
# button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


# def reset(event):
    # sfreq.reset()
    # samp.reset()
# button.on_clicked(reset)

# rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
# radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)


# def colorfunc(label):
    # l.set_color(label)
    # fig.canvas.draw_idle()
# radio.on_clicked(colorfunc)

plt.show()