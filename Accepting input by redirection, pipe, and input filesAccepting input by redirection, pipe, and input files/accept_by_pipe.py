#! python3
import sys

#Pipe is another form of redirection

for n in sys.stdin:
    
    print ( int(n.strip())//2 )