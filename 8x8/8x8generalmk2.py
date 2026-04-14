import dostuff
	
while True:
		favorabledirection = North
		for i in range (3):
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
		favorabledirection = East
		for i in range(3):
			for i in range(5):
				if i < 4:
					dostuff.do_grass()
					move(favorabledirection)
				else:
					dostuff.do_grass()
			if favorabledirection == East:
				favorabledirection = West
			else:
				favorabledirection = East
			move(South)
		for k in range(5):
			for i in range(5):
				if i < 4:
					dostuff.do_water()
					dostuff.do_a_pumpkin()
					move(favorabledirection)
				else:
					dostuff.do_water()
					dostuff.do_a_pumpkin()
			if favorabledirection == East:
				favorabledirection = West
			else:
				favorabledirection = East
			if k < 4:
				move(South)
			else:
				megapumpkin = False
				while not megapumpkin:
					favorabledirection = West
					firstmeasurement = measure() 
					move(North)
					move(North)
					move(North)
					move(North)
					move(East)
					move(East)
					move(East)
					move(East)
					secondmeasurement = measure()
					if firstmeasurement == secondmeasurement:
						megapumpkin = True
						harvest()
						move(East)
						move(South)
						move(South)
						move(South)
						move(South)
					else:
						for l in range(5):
							for m in range(5):
								if m < 4:
									get_entity_type()
									if get_entity_type() == Entities.Dead_Pumpkin:
										dostuff.do_a_pumpkin()
									move(favorabledirection)
								else:
									get_entity_type()
									if get_entity_type() == Entities.Dead_Pumpkin:
										dostuff.do_a_pumpkin()
							if favorabledirection == West:
								favorabledirection = East
							else:
								favorabledirection = West
							if l <4:
								move(South)
	
		
		


		
							