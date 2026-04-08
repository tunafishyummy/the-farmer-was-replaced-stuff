while True:
	for i in range(2):
		for i in range(6):
			if can_harvest():
				harvest()
			move(North)
		move(East)
	for i in range (4):
		for i in range(3):
			if can_harvest():
				harvest()
				plant(Entities.Tree)
			move(North)
			if get_ground_type() == Grounds.Grassland:
				till()
			if can_harvest():
				harvest()
			else:
				plant(Entities.Carrot)
			move(North)
		move(East)
		move(North)