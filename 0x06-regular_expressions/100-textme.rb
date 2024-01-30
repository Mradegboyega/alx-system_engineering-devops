#!/usr/bin/env ruby

# Regular expression to extract relevant information from log entries
regex = /\[from:(?<sender>[^\]]+)\] \[to:(?<receiver>[^\]]+)\] \[flags:(?<flags>[^\]]+)\]/

# Loop through each line of input
ARGF.each do |line|
  # Match the regular expression and extract sender, receiver, and flags
  match_data = line.match(regex)

  # Output the result in the specified format
  puts "#{match_data[:sender]},#{match_data[:receiver]},#{match_data[:flags]}" if match_data
end

