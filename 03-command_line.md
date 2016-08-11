# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
  List  information  about  the FILEs (the current directory by default).
       Sort entries alphabetically if none of -cftuvSUX nor --sort  is  speci‐
       fied.

`ls -a`  
       -a, --all
              do not ignore entries starting with .

`ls -l`   -l     use a long listing format

`ls -lh`   -h, --human-readable
              with -l and/or -s, print human readable sizes (e.g., 1K 234M 2G)


`ls -lah`  List files, use long listing format, include entries starting with a .

`ls -t`    list files, sort by modification time, newest first

`ls -Glp`  list files, apend group names, use long listing format, append / for directories

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

ls -R   Recursive. Also list files in subdirectories.
ls -d   List only directories
ls -o   Displays the long format listing, but excludes group name.
ls -b   Displays non-printing characters in octal
ls -L   Displays the file or directory referenced by a symbolic link.



---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

xargs is used to build and run a command line using standard input.  Many key linux commands (like awk and grep) will take the standard input as a parameter by using a pipe.

Example:
echo a b c d e f| xargs -p -n 3
/bin/echo a b c ?...y
/bin/echo d e f ?...a b c
y
d e f

 

