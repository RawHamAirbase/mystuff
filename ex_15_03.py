import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

cur.executescript('''
drop table if exists Artist;
drop table if exists Genre;
drop table if exists Album;
drop table if exists Track;

CREATE table Artist (id integer not null primary key AUTOINCREMENT unique,
                     name text unique );
CREATE table Genre (id integer not null primary key autoincrement unique,
                    name text unique);
CREATE table Album (id integer not null primary key autoincrement unique,
                    artist_id integer, title text unique);
CREATE table Track (id integer not null primary key autoincrement unique,
                    title text unique,
                    album_id integer,
                    genre_id integer,
                    len integer,
                    rating integer,
                    count integer);
''')

fname = input('Enter file name: ')
if len(fname) < 1: fname = 'Library.xml'

data = ET.parse(fname)
data_1 = data.findall('dict/dict/dict')

def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

for entry in data_1:
    if (lookup(entry, 'Track ID') is None) : continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    genre = lookup(entry, 'Genre')

    if name is None or artist is None or album is None :
        continue


    cur.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    try:
        genre_id = cur.fetchone()[0]
    except: genre_id = 'N/A'

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, len, rating, count, genre_id)
        VALUES ( ?, ?, ?, ?, ?, ?)''',
        (name, album_id, length, rating, count, genre_id))

    cur.execute('SELECT * from Track ORDER BY title ASC')


conn.commit()
