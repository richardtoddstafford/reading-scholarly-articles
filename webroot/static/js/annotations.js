function getAnnotations( field ) {
  /*
   * This function causes the browser to read a local JSON file which
   * defines the annotations in every field. The specified field is
   * retrieved, and its annotations are constructed.
   *
   * The process for this is:
   *  1) loop over the annotations defined for this field
   *  2) define an 'alt' attribute for the trigger element
   *  3) define a jQuery 'popover' call for the trigger element
   */

  $.getJSON(
    "content/assets/annotations.json",
    function( data ) {
      // Read in the dictionary of annotations from a central JSON
      // dictionary.
      console.log( "Successfully read in JSON annotations." );

      // Grab only the annotations for this specific field.
      var annotations = data[field];

      // Verify that the field name was valid and annotations were found.
      if( ! annotations ) {
        console.error( "Field name '" + field + "' was not found in the " +
          "annotations dictionary." );
        return;
      } else {
        console.log( "Found '" + field + "' in JSON dictionary." );
      }

      // Loop over each annotation found and set its trigger's alt text as
      // well as define the popover for it.
      console.log( "Applying annotation data to annotations." );
      $.each(
        annotations,
        function( index, annotation ) {

          // Set the alt description of the trigger element.
          $( annotation.id ).attr('alt', annotation.string);

          // Define the popover for this annotation.
          $( annotation.id ).popover({
            toggle:    "popover",
            trigger:   "click",
            placement: "auto",

            title:   annotation.title,
            content: annotation.string,
          });
        }
      );

    }
  );

}
