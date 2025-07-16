playlist=["TrackA","TrackB","TrackC","TrackD"]
playlist.remove('TrackC')
playlist.insert(0,'TrackX')
poped_str=playlist.pop(-1)
playlist.insert(1,poped_str)
print(*playlist)