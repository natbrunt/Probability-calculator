import copy
import random

class Hat():
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self,num_balls_drawn):

        if num_balls_drawn >= len(self.contents):
            copy = self.contents
            self.contents = []
            return copy

        else:
            random_balls = []
            for _ in range(num_balls_drawn):
                random_index = random.randint(0, len(self.contents)-1)
                random_balls.append(self.contents[random_index])
                self.contents.pop(random_index)
            return random_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # var for experiment success tracking
    M = 0
    for N in range(num_experiments):

        # create deep copy of both instances to compare
        hat_copy = copy.deepcopy(hat)
        expected_copy = copy.deepcopy(expected_balls)

        # now draw a certain amount from the hat
        colors_drawn = hat_copy.draw(num_balls_drawn)

        # For each color from the hat
        for color in colors_drawn:
            # if color is found in the expected_balls hat
            if (color in expected_copy) == True:
                # then remove 1 from that color's value
                expected_copy[color] = expected_copy[color] -1
            else:
                pass
        # after running the loop, check if all values have been set to zero to conclude that there is a match
        if(all(x <= 0 for x in expected_copy.values())):
            M +=1
    return round(M / num_experiments,3)

hat3 = Hat(red=10, black=10)

print(experiment(hat3, {"red":5, "black":3} , 9, 6000))
