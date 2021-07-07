#!/usr/bin/env ruby

ARGV.each do |input|
	h = input.scan(/Holberton/).join
	puts h
end
