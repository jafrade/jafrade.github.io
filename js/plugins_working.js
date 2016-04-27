// Avoid `console` errors in browsers that lack a console.
if (!(window.console && console.log)) {
    (function() {
        var noop = function() {};
        var methods = ['assert', 'clear', 'count', 'debug', 'dir', 'dirxml', 'error', 'exception', 'group', 'groupCollapsed', 'groupEnd', 'info', 'log', 'markTimeline', 'profile', 'profileEnd', 'markTimeline', 'table', 'time', 'timeEnd', 'timeStamp', 'trace', 'warn'];
        var length = methods.length;
        var console = window.console = {};
        while (length--) {
            console[methods[length]] = noop;
        }
    }());
}

// Place any jQuery/helper plugins in here.

$(document).ready(function(){
/* 	location.hash = ""; */
	
	$('#siteNav').onePageNav({
		changeHash: true
	});//jquery nav

	
/******************************************************************************	
	
	click function handling page scrolling

******************************************************************************/	

/*
   $('#siteNav a').bind('click', function(e) {
	e.preventDefault(); //prevent the "normal" behaviour which would be a "hard" jump
       
	var target = $(this).attr("href"); //Get the target
			
	// perform animated scrolling by getting top-position of target-element and set it as scroll target
	$('html, body').stop().animate({ scrollTop: $(target).offset().top }, 500, function() {
	     location.hash = target;  //attach the hash (#jumptarget) to the pageurl
	});
			
	return false;
   });
*/
/******************************************************************************	
	
	click function handling work detail

******************************************************************************/	
/*
   	$.ajaxSetup({cache:false});
	var ajax_load = "<img src='img/ajax-loader.gif' alt='loading' />";
	
	$('.workView').hide();


	$(".work-row .work_col a").bind('click', function(){
		//selects id of the li clicks 
		var itemId = $(this).attr('id');
		//loads the workpages page from server
		var loadUrl = 'work/workPages.html';
		//attaches the  id ("#") definition to the itemId var
		var idIt = '#'+itemId;
		//takes the url to the workpages page and targets selects the id within the page
		var stringIt = loadUrl + ' ' + idIt;
		//selects the header html from the details hover
		var headerContent = $(".details > h4",this).html();
		//loads the selected section (stringIt) into the work details content
		$(".workView .container").html(ajax_load).load(stringIt);

		$('html, body').stop().animate({ scrollTop: $('.workViewTarget').offset().top - 90}, 500, function() {
			$(".lightWrap h1").text(headerContent);	
			$(".lightWrap").prepend("<h1></h1>");
			
			//prepend an h1 tag into the work details
			//add the header html from the details hover into the work details header
			
			$('.workView').slideDown(1000);
			$(".closeWorkView").show();
			location.hash = idIt;  //attach the hash (#jumptarget) to the pageurl
			return false;

		});		

	});//end box li bind
	
	$(".closeWorkView").bind('click',function(){
		$(".closeWorkView").hide();
		$('html, body').stop().animate({ scrollTop: $(location.hash).offset().top - 330 }, 500, function() {
			$('.workView').slideUp(500);
		});	
		
		location.hash = "";
	});
*/
});




/*
$(document).keyup(function(e) {
    if (e.keyCode == 27) { // escape key
		$(".closeWorkView").hide();
		
		$('html, body').stop().animate({ scrollTop: $('#filterWork').offset().top }, 500, function() {
			$('.workView').slideUp(500);
		});	
    }
});

/******************************************************************************	
	
	Form Validation

******************************************************************************/	

$(document).ready(function() {
	$.validator.addMethod("equalToParam", function(value, element, param) {
	  return value == param;
	},
    "Does not match.");
    
    if($("#thankYou h1").length){
		setTimeout("$('#thankYou h1').fadeOut('slow');",2000);
	}
	else{
		//alert("ho");
	}
// validate signup form on keyup and submit
var validator = $("#form1").validate({
	rules: {
		firstName: "required",
		subject: "required",
		email: {
			required: true,
			email: true,
		},
		checkRobot: {
			equalToParam:"4",
		},
		mess: "required",
	},
	messages: {
		firstName: "Please tell me who you are",
		subject: "What is your message about?",
		email: "Can I please have your email so I can reply?",
		checkRobot: "You need to prove your not a robot first.",
		mess: "What is your message about?",
	},
	// specifying a submitHandler prevents the default submit, good for the demo
	submitHandler: function() {
		form.submit();
		//alert("submitted!");
	},
	// set this class to error-labels to indicate valid fields
	success: function(label) {
	// set &nbsp; as text for IE
	label.html("&nbsp;").addClass("checked");
	},
	
	});

	
});  
