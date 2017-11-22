def ex1and2():
	class animal(object):
		def __init__(self,sound, name, age, favorite_color):

			self.sound = sound
			self.name = name
			self.age = age
			self.favorite_color = favorite_color
		def eat (self,food):
			print("yummy!!" + self.name+" is eating " + food)	
		def description (self):	
			print(self.name + " is " + str(self.age) + " and loves the color " + self.favorite_color)
		def making_sound(self,x):
			
			print(self.name + " is " + "shouting " + ( self.sound )*x)


	Max = animal("3aw_3aw ","jack",11,"black")
	Max.eat("banana")
	Max.description()
	Max.making_sound(8)
def ex3():
	class Person(object):
		def __init__(self, name,age,city,gender,food,favorite_sport):
			self.name = name
			self.age = age
			self.city = city
			self.gender = gender
			self.food = food
			self.favorite_sport = favorite_sport
		def eat (self):
			print(self.name," eats ",self.food,"everyday")
		def sport (self):
			print(self.name," likes to play ",self.favorite_sport," everyday")


	Jack = Person("jack",15,"baitsahoor-sahooore-","girl","banana","soccer")
	Jack.eat()
	Jack.sport()
def extra():
	import random

	class Song(object):
		def __init__(self,songs):
			self.songs = songs
		def sing_me_a_song(self):
			print(self.songs)
			for lines in self.songs:
				print(lines)
		def sing_me_a_random_song(self):	
			for i in range(len(self.songs)):
				x = random.randint(0,len(self.songs)-1)
				print(self.songs[x])

	W = Song(["Roses are red,",
		"Violets are blue,",
		"I wrote this poem for you."])
	W.sing_me_a_random_song()


extra()
