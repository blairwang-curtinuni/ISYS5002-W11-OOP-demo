# Defining objects of the class "Song"
class Song:
    def __init__(self, song_title, musician, album):
        self.song_title = song_title
        self.musician = musician
        self.album = album
    
    def song_brief_description(self):
        return self.song_title + " by " + self.musician

    def now_playing(self):
        prepared_return = "NOW PLAYING: "
        prepared_return += "🎵 " + self.song_title + " by "
        prepared_return += "🎸 " + self.musician + " in "
        prepared_return += "📀 " + self.album
        return prepared_return

# The purpose of this function is to assemble a list of example
# songs, to demonstrate the functionality of this codebase.
def generate_example_songlist():
    s1 = Song("Love Story", "Taylor Swift", "Fearless")
    s2 = Song("グッバイバイ", "冨岡 愛", "Ai'scream")
    s3 = Song("Dynamite", "BTS", "Be")
    s4 = Song("Waltzing Matilda", "Slim Dusty", "Waltzing Matilda")
    s5 = Song("Way Back Home", "SHAUN", "Take (2018)")
    s6 = Song("Never Gonna Give You Up", "Rick Astley", "Unknown Album")

    # index  0   1   2   3   4   5
    return [s1, s2, s3, s4, s5, s6]
