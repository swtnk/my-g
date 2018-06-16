$(function(){
    $(".fl").css({
        "display": 'none'
    });
    $("input[name='btnG']").prop('value', 'Search The Web');
    $("input[name='btnG']").addClass("btn btn-primary");
    $("input[name='q']").css({
        'padding' : '5px'
    });
    $("input[name='q']").addClass("form-control");
    $("input[name='btnI']").css('display', 'none');
    $("td[width='25%']").css({
        "width" : $(window).width()/3
    });
    $(window).resize(function(){
        $("td[width='25%']").css({
            "width" : $(window).width()/3
        });
    });
})