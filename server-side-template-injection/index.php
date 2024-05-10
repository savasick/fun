<html>
<head>
<title>Lib</title>
</head>
<body>
<div align='center'>
<h1>PHP SSTI</h1>
<?php
if (isset($_GET['book'])) {
	$book = $_GET['book'];
	include 'vendor/twig/twig/lib/Twig/Autoloader.php';
	Twig_Autoloader::register();
	$loader = new Twig_Loader_String();
	$twig = new Twig_Environment($loader);
	$result = $twig->render($book);
	if ($result == "doriangray") {
		echo "The Picture of Dorian Gray is a novel and one of the most famous works of English writer Oscar Wilde. The novel was published in 1890.<br><br><button><a href='http://localhost/'>Back</a></button>";
	} elseif ($result == "warandpeace") {
		echo "War and Peace is a famous novel written by Leo Tolstoy. It was published in 1869 and is considered one of the greatest works of world literature.<br><br><button><a href='http://localhost/'>Back</a></button>";
	} elseif ($result == "1984") {
		echo "1984 is a novel written by George Orwell and published in 1949. The book describes a futuristic society known as Oceania, which is controlled by the totalitarian regime of the Party and its leader Big Brother.<br><br><button><a href='http://localhost/'>Back</a></button>";
	} else {
		echo "On this site you can familiarize yourself with his author's favorite books:<br>
		<a href='?book=doriangray'>1. The Picture of Dorian Grey</a><br>
		<a href='?book=warandpeace'>2. War and Peace</a><br>
		<a href='?book=1984'>3. 1984</a><br><br>";
		echo "Unfortunately, the descriptions for the book " . $result . " we don't have it on our website :(";
	}

} else {
	echo "On this site you can familiarize yourself with his author's favorite books:<br>
	<a href='?book=doriangray'>1. The Picture of Dorian Grey</a><br>
	<a href='?book=warandpeace'>2. War and Peace</a><br>
	<a href='?book=1984'>3. 1984</a><br>";
}

?>

</div>
</body>
</html>
