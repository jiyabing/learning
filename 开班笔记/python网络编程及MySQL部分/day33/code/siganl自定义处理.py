from signal import *
from time import sleep

def func(sig,frame):
	if sig == SIGALRM:
		print('alarm ring')
	elif sig == SIGINT:
		print("can't stop")

alarm(7)

signal(SIGALRM, func)
signal(SIGINT, SIG_DFL)

while True:
	print('wait for a signal...')
	sleep(2)