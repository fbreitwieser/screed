#!/usr/bin/env python

import sys
import seqparse

# A python implementation of the FASTQ database writer
if __name__ == "__main__":
    # Make sure the user entered the command line arguments correctly
    if (len(sys.argv) < 2) or (len(sys.argv) > 3):
        sys.stderr.write("ERROR: USAGE IS: %s <dbfilename>\n" % sys.argv[0]);
        exit(1)

    filename = sys.argv[1]
    seqparse.read_fastq_sequences(filename)

    print "Database saved in %s_squeaqr" % sys.argv[1]