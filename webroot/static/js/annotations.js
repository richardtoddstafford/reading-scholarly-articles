$("[rel='popover']").click(function () {
    $("[rel='popover']").not(this).popover('hide');
});
