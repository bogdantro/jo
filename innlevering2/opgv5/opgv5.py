import turtle
import time
import random

# Strl for spille window
WIDTH, HEIGHT = 700, 600

# Fargene som skal bli brukt
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']


# Funksjon som finner ut antall racers
def get_number_of_racers():
	racers = 0
	while True:
		racers = input('Enter the number of racers (2 - 10): ')
		if racers.isdigit():
			racers = int(racers)
		else:
			print('Input is not numeric... Try Again!')
			continue

		if 2 <= racers <= 10:
			return racers
		else:
			print('Number not in range 2-10. Try Again!')


# Funksjon for å starte spille, altså selve spillet
def race(colors):
	turtles = create_turtles(colors)

    # Start
	while True:
		for racer in turtles:
			distance = random.randrange(1, 20)
			racer.forward(distance)

			x, y = racer.pos()
			if y >= HEIGHT // 2 - 10:
				return colors[turtles.index(racer)]


# Funksjon for å lage turtels
def create_turtles(colors):
	turtles = []
	spacingx = WIDTH // (len(colors) + 1)
	for i, color in enumerate(colors):
		racer = turtle.Turtle()
		racer.color(color)
		racer.shape('turtle')
		racer.left(90)
		racer.penup()
		racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
		racer.pendown()
		turtles.append(racer)

	return turtles

def init_turtle():
	screen = turtle.Screen()
	screen.setup(WIDTH, HEIGHT)
	screen.title('Turtle Racing!')

racers = get_number_of_racers()
init_turtle()

# Random farger
random.shuffle(COLORS)
colors = COLORS[:racers]


# Slutt
winner = race(colors)
# Den viser hvem som vant
print("The winner is the turtle with color:", winner)
# Den venter 5 sekunder så ferdig
time.sleep(5)
