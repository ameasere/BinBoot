<?php
$filepoint = "magazinefile.txt";
if (!unlink($filepoint)) {
} else {
}
$weevil = $_GET['idx'];
$weevil = urlencode($weevil);
$weevil = str_replace("+","%20",$weevil);
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL,"https://lb.binweevils.com/php2/magazines/read/getListForWeevil.php?rndVar=0.4813810419291258");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
    'authority: lb.binweevils.com',
    'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'content-type: application/x-www-form-urlencoded',
    'accept: */*',
    'origin: https://play.binweevils.com',
    'x-requested-with: ShockwaveFlash/32.0.0.433',
    'sec-fetch-site: same-site',
    'sec-fetch-mode: no-cors',
    'sec-fetch-dest: embed',
    'referer: https://play.binweevils.com/',
    'accept-language: en-GB,en-US;q=0.9,en;q=0.8',
    'cookie: __utmz=183252021.1601122808.1.1.utmccn=(direct)|utmcsr=(direct)|utmcmd=(none); __utma=183252021.153974398.1601122808.1601672084.1601764310.21; __utmb=183252021; __utmc=183252021; laravel_session=9e59129610c0672ff85f1809f50847690ae2e0bc; weevil_name=Impeccable; sessionId=8b3173fae9d76b091f16d48bc7f3a49e; mp_679dc552faca5a2a4a5a6290a3250e4f_mixpanel=%7B%22distinct_id%22%3A%20%22174ca5b319c1a7-0de03c099e7c5c-397c095c-1fa400-174ca5b319daf%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fplay.binweevils.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22play.binweevils.com%22%7D; __cfduid=d949d1387b8e79ac3ef7cf3f5bd9c12771601766690; AUTH_BEARER_BW=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE2MDE3NjgxMDksImp0aSI6ImxsXC8zMkVjZ3dtVHRGOG1Tb3ZEcU95WDZWejJSeVBweVluNE0zOVVmTWhvPSIsImlzcyI6Ii5iaW53ZWV2aWxzLmNvbSIsIm5iZiI6MTYwMTc2ODEwOSwiZXhwIjoxNjAxNzcxNzA5LCJkYXRhIjoiYToxNjp7czo5OlwiX3ByZXZpb3VzXCI7YToxOntzOjM6XCJ1cmxcIjtzOjc1OlwiaHR0cDpcL1wvbGIuYmlud2Vldmlscy5jb21cL3dlZXZpbFwvcmVtYWluaW5nLXJldmVudWU_cm5kVmFyPTAuMTg4NzI3MDgzMTUwMjk3NFwiO31zOjU6XCJmbGFzaFwiO2E6Mjp7czozOlwib2xkXCI7YTowOnt9czozOlwibmV3XCI7YTowOnt9fXM6NjpcIl90b2tlblwiO3M6NDA6XCJVOENYbmpkTmVpeU1wV05WMWxRb1ZFcER4Rkd2dzl3VU02WUdabnI4XCI7czoxMDpcImxvZ2luX2tleTFcIjtzOjA6XCJcIjtzOjY6XCJ1c2VySURcIjtzOjEwOlwiSW1wZWNjYWJsZVwiO3M6NzpcInVzZXJJRFhcIjtpOjU2NDM4OTQ7czo2OlwidHljb29uXCI7aTowO3M6MTg6XCJsYXN0U3VibWlzc2lvblRpbWVcIjtpOjA7czo2OlwibmVzdElEXCI7czo3OlwiNDc4NzE0MFwiO3M6NTpcImluYmluXCI7aToxNDY1NDtzOjY6XCJwZXRJRHNcIjtzOjY6XCIyODMwODRcIjtzOjg6XCJ0eWNvb25UVlwiO2k6MDtzOjg6XCJsb2dpbktleVwiO2k6NTY0Mzg5NDtzOjg6XCJhcHBTcGFjZVwiO2E6MTp7czoxODpcImxhc3RTdWJtaXNzaW9uVGltZVwiO2k6MDt9czoxNzpcImxveWFsdHlDYXJkU3RhdHVzXCI7czo2OlwibGFwc2VkXCI7czo5OlwiX3NmMl9tZXRhXCI7YTozOntzOjE6XCJ1XCI7aToxNjAxNzY4MTA4O3M6MTpcImNcIjtpOjE2MDE3NjQzMDg7czoxOlwibFwiO3M6MTpcIjBcIjt9fSJ9.8_uuA9OHzVqT6wvbQK7iV5CtHrjbbuLeSFB6vpafYkFcJA4ca3IXk5bhmyTc1Cyj0VmOYSqgddOytENfIIvXyg',
    ));
curl_setopt($ch, CURLOPT_POSTFIELDS, 'idx=' . $weevil . '&hash=294de5d9c13fb50db696b22ef0b0d352&timer=1437105');
$server_output=curl_exec($ch);
curl_close($ch);
//Formatting start
$response = json_decode($server_output, true);
$responseCode = $response['responseCode'];
$amount = count($response['issues']);
$magarray = $response['issues'][0];
$name = $magarray['userWeevilID'];
$magname = $magarray['issueName'];
$magid = $magarray['newspaperID'];
$idx = "IDX: $weevil <br>";
$weevilname = "Weevil Name: $name <br>";
$rc = "Response Code: $responseCode <br>";
$amountpublished = "Amount published: $amount <br>";
$magazinename = "Magazine Name: $magname <br>";
$magazineid = "Magazine ID: $magid <br>";
$magcount = 0;
$magazinestotal = array();
foreach($response['issues'] as $magazine) {
    $magcount++;
    $id = $magazine['uniqueID'];
    $issue = $magazine['issueNum'];
    $views = $magazine['views'];
    $votes = $magazine['votes'];
    $mark = $magazine['mark'];
    $days = $magazine['daysAgo'];
    $entirerecord = "Unique ID: " . $id . " || Issue Number: " . $issue . " || Views: " . $views . " || Votes: " . $votes . " || Mark: " . $mark . " || Published: " . $days . " days go \n";
    $myfile = fopen("magazinefile.txt", "a+");
    fwrite($myfile, $entirerecord);
    fclose($myfile);
}
//Formatting end
?>
<!-- CSS and HTML formatting -->
<style>
    html {
  height: 100%;
}
body {
  margin:0;
  padding:0;
  font-family: sans-serif;
  font-size: 12px;
  background: linear-gradient(#141e30, #243b55);
}

.login-box {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 400px;
  padding: 40px;
  transform: translate(-50%, -50%);
  background: rgba(0,0,0,.5);
  box-sizing: border-box;
  box-shadow: 0 15px 25px rgba(0,0,0,.6);
  border-radius: 10px;
}

.login-box h2 {
  margin: 0 0 30px;
  padding: 0;
  color: #fff;
  text-align: center;
}

.login-box .user-box {
  position: relative;
}

.login-box .user-box input {
  width: 100%;
  padding: 10px 0;
  font-size: 16px;
  color: #fff;
  margin-bottom: 30px;
  border: none;
  border-bottom: 1px solid #fff;
  outline: none;
  background: transparent;
}
.login-box .user-box label {
  position: absolute;
  top:0;
  left: 0;
  padding: 10px 0;
  font-size: 16px;
  color: #fff;
  pointer-events: none;
  transition: .5s;
}

.login-box form a {
  position: relative;
  display: inline-block;
  padding: 10px 20px;
  color: #03e9f4;
  font-size: 16px;
  text-decoration: none;
  text-transform: uppercase;
  overflow: hidden;
  transition: .5s;
  margin-top: 40px;
  letter-spacing: 4px
}

.login-box a:hover {
  background: #03e9f4;
  color: #fff;
  border-radius: 5px;
  box-shadow: 0 0 5px #03e9f4,
              0 0 25px #03e9f4,
              0 0 50px #03e9f4,
              0 0 100px #03e9f4;
}

.login-box a span {
  position: absolute;
  display: block;
}

.login-box a span:nth-child(1) {
  top: 0;
  left: -100%;
  width: 100%;
  height: 2px;
  background: linear-gradient(90deg, transparent, #03e9f4);
  animation: btn-anim1 1s linear infinite;
}

@keyframes btn-anim1 {
  0% {
    left: -100%;
  }
  50%,100% {
    left: 100%;
  }
}

.login-box a span:nth-child(2) {
  top: -100%;
  right: 0;
  width: 2px;
  height: 100%;
  background: linear-gradient(180deg, transparent, #03e9f4);
  animation: btn-anim2 1s linear infinite;
  animation-delay: .25s
}

@keyframes btn-anim2 {
  0% {
    top: -100%;
  }
  50%,100% {
    top: 100%;
  }
}

.login-box a span:nth-child(3) {
  bottom: 0;
  right: -100%;
  width: 100%;
  height: 2px;
  background: linear-gradient(270deg, transparent, #03e9f4);
  animation: btn-anim3 1s linear infinite;
  animation-delay: .5s
}

@keyframes btn-anim3 {
  0% {
    right: -100%;
  }
  50%,100% {
    right: 100%;
  }
}

.login-box a span:nth-child(4) {
  bottom: -100%;
  left: 0;
  width: 2px;
  height: 100%;
  background: linear-gradient(360deg, transparent, #03e9f4);
  animation: btn-anim4 1s linear infinite;
  animation-delay: .75s
}

@keyframes btn-anim4 {
  0% {
    bottom: -100%;
  }
  50%,100% {
    bottom: 100%;
  }
}

</style>
<html lang="en">
  <body>
      <div class="login-box">
      <h2><?php echo $idx ?></h2>
      <h2><?php echo $weevilname ?></h2>
      <h2><?php echo $rc ?></h2>
      <h2><?php echo $smountpublished ?></h2>
      <h2><?php echo $magazinename ?></h2>
      <h2><?php echo $magazineid ?></h2>
      <form id="search" action="" method="post">
      <a href="magazinefile.txt">
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      Download magazine data<br><br>
      </a>
    <a href="weevilSearch.html">
    <span></span>
      <span></span>
      <span></span>
      <span></span>
      Return
    </a>
      </form>
      </div>
  </body>
</html>