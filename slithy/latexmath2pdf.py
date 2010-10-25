#!/usr/bin/python2.5
from __future__ import with_statement # Until Python 2.6
"""
Converts LaTeX math to png images.
Run latexmath2png.py --help for usage instructions.
"""

"""
Author:
    Kamil Kisiel <kamil@kamilkisiel.net>
    URL: http://www.kamilkisiel.net

Revision History:
    2007/04/20 - Initial version

TODO:
    - Make handling of bad input more graceful?
---

Some ideas borrowed from Kjell Fauske's article at http://fauskes.net/nb/htmleqII/

Licensed under the MIT License:

Copyright (c) 2007 Kamil Kisiel <kamil@kamilkisiel.net>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
IN THE SOFTWARE.
"""

import os
import sys
import tempfile
import getopt

# Default packages to use when generating output
default_packages = [
        'amsmath',
        'amsthm',
        'amssymb',
        'bm'
        ]

def __build_preamble(packages):
    preamble = '\documentclass{article}\n'
    for p in packages:
        preamble += "\usepackage{%s}\n" % p
    preamble += "\pagestyle{empty}\n\\begin{document}\n"
    return preamble

def __write_output_pdf(infile, outdir, workdir = '.', prefix = '', num = 0, size = 1):
    try:
        # Generate the DVI file
        latexcmd = 'latex -halt-on-error -output-directory %s %s'\
                % (workdir, infile)
        rc = os.system(latexcmd)
        # Something bad happened, abort
        if rc != 0:
            raise Exception('latex error')

        # Convert the DVI file to PNG's
        dvifile = infile.replace('.tex', '.dvi')
        outprefix = os.path.join(outdir, prefix)
#        dvicmd = "dvipng -T tight -x %.4f -z 9 -bg Transparent "\
#                "-o %s%%d.png %s" % (size * 1000.0, outprefix, dvifile)
#        dvicmd = "dvips -E -x %.4f  "\
#                "-o %s%d.eps %s" % (size * 1000.0, outprefix, num, dvifile)

        epsfile = infile.replace('.tex', '.eps')
        dvicmd = ("dvips -E -x %.4f  "\
                "-o %s %s") % (size * 1000.0, epsfile, dvifile)
        print dvicmd
        rc = os.system(dvicmd)
        if rc != 0:
            raise Exception('dvips error')
        pdfcmd = "epspdf %s %s%.4d.pdf" % (epsfile,outprefix,num)
        rc = os.system(pdfcmd)
        if rc != 0:
            raise Exception('epspdf error')
    finally:
        # Cleanup temporaries
        basefile = infile.replace('.tex', '')
        tempext = [ '.aux', '.dvi', '.log' ]
        for te in tempext:
            tempfile = basefile + te
            if os.path.exists(tempfile):
                os.remove(tempfile)


def __write_output_png(infile, outdir, workdir = '.', prefix = '', num = 0, size = 1):
    try:
        # Generate the DVI file
        latexcmd = 'latex -halt-on-error -output-directory %s %s'\
                % (workdir, infile)
        rc = os.system(latexcmd)
        # Something bad happened, abort
        if rc != 0:
            raise Exception('latex error')

        # Convert the DVI file to PNG's
        dvifile = infile.replace('.tex', '.dvi')
        outprefix = os.path.join(outdir, prefix)
        dvicmd = "dvipng -T tight -x %.4f -D 600.0 -z 6 -bg transparent " % (size * 1000.0) + \
                "-o %s%.4d.png %s" % (outprefix, num, dvifile)
#        dvicmd = "dvips -E -x %.4f  "\
#                "-o %s%d.eps %s" % (size * 1000.0, outprefix, num, dvifile)

#        epsfile = infile.replace('.tex', '.eps')
#        dvicmd = ("dvips -E -x %.4f  "\
#                "-o %s %s") % (size * 1000.0, epsfile, dvifile)
        print dvicmd
        rc = os.system(dvicmd)
        if rc != 0:
            raise Exception('dvipng error')
#        pdfcmd = "epspdf %s %s%.4d.pdf" % (epsfile,outprefix,num)
#        rc = os.system(pdfcmd)
#        if rc != 0:
#            raise Exception('epspdf error')
    finally:
        # Cleanup temporaries
        basefile = infile.replace('.tex', '')
        tempext = [ '.aux', '.dvi', '.log' ]
        for te in tempext:
            tempfile = basefile + te
            if os.path.exists(tempfile):
                os.remove(tempfile)



def math2img(eqs, outdir, packages = default_packages, prefix = '', num = 0, size = 1, fmt='pdf'):
    """
    Generate png images from $...$ style math environment equations.

    Parameters:
        eqs         - A list of equations
        outdir      - Output directory for PDF images
        packages    - Optional list of packages to include in the LaTeX preamble
        prefix      - Optional prefix for output files
        size        - Scale factor for output
    """
    try:
        # Set the working directory
        workdir = tempfile.gettempdir()

        # Get a temporary file
        fd, texfile = tempfile.mkstemp('.tex', 'eq', workdir, True)

        # Create the TeX document
        tex_lines = []
        tex_lines.append(__build_preamble(packages))
        tex_lines.append("\\begin{eqnarray*}%s\end{eqnarray*}" % (eqs,))
        tex_lines.append('\\end{document}')

        with os.fdopen(fd, 'w+') as f:
            f.writelines(tex_lines)

        if fmt=='pdf':
            __write_output_pdf(texfile, outdir, workdir, prefix, num, size)
        elif fmt=='png':
            __write_output_png(texfile, outdir, workdir, prefix, num, size)
        else:
            raise "math2img: unknown format '%s'" % fmt
    finally:
        if os.path.exists(texfile):
            os.remove(texfile)

def usage():
    print """
Usage: %s [OPTION] ... [FILE] ...
Converts LaTeX math input to PDF or PNG.

Options are:
    -h, --help              Display this help information
    --outdir=OUTDIR         PNG file output directory 
                            Default: the current working directory
    --packages=PACKAGES     Comma separated list of packages to use
                            Default: amsmath,amsthm,amssymb,bm
    --prefix=PREFIX         Prefix output file names with PREFIX
                            Default: no prefix
    --scale=SCALE           Scale the output by a factor of SCALE. 
                            Default: 1 = 100%%

    --format=[pdf|png]

Reads equations from the specified FILEs or standard input if none is given. One
equation is allowed per line of text and each equation is rendered to a separate
PNG image numbered sequentially from 1, with an optional prefix.
    """ % (os.path.split(sys.argv[0])[1])

def main():
    try:
        shortopts = [ 'h', ]
        longopts = [
                'help',
                'outdir=',
                'packages=',
                'prefix=',
                'scale=',
                'format=',
                ]
        opts, args = getopt.getopt(sys.argv[1:], shortopts, longopts)
    except getopt.GetoptError, err:
        scriptname = os.path.split(sys.argv[0])[1]
        print "%s: %s" % (scriptname, err)
        print "Try `%s --help` for more information." % scriptname
        sys.exit(2)

    packages = []
    prefix = ''
    outdir = os.getcwd()
    scale = 1.0
    fmt = 'png'
    
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        if o in ("--packages"):
            packages = a.split(',')
        if o in ("--prefix"):
            prefix = a
        if o in ("--outdir"):
            outdir = os.path.abspath(a)
        if o in ("--scale"):
            scale = float(a)
        if o in ("--format"):
            fmt = str(a)
            assert fmt in ("png","pdf"), "Format either pdf, or png"

    input = []
    if args:
        # If filenames were provided on the command line, read their equations
        for a in args:
            fd = os.open(a, os.O_RDONLY)
            with os.fdopen(fd, 'r') as f:
                cur = map(lambda i: i.strip('\n'), f.readlines())
                input.extend(cur)
    else:
        # Otherwise read from stdin
        input = map(lambda i: i.strip('\n'), sys.stdin.readlines())

    # Engage!
    math2img("\n".join(input), outdir, packages, prefix, size=scale, fmt = fmt)

if __name__ == '__main__':
    main()
