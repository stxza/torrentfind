#!/usr/bin/env ruby -rubygems
#
require 'rubygems'
require 'hpricot'
require 'open-uri'

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

puts search_the_pirate_bay
