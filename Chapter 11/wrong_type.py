def main():
    # Pass a string to show_mammal_info...
    show_mammal_info('I am a string')

# The show_mammal_info function accepts an object
# as an argument, and calls its show_species
# and make_sound methods.

def show_mammal_info(creature):
        creature.show_species()
        creature.make_sound()

# Call the main function.
main()
