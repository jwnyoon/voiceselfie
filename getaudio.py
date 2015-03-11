
#!/usr/bin/python

import scipy
import numpy
import sys

from numpy import *

from scipy.io.wavfile import read
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pyplot
from scipy.fftpack import fft, ifft
from pylab import *
from pylab import figure,polar,show
from numpy import arange,pi,cos
from math import *

def getwavdata(file):
	return scipy.io.wavfile.read(file)[1]

callerId = sys.argv[1]

audio = getwavdata('/opt/nginx/html/voiceselfi/%s.wav' % callerId)	

w = numpy.fft.fft(audio)

idx = numpy.argmax(numpy.abs(w))
freq_in_hertz = abs(freq * 11025)
print(freq_in_hertz)

if freq_in_hertz > 200 and freq_in_hertz <500:
	colorc = '#EFF5FB'
	print colorc
elif freq_in_hertz >= 500 and freq_in_hertz <800:
	colorc = '#E0F8E6'
	print colorc
elif freq_in_hertz >= 800 and freq_in_hertz <1200:
	colorc= '#ECE0F8'
	print colorc
else:
	colorc= '#EFEFFB'
	print colorc


pyplot.axis('off')

 
def p(k,n):
   return(((k-2)*n*(n+1))/2 -(k-3)*n)

k=int(round(freq_in_hertz/44))
n=int(round(freq_in_hertz/10))

polygonal_nums = [p(k,n) for n in range(n)]
theta = [2*pi*sqrt(n) for n in polygonal_nums]
r = [sqrt(n) for n in polygonal_nums]
 


#sgram = angle_spectrum(audio,Fs=2)
# this worked but is ugly
pyplot.clf()


pyplot.polar(theta,r,alpha=0.2, color='gray', fillstyle='full', linewidth=0.5)
pyplot.fill_between(theta,r,1,facecolor='gray', alpha=0.1)

pyplot.axis('off')
pyplot.savefig('/opt/nginx/html/voiceselfi/%s.png' % callerId,facecolor=colorc, alpha=0.2)