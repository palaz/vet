
$(document).ready(function() {

    $('.image-popup-no-margins').magnificPopup({
        type: 'image',
        closeOnContentClick: true,
        closeBtnInside: false,
        fixedContentPos: false,
        mainClass: 'mfp-with-zoom', // class to remove default margin from left and right side
        image: {
            verticalFit: true
        },
        zoom: {
            enabled: true,
            duration: 300 // don't foget to change the duration also in CSS
        }
    });

    $('.shape').shape({
        duration: '1000ms'
    });

    $('.carousel')
        .css("visibility", "visible")
        .transition({
            animation: 'fade in',
            duration: '750ms'
        })
    ;

    $('.ui.dropdown.item')
        .dropdown({
            on: 'hover',
            delay: {
                show: 100,
                hide: 300}
        })
    ;

    $('.ui.dropdown.button')
        .dropdown({
            delay: {
                show: 100,
                hide: 300}
        })
    ;

    $('.ui.accordion')
        .accordion({
            exclusive: true
        })
    ;

    $('.right.sidebar')
        .sidebar('attach events', '.toggle')
    ;

    $('.ani-card')
        .css("visibility", "visible")
        .transition({
            animation: 'browse in',
            duration: '750ms'
        })
    ;

    $('.ani-logo')
        .transition({
            animation: 'jiggle',
            duration: '1000ms'
        })
    ;

    setTimeout(function(){
            $('.pulse-logo')
                .css("visibility", "visible")
                .transition({
                    animation: 'drop in',
                    duration: '500ms'
                });
        },
        1000);


    $('article')
        .css("visibility", "visible")
        .transition({
            animation: 'slide down in',
            duration: '750ms'
        })
    ;


    $('.flip-img')
        .css("visibility", "visible")
        .transition({
            animation: 'horizontal flip in',
            duration: '1500ms'
        })
    ;

    $('.animated.call.icon')
        .transition('set looping')
        .transition({
            animation: 'tada',
            duration: '1.5s'
        })
    ;

    $('.left-side.button')
        .on('click', function() {
            $('.shape')
                .shape('flip left')
        })
    ;

    $('.right-side.button')
        .on('click', function() {
            $('.shape')
                .shape('flip right')
        })
    ;

    $('.ani-card')
        .popup({
            position: 'top center'
        })
    ;

    $('.servizio')
        .transition({
            animation : 'tada',
            duration  : '750',
            interval  : '150'
        })
    ;

});


new Waypoint.Inview({
    element: $('.flip-logo')[0],
    entered: function(direction) {
        if ($('.flip-logo').css("visibility") == "hidden")
            $('.flip-logo').css("visibility", "visible")
                .transition({
                    animation: 'scale in',
                    duration: '750ms'
                });
    }
});

new Waypoint.Inview({
    element: $('header')[0],

    exited: function(direction) {
        $('.main.menu')
            .css('visibility', 'visible')
            .transition({
                animation: 'slide down in',
                duration: '500ms'
            })
        ;
    },

    enter: function(direction) {
        if ($('.main.menu').css("visibility") == "visible")
            $('.main.menu')
                .transition({
                    animation: 'slide down',
                    duration: '500ms'
                })
                .css('visibility', 'hidden')
            ;
    }
});


