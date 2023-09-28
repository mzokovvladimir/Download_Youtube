from youtube_dl import YoutubeDL

videos: list[str] = ["https://www.youtube.com/watch?v=EjOg7zSoBCE"]

with YoutubeDL({}) as ydl:
    ydl.download(videos)