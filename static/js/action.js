// $(document).ready(function(){
//     $('[data-toggle="tooltip"]').tooltip();   
// });

$('a[data-toggle="tooltip"]').tooltip({
    animated: 'fade',
    placement: 'bottom',
    html: true
});

$(document).ready(function () {
    $('a.nav-link.dropdown-toggle').click(function() {
        location.href = this.href;
    });
});