$(document).ready(function () {
    // Open on #hamburger-bars click
    $("#hamburger-bars").click(function () {
        if ($("#popout").hasClass("hide")) {
            $("#popout").removeClass("hide");
            event.stopPropagation();
        }
    });
    // Close on #hamburger-x click
    $("#hamburger-x").click(function () {
        if (!$("#popout").hasClass("hide")) {
            $("#popout").addClass("hide");
            event.stopPropagation();
        }
    });
    // Close on external click
    $(document).click(function (event) {
        // .closest function returns array with jQuery object of closest #popout
        if (
            !$(event.target).closest("#popout").length &&
            !$("#popout").hasClass("hide")
        ) {
            $("#popout").addClass("hide");
        }
    });
    // Hide on scroll-down, show on scroll-up
    var oldScroll = $(window).scrollTop();
    $(window).on("scroll", function () {
        var newScroll = $(window).scrollTop();
        // Scrolling down - hide
        if (newScroll > oldScroll) {
            // Desktop
            if ($(window).width() > 575) {
                $("#desktop-scroll").css("top", $("#desktop-scroll").height() * -1);
            }
            // Mobile
            else {
                $("#mobile-scroll").css("top", $("#mobile-scroll").height() * -1);
            }
        }
        // Scrolling up - show
        else {
            $("#desktop-scroll, #mobile-scroll").css("top", 0);
        }
        oldScroll = newScroll;
    });
});