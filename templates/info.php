<?php 
$conn = mysqli_connect(
	'18.212.183.253',
	'jjoong',
	'1234',
	'pi',
	'3306');
if (mysqli_connect_errno()) 
{ 
	echo "Failed to connect to MySQL: " . mysqli_connect_error(); 
} 
$unique_num = $_GET["unique_num"];
$url = $_GET["url"];

$sql = "insert into cctv(unique_num,url) values('$unique_num','$url')"; 
$result = mysqli_query($conn, $sql); 
$row = mysqli_fetch_array($result);

// $sql1 = "select * from cctv";
// $re = mysqli_query($conn,$sql1);

// $cnt=1;
// while($result = mysqli_fetch_array($re))
// {
// 	print $cnt;
// 	$cnt++;
// 	for($i=0; $i<5; $i++)
// 	{
// 		print $result[$i];
// 		print "<br>";
// 	}
// }
mysqli_close($conn);
?>
