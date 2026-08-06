# Problem source
Google interview december 2025

# Problem
## Description:

You are tasked with building a management system for a snake breeding facility. The facility maintains an ongoing inventory of snakes and facilitates controlled reproduction.

Snakes can enter the system in one of two ways:

- Purchased: Brand new snakes brought into the facility. These snakes have no parentage history in the system and are guaranteed to be unrelated to any existing snakes.

- Bred: New snakes born directly in the facility from two existing snakes.

## Breeding Rules:

- Two snakes are allowed to breed if and only if they meet the following criteria:

- Opposite Sex: One snake must be Male and the other Female.

- Direct Lineage Isolation: A snake cannot breed with an ancestor or a descendant (e.g., Father-Daughter, Mother-Son, Grandparent-Grandchild).

## Requirements:

Implement a SnakeBreeder class that provides the following public interface:

add_snake(snake): Adds a newly purchased snake to the breeder system.

can_breed(snake1, snake2) -> bool: Returns True if snake1 and snake2 meet all requirements to breed, or False otherwise.

breed(snake1, snake2) -> Snake: Validates whether the two snakes can breed. If valid, generates a new offspring snake assigned to both parents, adds it to the system, and returns it. If invalid, returns an error or None