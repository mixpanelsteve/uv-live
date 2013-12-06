<?php

$fp = fopen('/var/www/webhooks/echo2.txt', 'a');
fwrite($fp, "\n-----\n" . date('Y-m-d , g:i-s-u a') . "\n-----\n");

foreach($_REQUEST as $param=>$value){
	fwrite($fp,"$param : $value \n");
}



$command = 'python /home/steve/uservoice/handler.py ' . escapeshellarg(json_encode($_REQUEST));
$temp = shell_exec($command);
fwrite($fp, json_decode($temp));
fclose($fp);

?>
