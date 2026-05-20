import blair_music

def main():
    # OBSERVATION 1: Saved up so many lines of code right here!
    my_songs = blair_music.generate_example_songlist()
    
    print("MY SONGS:")
    for index, this_song in enumerate(my_songs):
        # OBSERVATION 2:
        # enumerate will give us 0, 1, 2, 3, 4
        # but we want to display 1, 2, 3, 4, 5
        # so here's a sneaky trick...
        list_number = index + 1

        # Print out our song list
        print("The number", str(list_number), "song is:", this_song.song_brief_description())

    user_choice = input("Please enter the number of the song that you wish to listen to: ")
    print() # OBSERVATION 3: Sneaky new line

    if int(user_choice) in range(1, len(my_songs) + 1):
        selected_song_index = int(user_choice) - 1
        # OBSERVATION 4: This reverses the process in OBSERVATION 2...

        selected_song = my_songs[selected_song_index]      # my_songs[5]
        print("NOW PLAYING:", selected_song.now_playing())
        print("ENJOY! ☺️")
    else:
        print("Sorry, not a valid choice.")

if __name__ == "__main__":
    main()
