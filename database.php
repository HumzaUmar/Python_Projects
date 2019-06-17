<?php
if(isset($_POST['accessory_submit']))
{
	$dir = 'C:\xampp\htdocs\Terminal\Daily Accessory\daily/';
	$dh = opendir($dir);
	while($file = readdir($dh))
	{
	if(!is_dir($file))
	{
	@unlink($dir.$file);
	}
	}
	closedir($dh);
	$move = 'C:\xampp\htdocs\Terminal\Daily Accessory\daily';
	$str = $_FILES['accessory']['tmp_name'];
	$dir = 'C:\xampp\htdocs\Terminal\Daily Accessory\daily';
	$q = (count(glob("$dir/*.zip")) === 0) ? 'Empty' : 'Not empty';
	
	$Filenames = $_FILES['accessory']['name'];
	if ($q=="Empty")
		if (strpos($Filenames, 'accessory') !== False)
			{
				if ( move_uploaded_file( $_FILES['accessory']['tmp_name'], $move.'/'.$_FILES['accessory']['name']))
					{
						shell_exec("python C:\Users\RD1\PycharmProjects\PYTHONMAY2019\DailyFiles2ACCESSORY.py");
					
?>
<div class="alert alert-success" role="alert">
	<center><h5>EXPORT : <?php echo($_FILES['accessory']['name']) ?> SUCCESS</h5></center>
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



if(isset($_POST['handset_submit']))
{
	$dir = 'C:\xampp\htdocs\Terminal\Daily Handset\daily/';
	$dh = opendir($dir);
	while($file = readdir($dh))
	{
	if(!is_dir($file))
	{
	@unlink($dir.$file);
	}
	}
	closedir($dh);
	$move = 'C:\xampp\htdocs\Terminal\Daily Handset\daily';
	$str = $_FILES['handset']['tmp_name'];
	$dir = 'C:\xampp\htdocs\Terminal\Daily Handset\daily';
	$q = (count(glob("$dir/*.zip")) === 0) ? 'Empty' : 'Not empty';
	
	$Filenames = $_FILES['handset']['name'];
	if ($q=="Empty")
		if (strpos($Filenames, 'handset') !== False)
			{
				if ( move_uploaded_file( $_FILES['handset']['tmp_name'], $move.'/'.$_FILES['handset']['name']))
					{
						shell_exec("python C:\Users\RD1\PycharmProjects\PYTHONMAY2019\DaileyFiles3HANDEST.py");
					
?>
<div class="alert alert-success" role="alert">
	<center><h5>EXPORT : <?php echo($_FILES['handset']['name']) ?> SUCCESS</h5></center>
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



if(isset($_POST['lumsum_submit']))
{
	$dir = 'C:\xampp\htdocs\Terminal\Daily LumSum\daily/';
	$dh = opendir($dir);
	while($file = readdir($dh))
	{
	if(!is_dir($file))
	{
	@unlink($dir.$file);
	}
	}
	closedir($dh);
	$move = 'C:\xampp\htdocs\Terminal\Daily LumSum\daily';
	$str = $_FILES['lumsum']['tmp_name'];
	$dir = 'C:\xampp\htdocs\Terminal\Daily LumSum\daily';
	$q = (count(glob("$dir/*.zip")) === 0) ? 'Empty' : 'Not empty';
	
	$Filenames = $_FILES['lumsum']['name'];
	if ($q=="Empty")
		if (strpos($Filenames, 'lumpsum') !== False)
			{
				if ( move_uploaded_file( $_FILES['lumsum']['tmp_name'], $move.'/'.$_FILES['lumsum']['name']))
					{
						shell_exec("python C:\Users\RD1\PycharmProjects\PYTHONMAY2019\DailyFiles8LUMSUM.py");
					
?>
<div class="alert alert-success" role="alert">
	<center><h5>EXPORT : <?php echo($_FILES['lumsum']['name']) ?> SUCCESS</h5></center>
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




if(isset($_POST['pb_submit']))
{
	$dir = 'C:\xampp\htdocs\Terminal\Daily PB/daily/';
	$dh = opendir($dir);
	while($file = readdir($dh))
	{
	if(!is_dir($file))
	{
	@unlink($dir.$file);
	}
	}
	closedir($dh);
	$move = 'C:\xampp\htdocs\Terminal\Daily PB/daily';
	$str = $_FILES['pb']['tmp_name'];
	$dir = 'C:\xampp\htdocs\Terminal\Daily PB/daily';
	$q = (count(glob("$dir/*.zip")) === 0) ? 'Empty' : 'Not empty';
	
	$Filenames = $_FILES['pb']['name'];
	if ($q=="Empty")
		if (strpos($Filenames, 'pb') !== False)
			{
				if ( move_uploaded_file( $_FILES['pb']['tmp_name'], $move.'/'.$_FILES['pb']['name']))
					{
						shell_exec("python C:\Users\RD1\PycharmProjects\PYTHONMAY2019\DailyFiles1PB.py");
					
?>
<div class="alert alert-success" role="alert">
	<center><h5>EXPORT : <?php echo($_FILES['pb']['name']) ?> SUCCESS</h5></center>
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




if(isset($_POST['accessory_submit']))
{
	$dir = 'C:\xampp\htdocs\Terminal\Daily Accessory\daily/';
	$dh = opendir($dir);
	while($file = readdir($dh))
	{
	if(!is_dir($file))
	{
	@unlink($dir.$file);
	}
	}
	closedir($dh);
	$move = 'C:\xampp\htdocs\Terminal\Daily Accessory\daily';
	$str = $_FILES['accessory']['tmp_name'];
	$dir = 'C:\xampp\htdocs\Terminal\Daily Accessory\daily';
	$q = (count(glob("$dir/*.zip")) === 0) ? 'Empty' : 'Not empty';
	
	$Filenames = $_FILES['accessory']['name'];
	if ($q=="Empty")
		if (strpos($Filenames, 'accessory') !== False)
			{
				if ( move_uploaded_file( $_FILES['accessory']['tmp_name'], $move.'/'.$_FILES['accessory']['name']))
					{
						shell_exec("python C:\Users\RD1\PycharmProjects\PYTHONMAY2019\DailyFiles2ACCESSORY.py");
					
?>
<div class="alert alert-success" role="alert">
	<center><h5>EXPORT : <?php echo($_FILES['accessory']['name']) ?> SUCCESS</h5></center>
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




if(isset($_POST['accessory_submit']))
{
	$dir = 'C:\xampp\htdocs\Terminal\Daily Accessory\daily/';
	$dh = opendir($dir);
	while($file = readdir($dh))
	{
	if(!is_dir($file))
	{
	@unlink($dir.$file);
	}
	}
	closedir($dh);
	$move = 'C:\xampp\htdocs\Terminal\Daily Accessory\daily';
	$str = $_FILES['accessory']['tmp_name'];
	$dir = 'C:\xampp\htdocs\Terminal\Daily Accessory\daily';
	$q = (count(glob("$dir/*.zip")) === 0) ? 'Empty' : 'Not empty';
	
	$Filenames = $_FILES['accessory']['name'];
	if ($q=="Empty")
		if (strpos($Filenames, 'accessory') !== False)
			{
				if ( move_uploaded_file( $_FILES['accessory']['tmp_name'], $move.'/'.$_FILES['accessory']['name']))
					{
						shell_exec("python C:\Users\RD1\PycharmProjects\PYTHONMAY2019\DailyFiles2ACCESSORY.py");
					
?>
<div class="alert alert-success" role="alert">
	<center><h5>EXPORT : <?php echo($_FILES['accessory']['name']) ?> SUCCESS</h5></center>
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



if(isset($_POST['prepaid_residual_submit']))
{
	$dir = 'C:\xampp\htdocs\Terminal\Daily Prepaid Residual\daily/';
	$dh = opendir($dir);
	while($file = readdir($dh))
	{
	if(!is_dir($file))
	{
	@unlink($dir.$file);
	}
	}
	closedir($dh);
	$move = 'C:\xampp\htdocs\Terminal\Daily Prepaid Residual\daily';
	$str = $_FILES['prepaid_residual']['tmp_name'];
	$dir = 'C:\xampp\htdocs\Terminal\Daily Prepaid Residual\daily';
	$q = (count(glob("$dir/*.zip")) === 0) ? 'Empty' : 'Not empty';
	
	$Filenames = $_FILES['prepaid_residual']['name'];
	if ($q=="Empty")
		if (strpos($Filenames, 'prepaid_residual') !== False)
			{
				if ( move_uploaded_file( $_FILES['prepaid_residual']['tmp_name'], $move.'/'.$_FILES['prepaid_residual']['name']))
					{
						shell_exec("python C:\Users\RD1\PycharmProjects\PYTHONMAY2019\DailyFiles4PREPAIDRESIDUAL.py");
					
?>
<div class="alert alert-success" role="alert">
	<center><h5>EXPORT : <?php echo($_FILES['prepaid_residual']['name']) ?> SUCCESS</h5></center>
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





if(isset($_POST['prepay_residual_submit']))
{
	$dir = 'C:\xampp\htdocs\Terminal\Daily Prepay Residual\daily/';
	$dh = opendir($dir);
	while($file = readdir($dh))
	{
	if(!is_dir($file))
	{
	@unlink($dir.$file);
	}
	}
	closedir($dh);
	$move = 'C:\xampp\htdocs\Terminal\Daily Prepay Residual\daily';
	$str = $_FILES['prepay_residual']['tmp_name'];
	$dir = 'C:\xampp\htdocs\Terminal\Daily Prepay Residual\daily';
	$q = (count(glob("$dir/*.zip")) === 0) ? 'Empty' : 'Not empty';
	
	$Filenames = $_FILES['prepay_residual']['name'];
	if ($q=="Empty")
		if (strpos($Filenames, 'prepay_residual') !== False)
			{
				if ( move_uploaded_file( $_FILES['prepay_residual']['tmp_name'], $move.'/'.$_FILES['prepay_residual']['name']))
					{
						shell_exec("python C:\Users\RD1\PycharmProjects\PYTHONMAY2019\DailyFiles5PREPAY-RESIDUAL.py");
					
?>
<div class="alert alert-success" role="alert">
	<center><h5>EXPORT : <?php echo($_FILES['prepay_residual']['name']) ?> SUCCESS</h5></center>
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





if(isset($_POST['prepay_residual_submit']))
{
	$dir = 'C:\xampp\htdocs\Terminal\Daily Prepay Residual\daily/';
	$dh = opendir($dir);
	while($file = readdir($dh))
	{
	if(!is_dir($file))
	{
	@unlink($dir.$file);
	}
	}
	closedir($dh);
	$move = 'C:\xampp\htdocs\Terminal\Daily Prepay Residual\daily';
	$str = $_FILES['prepay_residual']['tmp_name'];
	$dir = 'C:\xampp\htdocs\Terminal\Daily Prepay Residual\daily';
	$q = (count(glob("$dir/*.zip")) === 0) ? 'Empty' : 'Not empty';
	
	$Filenames = $_FILES['prepay_residual']['name'];
	if ($q=="Empty")
		if (strpos($Filenames, 'prepay_residual') !== False)
			{
				if ( move_uploaded_file( $_FILES['prepay_residual']['tmp_name'], $move.'/'.$_FILES['prepay_residual']['name']))
					{
						shell_exec("python C:\Users\RD1\PycharmProjects\PYTHONMAY2019\DailyFiles5PREPAY-RESIDUAL.py");
					
?>
<div class="alert alert-success" role="alert">
	<center><h5>EXPORT : <?php echo($_FILES['prepay_residual']['name']) ?> SUCCESS</h5></center>
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





if(isset($_POST['residual_submit']))
{
	$dir = 'C:\xampp\htdocs\Terminal\Daily Residual\daily/';
	$dh = opendir($dir);
	while($file = readdir($dh))
	{
	if(!is_dir($file))
	{
	@unlink($dir.$file);
	}
	}
	closedir($dh);
	$move = 'C:\xampp\htdocs\Terminal\Daily Residual\daily';
	$str = $_FILES['residual']['tmp_name'];
	$dir = 'C:\xampp\htdocs\Terminal\Daily Residual\daily';
	$q = (count(glob("$dir/*.zip")) === 0) ? 'Empty' : 'Not empty';
	
	$Filenames = $_FILES['residual']['name'];
	if ($q=="Empty")
		if (strpos($Filenames, 'residual') !== False)
			{
				if ( move_uploaded_file( $_FILES['residual']['tmp_name'], $move.'/'.$_FILES['residual']['name']))
					{
						shell_exec("python C:\Users\RD1\PycharmProjects\PYTHONMAY2019\DailyFiles9RESIDUAL.py");
					
?>
<div class="alert alert-success" role="alert">
	<center><h5>EXPORT : <?php echo($_FILES['residual']['name']) ?> SUCCESS</h5></center>
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


?>


<?php include 'header.php';?>

	<div class="container-fluid">
			<br>
			<br>
			<center><h1>−− DATABASE AUTOMATION'S −−</h1></center>
			<br>
			<br>
				<div class="row">
					<div class="col-lg-5">
						<h4>Daily Accessory</h4>
						<form enctype="multipart/form-data" method="POST">
							<div class="input-group mb-3">
							  <input type="file" name="accessory" class="form-control cbutton">
								<div class="input-group-append">
									<button type="submit" name ='accessory_submit' value="Send" class="btn btn-outline-success">PROCESS</button>
									<!-- <button type="submit" name ='accessory_submit' value="Send" class="btn btn-outline-primary">DOWNLOAD</button>	
									<button type="submit" name ='accessory_accessory_stop' value="Send" class="btn btn-outline-danger">STOP</button>
									<button type="submit" name ='accessory_empty' value="Send" class="btn btn-outline-warning">INVALID</button> -->
								</div>
							</div>
						</form>
					</div>
					<div class="col-lg-2">
						<br>
						<br>
					</div>
					<div class="col-lg-5">
						<h4>Daily Handset</h4>
						<form enctype="multipart/form-data" method="POST">
							<div class="input-group mb-3">
								 <input type="file" name="handset" class="form-control cbutton">
								<div class="input-group-append">
									<button type="submit" name ='handset_submit' value="Send" class="btn btn-outline-success">PROCESS</button>
									<!-- <button type="submit" name ='submit2_2' value="Send" class="btn btn-outline-primary">DOWNLOAD</button>
									<button type="submit" name ='stop_2' value="Send" class="btn btn-outline-danger">STOP</button>
									<button type="submit" name ='empty_2' value="Send" class="btn btn-outline-warning">INVALID</button>
 -->								</div>
							</div>
						</form>
					</div>
				</div>
				<br>
				<br>
				<br>
				<div class="row">
					<div class="col-sm-5">
						<h4>Daily LumSum</h4>
						<form enctype="multipart/form-data" method="POST">
							<div class="input-group mb-3">
								<div class="custom-file">
									<input type="file" name="lumsum" class="form-control cbutton">
								</div>
								<div class="input-group-append">
									<button type="submit" name ='lumsum_submit' value="Send" class="btn btn-outline-success">PROCESS</button>
									<!-- <button type="submit" name ='submit3_3' value="Send" class="btn btn-outline-primary">DOWNLOAD</button>
									<button type="submit" name ='stop' value="Send" class="btn btn-outline-danger">STOP</button>
									<button type="submit" name ='empty' value="Send" class="btn btn-outline-warning">INVALID</button> -->
								</div>
							</div>
						</form>
					</div>
					<div class="col-sm-2">
						<br>
						<br>
					</div>
					<div class="col-sm-5">
						<h4>Daily PB</h4>
						<form enctype="multipart/form-data" method="POST">
							<div class="input-group mb-3">
								<div class="custom-file">
									<input type="file" name="pb" class="form-control cbutton">
								</div>
								<div class="input-group-append">
									<button type="submit" name ='pb_submit' value="Send" class="btn btn-outline-success">PROCESS</button>
							<!-- 		<button type="submit" name ='submit4_4' value="Send" class="btn btn-outline-primary">DOWNLOAD</button>
									<button type="submit" name ='stop' value="Send" class="btn btn-outline-danger">STOP</button>
									<button type="submit" name ='empty' value="Send" class="btn btn-outline-warning">INVALID</button> -->
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
						<h4>Daily Prepaid Residual</h4>
						<form enctype="multipart/form-data" method="POST">
							<div class="input-group mb-3">
								<div class="custom-file">
									<input type="file" name="prepaid_residual" class="form-control cbutton">
									<!-- <input type="file" class="custom-file-input" name="rma"  id="exampleInputFilerma">
									<label class="custom-file-label" for="inputGroupFile02">Choose file</label> -->
								</div>
								<div class="input-group-append">
									<button type="submit" name ='prepaid_residual_submit' value="Send" class="btn btn-outline-success">PROCESS</button>
									<!-- <button type="submit" name ='submit5_5' value="Send" class="btn btn-outline-primary">DOWNLOAD</button>
									<button type="submit" name ='stop' value="Send" class="btn btn-outline-danger">STOP</button>
									<button type="submit" name ='empty' value="Send" class="btn btn-outline-warning">INVALID</button> -->
								</div>
							</div>
						</form>
					</div>
					<div class="col-sm-2">
						<br>
						<br>
					</div>
					<div class="col-sm-5">
						<h4>Daily Prepay Residual</h4>
						<form enctype="multipart/form-data" method="POST">
							<div class="input-group mb-3">
								<div class="custom-file">
									<input type="file" name="prepay_residual" class="form-control cbutton">
								</div>
								<div class="input-group-append">
									<button type="submit" name ='prepay_residual_submit' value="Send" class="btn btn-outline-success">PROCESS</button>
							<!-- 		<button type="submit" name ='submit6_6' value="Send" class="btn btn-outline-primary">DOWNLOAD</button>
									<button type="submit" name ='stop' value="Send" class="btn btn-outline-danger">STOP</button>
									<button type="submit" name ='empty' value="Send" class="btn btn-outline-warning">INVALID</button> -->
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
						<h4>Daily Spiff</h4>
						<form enctype="multipart/form-data" method="POST">
							<div class="input-group mb-3">
								<div class="custom-file">
									<input type="file" name="PR5" class="form-control cbutton">
									<!-- <input type="file" class="custom-file-input" name="rma"  id="exampleInputFilerma">
									<label class="custom-file-label" for="inputGroupFile02">Choose file</label> -->
								</div>
								<div class="input-group-append">
									<button type="submit" name ='submit5' value="Send" class="btn btn-outline-success">PROCESS</button>
									<!-- <button type="submit" name ='submit5_5' value="Send" class="btn btn-outline-primary">DOWNLOAD</button>
									<button type="submit" name ='stop' value="Send" class="btn btn-outline-danger">STOP</button>
									<button type="submit" name ='empty' value="Send" class="btn btn-outline-warning">INVALID</button> -->
								</div>
							</div>
						</form>
					</div>
					<div class="col-sm-2">
						<br>
						<br>
					</div>
					<div class="col-sm-5">
						<h4>Daily Statement</h4>
						<form enctype="multipart/form-data" method="POST">
							<div class="input-group mb-3">
								<div class="custom-file">
									<input type="file" name="PR6" class="form-control cbutton">
									<!-- <input type="file" class="custom-file-input" name="rma"  id="exampleInputFilerma">
									<label class="custom-file-label" for="inputGroupFile02">Choose file</label> -->
								</div>
								<div class="input-group-append">
									<button type="submit" name ='submit6' value="Send" class="btn btn-outline-success">PROCESS</button>
								<!-- 	<button type="submit" name ='submit6_6' value="Send" class="btn btn-outline-primary">DOWNLOAD</button>
									<button type="submit" name ='stop' value="Send" class="btn btn-outline-danger">STOP</button>
									<button type="submit" name ='empty' value="Send" class="btn btn-outline-warning">INVALID</button> -->
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
						<h4>Daily Residual</h4>
						<form enctype="multipart/form-data" method="POST">
							<div class="input-group mb-3">
								<div class="custom-file">
									<input type="file" name="residual" class="form-control cbutton">

								</div>
								<div class="input-group-append">
									<button type="submit" name ='residual_submit' value="Send" class="btn btn-outline-success">PROCESS</button>
							<!-- 		<button type="submit" name ='submit5_5' value="Send" class="btn btn-outline-primary">DOWNLOAD</button>
									<button type="submit" name ='stop' value="Send" class="btn btn-outline-danger">STOP</button>
									<button type="submit" name ='empty' value="Send" class="btn btn-outline-warning">INVALID</button> -->
								</div>
							</div>
						</form>
					</div>
					<div class="col-sm-2">
						<br>
						<br>
					</div>
					<div class="col-sm-5">
						<h4>#</h4>
						<form enctype="multipart/form-data" method="POST">
							<div class="input-group mb-3">
								<div class="custom-file">
									<input type="file" name="PR6" class="form-control cbutton">
									<!-- <input type="file" class="custom-file-input" name="rma"  id="exampleInputFilerma">
									<label class="custom-file-label" for="inputGroupFile02">Choose file</label> -->
								</div>
								<div class="input-group-append">
									<button type="submit" name ='submit6' value="Send" class="btn btn-outline-success">PROCESS</button>
				<!-- 					<button type="submit" name ='submit6_6' value="Send" class="btn btn-outline-primary">DOWNLOAD</button>
									<button type="submit" name ='stop' value="Send" class="btn btn-outline-danger">STOP</button>
									<button type="submit" name ='empty' value="Send" class="btn btn-outline-warning">INVALID</button> -->
								</div>
							</div>
						</form>
					</div>
				</div>
			</div>

</body>
</html>