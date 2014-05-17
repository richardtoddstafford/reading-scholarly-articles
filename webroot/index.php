<?php
$request_uri = @parse_url($_SERVER['REQUEST_URI']);
$path = substr($request_uri['path'], 1);
?>

<!DOCTYPE html>
<html>
<head>

  <!-- Basic Page Needs
  ================================================== -->
  <meta charset="utf-8">
  <title>Anatomy of a Scholarly Article</title>

  <!-- CSS
  ================================================== -->
  <link rel="stylesheet" href="static/css/bootstrap.min.css">
  <link rel="stylesheet" href="static/css/fonts.css">

  <!-- Favicons
  ================================================== -->
  <link rel="shortcut icon" href="static/imgs/favicon.ico">

  <!-- Javascript
  ================================================== -->
  <script src="static/js/jquery.min.js"></script>
  <script src="static/js/bootstrap.min.js"></script>

</head>
<body>


  <!-- Navigation Bar
  ================================================== -->

  <div class="navbar navbar-default">
    <div class="container">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">
          <span class="sr-only">Toggle navigation</span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand" href="/">Anatomy of a Scholarly Article</a>
      </div>

      <!-- Collect the nav links, forms, and other content for toggling -->
      <div class="collapse navbar-collapse navbar-ex1-collapse">
        <ul class="nav navbar-nav">
          <li><a href="">About</a></li>
          <li class="dropdown">
            <a href="#" class="dropdown-toggle"
            data-toggle="dropdown">Select Field <b class="caret"></b></a>
            <ul class="dropdown-menu">
              <li><a href="/math">Mathematics</a></li>
              <li><a href="/natsci">Natural Sciences</a></li>
              <li><a href="/cs">Computer Science</a></li>
              <li><a href="/lit">Literature</a></li>
              <li><a href="/gov">Government</a></li>
            </ul>
          </li>
        </ul>
      </div><!-- /.navbar-collapse -->
    </div><!-- /.container -->
  </div>


  <!-- Primary Page Layout
  ================================================== -->



  <div class="container">


    <!-- Header Row
    ================================================ -->
    <div class="row">
      <div class="col-lg-12">
        <div class="page-header">
          <h1>
            <?php
            switch( $path ) {
              case 'math':
                echo "Mathematics";
                break;
              case 'natsci':
                echo "Natural Sciences";
                break;
              default:
                echo "Anatomy of a Scholarly Article";
            }
            ?>
          </h1>
        </div>
      </div>
    </div>

    <?php
    switch( $path ) {
      case 'math':
        include("content/math.content");
        break;
      case 'natsci':
        include("content/natsci.content");
        break;
      default:
        include("content/index.content");
    }
    ?>


  </div>


</body>
</html>
