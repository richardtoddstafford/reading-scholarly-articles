import os
import sys
import logging


def welcome_msg():
    print( "    _    _ _______ __  __ _      _  __         " )
    print( "   | |  | |__   __|  \/  | |    (_)/ _|        " )
    print( "   | |__| |  | |  | \  / | |     _| |_ _   _   " )
    print( "   |  __  |  | |  | |\/| | |    | |  _| | | |  " )
    print( "   | |  | |  | |  | |  | | |____| | | | |_| |  " )
    print( "   |_|  |_|  |_|  |_|  |_|______|_|_|  \__, |  " )
    print( "                                        __/ |  " )
    print( "                                       |___/   " )
    print( "                                               " )
    print( "           Welcome to HTMLify v0.0a            " )
    print( "                                               " )
    print( " Line prefix definitions:                      " )
    print( "                                               " )
    print( " * Prompt:   This field must be filled         " )
    print( " + Prompt:   Enter as many as you want, leave blank to end." )
    print( "                                               " )


# Read any line of input from stdin.
def read_line( prompt="Enter line." ):
    print( prompt )
    return sys.stdin.readline()[:-1]


# Read only non-empty lines of input from stdin.
def read_valid_line( prompt="Enter nonempty line." ):
    while True:
        line = read_line( prompt )
        if line != "":
            return line


# Read lines from stdin until empty.
def read_until_empty( prompt="Enter lines, one at a time." ):
    print( prompt )
    lines = []
    for line in sys.stdin:
        if line[:-1] == "":
            break
        lines.append( line[:-1] )
    return lines


# Read a whole paragraph from stdin.
def read_par( prompt="Enter paragraph. Empty line to end." ):
    lines = read_until_empty( prompt )
    return '\n'.join( lines )


# Read paragraphs until empty.
def read_pars( prompt="You will be prompted to enter multiple paragraphs." ):
    print( prompt )
    pars = []
    while True:
        par = read_par( )
        if par[:-1] == "":
            break
        pars.append( par )
    return pars


# Wrap an item in an element (tag or tag with attributes).
def wrap_in( item, element="p"  ):
    try:
        tag = element[:element.index(" ")]
    except ValueError:
        tag = element
    out = ""
    if type( item ) is list:
        for i in item:
            out = "%s\n<%s>%s</%s>\n" % (out, element, i, tag)
    elif type( item ) is str:
        out = "%s\n<%s>%s</%s>\n" % (out, element, item, tag)
    else:
        raise Exception("Unhandleable type in wrap_in_paragraphs.")
    return out


# Generate a simple row wrapping around some contents.
def get_row( contents="\n" ):
    return "<div class=\"row\">\n" \
           "  <div class=\"col-sm-12\">\n" \
           "    %s\n" \
           "  </div>\n" \
           "</div>" % contents


# Generate an empty section spacer.
def get_section_space():
    return "<div class=\"hidden-xs row section-space\">" \
           "</div>"


def main():

    # Format logging.
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

    # Initialize 'global' variables.
    DIR_PAGES = "pages"
    DIR_ARTICLES = os.path.join( DIR_PAGES, "articles" )
    DIR_SITE_PAGES = os.path.join( DIR_PAGES, "site" )
    logging.info( "Article storage in %s.", DIR_ARTICLES )

    # Print annoying welcome message.
    welcome_msg()

    # Set up data collection.
    data = {}

    # Collect field meta data.
    print( "\n1) Enter field metadata." )
    data['field_id']    = read_valid_line( "*  Enter field ID (ex: eng, cs, sci)." ).lower()
    data['field_title'] = read_valid_line( "*  Enter field title.")

    # Pull in overview paragraphs.
    print( "\n2) Enter the field overview, paragraph by paragraph." )
    overview_pars = read_pars( )
    data['overview'] = wrap_in( overview_pars )

    # Pull in title.
    print( "\n3) Complete basic article fields." )
    title = read_valid_line( "*  Title: " )
    data['title'] = wrap_in( title, "h1" )

    # TODO: Format authors & affiliations.
    authors  = read_until_empty( "+  Author (one at a time): " )

    affiliations = {}
    for author in authors:
        affiliations[author] = read_until_empty( "+  Affiliations for %s, one "
                "at a time: " % author )

    # Pull in abstract.
    abstract = read_valid_line( "*  Abstract: " )
    abstract = "<strong><em>Abstract</em></strong> — %s" % abstract
    data['abstract'] = wrap_in( abstract )

    # Start pulling in sections.
    print( "\n4) Start copying in sections from the text. Begin with headings." )
    headings = input_until_empty( "+ Enter TOP-LEVEL section headings: " )
    sections = {}
    for heading in headings:
        while True:
            sections[heading] = readstd( "+ Paragraph for %s: " % heading )



    ## Stat directory location.
    #new_article_path = os.path.join( DIR_ARTICLES, field_id )

    #try:
    #    os.mkdir( new_article_path )
    #except OSError:
    #    logging.error( "Path %s already exists, exiting.", new_article_path )
    #    quit()

    #logging.info( "Created directory %s.", new_article_path )



if __name__ == '__main__':
    main()
