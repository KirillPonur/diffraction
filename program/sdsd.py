import matplotlib as mpl
mpl.use( "cairo" )

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True

data = np.random.rand( 50, 50 )

plt.imshow( data, interpolation='nearest' )
plt.xlabel( 'X Label' )
plt.savefig( 'agg.pdf' )