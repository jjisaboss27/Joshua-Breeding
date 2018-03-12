# Joshua Breeding

MediaType = input("what is the media type?: ")
Title = input("What is the title?: ")
Artist = input("What is the artist?: ")
Date = input("What is the date it was created?: ")
Genre = input("What is the genre?: ")
Rating = float(input("How do you rate the work?: ")

Data = [MediaType,Title,Artist,Date,Genre,Rating]

music = []
movie = []
show = []
art = []
others = []

if MediaType == "music":
    music.append(Title)
elif MediaType == "movie":
    movie.append(Title)
elif MediaType == "show":
    show.append(Title)
elif MediaType == "art":
    art.append(Title)
else:
    others.append(Title)
