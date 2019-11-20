# showstatus

This is a very simple script - all it does is concatenate the contents of the
files in the ~/.local/status directory, and prints it on standard output. I use
it in my tmux setup; Once per minute, tmux will call this script and add its
output to the tmux status line.

This means that I can have other scripts on my machine which add these brief 
little status files to the ~/.local/status directory, and their contents is 
displayed on my tmux screen. For example, I wrote a little weather app which
puts the current weather in such a file so I always have an uptodate weather
report on my screen.
