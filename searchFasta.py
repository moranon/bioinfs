# Search
#
# Jeff Parker        Feb 2009
#
# Take a string and find matches in a Fasta file
#    This can be useful when validating other tools
#    Search is not case sensitive
#
# Usage:
#       python search.py <file> <pattern>
#
# Pattern can be in quotes, or a single string
#
#       python search.py EColiK12.fasta "atggttaaag tttatgcccc" 
#       python search.py EColiK12.fasta  atggttaaagtttatgcccc

import string
import sys
import cs190FileUtil    # Utility to read Fasta files

if (len(sys.argv) < 3):
    print "Usage:   python", sys.argv[0], "<filename> <pattern>"
else:
    text = cs190FileUtil.readFastaFile(sys.argv[1])
    pattern = sys.argv[2]
    pattern = cs190FileUtil.prepare(pattern)  # Remove any blanks

    print "Search for", pattern

    # Look for start
    for pos in xrange(len(text)):
        if (pattern == text[pos:pos+len(pattern)]):
            # Print positions starting with 1
            print "Start:", pos+1
