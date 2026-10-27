# 🐾 Pet Manager

A command-line program for keeping track of pets, written in Python.
This is my first project, built while learning Python from scratch.

## Features
- **Add** a pet with its name, species and age
- **Show** all pets
- **Find** a pet by name and see its details
- **Remove** a pet
- **Input validation**: the menu only accepts numbers, unknown options are rejected, and duplicate pet names are blocked
- **Case-insensitive** names: "Kaneki" and "kaneki" are treated as the same pet

## Example
```
--- PET MANAGER ---
1. Add a pet
2. Show all pets
3. Find a pet
4. Remove a pet
5. Quit
What do you want to do: 3
Which pet are you looking for: Kaneki
kaneki is here and it's a centipede, 7 years old
```

## How to run
Requires Python 3.

```
python pet_manager.py
```

## What I learned
- Writing and reusing functions
- Loops and menu-driven programs
- Validating user input
- Storing structured data in nested dictionaries

## Planned improvements
- Save pets to a file so they're kept after quitting
- Error handling for unexpected input
- Rewrite using classes
