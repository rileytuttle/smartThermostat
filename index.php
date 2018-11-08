<!DOCTYPE html>
<!--TheFreeElectron 2015, http://www.instructables.com/member/TheFreeElectron/ -->

<html>
    <head>
        <meta charset="utf-8" />
        <title>Raspberry Pi Gpio</title>
    </head>
    <body>
    <!-- On/Off button's picture -->
    <!-- display current temp
                 scheduled temp and option to set new temp -->
        <!-- $temp = shell_exec("python -c 'from thermostatfunctions import getTemp; getTemp()'") -->
    	<?php echo "<p>current temp is </p>"; ?>
      <form action="" method="post">
        set temp to: <input type="number" name="newTemp" min="50" max="100" step="5"><br>
        <input type="submit">
      </form>
      <?php
        if(isset($_POST["newTemp"])) {
         echo $_POST["newTemp"]; 
	 // shell_exec("python -c'import thermostatFunctions as thermostat; thermostat.setTemp($_POST["newTemp"])'"
	 $_POST=array();
	}
	?>
    </body>
</html>
