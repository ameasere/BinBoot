<?php
$date = new DateTime();
$date = $date->format("y:m:d h:i:s");
$username = $_POST['Username'];
if (empty($username)) {
    echo "Invalid Parameters.";
    exit();
} else {
    echo "<body>";
}
$entireline = "---------------------\nUsername:$username\nLogged in:$date\n---------------------\n";
$thisfile = fopen("loginLogs.txt", "a+");
fwrite($thisfile, $entireline);
fclose($thisfile);
?>
