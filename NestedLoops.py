print('This is my first program')

albums = (
        ('Album1_Name',
         'Arist_Name',
         'Release year',
         ('Songs',
          (
              ('1', 'SongOne'),
              ('2', 'SongTwo')
          )
          )
         ),
        (
            'Album2_Name',
            'Arist2_Name',
            'Release year_2',
            ('Songs2',
             (
                 ('1', 'SongOneTwo'),
                 ('2', 'SongTwoTwo')
             )
             )
        )
    )

for album in albums:
    print(album)
    albumName, artistName, releaseYear, songs = album
    print(albumName, artistName, releaseYear, songs,sep=':::')
    fieldTitle, songNames = songs
    for song in songNames:
        print(song, sep='---------')
