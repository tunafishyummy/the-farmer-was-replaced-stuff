import dostuff
while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
		#do a flip on every tile
			dostuff.do_a_pumpkin()
			move(North)
		move(East)