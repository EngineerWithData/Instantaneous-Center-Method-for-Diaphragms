from __future__ import division

def support_group(n_col, n_row, col_spacing, row_spacing): # fasteners at exterior and interior supports (ref: Fig D1-1
	# of AISI S310-16)
	x_support = []
	y_support = []
	for i in range(n_col):
		for j in range(n_row):
			x_support.append(i*col_spacing - (n_col-1) * col_spacing/2)
			y_support.append(j*row_spacing - (n_row-1) * row_spacing/2)
	return x_support, y_support

def end_group(n_col, n_row, col_spacing, row_spacing): # fasteners at exterior and interior supports (ref: Fig D1-1
	# of AISI S310-16)
	x_end = []
	y_end = []
	for i in range(n_col):
		for j in range(n_row):
			x_end.append(i*col_spacing - (n_col-1) * col_spacing/2)
			y_end.append(j*row_spacing - (n_row-1) * row_spacing/2)
	return x_end, y_end

def edge_group(n_col, n_row, col_spacing, row_spacing):  # fasteners at arc spot welds (edge connection)
	#w=width
	x_edge = []
	y_edge = []
	for i in range(n_col):
		for j in range(n_row):
			x_edge.append(i*col_spacing - (n_col-1) * col_spacing/2)
			y_edge.append(j*row_spacing - (n_row-1) * row_spacing/2)
	return x_edge, y_edge

def side_group(n_col, n_row, col_spacing, row_spacing):  # fasteners at arc spot welds (edge connection)
	#w=width
	x_side = []
	y_side = []
	for i in range(n_col):
		for j in range(n_row):
			x_side.append(i*col_spacing - (n_col-1) * col_spacing/2)
			y_side.append(j*row_spacing - (n_row-1) * row_spacing/2)
	return x_side, y_side