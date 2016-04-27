<?php
$firstName = $_POST["firstName"];
$subject = $_POST["subject"];
$email = $_POST["email"];
$mess = $_POST["mess"];


$to ='jason@jasonfrade.com';
$message = "This message is from ". $firstName . ".". " Their email is " .  $email .".". " Their Message is: " . $mess . ".";
$headers = "From:" . $email;

mail($to,$subject,$message,$headers);

header("Location: http://jasonfrade.com/portfolio/index.php");
/* Make sure that code below does not get executed when we redirect. */
exit;
?>


