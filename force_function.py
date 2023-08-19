import math as m

def force(IC, support_x, support_y, side_x, side_y, k_arc, delta_f_arc, P_f_arc, k_side, delta_f_side,
                  P_f_side, Mp):
	n = len(support_x + side_x)
	x1 = IC[0] # x1, IC for the elastic case
	y1 = IC[1] # y1, IC for the elastic case

	xi = [] #xi, distance from IC
	yi = [] #yi, distance from IC
	di = []
	deltai = []
	Ri = []

	Rxi = []
	Ryi = []
	moment = []

	fastener_x = support_x + side_x
	fastener_y = support_y + side_y

	for x in fastener_x:
		xi.append(x - x1)

	for y in fastener_y:
		yi.append(y - y1)

	for i in range(n):
		if di == 0:
			di.append(1e-7)
		else:
			di.append(m.sqrt(xi[i] **2 + yi[i]**2))

	gamma_side = 1 - (P_f_side/(k_side * delta_f_side))

	for i in range(len(support_x)): #support
		ratio = 0.3
		deltai.append((di[i] / max(di)) * delta_f_arc)
		if deltai[i] < P_f_arc / k_arc:
			Ri.append(k_arc * (deltai[i]) / P_f_arc)
		elif deltai[i] < (ratio*P_f_arc-P_f_arc)/(-k_arc)+P_f_arc/k_arc:
			Ri.append((-k_arc*(deltai[i]-P_f_arc/k_arc)+P_f_arc) / P_f_arc)
		else:
			Ri.append(ratio * P_f_arc/P_f_arc)
		moment.append(Ri[i] * di[i])

	for i in range(len(support_x), len(support_x + side_x)): #side-lap
		deltai.append((di[i] / max(di)) * delta_f_side)
		Ri.append((k_side*(deltai[i]-gamma_side*delta_f_side*(deltai[i]/delta_f_side)**(
				1/gamma_side)))/P_f_side)
		moment.append(Ri[i] * di[i])

	M_i = sum(moment) #Total moment of all the fasteners
	R_ult = -1 * Mp / M_i #Mp = moment about IC of normalized applied force P
	P_ult = -M_i/Mp

	for i in range(n):
		Rxi.append(-1 * (yi[i] * Ri[i]) / di[i] * R_ult)
		Ryi.append((xi[i] * Ri[i]) / di[i] * R_ult)

	Rx = sum(Rxi)
	Ry = sum(Ryi)

	output = [["R_ult", R_ult],["P_ult", P_ult],["x distance of fastener from IC", xi], ["y distance of "
	                                                                                           "fastener from IC", yi],
	         ["distance of fastener from IC",di], ["delta",deltai], ["force on one fastener",Ri],
	         ["x-component of fastener force", Rxi], ["y-component of fastener force", Ryi], ["M_i",moment]]

	return Rx, Ry, M_i, output