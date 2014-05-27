# Reading a Scholarly Article

This project is heavily based on the original [NCSU Library application by
the same name](https://www.lib.ncsu.edu/tutorials/scholarly-articles/)

## Release 0.4

* Pushed down footer
* Changed project name

### ToDo

* Add more fields' papers
  * Create Pulic Health article
  * Create Humanities article
* Create annotations for every field
* Change colorscheme
* Use a simpler font
* Make annotation triggers more visually distinctive
* Flesh out homepage text & documentation
* Make the 'return home' icon a little more distinct
* Add a copyright notice at the bottom of each article

## Setup

The only system requirement for this project is PHP 5. This is used,
minimally, for the templating system.

The following Apache virtualhost configuration directives are highly
recommended.

    ...
    DocumentRoot /path/to/install/webroot
    <Directory /path/to/install/webroot>
        DirectoryIndex index.php
        Options -Indexes
        AllowOverride FileInfo
        ...
    </Directory>
    ...


## Getting Started

There are two main ways to contribute to this project:

* adding new article translations
* maintaining popover article annotations

### Adding New Translations

Creating a new article translation is a labor intensive process. The first
step is duplicating the sample article in the content directory:

    cp webroot/content/sample.content webroot/content/newfield.content

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

    <img src="content/assets/newfield/figXXX.png"
    class="figure"/>

    <p class="caption">
      Fig. XXX. Caption text.
    </p>

and place it inline at the same level as the `<p></p>` blocks of your
section.

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

#### Adding the content

Now that you have the `AnnotationName` trigger installed, it's a simple
matter of placing the following code in a new file
`webroot/content/assets/newfield/annotations.js`:

    $("#AnnotationName").popover({
      toggle:    "popover",
      trigger:   "click",
      placement: "auto", // top, left, bottom, right

      title:   "Title text here",
      content: "Body text here",
    });

Make sure to include this new file at the very end of the
`newfield.content` file you created.

    <script src="content/assets/newfield/annotations.js">
    </script>
