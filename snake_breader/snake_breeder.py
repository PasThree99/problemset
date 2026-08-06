import random

MALE   = 0
FEMALE = 1

class Snake:
    def __init__(self):
        self.sex = random.randint(0,1)
        self.mother = None
        self.father = None

class SnakeBreeder:
    def __init__(self):
        self.count = 0
        self.snakes = []

    def _is_ancestor(self, start:Snake, target):
        stack = [start.father, start.mother]
        visited = []
        while len(stack) > 0:
            elem = stack.pop()
            if elem == None:
                continue
            if elem == target:
                return True
            if elem not in visited:
                visited.append(elem)
                stack.extend([elem.father, elem.mother])
        return False


    def can_breed(self, snake1:Snake, snake2:Snake) -> bool:
        # Sex must be oposites
        if snake1.sex == snake2.sex:
            return False

        if (self._is_ancestor(snake1, snake2) or 
            self._is_ancestor(snake2, snake1)):
            return False
        
        return True



    def breed(self, snake1:Snake, snake2:Snake):
        if not self.can_breed(snake1, snake2):
            print("ERROR: Snakes cannot breed!")
            return None
        
        father = snake1 if snake1.sex == MALE else snake2
        mother = snake1 if snake1.sex == FEMALE else snake2

        new_born = Snake()
        new_born.father = father
        new_born.mother = mother
        self.add_snake(new_born)
        return new_born
            

    def add_snake(self, new_snake:Snake):
        if new_snake in self.snakes:
            print("ERROR: Snake already on the breeder")
            return
        
        self.snakes.append(new_snake)
        self.count += 1