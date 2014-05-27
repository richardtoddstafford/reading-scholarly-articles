$("[rel='annotation']").click(function () {
    $("[rel='annotation']").not(this).popover('hide');
    $("[rel='annotation']").not(this).removeClass("active");
    $(this).toggleClass("active");
});
