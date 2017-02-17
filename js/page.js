//Add Hover effect to menus
$('ul.nav li.dropdown').hover(function() {
    if ($(window).width() >= 768) {
        $(this).find('.dropdown-menu').stop(true, true).delay(0).fadeIn(100);
    }
}, function() {
    if ($(window).width() >= 768) {
        $(this).find('.dropdown-menu').stop(true, true).delay(0).fadeOut(100);
    }
});
