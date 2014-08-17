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
* maintaining popover article annotations

### Adding New Papers

Creating a new article translation is a labor intensive process. The first
step is duplicating an existing article in the content and title
directories:

    cp pages/content/cs pages/content/newfield
    cp pages/title/cs   pages/title/newfield

Begin editing your new `newfield.content` file. It contains four sample
sections and one sample popover annotation. Begin by completing the Title,
Author, and Abstract sections.

#### Adding a new section

Copy the sample Section block of code

    <!-- {{{ Section
    ========================================= -->
    <div class="hidden-xs row section-space">
    </div>

    <div class="row">
      <hr class="visible-xs" />
      <div class="col-sm-12 text-center serif uppercase">
        I. Section Title
      </div>
    </div>

    <div class="row">
      <div class="col-sm-12">

        <p>
          Section text.
        </p>

      </div>
    </div>
    <!-- }}} -->

and begin filling in text within the `<p></p>` blocks.

#### Adding a figure

To add a figure with a caption, simply use the template code:

    <img src="assets/newfield/figXXX.png" class="figure"/>

    <p class="caption">
      Fig. XXX. Caption text.
    </p>

and place it inline at the same level as the `<p></p>` blocks of your
section. Graphical assets can be stored in a new folder
`webroot/content/assets/newfield`.

### Adding New Popover Annotations

Popover annotations consist of two parts: the trigger and the content.

#### Adding a new trigger

The trigger of a popover annotation is the portion of the article text that
will become interactive. To mark a portion of the HTML article as
interactive, simply modify the containing HTML element as:

    id="AnnotationName"
    rel="annotation"

The `id` will be the name of this annotation. The `rel` attribute is used
to style and define behaviour of the triggering element.

For example, an annotation on a paragraph might look like

    <p id="AnnotationName" rel="annotation"> ... </p>

#### Adding the content

Now that you have the `AnnotationName` trigger installed, it's a simple
matter of adding a section to the central annotation dictionary file,
`assets/annotations.json`. Note that this file follows
standard JSON syntax, so make sure to check that it's valid after every
edit by using a tool like [JSONLint](http://jsonlint.com).

    "newfield": [
      {
        "id": "#AnnotationName",
        "title": "Annotation Title",
        "string": "The body of the annotation."
      },
      {
        "id": "#AnotherAnnotation",
        "title": "Annotation Title",
        "string": "The body of another annotation."
      }
    ]

If you're unfamiliar with JSON syntax, good
[tutorials](http://www.w3schools.com/json/) are available online. One of
the most common issues is forgetting commas `,` when required.

#### Linking to the content

Now that annotations and their triggers are defined, insert this code at
the end of the `newfield.content` file you just created.

    <script>
      getAnnotations( "newfield" );
    </script>

This code activates the annotations defined in `annotations.json` for the
`newfield.content` page. Make sure that the `newfield` name you picked
matches.
