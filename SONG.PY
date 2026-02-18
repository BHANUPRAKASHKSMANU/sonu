import time
from threading import Thread, Lock
import sys

lock = Lock()

# Function to animate text and create a typewriter effect
def animate_text(text, delay=0.05):  # Reduced delay for faster typewriter effect
    """Print each character with a delay to create a typewriter effect."""
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()  # To move to the next line after finishing a lyric

# Function to delay and animate each lyric
def sing_lyric(lyric, delay, speed):
    """Delay the lyric's appearance and then animate it with the typewriter effect."""
    time.sleep(delay)  # Wait before showing the lyric
    animate_text(lyric, speed)

# Main function to run the song
def sing_song():
    lyrics = [
    
        # Adding the new section you requested:
        ("Aadisi Nodu Beelisi Nodu",0.1) , ("Uruli Hogadu Aadisi Nodu Beelisi Nodu", 0.1),
        ("Uruli Hogadu ",0.1),
        ("Ene Barali Yaarigu Sothu", 0.1),
        ("Thaleya Baagadu", 0.1),
        ("Endigu Naanu Heege Iruve", 0.1),
        ("Endu Naguvudu Heege Naguthaliruvudu", 0.1),
        ("Aadisi Nodu Beelisi Nodu", 0.1),
        ("Uruli Hogadu", 0.1)
    ]
    
    delays = [
        0.0,    # start of song
        5.0,    # line 2
        10.0,   # line 3
        15.0,   # line 4
        20.0,   # line 5
        25.0,   # line 6
        30.0,   # line 7
        35.0,   # line 8
        40.0,   # line 9
        45.0,   # line 10
        50.0,   # line 11
        55.0,   # line 12
        60.0,   # line 13
        65.0,   # line 14
        70.0,   # line 15
        75.0,   # line 16
        80.0,   # line 17
        85.0,   # line 18
        90.0,   # line 19
        95.0,   # line 20
        100.0,  # line 21
        105.0,  # line 22
        110.0 # line 23
        
    ]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        start_delay = delays[i] if i < len(delays) else 0
        t = Thread(target=sing_lyric, args=(lyric, start_delay, speed))
        threads.append(t)
        t.start()
    
    # Adding a 5-second delay after starting all threads before joining them
    time.sleep(5)  # This will pause for 5 seconds before continuing

    for thread in threads:
        thread.join()

# Entry point for running the script
if __name__ == "__main__":  # Corrected if statement
    sing_song()
