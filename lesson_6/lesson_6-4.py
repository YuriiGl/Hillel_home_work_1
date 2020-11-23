import json
path = 'acdc.json'
with open(path,'r') as f:
    data = json.loads(f.read())
    duration_list=[int(track['duration']) for track in
                   data['album']['tracks']['track']]
    print(duration_list)
    print(sum(duration_list))