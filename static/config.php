<?php 
define('DBSERVER', 'localhost');
define('DBUSERNAME', '');
define('DBPASSWORD', '');
define('DBNAME','database');

$db = mysqli_connect(DBSERVER, DBUSERNAME, DBPASSWORD, DBNAME);

if ($db === false){
    die("Error: connection error." . mysqli_connect_error());
}
?>