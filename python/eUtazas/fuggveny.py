def Napokszama(e1,h1,n1,e2,h2,n2):
	h1 = (h1 + 9) % 12
	e1 = e1 - h1 // 10
	d1= 365*e1 + e1 // 4 - e1 // 100 + e1 // 400 + (h1*306 + 5) // 10 + n1 - 1
	h2 = (h2 + 9) % 12
	e2 = e2 - h2 // 10
	d2= 365*e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2*306 + 5) // 10 + n2 - 1
	napokszama= d2-d1
	return napokszama