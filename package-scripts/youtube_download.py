from pytube import YouTube  # pip install pytube

url = input("Type link from Youtube: ")
path = input("Type path to save that file: ")
yt = YouTube(url)

print("Title: ", yt.title)
print("Views: ", yt.views)
print("Length: ", yt.length)
print("Rating: ", yt.rating)

# get best resolution
ys = yt.streams.get_highest_resolution()

print("Streaming...")
ys.download()
print("Download is finished.")
