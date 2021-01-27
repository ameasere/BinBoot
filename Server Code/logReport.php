<?php
$date = new DateTime();
$date = $date->format("y:m:d h:i:s");
$username = $_POST['Username'];
$kicked = $_POST['Action'];
$victim = $_POST['Victim'];
$extras = $_POST['Extra'];
if (empty($username)) {
    echo "Invalid Parameters.";
    exit();
} else {
    echo "<body>";
}
$entireline = "---------------------\nUsername:$username\nAction:$kicked\nVictim:$victim\nTime:$date\nExtras:$extras\n\n---------------------\n";
$thisfile = fopen("logReport.txt", "a+");
fwrite($thisfile, $entireline);
fclose($thisfile);
?>