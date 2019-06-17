<?php
if(isset($_POST['submit1']))
{
	$dir = 'C:\xampp\htdocs\Terminal\DAILY REPORT LIST\daily/';
	$dh = opendir($dir);
	while($file = readdir($dh))
	{
	if(!is_dir($file))
	{
	@unlink($dir.$file);
	}
	}
	closedir($dh);
	$move = 'C:\xampp\htdocs\Terminal\DAILY REPORT LIST\daily';
	$str = $_FILES['rma']['tmp_name'];
	$dir = 'C:\xampp\htdocs\Terminal\DAILY REPORT LIST\daily';
	$q = (count(glob("$dir/*.zip")) === 0) ? 'Empty' : 'Not empty';
	
	$Filenames = $_FILES['rma']['name'];
	if ($q=="Empty")
		if (strpos($Filenames, 'drar') !== False)
			{
				if ( move_uploaded_file( $_FILES['rma']['tmp_name'], $move.'/'.$_FILES['rma']['name']))
					{
						shell_exec("python C:\Users\RD1\PycharmProjects\PYTHONMAY2019\TermianlDailyOne.py");
?>
<div class="alert alert-success" role="alert">
	<center><h5>EXPORT : <?php echo($_FILES['rma']['name']) ?> SUCCESS</h5></center>
</div>
<?php
}
}
else
{
?>
<div class="FILEERROR alert alert-danger" role="alert">
	<center><h5>INVALID FILE ERROR</h5></center>
</div>
<?php
}
else
{
echo "FOLDER IS NOT EMPTY";
}
}
if(isset($_POST['submit1_1']))
{
$file = basename($_GET['file']);
$file = 'C:\xampp\htdocs\Terminal\DAILY REPORT LIST\export/Master_DTAR_data.xlsx'.$file;
if(!file_exists($file))
{
?>
<div class="FILEERROR alert alert-danger" role="alert">
	<center><h5>FILE NOT FOUND</h5></center>
</div>
<?php
}
else
{
header('Content-Description: File Transfer');
header('Content-Type: application/octet-stream');
header('Content-Disposition: attachment; filename="'.basename($file).'"');
header('Expires: 0');
header('Cache-Control: must-revalidate');
header('Pragma: public');
header('Content-Length: ' . filesize($file));
flush(); // Flush system output buffer
readfile($file);
exit;
}
}
if(isset($_POST['submit2']))
{
$dir = 'C:\xampp\htdocs\Terminal\DAILY REPORT LIST WITH FOLDERS\daily/';
$dh = opendir($dir);
while($file = readdir($dh))
{
if(!is_dir($file))
{
@unlink($dir.$file);
}
}
closedir($dh);
$move = 'C:\xampp\htdocs\Terminal\DAILY REPORT LIST WITH FOLDERS\daily';
$str = $_FILES['PR']['tmp_name'];
$dir = 'C:\xampp\htdocs\Terminal\DAILY REPORT LIST WITH FOLDERS\daily';
$q = (count(glob("$dir/*.zip")) === 0) ? 'Empty' : 'Not empty';
$Filenames = $_FILES['PR']['name'];
if ($q=="Empty")
	if (strpos($Filenames, 'drar') !== False)
		{
			if ( move_uploaded_file( $_FILES['PR']['tmp_name'], $move.'/'.$_FILES['PR']['name']))
				{
					// echo 'EXPORT : ';
					// echo($_FILES['PR']['name']);
					// shell_exec("python C:\Users\RD1\PycharmProjects\PYTHONMAY2019\PRAutomation.py");
					// echo" : SUCESSS";
					shell_exec("python C:\Users\RD1\PycharmProjects\PYTHONMAY2019\TerminalDailyTwo.py");
?>
<div class="alert alert-success" role="alert">
	<center><h5>EXPORT : <?php echo($_FILES['PR']['name']) ?> SUCCESS</h5></center>
</div>
<?php
}
}
else
{
?>
<!-- <div class="FILEERROR alert alert-danger fixed-bottom" role="alert"> -->
<div class="FILEERROR alert alert-danger" role="alert">
	<center><h5>INVALID FILE ERROR</h5></center>
</div>
<?php
}
else
{
echo "FOLDER IS NOT EMPTY";
}
}
if(isset($_POST['submit2_2']))
{
$file = basename($_GET['file']);
$file = 'C:\xampp\htdocs\Terminal\DAILY REPORT LIST WITH FOLDERS\export/Master_DRL_data.xlsx'.$file;
if(!file_exists($file))
{
?>
<div class="FILEERROR alert alert-danger" role="alert">
	<center><h5>FILE NOT FOUND</h5></center>
</div>
<?php
}
else
{
header('Content-Description: File Transfer');
header('Content-Type: application/octet-stream');
header('Content-Disposition: attachment; filename="'.basename($file).'"');
header('Expires: 0');
header('Cache-Control: must-revalidate');
header('Pragma: public');
header('Content-Length: ' . filesize($file));
flush(); // Flush system output buffer
readfile($file);
exit;
}
}
if(isset($_POST['empty_2']))
{
$file2 = basename($_GET['file']);
$file2 = 'C:\xampp\htdocs\Terminal\DAILY REPORT LIST WITH FOLDERS\empty/DRL_Invalid_List.xlsx'.$file2;
if(!file_exists($file2))
{
?>
<div class="FILEERROR alert alert-danger" role="alert">
	<center><h5>FILE NOT FOUND</h5></center>
</div>
<?php
}
else
{
header('Content-Description: File Transfer');
header('Content-Type: application/octet-stream');
header('Content-Disposition: attachment; filename="'.basename($file2).'"');
header('Expires: 0');
header('Cache-Control: must-revalidate');
header('Pragma: public');
header('Content-Length: ' . filesize($file2));
flush(); // Flush system output buffer
readfile($file2);
exit;
}
}









if(isset($_POST['empty']))
{
$file2 = basename($_GET['file']);
$file2 = 'C:\xampp\htdocs\Terminal\DAILY REPORT LIST\empty/DTAR_Invalid_List.xlsx'.$file2;
if(!file_exists($file2))
{
?>
<div class="FILEERROR alert alert-danger" role="alert">
	<center><h5>FILE NOT FOUND</h5></center>
</div>
<?php
}
else
{
header('Content-Description: File Transfer');
header('Content-Type: application/octet-stream');
header('Content-Disposition: attachment; filename="'.basename($file2).'"');
header('Expires: 0');
header('Cache-Control: must-revalidate');
header('Pragma: public');
header('Content-Length: ' . filesize($file2));
flush(); // Flush system output buffer
readfile($file2);
exit;
}
}


if(isset($_POST['zip']))
{
$file2 = basename($_GET['file']);
$file2 = 'C:\xampp\htdocs\Terminal\DAILY REPORT LIST\invalid/DTAR_Invalid_PDF.zip'.$file2;
if(!file_exists($file2))
{
?>
<div class="FILEERROR alert alert-danger" role="alert">
	<center><h5>FILE NOT FOUND</h5></center>
</div>
<?php
}
else
{
header('Content-Description: File Transfer');
header('Content-Type: application/octet-stream');
header('Content-Disposition: attachment; filename="'.basename($file2).'"');
header('Expires: 0');
header('Cache-Control: must-revalidate');
header('Pragma: public');
header('Content-Length: ' . filesize($file2));
flush(); // Flush system output buffer
readfile($file2);
exit;
}
}







?>


<?php include 'header.php';?>



			<div class="container-fluid">
			<br>
			<br>
			<center><h1>−− EXTRACTING AUTOMATION'S −−</h1></center>
			<br>
			<br>
				<div class="row">
					<div class="col-lg-5">
						<h4>DAILY TRANSACTION AUDIT REPORT - ZIP</h4>
						<form enctype="multipart/form-data" method="POST">
							<div class="input-group mb-3">
							  <input type="file" name="rma" class="form-control cbutton">
								<!-- <div class="custom-file">
									<input type="file" class="custom-file-input" name="rma"  id="exampleInputFilerma">
									<label class="custom-file-label" for="exampleInputFilerma">Choose file</label>
								</div> -->
								<div class="input-group-append">
									<button type="submit" name ='submit1' value="Send" class="btn btn-outline-success">PROCESS</button>
									<button type="submit" name ='submit1_1' value="Send" class="btn btn-outline-primary">DOWNLOAD</button>	
									<button type="submit" name ='stop' value="Send" class="btn btn-outline-danger">STOP</button>
									<button type="submit" name ='empty' value="Send" class="btn btn-outline-warning">INVALID</button>
									<button type="submit" name ='zip' value="Send" class="btn btn-outline-info">ZIP</button>
								</div>
							</div>
						</form>
					</div>
					<div class="col-lg-2">
						<br>
						<br>
					</div>
					<div class="col-lg-5">
						<h4>ALL DAILY REPORT LIST WITH FOLDERS - ZIP</h4>
						<form enctype="multipart/form-data" method="POST">
							<div class="input-group mb-3">
								 <input type="file" name="PR" class="form-control cbutton">
								<!-- <div class="custom-file">
									<input type="file" class="custom-file-input" name="PR"  id="exampleInputFilePR">
									<label class="custom-file-label" for="inputGroupFile03">Choose file</label>
								</div> -->
								<div class="input-group-append">
									<button type="submit" name ='submit2' value="Send" class="btn btn-outline-success">PROCESS</button>
									<button type="submit" name ='submit2_2' value="Send" class="btn btn-outline-primary">DOWNLOAD</button>
									<button type="submit" name ='stop_2' value="Send" class="btn btn-outline-danger">STOP</button>
									<button type="submit" name ='empty_2' value="Send" class="btn btn-outline-warning">INVALID</button>
								</div>
							</div>
						</form>
					</div>
				</div>
				<br>
				<br>
				<br>
				<div class="row">
					<div class="col-sm-5">
						<h4>FILE 3</h4>
						<form enctype="multipart/form-data" method="POST">
							<div class="input-group mb-3">
								<div class="custom-file">
									<input type="file" name="PR3" class="form-control cbutton">
									<!-- <input type="file" class="custom-file-input" name="rma"  id="exampleInputFilerma">
									<label class="custom-file-label" for="inputGroupFile02">Choose file</label> -->
								</div>
								<div class="input-group-append">
									<button type="submit" name ='submit3' value="Send" class="btn btn-outline-success">PROCESS</button>
									<button type="submit" name ='submit3_3' value="Send" class="btn btn-outline-primary">DOWNLOAD</button>
									<button type="submit" name ='stop' value="Send" class="btn btn-outline-danger">STOP</button>
									<button type="submit" name ='empty' value="Send" class="btn btn-outline-warning">INVALID</button>
								</div>
							</div>
						</form>
					</div>
					<div class="col-sm-2">
						<br>
						<br>
					</div>
					<div class="col-sm-5">
						<h4>FILE 4</h4>
						<form enctype="multipart/form-data" method="POST">
							<div class="input-group mb-3">
								<div class="custom-file">
									<input type="file" name="PR4" class="form-control cbutton">
									<!-- <input type="file" class="custom-file-input" name="rma"  id="exampleInputFilerma">
									<label class="custom-file-label" for="inputGroupFile02">Choose file</label> -->
								</div>
								<div class="input-group-append">
									<button type="submit" name ='submit4' value="Send" class="btn btn-outline-success">PROCESS</button>
									<button type="submit" name ='submit4_4' value="Send" class="btn btn-outline-primary">DOWNLOAD</button>
									<button type="submit" name ='stop' value="Send" class="btn btn-outline-danger">STOP</button>
									<button type="submit" name ='empty' value="Send" class="btn btn-outline-warning">INVALID</button>
								</div>
							</div>
						</form>
					</div>
				</div>
				<br>
				<br>
				<br>
				<div class="row">
					<div class="col-sm-5">
						<h4>FILE 5</h4>
						<form enctype="multipart/form-data" method="POST">
							<div class="input-group mb-3">
								<div class="custom-file">
									<input type="file" name="PR5" class="form-control cbutton">
									<!-- <input type="file" class="custom-file-input" name="rma"  id="exampleInputFilerma">
									<label class="custom-file-label" for="inputGroupFile02">Choose file</label> -->
								</div>
								<div class="input-group-append">
									<button type="submit" name ='submit5' value="Send" class="btn btn-outline-success">PROCESS</button>
									<button type="submit" name ='submit5_5' value="Send" class="btn btn-outline-primary">DOWNLOAD</button>
									<button type="submit" name ='stop' value="Send" class="btn btn-outline-danger">STOP</button>
									<button type="submit" name ='empty' value="Send" class="btn btn-outline-warning">INVALID</button>
								</div>
							</div>
						</form>
					</div>
					<div class="col-sm-2">
						<br>
						<br>
					</div>
					<div class="col-sm-5">
						<h4>FILE 6</h4>
						<form enctype="multipart/form-data" method="POST">
							<div class="input-group mb-3">
								<div class="custom-file">
									<input type="file" name="PR6" class="form-control cbutton">
									<!-- <input type="file" class="custom-file-input" name="rma"  id="exampleInputFilerma">
									<label class="custom-file-label" for="inputGroupFile02">Choose file</label> -->
								</div>
								<div class="input-group-append">
									<button type="submit" name ='submit6' value="Send" class="btn btn-outline-success">PROCESS</button>
									<button type="submit" name ='submit6_6' value="Send" class="btn btn-outline-primary">DOWNLOAD</button>
									<button type="submit" name ='stop' value="Send" class="btn btn-outline-danger">STOP</button>
									<button type="submit" name ='empty' value="Send" class="btn btn-outline-warning">INVALID</button>
								</div>
							</div>
						</form>
					</div>
				</div>
			</div>
				</body>
			</html>



