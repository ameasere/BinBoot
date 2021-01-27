<?php
$username = $_POST['user'];
$ipaddr = $_POST['IP'];
$hostname = $_POST['hostname'];
$banuser = array("misty-dayz", "ChanTilly-Lace","misty-nitez"); //Prevent snitching, the booter would log out or refuse to log in these usernames.
$banip = array(); //Didn't have any IPs to ban yet
$banhost = array(); //Didn't have any hostnames to ban
$date = new DateTime();
$date = $date->format("y:m:d h:i:s");
if (empty($username)) {
    echo "Invalid Parameters.";
    exit();
}
$entireline = "---------------------\nUsername:$username\nPassed through:$date\nIP:$ipaddr\nHost:$hostname\n---------------------\n";
$thisfile = fopen("banlogs.txt", "a+");
fwrite($thisfile, $entireline);
fclose($thisfile);
foreach ($banuser as $user) {
    if ($user === $username) {
        echo "134";
        $entireline = "Banned Username\n";
        $thisfile = fopen("banlogs.txt", "a+");
        fwrite($thisfile, $entireline);
        fclose($thisfile);
    } else {
        foreach ($banip as $user) {
            if ($user === $ipaddr) {
                echo "134";
                $entireline = "Banned IP\n";
                $thisfile = fopen("banlogs.txt", "a+");
                fwrite($thisfile, $entireline);
                fclose($thisfile);
            } else {
                foreach ($banhost as $user) {
                    if ($user === $hostname) {
                        echo "134";
                        $entireline = "Banned Host\n";
                        $thisfile = fopen("banlogs.txt", "a+");
                        fwrite($thisfile, $entireline);
                        fclose($thisfile);
                    } else {
                        echo "555";
                        $entireline = "Allowed\n";
                        $thisfile = fopen("banlogs.txt", "a+");
                        fwrite($thisfile, $entireline);
                        fclose($thisfile);
                    }
                }
            }
        }

    }
}
/*
Response 134 was a signal to the Client that a banned user had tried to log into the booter. 555 was the correct response to log in. If no response was found, it refused entry
no matter what username you tried to enter.
*/
?>