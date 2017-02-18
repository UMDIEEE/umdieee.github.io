// Add Hover effect to menus
$('ul.nav li.dropdown').hover(function() {
    if ($(window).width() >= 768) {
        $(this).find('.dropdown-menu').stop(true, true).delay(0).fadeIn(100);
    }
}, function() {
    if ($(window).width() >= 768) {
        $(this).find('.dropdown-menu').stop(true, true).delay(0).fadeOut(100, function() {
                /* Unset "display: none;" */
                this.style.display = "";
            }
        );
    }
});

function umdieee_toggleAdjust() {
    var menus = $('ul.nav li.dropdown .dropdown-toggle');
    if ($(window).width() >= 768) {
        console.log("attempting to remove data-toggle attr");
        menus.removeAttr("data-toggle");
        menus.attr('aria-expanded', 'false');
        menus.parent().removeClass('open');
        menus.find('.dropdown-menu').stop(true, true).delay(0).fadeOut(100, function() {
                /* Unset "display: none;" */
                this.style.display = "";
            }
        );
    } else {
        console.log("adding data-toggle attr");
        menus.attr("data-toggle", "dropdown");
    }
}

$(window).resize(umdieee_toggleAdjust);
$(document).ready(umdieee_toggleAdjust);
