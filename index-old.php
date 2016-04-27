<?php

$thankUser = false;

if(!empty($_POST['pb'])){
	$firstName = $_POST["firstName"];
	$subject = $_POST["subject"];
	$email = $_POST["email"];
	$mess = $_POST["mess"];
	$to ='jason.a.frade@gmail.com';
	$message = "This message is from ". $firstName . ".". " Their email is " .  $email .".". " Their Message is: " . $mess . ".";
	$headers = "From:" . $email;
	mail($to,$subject,$message,$headers);
	$thankUser = true;
}
else{
	$thankUser = false;
}
?>

<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
<head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" container="IE=edge,chrome=1">
        <title>User Experience Design Portfolio of Jason Frade</title>
        <meta name="description" container="User Experience Design Portfolio of Jason Frade">
        <meta name="viewport" container="width=device-width, initial-scale=1, maximum-scale=1">
        <meta name="keywords" container="Usability,UX,Web Design,Boston,HTML,HTML5,CSS,CSS3,jQuery,Jason Frade, Portfolio,">

        <!-- Place favicon.ico and apple-touch-icon.png in the root directory -->
         <link rel="shortcut icon" href="http://www.jasonfrade.com/favicon.ico">
         <link rel="apple-touch-icon" sizes="57x57" href="apple-touch-icon-57x57-precomposed.png" />
         <link rel="apple-touch-icon" sizes="72x72" href="apple-touch-icon-72x72-precomposed.png" />
         <link rel="apple-touch-icon" sizes="114x114" href="apple-touch-icon-114x114-precomposed.png" />
         <link rel="apple-touch-icon" sizes="144x144" href="apple-touch-icon-144x144-precomposed.png" />

        <link rel="stylesheet" href="css/normalize.css">
        <link rel="stylesheet" href="css/style_working.css">
        <link rel="stylesheet" href="css/font-awesome.min.css">        

        <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
        <script>window.jQuery || document.write('<script src="js/vendor/jquery-1.10.2.min.js"><\/script>')</script>
        <script src="js/plugins_working.js"></script>
        
<!--         <script type="text/javascript" src="http://jzaefferer.github.com/jquery-validation/jquery.validate.js"></script> -->
        <script src="js/waypoints.js"></script>
        <script src="js/validatious-custom-0.9.1.min.js"></script>       
        <script src="js/vendor/modernizr-2.6.1.min.js"></script>        
        

        <script type="text/javascript" src="js/jquery.nav.js"></script>
        <script type="text/javascript" src="js/jquery.scrollTo.js"></script>
        <script type="text/javascript" src="js/nbw-parallax.js"></script>
		<script type="text/javascript" src="js/jquery.localscroll-1.2.7-min.js"></script>
       	<script type="text/javascript" src="//use.typekit.net/lsx1pur.js"></script>
        <script type="text/javascript">try{Typekit.load();}catch(e){}</script>




</head>
    <body>

        <!--[if lt IE 7]>
            <p class="chromeframe">You are using an outdated browser. <a href="http://browsehappy.com/">Upgrade your browser today</a> or <a href="http://www.google.com/chromeframe/?redirect=true">install Google Chrome Frame</a> to better experience this site.</p>
        <![endif]-->
            		<div id="thankYou">
                   		<?php if(!empty($_POST['pb']) && $thankUser = true){
                    	echo "<h1>Thanks for contacting me!</h1>";
               
                    	}?>
                    </div>
                    

            <header>
            	<div class="container">
           			<div id="welcome"></div>
                    <nav>
	                    <div class="col-6" id="logo">
		                    <a href="#top_of_page">
		                    	<img src="..///img/icon/miniLogo.png">
		                    	<span>Jason Frade</span>
		                    </a>
	                    </div>
	                    
	                    <div class="col-6">
	                        <ul id="siteNav">
	                            <li class="current"><a href="#top_of_page">Work</a></li>
	                            <li><a href="#aboutLand">About</a></li>
	                            <li><a href="#contact">Contact</a></li>
	                        </ul>
	                    </div>
	                    
                    </nav>
                </div>
            </header>
            
            <div class="hero_shot" id="top_of_page">
            	<img src="img/large/workspace.jpg">
            </div>
            
            <section id="work">
            	<div class="container">
	            	<div class="section_header">
		            	<h1>My Work</h1>   
	                </div>
	                                                            
                    <div class="row work-row">
                    	<div class="work_col col-4">
                    		<a href="work/coke.html" id="beverage">
                    			<img src="img/thumbs/coca_cola_thumb.png" alt="Fortune 500 Website User Analysis"> 
                    			<p class="project_title">Coca Cola</p>
                    			<p class="project_desc">Heuristic & User Analysis</p>                   	
                    		</a>
                    	</div>
                    	<div class="work_col col-4">
	                    	<a href="work/open_table.html" id="reservation">
	                    		<img src="img/thumbs/open_table_thumb.png" alt="Online Reservation Portal	 Website User Analysis">
                    			<p class="project_title">Open Table</p>
                    			<p class="project_desc">Heuristic & User Analysis</p>                   	
	                    	</a>
                    	</div>
                    	<div class="work_col col-4">
                    		<a href="work/freetime.html" id="freetime">
                    			<img src="img/thumbs/freetime_thumb.png" alt="Freetime App Design">
                    			<p class="project_title">FreeTime</p>
                    			<p class="project_desc">iPhone App Design</p>                   	
                    		</a>	
                    	</div>
                    </div>      
                                                                     
                    <div class="row work-row">
                    	<div class="work_col col-4">
                    		<a href="work/prius.html" id="prius">
                    			<img src="img/thumbs/prius_thumb.png" alt="prius console redesign">
                    			<p class="project_title">Toyota Prius</p>
                    			<p class="project_desc">Automobile Console App</p>                   	
                    		</a>	
                    	</div>
                    	<div class="work_col col-4">
                    		<a href="work/urbanscape.html" id="urban">
	                    		<img src="img/thumbs/urbanscape_thumb.png" alt="Urbanscape Design">
                    			<p class="project_title">Urbanscape</p>
                    			<p class="project_desc">Illustrator Concept</p>                   	
                    		</a>
                    	</div>                                        
                    	<div class="work_col col-4">
	                    	<a href="work/50s_horror_poster.html" id="poster">
	                    		<img src="img/thumbs/50sPoster_thumb.png" alt="1950's Horror Movie Poster">
                    			<p class="project_title">1950's Horror Poster</p>
                    			<p class="project_desc">Illustrator Concept</p>                   	
	                    	</a>	
                    	</div> 
                    </div> 
                   
            	</div>
            </section>
            
            
            <section id="about">
            	<div id="aboutLand"></div>
            	<div class="container">
                    <div class="section_header">
                        <h1>About</h1>
                    </div>                        
                    <div class="col col-7">
	                    <div class="about_copy">
	                    	<p>
	                    	<h4 class="about_copy_strong">Who am I?</h4> <p>My name is Jason Frade and I am motivated, I am creative, I am a collaborator, and I am a User Experience Designer.</p>
	                    	</p>
	
	                    	<p>Working as a user experience designer is the best job in the world. It is a job that allows me to think inside and outside of the box. I specialize in interaction design, usability and user research for web and mobile applications.	                    	
	                    	</p>
	
	                    	<p>I have been working for the past year creating a unique business web application experience for XPO Logistics, the fourth largest freight brokerage company in North America. In this role I have been responsible for developing their application used by the company’s 1,000+ employees.
	                    	</p>
	                    	<h4>A little extra something about me</h4>
	                    	<p>Working as a user experience designer is a huge part of my life because I am always thinking about ways to improve a user’s experience.. But there are a lot of things that make up who I am. I am a nerd at heart; cracking inside jokes about Star Wars movies(episodes 4-6), spending a whole day watching Harry Potter movies, and reading Game of Thrones is just a start to my nerdiness. </p>
	                    	<p>Other than being nerdy I also enjoy learning new cooking techniques, experiencing new wines, and traveling to new and exciting places.</p>
	                    </div>
                    </div>
                    
                    <div class="col col-5">
	                    <div class="about_img">
	                    	<img src="../img/meImg.jpg" />
	                    </div>
	                    <a href="http://jasonfrade.com/documents/Frade_resume.pdf" target="_blank" class="btn btn-large resume_btn">Browse My Resume</a>
                    </div>
                </div>
            </section>
            
            <section id="contact">
            	<div class="container">
                    <div class="section_header">
                        <h1>Contact</h1>
                    </div>
                    
                    <div class="col-6">	                        
	                        <form action="index.php" method="post" class="validate contact_form">
	                        		<input type="hidden" name="pb" value="pb" />
	                        	<div>
	                        		<label>First Name: <span class="form_required">&nbsp;&nbsp;(required)</span></label>
	                                <input type="text" class="required" id="firstName" name="firstName" title="Please tell me who you are" />
	                            </div>
	                            
	                            <div>
	                        		<label>Email: <span class="form_required">&nbsp;&nbsp;(required)</span></label>
		                            <input type="email" class="required email" id="email" name="email" title="Can I please have your email so I can reply?"/>
	                            </div>
	                            
	                            <div>
	                        		<label>Subject: <span class="form_required">&nbsp;&nbsp;(required)</span></label>
	    	                        <input type="text" class="required" id="subject" name="subject" title="What is the subject of you message?"/>
	                            </div>
	                            
	                            <div>
	                        		<label>Message: <span class="form_required">&nbsp;&nbsp;(required)</span></label>
	            	                <textarea id="mess" class="required" name="mess" title="What is your message about?"></textarea>
	                            </div>
	                	            <input type="submit" class="btn submit_btn" value="Send Email" />
	                        </form>
                    </div>                    
                    
                    <div class="col-5 social_media_col">
                    	<p class="contact_copy">Feel free to contact me with any job opportunites.</p>
                    	
                    	<ul class="contact_social_media">
                    		<li>
                    			<a href="http://www.linkedin.com/pub/jason-frade/31/a2b/b96" target="_blank">
                    				<i class="fa fa-linkedin-square"></i>
	                            </a>
	                        </li>
	                            
	                        <li>
		                        <a href="https://twitter.com/JasonFrade" target="_blank">
		                        	<i class="fa fa-twitter"></i>
		                        </a>
	                        </li>
	                            
	                        <li>
		                        <a href="http://dribbble.com/jafrade" target="_blank">
		                        	<i class="fa fa-dribbble"></i>
		                        </a>
	                        </li>
	                   </ul>                    
                    </div>
                    
                </div>
            </section>
            
            <footer>
            	<div class="container">
                    <div id="copywrite">
                    	<div id="copy">©2014 Designed and Developed by: Jason Frade </div>
                        <div id="miniLogo"><img src="img/icon/miniLogo.png" alt="logo" /></div>
                    </div>
				</div>
            </footer>


        <!-- Google Analytics: change UA-XXXXX-X to be your site's ID. -->
        <script type="text/javascript">

 			 var _gaq = _gaq || [];
 			 _gaq.push(['_setAccount', 'UA-36772957-1']);
 			 _gaq.push(['_trackPageview']);
 			 (function() {
 			 	var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
 			 	ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
 			 	var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  				})
  			();

		</script>

    </body>
</html>