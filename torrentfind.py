#!/usr/bin/env python

import xmlparser
import lastfmstats
import string
import webbrowser
import urllib
import urllib2

def search_pirate_bay(album, num):
    """album is a list (of lists) containing
    [0] album rank on last.fm
    [1] album name
    [2] artist name
    num is the max albums to search for each artist
    """
    
    for i in range(0, num):
        search = '%20'.join(album[i])
        search_string = 'http://thepiratebay.org/search/%s/0/7/0' % search
        webbrowser.open(search_string)

def retrieve_xml_data(user, method, extra_data=None):
    lfm = lastfmstats.Lastfm_Stats()
    lfm.set_user(user)
    lfm.set_method(method)
    if extra_data is not None:
        lfm.add_get_data(extra_data)
    lfm.request_data()
    return lfm.filename
    
def parse_data(filename, wanted_data):
    par = xmlparser.XML_Parser(filename, wanted_data)
    par.run_iterator()
    return par.collected
    
def run():
    user = 'woodenbrick'
    fname = retrieve_xml_data(user, 'user.getLovedTracks')
    parser = xmlparser.XML_Parser(fname, ['name', 'name'])
    parser.run_iterator()
    loved_tracks = parser.collected

    #for each loved track, we need to get the top 5 albums of this artist
    for track in loved_tracks:
        #check our database and see if this artist has already been added
        #if so, continue to next
        while True:
            answer = raw_input('Would you like to search for albums by %s? You loved the track %s\ny/n:'
              % (track[1], track[0]))
            if answer == 'y' or answer == 'n':
                break
            else:
                print 'please answer y or n'
        if answer == 'y':
            #add to database
            artist_info = {'artist' : track[1]}
            fname = retrieve_xml_data(user, 'artist.getTopAlbums', artist_info)
            parser = xmlparser.XML_Parser(fname, ['name', 'album', 'name'], {'album' : 'rank'})
            parser.run_iterator()
            albums = parser.collected
            #lets just get the top album for now
            search_pirate_bay(albums, 1)
    
if __name__ == '__main__':
    run()
