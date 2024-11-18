class Bird:
    def sound(self):
        return "Some generic bird sound"

class Sparrow(Bird):
    def sound(self):
        return "Chirp"

class Parrot(Bird):
    def sound(self):
        return "Squawk"

def make_bird_sound(bird):
    print(bird.sound())

sparrow = Sparrow()
parrot = Parrot()

make_bird_sound(sparrow)
make_bird_sound(parrot)
