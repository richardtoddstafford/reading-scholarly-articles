import os
import sys
import logging

class Section():

    def __init__(self,
                 heading = "Section Heading",
                 level = "1",
                 pars = ["First paragraph."]):
        self.heading = heading
        self.level = level
        self.pars = pars


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


# Read in a single line of input.
def read_line( prompt="" ):
    return input( prompt )


# Read in a single, non-empty line of input.
def read_line_valid( prompt="" ):
    line = read_line( prompt )
    if line != "": return line
    else: return read_line_valid( prompt )


# Read multiple lines into a list until an empty line is given.
def read_line_multi( prompt="" ):
    lines = []
    while True:
        line = read_line( prompt )
        if line == "":
            break
        lines.append( line )
    return lines


# Prompt the user to proceed.
def proceed( prompt="Continue input? [y/n]: " ):
    usr = read_line( prompt ).lower()
    if usr == "y": return True
    if usr == "n": return False
    return proceed( prompt )


# Read in a single paragraph of input.
# ^D ends input.
def read_par( prompt="Type paragraph below. CTRL+D to end." ):
    if prompt != "":
        print( prompt )
    lines = []
    for line in sys.stdin:
        lines.append( line[:-1] )
    return '\n'.join( lines )


# Read in multiple paragraphs into a list until an empty paragraph is
# given.
def read_par_multi( prompt="" ):
    if prompt != "":
        print( prompt )
    pars = []
    while True:
        par = read_par( )
        pars.append( par )
        if not proceed( "Enter another paragraph? (y/n): " ):
            break
    return pars


# Wrap an item in an element (tag or tag with attributes).
# If that item is a list, wrap each item in that list individually.
def wrap_in( item, element="p"  ):
    try:
        tag = element[:element.index(" ")]
    except ValueError:
        tag = element
    out = None
    if type( item ) is list:
        out = []
        for i in item:
            out.append( "<%s>%s</%s>\n" % (element, i, tag) )
    elif type( item ) is str:
        out = ""
        out = "%s\n<%s>%s</%s>\n" % (out, element, item, tag)
    else:
        raise Exception("Unhandleable type of: %s." % item)
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
    logging.info( "Begin data collection." )
    data = {}

    # Collect field meta data.
    print( "\n1) Enter field metadata." )
    data['field_id']    = read_line_valid( "Enter field ID (ex: eng, cs, sci): " ).lower()
    data['field_title'] = read_line_valid( "Enter field title: ")

    """
    # Pull in overview paragraphs.
    print( "\n2) Enter the field overview, paragraph by paragraph." )
    data['overview'] = read_par_multi( )
    """


    # Pull in title.
    print( "\n3) Enter article title." )
    data['title'] = read_line_valid( "Title: " )


    # Pull in authors and affiliations.
    print( "\n4) Enter authors and affiliations.\n"
           "   Author names one at a time, with an empty line to end." )
    data['authors'] = read_line_multi( "Author name (one at a time): " )


    data['affiliations'] = []
    for author in data['authors']:
        data['affiliations'].append( read_par( "Enter affiliation for "
                "%s." % author ) )


    # Pull in abstract.
    print( "\n5) Enter paragraphs of abstract." )
    data['abstract'] = read_par_multi( )


    # Start pulling in sections.
    print( "\n6) Begin entering sections." )
    data['sections'] = []
    while True:
        data['sections'].append( Section(
            heading = read_line_valid( "Section heading: " ),
            level   = read_line_valid( "Section level (1,2,3...): " ),
            pars    = read_par_multi( "Enter section paragraphs below." ) ) )
        if not proceed( "Enter another section? (y/n): " ):
            break


    # Begin converting the overview into paragraphs.
    logging.info( "Begin formatting overview." )
    data['overview'] = wrap_in( data['overview'], "p" )
    data['overview'] = '\n'.join( data['overview'] )

    # Begin converting raw article data to formatted niceness.
    logging.info( "Begin formatting article." )
    data['article'] = ""

    data['title'] = get_row( wrap_in( data['title'], "h1" ) )
    data['article'] = "%s\n%s\n" % (data['article'], data['title'])

    data['authors'] = wrap_in( data['authors'], "strong" )
    data['authors'] = ', '.join( data['authors'] )
    data['authors'] = wrap_in( data['authors'], "p" )
    data['authors'] = get_row( data['authors'] )
    data['article'] = "%s\n%s\n" % (data['article'], data['authors'])

    data['affiliations'] = wrap_in( data['affiliations'], "em" )
    data['affiliations'] = ','.join( data['affiliations'] )
    data['affiliations'] = wrap_in( data['affiliations'], "p" )
    data['affiliations'] = get_row( data['affiliations'] )
    data['article'] = "%s\n%s\n" % (data['article'], data['affiliations'])

    data['abstract'][0] = "<strong><em>Abstract</em></strong> — %s" % data['abstract'][0]
    data['abstract'] = wrap_in( data['abstract'] )
    data['abstract'] = '\n'.join( data['abstract'] )
    data['abstract'] = get_row( data['abstract'] )
    data['article'] = "%s\n%s\n" % (data['article'], data['abstract'])

    for section in data['sections']:
        section.heading = wrap_in( section.heading, "h%s" % section.level )
        section.heading = get_row( section.heading )
        data['article'] = "%s\n%s\n" % (data['article'], section.heading)

        section.pars = wrap_in( section.pars, "p" )
        section.pars = '\n'.join( section.pars )
        section.pars = get_row( section.pars )
        data['article'] = "%s\n%s\n" % (data['article'], section.pars)


    # Begin writing to file.
    logging.info( "Begin writing to file." )

    # Stat directory location.
    new_article_path = os.path.join( DIR_ARTICLES, data['field_id'] )

    try:
        os.mkdir( new_article_path )
    except OSError:
        logging.error( "Path %s already exists, exiting.", new_article_path )
        quit()

    logging.info( "Created directory %s.", new_article_path )

    FILE_TITLE = os.path.join( new_article_path, "title" )
    FILE_OVERVIEW = os.path.join( new_article_path, "overview" )
    FILE_ARTICLE = os.path.join( new_article_path, "article" )
    FILE_COPYRIGHT = os.path.join( new_article_path, "copyright" )

    title = open( FILE_TITLE, "w" )
    title.write( data['field_title'] )
    title.close()

    copyright = open( FILE_COPYRIGHT, "w" )
    copyright.write( "Nothing here." )
    copyright.close()

    """
    overview = open( FILE_OVERVIEW, "w" )
    overview.write( data['overview'] )
    overview.close()
    """

    article = open( FILE_ARTICLE, "w" )
    article.write( data['article'] )
    article.close()


if __name__ == '__main__':
    main()
