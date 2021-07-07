#!/usr/bin/env ruby

#Create a Ruby script that takes one argument and passes it to a regular
#expression matching method

ARGV.each do |input|
	h = input.scan(/^h\wn$/).join
	puts h
end
