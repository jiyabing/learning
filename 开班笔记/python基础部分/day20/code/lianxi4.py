class Bicycle:
	def run(self,km):
		print('自行车骑行了',km,'公里')

class EBicycle(Bicycle):

	def __init__(self,v=5):
		self.volume = v
		
	
	
	def fill_charge(self,vol):
		self.volume += vol
		print('充电',vol,'度')
		print('此时电量',self.volume,'度')
	
	
	def run(self,km):
		'''
		if km <= self.volume*10:
			print('电动骑行了',km,'公里')
			self.volume -= km/10
			print('剩余电量',self.volume,'度')
		else:
			print('电动骑行了',self.volume*10,'公里')
			super().run(km-self.volume*10)
			self.volume = 0
		'''
		e_km = min(km,self.volume*10)
		if e_km > 0:
			print('电动骑行了',km,'公里')
			self.volume -= e_km/10
		if km > e_km:
			super().run(km - e_km)
	


b = EBicycle()
b.run(10)
b.fill_charge(5)
b.run(100)
b.fill_charge(6)
b.run(70)