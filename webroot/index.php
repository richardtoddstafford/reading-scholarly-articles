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
  <link rel="stylesheet" href="static/css/body.css">

  <!-- Javascript
  ================================================== -->
  <script src="static/js/jquery.min.js"></script>
  <script src="static/js/bootstrap.min.js"></script>

  <!-- Favicons
  ================================================== -->
  <link rel="shortcut icon" href="static/imgs/favicon.ico">

</head>
<body>
  <!-- Primary Page Layout
  ================================================== -->

  <div id="wrap">

    <div class="container">


      <!-- Header Row
      ================================================ -->
      <div class="row">
        <div class="col-md-10 col-md-offset-1">
          <div class="page-header">
            <h1>
            <span class="pull-right"><a href="/"><i class="fa fa-home"
            title="Return Home"></i></a></span>
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
                case 'socialscience':
                  echo "Social Science";
                  break;
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
        case 'socialscience':
          include("content/socialscience.content");
          break;
#      case 'humanities':
#        include("content/humanities.content");
#        break;
        case '':
          include("content/index.content");
        default:
          break;
      }
      ?>

    </div>

  </div>

  <div id="footer">

    <div class="container">
      <div class="row">
        <div class="col-sm-10 col-sm-offset-1 text-center">
          <span class="pull-right"><a href="#top">Return to top</a></span>
          Built by <a href="http://michel.rouly.net">Michel Rouly</a> for
          <a href="//gmu.edu">George Mason University</a> with
          <a href="http://www.gnu.org/licenses/gpl-3.0.txt">some rights
          reserved</a>.
        </div>
      </div>
    </div>

  </div>

  <!-- Javascript
  ================================================== -->
  <script src="static/js/latexit.js"></script>
  <script src="static/js/annotations.js"></script>

</body>
</html>
