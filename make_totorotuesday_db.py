import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('totorotuesday.db')
cursor = conn.cursor()

# Create the tags table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tags (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')

# Create the totorotuesday table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS totorotuesday (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')

# Create the junction table totorotuesday_tags
cursor.execute('''
    CREATE TABLE IF NOT EXISTS totorotuesday_tags (
        totoro_id INTEGER,
        tag_id INTEGER,
        FOREIGN KEY (totoro_id) REFERENCES totorotuesday(id),
        FOREIGN KEY (tag_id) REFERENCES tags(id),
        PRIMARY KEY (totoro_id, tag_id)
    )
''')

# Data for tags
tags_data = [
    'animal',
    'anime',
    'art',
    'book',
    'canada',
    'celebrity',
    'design',
    'fantasy',
    'food',
    'ghibli',
    'holiday',
    'india',
    'individual',
    'japan',
    'job',
    'misc',
    'movie',
    'music',
    'politics',
    'progressive',
    'sport',
    'stationary',
    'technology',
    'tv',
    'videogame',
    'webcomic',
    'youtuber'
]

# Insert data into the tags table
for tag in tags_data:
    cursor.execute('INSERT INTO tags (name) VALUES (?)', (tag,))

# Data for totorotuesday
totorotuesday_data = [
    'BONUSDAIKON.jpg',
    'BONUStotorotuesdayhomestar02.jpg',
    'BONUStotorotuesdayhomestar03.jpg',
    'BONUStotorotuesdaypeen.jpg',
    'totorotuesdayanne.jpg',
    'totorotuesdayartofmeishirt.jpg',
    'totorotuesdayatashinchi.png',
    'totorotuesdaybaconandegg.jpg',
    'totorotuesdaybanksy.jpg',
    'totorotuesdaybaseball.jpg',
    'totorotuesdaybase.jpg',
    'totorotuesdaybigmac.jpg',
    'totorotuesdaybikini.jpg',
    'totorotuesdayblankslate.jpg',
    'totorotuesdayblmfist.jpg',
    'totorotuesdaybobross.jpg',
    'totorotuesdaybourbonmoth.jpg',
    'totorotuesdaybowling.jpg',
    'totorotuesdaybozotheclownandbutch.jpg',
    'totorotuesdaybozotheclownnobutchrainbowhair.jpg',
    'totorotuesdaybuddyholly.jpg',
    'totorotuesdaycalvinandhobbes.jpg',
    'totorotuesdaychtulhuandkraken.jpg',
    'totorotuesdaycinnamonbuncoffeesimplebreakfast.jpg',
    'totorotuesdaycoloringbook1.jpg',
    'totorotuesdaycoloringbook2.jpg',
    'totorotuesdaycoloringbook3(fixed).jpg',
    'totorotuesdaycupcake.jpg',
    'totorotuesdaydali01.jpg',
    'totorotuesdaydali02.jpg',
    'totorotuesdaydogen.jpg',
    'totorotuesdaydoom01.jpg',
    'totorotuesdaydoom04(left).jpg',
    'totorotuesdaydoraemon.jpg',
    'totorotuesdaydrawstotoro.jpg',
    'totorotuesdayduchamp.jpg',
    'totorotuesdayelementaryBLUE.jpg',
    'totorotuesdayelementaryGREEN.jpg',
    'totorotuesdayelementaryPINK.jpg',
    'totorotuesdayelementaryRED.jpg',
    'totorotuesdayelementaryYELLOW.jpg',
    'totorotuesdayericcarle.jpg',
    'totorotuesdayevera.jpg',
    'totorotuesdayeveraxmas.jpg',
    'totorotuesdayexplodingdog.png',
    'totorotuesdayganesha.jpg',
    'totorotuesdaygiroditalia.jpg',
    'totorotuesdayglenngould(blink).jpg',
    'totorotuesdayglenngould.jpg',
    'totorotuesdayglico.jpg',
    'totorotuesdaygoalie.jpg',
    'totorotuesdayhaloinfinite.jpg',
    'totorotuesdayhaloinfinitewithsuitandcraig.jpg',
    'totorotuesdayhilda3.jpg',
    'totorotuesdayhomemovies.jpg',
    'totorotuesdayhomestar01.jpg',
    'totorotuesdayjasmine.jpg',
    'totorotuesdayjellyfish.png',
    'totorotuesdayjoelhaverFINALGLITCH.jpg',
    'totorotuesdayJORDANONENIKE.jpg',
    'totorotuesdaylofigirl.jpg',
    'totorotuesdaylolitafashion.jpg',
    'totorotuesdaylostartpress.jpg',
    'totorotuesdaymagritte.jpg',
    'totorotuesdaymarccanadapost.jpg',
    'totorotuesdaymarccorona.jpg',
    'totorotuesdaymarcjapanhunter.jpg',
    'totorotuesdaymarcjapanpost.jpg',
    'totorotuesdaymarcnoface.jpg',
    'totorotuesdaymarconepunchman.jpg',
    'totorotuesdaymarcrick.jpg',
    'totorotuesdaymariosunshine.jpg',
    'totorotuesdayminion.jpg',
    'totorotuesdaymoana.jpg',
    'totorotuesdaymoanawithbackground.jpg',
    'totorotuesdaymonotaroLOGO.jpg',
    'totorotuesdaymrbeast.png',
    'totorotuesdayonion.jpg',
    'totorotuesdayonsen.jpg',
    'totorotuesdayoshiritantei.jpg',
    'totorotuesdaypacmanandghost.jpg',
    'totorotuesdayparent.jpg',
    'totorotuesdaypencil.jpg',
    'totorotuesdaypikachu1.jpg',
    'totorotuesdaypipe.jpg',
    'totorotuesdaypride.jpg',
    'totorotuesdaypython.jpg',
    'totorotuesdayrexkrueger.jpg',
    'totorotuesdayrogers.jpg',
    'totorotuesdayroughneck.jpg',
    'totorotuesdayrunthejewels.jpg',
    'totorotuesdaysailormoon.jpg',
    'totorotuesdaysapporo.jpg',
    'totorotuesdaysenku.jpg',
    'totorotuesdaysetsubun (1).jpg',
    'totorotuesdaysetsubun.jpg',
    'totorotuesdaysloth.jpg',
    'totorotuesdayspiritbear.jpg',
    'totorotuesdaystevienicks.jpg',
    'totorotuesdaysurfmarc.jpg',
    'totorotuesdaytaxidriver.jpg',
    'totorotuesdayteruterubouzu.jpg',
    'totorotuesdaytheprisoner1967.jpg',
    'totorotuesdaytotoro.jpg',
    'totorotuesdaytrover.jpg',
    'totorotuesdaytruthandreconciliationday.jpg',
    'totorotuesdayUKRAINE.jpg',
    'totorotuesdayusagi.jpg',
    'totorotuesdayvietnamcoffee3.jpg',
    'totorotuesdayvolkwagen.jpg',
    'totorotuesdaywhisltindiesel.png',
    'totorotuesdaywindowsxp.jpg',
    'totorotuesdayxkcd.jpg',
    'totoroukulele.jpg',
    'tuesdaytotoroonigiri.jpg'
]

# Insert data into the totorotuesday table
for name in totorotuesday_data:
    cursor.execute('INSERT INTO totorotuesday (name) VALUES (?)', (name,))

# Sample data for totorotuesday_tags (your provided relations)
relations_data = [
    (1, 16), (2, 16), (3, 16), (4, 16), (5, 4), (5, 5), (5, 17), (5, 24), (6, 2), (6, 3),
    (6, 10), (7, 2), (8, 9), (9, 3), (10, 21), (11, 25), (12, 9), (13, 16), (14, 10), (15, 19),
    (15, 20), (15, 21), (16, 3), (16, 13), (17, 27), (18, 21), (19, 24), (20, 24), (21, 18),
    (21, 13), (22, 3), (23, 8), (23, 1), (24, 9), (25, 3), (25, 22), (26, 3), (26, 22), (27, 3),
    (27, 22), (28, 24), (29, 3), (30, 3), (31, 27), (32, 25), (33, 25), (34, 2), (35, 22), (36, 3),
    (37, 14), (38, 14), (39, 14), (40, 14), (41, 14), (42, 4), (42, 13), (45, 26), (46, 12), (47, 21),
    (48, 18), (49, 18), (49, 13), (50, 14), (51, 21), (51, 5), (52, 25), (53, 25), (54, 24), (55, 24),
    (56, 26), (57, 17), (58, 1), (59, 27), (60, 21), (61, 27), (62, 14), (63, 4), (63, 27), (64, 3),
    (65, 5), (65, 15), (66, 20), (67, 14), (67, 15), (68, 14), (68, 15), (69, 10), (70, 2), (71, 24),
    (72, 25), (73, 17), (74, 17), (75, 17), (76, 14), (76, 22), (77, 27), (78, 9), (79, 14), (80, 2),
    (81, 25), (82, 20), (83, 22), (84, 2), (85, 3), (86, 20), (87, 7), (87, 23), (88, 27), (89, 24),
    (89, 6), (89, 13), (90, 15), (90, 5), (91, 18), (92, 2), (93, 14), (93, 9), (94, 2), (96, 14),
    (96, 11), (97, 1), (98, 1), (98, 5), (99, 18), (100, 21), (101, 17), (102, 14), (103, 17), (104, 10),
    (105, 25), (106, 20), (107, 20), (108, 16), (108, 1), (109, 9), (110, 23), (111, 27), (112, 23),
    (113, 23), (113, 26), (114, 18), (114, 10), (115, 9), (115, 14)
]


# Insert data into the totorotuesday_tags table
for relation in relations_data:
    cursor.execute('INSERT INTO totorotuesday_tags (totoro_id, tag_id) VALUES (?, ?)', relation)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database created successfully!")
