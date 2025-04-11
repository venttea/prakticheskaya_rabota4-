class Media:
    def play(self):
        return "Playing media"

    def pause(self):
        return "Pausing media"


class Music(Media):
    def play(self):
        return "Playing music track"


class Video(Media):
    def play(self):
        return "Playing video file"

media = Media()
print(media.play())
print(media.pause())

music = Music()
print(music.play())
print(music.pause())

video = Video()
print(video.play())
print(video.pause())
