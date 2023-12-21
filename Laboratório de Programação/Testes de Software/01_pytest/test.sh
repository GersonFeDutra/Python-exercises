#!/bin/bash
py.test ./main.py > main.log # Save to log file
py.test ./main.py # Print output

#py.test ./main.py > >(tee -a main.log)
# py.test ./main.py | tee main.log

# Print and save, while keeping colors
# Not working: printing without colors
# py.test ./main.py | tee >(sed -r 's/\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]//g' > main.log)

# Don't working: not filtering all color characters
# unbuffer py.test ./main.py | tee >(sed -r 's/\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]//g' > main.log)
# Note: unbuffer is installed with `sudo apt-get install expect-dev`
# See: <https://superuser.com/questions/352697/preserve-colors-while-piping-to-tee#751809>
