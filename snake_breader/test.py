import unittest
from snake_breeder import Snake, SnakeBreeder, MALE, FEMALE

class TestSnakeBreeder(unittest.TestCase):

    def setUp(self):
        """Set up a fresh breeder instance and base snakes before each test."""
        self.breeder = SnakeBreeder()
        
        # Bought base snakes (unrelated)
        self.adam = Snake()
        self.adam.sex = MALE
        
        self.eve = Snake()
        self.eve.sex = FEMALE
        
        self.breeder.add_snake(self.adam)
        self.breeder.add_snake(self.eve)

    def test_add_snake(self):
        """Test adding bought snakes and preventing duplicates."""
        self.assertEqual(self.breeder.count, 2)
        
        # Adding duplicate snake should fail
        self.breeder.add_snake(self.adam)
        self.assertEqual(self.breeder.count, 2)

    def test_same_sex_breeding(self):
        """Test that snakes of the same sex cannot breed."""
        male_snake = Snake()
        male_snake.sex = MALE
        self.breeder.add_snake(male_snake)
        
        self.assertFalse(self.breeder.can_breed(self.adam, male_snake))

    def test_unrelated_breeding(self):
        """Test that two unrelated opposite-sex snakes can breed."""
        self.assertTrue(self.breeder.can_breed(self.adam, self.eve))
        
        baby = self.breeder.breed(self.adam, self.eve)
        self.assertIsNotNone(baby)
        self.assertEqual(self.breeder.count, 3)
        self.assertEqual(baby.father, self.adam)
        self.assertEqual(baby.mother, self.eve)

    def test_parent_child_breeding(self):
        """Test that a parent cannot breed with their child."""
        child = self.breeder.breed(self.adam, self.eve)
        child.sex = FEMALE if self.adam.sex == MALE else MALE  # Ensure opposite sex
        
        # Father-Daughter check
        self.assertFalse(self.breeder.can_breed(self.adam, child))
        # Daughter-Father check (reverse order)
        self.assertFalse(self.breeder.can_breed(child, self.adam))

    def test_grandparent_grandchild_breeding(self):
        """Test that a grandparent cannot breed with their grandchild across generations."""
        # Gen 1: Adam (M) + Eve (F) -> Child1 (M)
        child1 = self.breeder.breed(self.adam, self.eve)
        child1.sex = MALE
        
        # Bought Snake: Mary (F)
        mary = Snake()
        mary.sex = FEMALE
        self.breeder.add_snake(mary)
        
        # Gen 2: Child1 (M) + Mary (F) -> Grandchild (F)
        grandchild = self.breeder.breed(child1, mary)
        grandchild.sex = FEMALE
        
        # Grandfather-Granddaughter check
        self.assertFalse(self.breeder.can_breed(self.adam, grandchild))
        # Grandmother-Grandson check (Eve & Grandchild if Grandchild was Male)
        grandchild_male = Snake()
        grandchild_male.sex = MALE
        grandchild_male.father = child1
        grandchild_male.mother = mary
        self.breeder.add_snake(grandchild_male)
        
        self.assertFalse(self.breeder.can_breed(self.eve, grandchild_male))

    def test_bought_snakes_can_always_breed_if_opposite_sex(self):
        """Test that two newly bought snakes with no parents are fully compatible."""
        snake1 = Snake()
        snake1.sex = MALE
        snake2 = Snake()
        snake2.sex = FEMALE
        
        self.breeder.add_snake(snake1)
        self.breeder.add_snake(snake2)
        
        self.assertTrue(self.breeder.can_breed(snake1, snake2))

if __name__ == "__main__":
    unittest.main()