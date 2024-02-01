#!/usr/bin/env ruby

log_line = ARGV[0]

# Extracting sender, receiver, and flags from the log line
sender = log_line.scan(/\[from:(\S+)\]/).flatten.first
receiver = log_line.scan(/\[to:(\S+)\]/).flatten.first
flags = log_line.scan(/\[flags:(.*?)\]/).flatten.first

# Outputting the result in the required format
puts "#{sender},#{receiver},#{flags}"

