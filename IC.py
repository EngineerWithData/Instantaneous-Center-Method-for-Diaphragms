from force_function import *
import math as m

def IC(support_x, support_y, side_x, side_y, k_arc, delta_f_arc, P_f_arc, k_side, delta_f_side, P_f_side, Ecc_x,
      Ecc_y, Ecc_angle):

	fastener_x = support_x + side_x
	fastener_y = support_y + side_y
	n = len(fastener_x) # quantity of fasteners
	output = []
	output.append(n)

	x_o = sum(fastener_x)/len(fastener_x) # x-centroid
	y_o = sum(fastener_y)/len(fastener_y) # y-centroid

	Ecc_radian = m.radians(90 - Ecc_angle)
	P_x = -1 * m.cos(Ecc_radian) #x-component of P
	P_y = -1 * m.sin(Ecc_radian) #y-component of P
	Mo = (-1 * P_x * (Ecc_y - y_o)) + (P_y * (Ecc_x - x_o)) # moment of P about the centroid

	J = 0
	for i in range(n):
		J = J + (fastener_x[i] - x_o) ** 2 + (fastener_y[i] - y_o) ** 2

	ax = (-1*P_y*J) / (n*Mo) # x-component of distance from centroid of fastener group to IC
	ay = (P_x*J) / (n*Mo) # y-component of distance from centroid of fastener group to IC
	elastic_IC = [x_o + ax, y_o + ay]  # Instantaneous Center
	Mp = (-1 * P_x * (Ecc_y - y_o - ay)) + (P_y * (Ecc_x - x_o - ax)) # moment of P about I.C.

	Rx, Ry, Mi, table_ = force(elastic_IC, support_x, support_y, side_x, side_y, k_arc,
	                                   delta_f_arc, P_f_arc, k_side, delta_f_side, P_f_side, Mp)

	output.append(["P of unit magnitude", P_x, P_y])
	output.append(["Moment of P about centroid", Mo])
	output.append(['Polar moment of inertia', J])
	output.append(["x- component of distance from centroid to IC", ax,
	               "y- component of distance from centroid to IC", ay])
	output.append(["Mp", Mp])
	output.append(["Rx", Rx, "Ry", Ry, "Mi", Mi, "Per fastener output", table_])

	F_xx = P_x + Rx # x-component of unbalanced force
	F_yy = P_y + Ry # y-component of unbalanced force
	F = m.sqrt(F_xx ** 2 + F_yy ** 2) #magnitude of unbalanced force, F is not zero unless the IC is correctly located
	ax_new = (-1 * F_yy * J) / (n * Mo)
	ay_new = (F_xx * J) / (n * Mo)
	output.append(["x-component of unbalanced force", F_xx, "y-component of unbalanced force",
	               F_yy, "magnitude of unbalanced force", F])
	output.append(["x- component of distance from centroid to IC", ax_new,
	               "y- component of distance from centroid to IC", ay_new])

	new_IC = elastic_IC
	iter = 0

	while iter < 10000:

		new_IC = [new_IC[0] + ax_new, new_IC[1] + ay_new]
		Mp_new = (-1 * P_x * (Ecc_y - new_IC[1])) + (P_y * (Ecc_x - new_IC[0]))

		Rx, Ry, Mi, table = force(new_IC, support_x, support_y, side_x, side_y, k_arc, delta_f_arc, P_f_arc,
		                          k_side, delta_f_side, P_f_side, Mp_new)
		F_xx = P_x + Rx
		F_yy = P_y + Ry
		F = m.sqrt(F_xx **2 + F_yy **2)

		ax_new = ((-1 * F_yy * J) / (n * Mo))
		ay_new = ((F_xx * J) / (n * Mo))

		Cu = abs(Mi / Mp_new)

		if F <= 0.001: #tolerance = 0.0001
			iter = 10000
		else:
			iter += 1


	output.append(["Table", table])
	output.append(["F_xx", F_xx, "F_yy", F_yy, "F", F])
	output.append(["I.C.", new_IC])
	output.append(["Rx", Rx, "Ry", Ry, "Mi", Mi, "Per Bolt Table", table])


	return output, new_IC, Cu
