$(document).ready(function () {
    
    var royalAlbertHeader = "Englands Royal Albert Hall";
    var volkswagenHeader = "1966 Volkswagen";
    var rollsRoyceHeader = "1930s Rolls Royce";
    var harryPotterHeader = "Harry Potter's Diagon Alley";
    var tardisHeader = "Inside The Tardis";
    var munnyDoctorHeader = "The Eleventh Doctor";
    var emersonHeader = "Emerson Digital Painting";

    var royalAlbertDescription = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi malesuada, mauris in elementum porta, elit purus aliquam magna, sit amet pretium ipsum orci eu libero.";
    var volkswagenDescription = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi malesuada, mauris in elementum porta, elit purus aliquam magna, sit amet pretium ipsum orci eu libero.";
    var rollsRoyceDescription = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi malesuada, mauris in elementum porta, elit purus aliquam magna, sit amet pretium ipsum orci eu libero.";
    var harryPotterDescription = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi malesuada, mauris in elementum porta, elit purus aliquam magna, sit amet pretium ipsum orci eu libero.";
    var tardisDescription = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi malesuada, mauris in elementum porta, elit purus aliquam magna, sit amet pretium ipsum orci eu libero.";
    var munnyDoctorDescription = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi malesuada, mauris in elementum porta, elit purus aliquam magna, sit amet pretium ipsum orci eu libero.";
    var emersonDescription = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi malesuada, mauris in elementum porta, elit purus aliquam magna, sit amet pretium ipsum orci eu libero.";
    
    
    $(".headerRoyalAlbert").text(royalAlbertHeader);
    $(".headerVolkswagen").text(volkswagenHeader);
    $(".headerRollsRoyce").text(rollsRoyceHeader);
    $(".headerHarryPotter").text(harryPotterHeader);
    $(".headerTardis").text(tardisHeader);
    $(".headerMunnyDoctor").text(munnyDoctorHeader);
    $(".headerEmerson").text(emersonHeader);

    
    $(".descriptionRoyalAlbert").text(royalAlbertDescription);
    $(".descriptionVolkswagen").text(volkswagenDescription);
    $(".descriptionRollsRoyce").text(rollsRoyceDescription);
    $(".descriptionHarryPotter").text(harryPotterDescription);
    $(".descriptionTardis").text(tardisDescription); 
    $(".descriptionMunnyDoctor").text(munnyDoctorDescription);
    $(".descriptionEmerson").text(emersonDescription);

    
    $('a[href*=#]:not([href=#])').click(function () {
        if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
            var target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
            if (target.length) {
                $('html,body').animate({
                    scrollTop: target.offset().top
                }, 1000);
                return false;
            }
        }
    });


    //Hide prev and next arrows
    $("#project_gallery_prev").hide();
    $("#project_gallery_next").hide();

    //hide and show prev arrow when mouse enters and exits
    $(".project_slider").mouseenter(function () {
        $("#project_gallery_prev").show();
    });
    $(".project_slider").mouseleave(function () {
        $("#project_gallery_prev").hide();
    });

    //hide and show next arrow when mouse enters and exits
    $(".project_slider").mouseenter(function () {
        $("#project_gallery_next").show();
    });
    $(".project_slider").mouseleave(function () {
        $("#project_gallery_next").hide();
    });


    //this makes it so the button doesn't bug out when leaving the project slider and entering the button
    $("#project_gallery_next").mouseenter(function () {
        $(this).show();
        $("#project_gallery_prev").show();
    });
    $("#project_gallery_next").mouseleave(function () {
        $(this).hide();
        $("#project_gallery_prev").hide();
    });

    //this makes it so the button doesn't bug out when leaving the project slider and entering the button
    $("#project_gallery_prev").mouseenter(function () {
        $(this).show();
        $("#project_gallery_next").show();
    });
    $("#project_gallery_prev").mouseleave(function () {
        $(this).hide();
        $("#project_gallery_next").hide();
    });

    
});