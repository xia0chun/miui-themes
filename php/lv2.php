<?php header('Content-Type:text/html;charset=utf-8'); ?>
<?php
include('simple_html_dom.php');
// Create DOM from URL or file
$html = file_get_html('http://zhuti.xiaomi.com/detail/e65047e0-203a-41ce-8b7a-a6eb5e5e8107');

//匹配开始
foreach($html->find('div[class=mod userinfos]') as $userinfos)
	foreach($userinfos->find('div[class=bd]') as $bd)
		echo $bd . ' ' . '<br>';
foreach($html->find('div[class=mod detail-infos]') as $detailinfo)
	foreach($detailinfo->find('div[class=bd]') as $bd)
		echo $bd . ' ' . '<br>';

	
?>
