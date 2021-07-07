#!/usr/bin/env ruby

#Create a Ruby script that takes one argument and passes it to a regular
#expression matching method

ARGV.each do |input|
	h = input.scan(/h[0-9a-zA-Z_]*\W*n/).join
	puts h
end
