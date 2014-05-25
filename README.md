# Anatomy of a Scholarly Article

This project is heavily based on the original [NCSU Library application by
the same name](https://www.lib.ncsu.edu/tutorials/scholarly-articles/)

## Release 0.3

* Added initial CSS framework.
* Minimally structured website.
* Introduced simple PHP templating system
* Completed Engineering articles translation

### ToDo

* Add in 'popover' text descriptions.
* Create more articles

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
interactive, simply modify it as

    <a id="AnnotationName">text for trigger</a>

#### Adding the content

Now that you have the `AnnotationName` trigger installed, it's a simple
matter of placing the following code at the very end of the article content
file. Make sure the IDs match!


    <script>
      $("#AnnotationName").popover({
        toggle:    "popover",
        trigger:   "click",
        placement: "top", // top, left, bottom, right, auto

        title:   "Title text here",
        content: "Body text here",
      });
    </script>
