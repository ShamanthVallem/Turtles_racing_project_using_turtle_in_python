import turtle
import time
import random

width = 500
height = 500
colors = ['cyan', 'red', 'blue', 'black', 'green', 'orange', 'pink', 'grey', 'darkviolet', 'brown']

def get_number_of_racers():
	racers = 0
	while True:
		racers = input("Enter the number of racers(2-10): ")
		if racers.isdigit():
			racers = int(racers)
		else:
			print("Please Enter a numeric value between 2-10.")
			continue

		if 2 <= racers <= 10:
			return racers
		else:
			print("Please Enter a value between 2-10: ")


def race(colors):
	turtles = create_turtles(colors)

	while True:
		for racer in turtles:
			distance = random.randrange(1, 20)
			racer.forward(distance)
			x, y = racer.pos()
			if(y >= height//2 -15):
				time.sleep(3)
				return colors[turtles.index(racer)]


def create_turtles(colors):
	# colors.Turtle()
	spacingx = width//(len(colors)+1)
	turtles = []
	for i, color in enumerate(colors):
		racer = turtle.Turtle()
		racer.color(color)
		racer.shape('turtle')
		racer.left(90)
		# time.sleep(1)
		racer.penup()
		racer.setpos(-width//2 + (i+1)*spacingx , -(height//2)+20)
		racer.pendown()
		turtles.append(racer)

	return turtles

def init_turlte():
	_ = turtle.Screen()
	_.setup(width, height)
	_.title("Racing")

	
racers = get_number_of_racers()
init_turlte()
# time.sleep(5)


random.shuffle(colors)
colors = colors[:racers]
print(colors)
winner = race(colors)
print(f"The winner of the race is turtle with color: {winner}.")
# create_turtles(colors)



