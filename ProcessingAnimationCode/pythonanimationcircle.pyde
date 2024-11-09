# Set the length of each beat for the circles in milliseconds (1 second)
beat_length = 1000

# These are trackers to remember when the last melody and drum beats occurred
# Making the numbers "0" simply just gives them a starting point.
last_melody_beat = 0
last_drum_beat = 0

# Initial sizes for the melody and drum circles
# Melody circle is much larger due to the main beat
melody_circle_size = 50
drum_circle_size = 30

# Starting colour for the melody circle, set to a soft red
melody_color = color(255, 100, 100)

# Generate random colours for each of the drum circles, set as a list for 4 drum "beat" colours
# The for in range function, its essential to ensure multiple colours
drum_colors = [color(random(255), random(255), random(255)) for _ in range(4)]

# Delay in 8 milliseconds before the drum circles start in song
drum_delay = 8000  

def setup():
    # Set up the canvas size to 600x400 pixels
    #def allows to define the function "set up" and set up means to run code once during the beginning.
    size(600, 400)
    
    # Initialize the melody beat timer with the current time.
    #This part of the code is essentially initializing a timer by storing the starting point in milliseconds. It’s useful for tracking time intervals, like creating pauses or beats, by later checking how much time has passed since this initial timestamp.
    global last_melody_beat
    last_melody_beat = millis()

def draw():
    # Give access to global variables that track time and colours
    # By declaring these variables as global, draw() can modify their values directly. This is important for creating interactive or animated effects because the function can adjust them frame-by-frame, synchronizing visual changes with time intervals for beats. Without global, changes to these variables would be local to the function, and the animation would not work as expected.
    global last_melody_beat, last_drum_beat, melody_circle_size, drum_circle_size 
    global melody_color, drum_colors

    # Set background colour to dark gray each frame for a clean slate
    background(30)

    # Check if enough time has passed for the next melody beat
    #This timing check allows the melody to play at regular intervals. Without it, the melody beat would not sync with the intended rhythm, and notes could play too quickly or too slowly. Resetting the timer ensures consistent intervals between beats, creating a steady rhythm.
    if millis() - last_melody_beat >= beat_length:
        # Reset the melody beat time to the current time
        last_melody_beat = millis()

        # Choose a new random colour for each melody beat to keep it interesting
        melody_color = color(random(255), random(255), random(255))

        # Reset the melody circle size back to its starting size
        melody_circle_size = 50

    # After the drum delay, check if enough time has passed for the next drum beat
    if millis() >= drum_delay and millis() - last_drum_beat >= beat_length:
        # Reset the drum beat time
        last_drum_beat = millis()

        # Generate new random colours for each drum circle
        drum_colors = [color(random(255), random(255), random(255)) for _ in range(4)]

        # Reset drum circle size for beat animation
        drum_circle_size = 30

    # Gradually increase the melody circle size up to a limit of 100 for a pulsing effect
    melody_circle_size = min(melody_circle_size + 1.5, 100)

    # Gradually increase the drum circle size up to a limit of 60, also creating a pulsing effect
    drum_circle_size = min(drum_circle_size + 1.5, 60)

    # Draw the melody circle in the center of the canvas, filling it with the melody colour
    fill(melody_color)
    ellipse(width / 2, height / 2, melody_circle_size, melody_circle_size)

    # If the drum delay has passed, draw each drum circle in a square pattern around the melody circle
    if millis() >= drum_delay:
        # Define fixed positions for the four drum circles around the melody circle
        drum_positions = [(width/2 + 100, height/2), (width/2 - 100, height/2),
                          (width/2, height/2 + 100), (width/2, height/2 - 100)]
        
        # This loop will run four times, with i taking values from 0 to 3. This is used to access each of the four drum circles individually.
        for i in range(4):
            # Fill each drum circle with its respective colour from drum_colors
            fill(drum_colors[i])
            # Draw each drum circle at its designated position
            ellipse(drum_positions[i][0], drum_positions[i][1], drum_circle_size, drum_circle_size)
            
#All the global variables; 
#last_melody_beat: Tracks the last time a melody beat occurred to time the next one.
#last_drum_beat: Tracks the last time a drum beat occurred for the drum animation.
#melody_circle_size: Stores the current size of the melody circle, which animates to simulate a beat.
#drum_circle_size: Stores the size of the drum circles, which also animate with each beat.
#melody_color: Holds the current color of the melody circle, changing with each beat.
#drum_colors: A list of colors for each drum circle, allowing each to be individually colored.
#beat_length: Defines the duration of each beat, typically in milliseconds (e.g., 1000 ms for 1 second).
#drum_positions: Holds the x and y coordinates for each drum circle, used to position them on the screen.
