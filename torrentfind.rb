#!/usr/bin/env ruby -rubygems
#
require 'rubygems'
require 'hpricot'
require 'rss/1.0'
require 'rss/2.0'
require 'open-uri'

PandoraFav = 'http://feeds.pandora.com/feeds/people/ykabhinav/favorites.xml'
LastfmFav = ''

Search = ARGV.join ' '

def search_the_pirate_bay
  doc = Hpricot(open("http://thepiratebay.org/search/#{Search}/0/99/0"))

	results = (doc/"#searchResult")
	(results/"tr//a").each do |result|
		next unless result["href"] =~ /.*cat.*/

		puts result
	end
end

def search_mininova

end

def get_fav_pandora
	content = open(PandoraFav).read
	rss = RSS::Parser.parse(content, false)

	artists = []
	rss.items.collect do |item|
		song, artist = item.title.split(' by ')
		artists << artist
	end
	artists = artists.sort.uniq
	puts artists
end

def get_fav_lastfm

end

get_fav_pandora
