$(document).ready(function () {
    (function () {
        var words = ["Python", "C/C++", "Ruby", "Machine Learning", "Data Structure"],
            i = 0;
        setInterval(function () {
            $('#words').fadeOut(function () {
                $(this).html(words[(i = (i + 1) % words.length)]).fadeIn();
            });
        }, 3000)
    })();
});

$(document).ready(function () {
    $('.title-body').hover(function () {
        console.log("Clicked!!");
    });
});