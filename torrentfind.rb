#!/usr/bin/env ruby -rubygems
#
require 'rubygems'
require 'hpricot'
require 'open-uri'

search = $ARGV

def search_the_pirate_bay
  doc = Hpricot(open("http://thepiratebay.org/search/#{$ARGV.join}/0/99/0"))

end

print search_the_pirate_bay

