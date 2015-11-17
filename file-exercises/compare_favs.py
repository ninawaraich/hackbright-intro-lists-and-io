def opening_files(name):
	fav_foods = open(name)
	fav_foods_list = fav_foods.readlines()
	fav_foods.close()
	return fav_foods_list


nina_fav_foods = opening_files("nina_fav_foods.txt")
sara_fav_foods = opening_files("sara_fav_foods.txt")

print nina_fav_foods, sara_fav_foods

if nina_fav_foods[0]==sara_fav_foods[0]:
	print "Our favorite foods are the same :)"
else:
	print "Our favorite foods are different :("







