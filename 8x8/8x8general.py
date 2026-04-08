favorabledirection = North
import dostuff
	
while True:
		for i in range (5):
			for j in range(4):
				dostuff.do_a_carrot()
				move(favorabledirection)
				
				if j < 3:
					dostuff.do_a_tree()
					move(favorabledirection)
	
				if j == 3:
					dostuff.do_a_tree()
				
			move(East)
			if favorabledirection == North:
				favorabledirection = South
			else:
				favorabledirection = North
			
		for i in range(3):
			for i in range(8):
				dostuff.do_grass()
				move(North)
			move(East)
		favorabledirection = North
		if get_pos_y() == 7:
			for i in range (7):
				move(South)


		
