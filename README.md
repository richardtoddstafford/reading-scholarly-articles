# Reading a Scholarly Article

This project is heavily based on the original [NCSU Library application by
the same name](https://www.lib.ncsu.edu/tutorials/scholarly-articles/)

## Release 0.4

* Pushed down footer
* Changed project name
* Made annotation dictionary easier to edit (JSON)
* Simplified font (made more readable)
* Added a copyright notice at the bottom of each article
* Noted the 'return home' icon in tool instructions
* Split fields into simple tree hierarchy
* Added build scripts
* Removed PHP templating in favour of a build system
* Introduced compatible block/inline trigger system
* Created placeholder pages for fields not-yet-decided-on

### ToDo

* Finish remaining fields' papers
* Simulate pagination
* Create annotations for every field
* Make annotation triggers more visually distinctive
* Flesh out homepage text & documentation

## Setup

The following Apache virtualhost configuration directives are highly
recommended.

    ...
    DocumentRoot /path/to/install/webroot
    <Directory /path/to/install/webroot>
        DirectoryIndex index.html
        Options -Indexes
        ...
    </Directory>
    ...

## Getting Started

There are two main ways to contribute to this project:

* adding new article translations
* maintaining current articles

### Deploy Project

To build the project into the default `webroot` directory, simply run the
build script. Point your webserver to the new directory.

    $ ./build.sh

### Adding New Papers

Creating a new article translation is a labor intensive process. The first
step is duplicating the sample article in the article directory:

    cp -r pages/articles/sample pages/articles/newfield

This should create five new files:

    pages/articles/newfield/annotations.json
    pages/articles/newfield/article.html
    pages/articles/newfield/copyright.txt
    pages/articles/newfield/overview.html
    pages/articles/newfield/title.txt

#### Setting the Field Title (title.txt)

This is the simplest component file. Just enter the title of this field on
a single line (eg. Computer Science or Sociology).

#### Field Overview (overview.html)

Create an introduction to the field in this file. All the templating is
taken care of for you, just add paragraphs in this file:

    <p> ... </p>

#### Article Copyright Notice (copyright.txt)

Put any copyright notice for the article in plain text in this file. It can
be blank if there is no applicable notice.

#### Article Annotations (annotations.json)

Enter annotations as a list of JS objects. The `id` refers to the name of
this annotation (and is used to link in with the article text), the `title`
is a human readable title (what appears in the popover title bar), and the
`string` is the annotation text.

    {"annotations": [
      {
        "id": "#sample",
        "title": "Sample",
        "string": "This is a sample."
      }
    ]}

Note that this file follows standard JSON syntax, so make sure to check
that it's valid after every edit by using a tool like
[JSONLint](http://jsonlint.com). If you're unfamiliar with JSON syntax,
good [tutorials](http://www.w3schools.com/json/) are available online. One
of the most common issues is forgetting commas `,` when required.

#### Article Body (article.html)

This is the most time consuming part of adding a new field. Look around
other fields for examples, but the general idea is to use standard
Bootstrap CSS to create an approximation of a scholarly article.

##### Adding a new section

Copy this sample Section block of code

    <div class="row">
      <div class="col-sm-12">
        <h2>I. Section Title</h2>
      </div>
    </div>

    <div class="row">
      <div class="col-sm-12">

        <p>
          Section text.
        </p>

      </div>
    </div>

and begin filling in text within the `<p></p>` blocks.

#### Adding a figure

To add a figure with a caption, simply use the template code:

    <img src="assets/newfield/figXXX.png" class="figure"/>

    <p class="caption">
      Fig. XXX. Caption text.
    </p>

and place it in your section. Graphical assets for a field (including
figures and equations) should be stored in the folder
`pages/articles/newfield/assets`.

#### Adding New Popover Annotations

Popover annotations consist of two parts: the trigger and the content.

##### Adding a new trigger

The trigger of a popover annotation is the portion of the article text that
will become interactive. To mark a portion of the HTML article as
interactive, simply modify the containing HTML element as:

    id="AnnotationName"
    rel="annotation"

The `id` will be the name of this annotation. The `rel` attribute is used
to style and define behaviour of the triggering element.

For example, an annotation on a paragraph might look like

    <p id="AnnotationName" rel="annotation"> ... </p>

If the annotation is to be an inline annotation, also set the element's
class attribute like

    <p id="AnnotationName" rel="annotation" class="inline"> ... </p>
