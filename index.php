﻿<!DOCTYPE html>
<!--TheFreeElectron 2015, http://www.instructables.com/member/TheFreeElectron/ -->

<html>
    <head>
        <meta charset="utf-8" />
        <title>Thermostat</title>
    </head>
    <body>
    <!-- On/Off button's picture -->
    <!-- display current temp
                 scheduled temp and option to set new temp -->
        <?php
	//$command = escapeshellcmd('python -c'from thermostatFunctions import getTemp; temp=getTemp(); print(temp)'2>&1');
	$command = "sudo python -c'from thermostatFunctions import getTemp; temp=getTemp(); print(temp)' 2>&1";
	
	//echo "$command";
	//echo "<br>";
	$temp = shell_exec($command)*9/5+32;
	echo "The current temp is $temp deg";
	echo "<br>";
	$command = "sudo python -c'from thermostatFunctions import getState; temp=getState(); print(temp)' 2>&1";
	$state = shell_exec($command);
	if($state == 1){
		echo "thermostat is currently on";
	} else {
		echo "thermostat is currently off";
	}
	?>
      <form action="" method="post">
        set temp to: <input type="number" name="newTemp" min="50" max="100" step="5"><br>
        <input type="submit">
      </form>
      <?php
	//$command = "sudo python -c'from thermostatFunctions import *; setTemp($_POST["newTemp"])' 2>&1";
        //echo $command;
	if(isset($_POST["newTemp"])) {
        	echo "setting temp to $_POST[newTemp]";
	 	echo "<br>";
		//$command="sudo python -c'from thermostatFunctions import *; setTemp($_POST[newTemp])' 2>&1";
		$celsius=($_POST[newTemp]-32)*5/9;
		$command = "sudo ./setTemp.sh $celsius";
		//echo $command;
		//echo "<br>";
	 //$command = "sudo python -c'from thermostatFunctions import *; setTemp($_POST["newTemp"])' 2>&1";
	 //echo $command
	 	$output=shell_exec($command);
	 	echo "$output";
		$_POST[newTemp]=array();
	}
	?>
    </body>
</html>
