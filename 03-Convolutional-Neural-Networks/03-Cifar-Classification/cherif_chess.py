import re

# white_name, white_elo, black_name, black_elo, opening_id, place, date, number_moves, result

chess_data = []
game_data = []

with open('cherif_chess.txt', 'r') as f:
    text = (row for row in f.readlines())
    
name_pattern = r'\w+,\w+'
elo_regex = r'(\()(\d{4})(\))'
opening_id_pattern = r'(\[)(\w\d+)(\])'
place_pattern = r'(.*)(\(\d\))'
date_pattern = r'\d{2}\.\d{2}\.\d{4}'
final_move_pattern = r'(.*)(\s)(\d{1,3})(\.)(.{8,14})(0-1)'# | (.*)(\d{1,3}\.)(.{8,14})(1-0) | (.*)(\d{1,3}\.)(.{8,14})(1/2-1/2)'

for row in text:
    if '[' in row:
        if game_data:
            chess_data.append(game_data)
            game_data = []
        id = re.findall(opening_id_pattern, row)
        game_data.append(id[0][1])        
        names = re.findall(name_pattern, row)
        for name in names:
            game_data.append(name)
        elos = re.findall(elo_regex, row)
        for elo in elos:
            game_data.append(elo[1])
    place = re.findall(place_pattern, row)
    if place:
        game_data.append(place[0][0].strip())
    date = re.findall(date_pattern, row)
    if date:
        game_data.append(date[0])
    if '0-1' in row:
        game_data.append('black win')
        final_move_pattern = r'(.*)(\s)(\d{1,3})(\.)(.{4,14})(0-1)'
        final_move = re.findall(final_move_pattern, row)
        game_data.append(final_move[0][2])
    elif '1-0' in row:
        game_data.append('white win')
        final_move_pattern = r'(.*)(\s)(\d{1,3})(\.)(.{4,14})(1-0)'
        final_move = re.findall(final_move_pattern, row)
        game_data.append(final_move[0][2])
    elif '1/2-1/2' in row:
        game_data.append('draw')
        final_move_pattern = r'(.*)(\s)(\d{1,3})(\.)(.{4,14})(1/2-1/2)'
        final_move = re.findall(final_move_pattern, row)
        game_data.append(final_move[0][2])
chess_data.append(game_data) # last game data

for e in chess_data:
    print(e)
            
# opening id
# opening_id_pattern = r'\[\w\d+\]'
# for elo in text:
#     if re.findall(opening_id_pattern, elo):
#         print(re.findall(opening_id_pattern, elo))

# place
# place_pattern = r'(.*)(\(\d\))'
# for row in text:
#     if re.findall(place_pattern, row):
#         print(re.findall(place_pattern, row)[0][0].strip())

# date
# date_pattern = r'\d{2}\.\d{2}\.\d{4}'
# for row in text:
#     if re.findall(date_pattern, row):
#         print(re.findall(date_pattern, row)[0])

# result
# for row in text:
#     if '1-0' in row:
#         print('1-0')
#     elif '0-1' in row:
#         print('0-1')
#     else:
#         print('draw')

# nb_moves
# final_move_pattern = r'(.*)(\s)(\d{1,3})(\.)(.{8,14})(0-1)'# | (.*)(\d{1,3}\.)(.{8,14})(1-0) | (.*)(\d{1,3}\.)(.{8,14})(1/2-1/2)'
# text = '58.Kf6 g4 59.Rg8 Kf4 60.Rg5 Ke4 61.Rg8 Ke3 62.Re8+ Kf2 63.Kg5 g3 64.Ra8 g2 65.Ra2+ Kg1 0-1'
# print(re.findall(final_move_pattern, text)[0][2])