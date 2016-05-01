<!DOCTYPE html>
<html>

<head>
    <title></title>

    <link rel="stylesheet" type="text/css" href="css/styles.css" />
    <link rel="stylesheet" type="text/css" href="less/styles.less" />
    <link rel="stylesheet" type="text/css" href="css/jquery.maximage.css" />
    
    <style>
/*
        .main-site {
            background-image: url(img/_assets/linen.png);
            background-repeat: repeat;
        }
*/
    </style>
</head>

<body>
    <header class="site-header">
        <nav class="main-nav">
            <p class="main-nav-logo">
                <a href="index.html">
                    <span>diana dolishny</span>
                </a>
            </p>

            <div class="main-nav-right">
                <ul>
                    <li><a href="index.html">Home</a>
                    </li>
                    <li><a href="work.html">Projects</a>
                    </li>
                    <li><a href="about.html">About</a>
                    </li>
                    <li><a href="contact.php"  class="nav_current">Contact</a>
                    </li>
                </ul>
            </div>
        </nav>
    </header>

    <div class="main-site">


        <div class="content_wrapper">
            <div class="row row_space_6 row_space_top_6 center">
                <h1>Contact</h1>
                <p>I'm available for hire!</p>
            </div>

            <div class="row row_space_6 about_content">
                <fieldset id="contact_form">
                    <div id="result"></div>
                    <label for="name"><span>Name</span>
                        <input type="text" name="name" id="name" autofocus />
                    </label>

                    <label for="email"><span>Email Address</span>
                        <input type="email" name="email" id="email"  />
                    </label>

                    <label for="subject"><span>Subject</span>
                        <input type="text" name="subject" id="subject"  />
                    </label>

                    <label for="message"><span>Message</span>
                        <textarea name="message" id="message" ></textarea>
                    </label>

                    <label><span>&nbsp;</span>
                        <button class="submit_btn" id="submit_btn">Send</button>
                    </label>
                </fieldset>
            </div>

        </div>
    </div>

     <footer class="site-footer">

            <div class="col-4 legal">
                <p>
                    <i class="fa fa-copyright"></i>2014 Designed and developed by <a href="jasonfrade.com">Jason Frade</a>.
                </p>
            </div>
            
            <div class="col-4 logo">
                <a href="index.html">diana dolishny</a>
            </div>

            <div class="col-4 footer_nav">
                <ul>
                    <li><a href="index.html">Home</a>
                    </li>
                    <li><a href="work.html" class="nav_current">Projects</a>
                    </li>
                    <li><a href="about.html">About</a>
                    </li>
                    <li><a href="contact.php">Contact</a>
                    </li>
                </ul>
            </div>       
    </footer>

    <script src='http://ajax.googleapis.com/ajax/libs/jquery/2.0.0/jquery.js'></script>
    <script src="js/jquery.cycle.all.js" type="text/javascript" charset="utf-8"></script>
    <script src="js/jquery.maximage.js" type="text/javascript" charset="utf-8"></script>
    <script type="text/javascript" src="js/jquery.easing.min.js"></script>
    <script type="text/javascript">
    $(document).ready(function() {
        $("#submit_btn").click(function() { 
            //get input field values
            var user_name       = $('input[name=name]').val(); 
            var user_email      = $('input[name=email]').val();
            var user_subject      = $('input[name=subject]').val();
            var user_message    = $('textarea[name=message]').val();

            //simple validation at client's end
            //we simply change border color to red if empty field using .css()
            var proceed = true;
            if(user_name==""){ 
                $('input[name=name]').css('border-color','red'); 
                proceed = false;
            }
            if(user_email==""){ 
                $('input[name=email]').css('border-color','red'); 
                proceed = false;
            }
            if(user_subject=="") {    
                $('input[name=subject]').css('border-color','red'); 
                proceed = false;
            }
            if(user_message=="") {  
                $('textarea[name=message]').css('border-color','red'); 
                proceed = false;
            }

            //everything looks good! proceed...
            if(proceed) 
            {
                //data to be sent to server
                post_data = {'userName':user_name, 'userEmail':user_email, 'userSubject':user_subject, 'userMessage':user_message};

                //Ajax post data to server
                $.post('contact_submit.php', post_data, function(response){  

                    //load json data from server and output message     
                    if(response.type == 'error')
                    {
                        output = '<div class="error">'+response.text+'</div>';
                    }else{
                        output = '<div class="success">'+response.text+'</div>';

                        //reset values in all input fields
                        $('#contact_form input').val(''); 
                        $('#contact_form textarea').val(''); 
                    }

                    $("#result").hide().html(output).slideDown();
                }, 'json');

            }
        });

        //reset previously set border colors and hide all message on .keyup()
        $("#contact_form input, #contact_form textarea").keyup(function() { 
            $("#contact_form input, #contact_form textarea").css('border-color',''); 
            $("#result").slideUp();
        });

    });
    </script>

</body>

</html>


