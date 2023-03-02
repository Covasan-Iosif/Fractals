import pygame
import sys
import math
import colorsys

pygame.init()

# Dimensions for the screen
WIDTH = 1920
HEIGHT = 1080

# Arguments
l_system_text = sys.argv[1] # The file with the axiom
start = int(sys.argv[2]), int (sys.argv[3]) # Coordinates of the start point
length = int(sys.argv[4])   # The length of every line
ratio = float(sys.argv[5]) # Difference between generations

# Reading the file with the format:
# axiom
# number of rules
# the rules
# the angle in degrees

with open(l_system_text) as f:
    axiom = f.readline()
    num_rules = int(f.readline())
    rules = {} #dictionary for rules
    for i in range(num_rules):
        rule = f.readline().split(' ')
        rules[rule[0]] = rule[1]
    angle = math.radians(int(f.readline())) 

class LSystem():
    def __init__(self, axiom, rules, angle, start, length, ratio):
        self.sentence = axiom
        self.rules = rules
        self.angle = angle 
        self.start = start
        self.x,self.y = start
        self.length = length
        self.ratio = ratio
        self.theta = math.pi / 2
        self.position = []

    def __str__(self):
        return self.sentence

    # Function to generate the new generation sentence (applying the rules)
    def generate(self):
        self.x,self.y = self.start
        self.theta = math.pi / 2
        self.length *= self.ratio
        new_sentence = ""
        for char in self.sentence:
            mapped = char
            try:
                mapped = self.rules[char]
            except:
                pass
            new_sentence += mapped
        self.sentence = new_sentence

    # Function to draw the sentence   
    # F draws forward
    # + turns left with "angle" dregrees
    # - turns right with "angle" dregrees
    # [ saving the current values for position and angle  
    # ] restores the saved values 
    def draw(self, screen):
        hue = 0
        for char in self.sentence:
            if char == "F":
                x2 = self.x - self.length * math.cos(self.theta)
                y2 = self.y - self.length * math.sin(self.theta)
                pygame.draw.line(screen, (hsv2rgb(hue, 1, 1)), (self.x,self.y), (x2,y2))
                self.x, self.y = x2, y2
            elif char == "+":
                self.theta += self.angle
            elif char == "-":
                self.theta -= self.angle
            elif char == "[":
                self.position.append({'x': self.x, 'y': self.y, 'theta': self.theta})
            elif char =="]":
                position = self.position.pop()
                self.x, self.y, self.theta = position['x'], position['y'], position['theta']   
            hue += 0.00005 

# Function for colors
def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

def main():
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.mouse.set_visible(False)

    fractal = LSystem(axiom, rules, angle, start, length, ratio)

    # Running conditions
    # Press SPACE for the next generation
    # Press ESC for exiting
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_SPACE]:
                screen.fill((0, 0, 0))
                fractal.draw(screen)
                fractal.generate()
            if keystate[pygame.K_ESCAPE]:
                pygame.quit()
        pygame.display.update()

main()



# Classic-Sierpinski-curve         python fractals.py fractals/classic-sierpinski-curve.txt 1150 750 30 0.5
# Dragon-curve:                    python fractals.py fractals/dragon-curve.txt 960 540 200 0.75
# Hilbert-curve                    python fractals.py fractals/hilbert-curve.txt 1920 1080 250 0.67
# Hilbert-curve-II                 python fractals.py fractals/hilbert-curve-II.txt 0 1080 50 0.7
# Koch-snowflake:                  python fractals.py fractals/koch-snowflake.txt 1200 900 100 0.5
# Krishna-anklets                  python fractals.py fractals/krishna-anklets.txt 1400 550 60 0.8
# Levy-curve                       python fractals.py fractals/levy-curve.txt 1100 750 70 0.8
# Moore-curve                      python fractals.py fractals/moore-curve.txt 1000 1080 50 0.8
# Peano-curve                      python fractals.py fractals/peano-curve.txt 0 1080 70 0.7
# Peano-Gosper-curve:              python fractals.py fractals/peano-gosper-curve.txt 600 280 200 0.5
# Plant:                           python fractals.py fractals/plant.txt 960 1000 100 0.6






















