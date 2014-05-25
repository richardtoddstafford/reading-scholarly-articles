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
  <link rel="stylesheet" href="static/css/font-awesome.min.css">
  <link rel="stylesheet" href="static/css/fonts.css">
  <link rel="stylesheet" href="static/css/article.css">
  <link rel="stylesheet" href="static/css/annotations.css">

  <!-- Javascript
  ================================================== -->
  <script src="static/js/jquery.min.js"></script>
  <script src="static/js/bootstrap.min.js"></script>

  <!-- Favicons
  ================================================== -->
  <link rel="shortcut icon" href="static/imgs/favicon.ico">

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
          <li><a href="/">About</a></li>
          <li class="dropdown">
            <a href="#" class="dropdown-toggle"
            data-toggle="dropdown">Select Field <b class="caret"></b></a>
            <ul class="dropdown-menu">
              <li><a href="/engineering">Engineering</a></li>
              <li><a href="/science">Life Science</a></li>
              <li><a href="/health">Public Health</a></li>
              <li><a href="/socialscience">Social Science</a></li>
              <li><a href="/humanities">Humanities</a></li>
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
              case 'engineering':
                echo "Engineering";
                break;
              case 'science':
                echo "Life Science";
                break;
#              case 'health':
#                echo "Public Health";
#                break;
#              case 'socialscience':
#                echo "Social Science";
#                break;
#              case 'humanities':
#                echo "Humanities";
#                break;
              case '':
                echo "Anatomy of a Scholarly Article";
                break;
              default:
                echo "Page not found";
            }
            ?>
          </h1>
        </div>
      </div>
    </div>

    <?php
    switch( $path ) {
      case 'engineering':
        include("content/engineering.content");
        break;
      case 'science':
        include("content/science.content");
        break;
#      case 'health':
#        include("content/health.content");
#        break;
#      case 'socialscience':
#        include("content/socialscience.content");
#        break;
#      case 'humanities':
#        include("content/humanities.content");
#        break;
      case '':
        include("content/index.content");
      default:
        break;
    }
    ?>

    <footer>
      <div class="row">
        <div class="col-sm-12 text-center">
          Built by <a href="http://michel.rouly.net">Michel Rouly</a> for
          <a href="//gmu.edu">George Mason University</a> with
          <a href="http://www.gnu.org/licenses/gpl-3.0.txt">some rights
          reserved</a>.
        </div>
      </div>
    </footer>


  </div>

  <!-- Javascript
  ================================================== -->
  <script src="static/js/latexit.js"></script>
  <script src="static/js/annotations.js"></script>

</body>
</html>
