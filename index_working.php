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
        <link rel="stylesheet" href="css/style-working.css">
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
		                    	<img src="img/icon/miniLogo.png" height="47" width="47">
		                    	<span>Jason Frade</span>
		                    </a>
	                    </div>
	                    
	                    <div class="col-6 last">
	                        <ul>
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
	            	<div class="row row_space_top_7 row_space_7 center_text">
		            	<h1>My Work</h1>   
	                </div>

                        <div class="row row_space_top_7 row_space_7">
                            
                                <div class="col-7 screen">
                                    <img src="img/large/freetime/freetime_overview.png" alt="overview_freetime" />
                                </div>
                                
                                <div class="col-5 last">
                                    <h3>FreeTime Time Tracking App</h3>
                                    <p>                         
                                    Working freelance can be cumbersome, finding new projects, and tracking existing projects is a considerable amount of work to be doing, and tracking the project shouldn't be a strenuous process. My vision for this project was to create a simplistic and engaging mobile application. I wanted to make it as easy as possible for someone to open the app and understand in seconds how to create a project, the projects tasks, and start tracking those said tasks, and not have to spend unnecessary time learning how to use the application.
                                    </p>
                                    <a href="work/freetime.html" class="btn">View Project</a>
                                </div>
                            
                        </div>

                    	
                        <div class="row row_space_top_7 row_space_7 row_top_border">
                            
                            
                                <div class="col-7">
                                    <img src="img/large/coca_cola_overview.png" alt="coke overview" />
                                </div>
                                
                                <div class="col-5 last">
                                    <h3>Coca Cola Heauristic & User Analysis</h3>
                                    <p>
                                        The Coca Cola website is a way for the company to communicate recent promotions to their users, as well as creating a gateway to their secondary Coca Cola Company Website. I began this project by administering a heuristic analysis of the website, this was done to form a more solid understanding of where the pain points were in the website and how they could be solved. I continued to test the website with a few users in order to further solidify my findings.
                                    </p>
                                    <a href="work/coke.html" class="btn">View Project</a>
                                </div>
                            
                        </div>


                    <div class="row row_space_top_7 row_space_7 row_top_border">
                        
                        
                            <div class="col-7">
                                <img  src="img/large/open_table_overview.png" alt="open table overview"/>
                            </div>
                            
                            <div class="col-5 last">
                                <h3>Open Table Heuristic & User Analysis</h3>
                                <p>
                                    Open Table is a website that empowers their users to schedule reservations to restaurants at their own leisure, without having to deal with the hassle of calling the restaurant during busy or off hours. I took the challenge to discover where the websites pain points were and what could be done in order to improve them to make the website a more engaging experience for their users. This involved administering a heuristic and user analysis, and envisioning how the website could could be improved to meet the users needs.
                                </p>
                                <a href="work/open_table.html" class="btn">View Project</a>
                            </div>
                        
                    </div>

                    <div class="row row_space_top_7 row_space_7 row_top_border">
                        
                            <div class="col-7">
                                <img src="img/large/prius/prius_overview.png" alt="overview_prius" />
                            </div>
                            
                            <div class="col-5 last">
                                <h3>Toyota Prius Console Design</h3>
                                <p>
                                    The Toyota Prius mileage game is an exclusive game for Prius owners. The goal of the game is to be the person to reach the highest MPG, for the longest duration. Playing the game requires the driver to have the ability to monitor the consumption of gas and electricity.
                                </p>
                                <a href="work/prius.html" class="btn">View Project</a>
                            </div>
                        
                    </div>


                    <div class="row row_space_top_7 row_space_7 row_top_border">
                        
                            <div class="col-7">
                                <img src="img/large/urbanscape.jpg"/>
                            </div>
                            
                            <div class="col-5 last">
                                <h3>Urbanscape Illustration</h3>
                                <p>
                                    The Toyota Prius mileage game is an exclusive game for Prius owners. The goal of the game is to be the person to reach the highest MPG, for the longest duration. Playing the game requires the driver to have the ability to monitor the consumption of gas and electricity.
                                </p>
                                <a href="work/urbanscape.html" class="btn">View Project</a>
                            </div>
                        
                    </div>

                    <div class="row row_space_top_7 row_space_7 row_top_border">
                        
                            <div class="col-7">
                                <img src="img/large/50Poster.jpg" height="600">
                            </div>
                            
                            <div class="col-5 last">
                                <h3>1950's Horror Movie Poster</h3>
                                <p>
                                    The Toyota Prius mileage game is an exclusive game for Prius owners. The goal of the game is to be the person to reach the highest MPG, for the longest duration. Playing the game requires the driver to have the ability to monitor the consumption of gas and electricity.
                                </p>
                                <a href="work/50s_horror_poster.html" class="btn">View Project</a>
                            </div>
                        
                    </div>
                   
            	</div>
            </section>
            
            
            <section id="about">
            	<div id="aboutLand"></div>
            	<div class="container">
                    <div class="row row_space_top_7 row_space_7 center_text">
                        <h1>About Me</h1>
                        <blockquote class="row_space_5">My name is Jason Frade and I am a User Experience Designer.</blockquote>
                    </div> 

                     <div class="col col-3">
                        <div class="about_img">
                            <img src="img/meImg.jpg">
                        </div>
                         <a href="http://jasonfrade.com/documents/Frade_resume.pdf" target="_blank" class="btn btn-large resume_btn">View My Resume</a>
                    </div>     

                    <div class="col col-9 last">
	                    <div class="about_copy">
	                    	
	                    	<p>Being a user experience designer, to me, is the best job in the world. My primary job is to listen and observe people as they use products so that I can better understand what they like and what causes them pain. This allows me to create simple solutions that result in people having more enjoyable experiences. </p>

                            <p>In my process of designing products, talking and listening to the people who use your product is the most important thing you can do to improve your product. However, there are some other principles that I believe are important to designing products:</p>

                            <h4 class="row_space_top_3">Iteration is key</h4>
                            <p>The first solution out of the gate is almost never the best solution, so one must continue to iterate in order to improve upon the design and experience.</p>

                            <h4 class="row_space_top_3">"Simplicity, above all else, will attain the most reactions."</h4>
                            <p>Simplicity in a product is key to removing distraction and focusing the user on what the primary goal is. </p>


	                    	<h3 class="row_space_top_7">A Little More about me</h3>
                            <p class="row_space_top_3">Working as a user experience designer is a huge part of my life. But there are a lot more things that make up who I am. At heart I am truly a nerd. I would be happy spending an entire day have a Star Wars, Harry Potter, or Game of Thrones viewing marathon.</p>

	                    	<p>Aside from being a nerd I am extremely passionate about cooking, tasting new wines, and traveling to new and exciting places.</p>
	                    </div>

                       
                    </div>
                    
                   
                </div>
            </section>
            
            <section id="contact">
            	<div class="container">
                    <div class="row row_space_top_7 row_space_7 center_text">
                        <h1>Contact</h1>
                        <blockquote class="row_space_5">I'm currently available for new opportunities</blockquote>
                    </div>
                    
                    <div class="center_form">	                        
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
	                	            <input type="submit" class="submit_btn" value="Send Email" />
	                        </form>
                    </div>                    
                    
                </div>
            </section>
            
            <footer>
            	<div class="container">
                    <div class="col-6 copywrite">
                            <span class="copy">©2014 Designed and Developed by: Jason Frade </span>
                    </div>

                    <ul class="col-6 last contact_social_media">
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