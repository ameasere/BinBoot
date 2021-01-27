<?php
$checksum = $_POST['Hash'];
$date = new DateTime();
$date = $date->format("y:m:d h:i:s");
$ipaddr = $_POST['IP'];
if (strlen($ipaddr) < 7) {
    echo "Parameters wrong. Try again.";
}
$hostname = $_POST['Hostname'];
$entireline = "---------------------\nHost:$hostname\nIP:$ipaddr\nTime:$date\n---------------------\n";
/*
$myfile = fopen("checksum.txt", "w");
fwrite($myfile, $checksum);
fclose($myfile);
*/
$thisfile = fopen("logs.txt", "a+");
fwrite($thisfile, $entireline);
fclose($thisfile);
if ($checksum == "30d90ebb7d9df7d101a35f0ebf06ce1b" || $checksum === "1774a45c7dfc590b6b5e8e4ead70e053") {
    /*
If checksums from Client did not match these, you would get "Authentication failed" in the Client. If they matched, you would be allowed entry.
Two checksums were needed: Left one for Linux users, right one needed for Windows users. Versions checksums never matched once PyArmor was used.
PyArmor saves the file structure of it's own files in the /dist/ directory. Moving them to a Windows machine meant that PyArmor could no longer
find it's files as the directory structure looked like C:\Users\<my name>\Desktop\BinBoot\dist instead of /home/<my name>/Desktop/BinBoot/Desktop.
This means that they files would have to be PyArmor'd on separate OS' and therefore new checksums generated.

Checksums worked like this:

-Client reads entire .py script and hashed them with a SHA algorithm (SHA-256 I think it was)
-Client sends this to server (solitairesec.000webhostapp.com/solitaireSec/binbootReg.php)
-If hash did not match the ones above, "responseC0degp44a" is not sent and therefore the client sees an empty response code and refuses access

PyArmor stopped the user directly interfering with the script, hence why this all worked. Wireshark was the only way to see what was happening - 
and you cannot manually intercept connections to the server and then send your own response code.
    */
    echo "responseC0degp44a"; 
} else { 
    echo "";
}
?>
