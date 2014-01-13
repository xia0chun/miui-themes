<?php header('Content-Type:text/html;charset=utf-8'); ?>
<?php
include('simple_html_dom.php');
// Create DOM from URL or file
$html = file_get_html('http://zhuti.xiaomi.com/compound?page=1&sort=New');

//匹配开始
foreach($html->find('div.thumb a') as $a)
	echo $a->href . ' ' . $a->title . '<br>';
	
foreach($html->find('div.thumb img') as $img)
	echo $img->{'data-src'} . '<br>'
?>
