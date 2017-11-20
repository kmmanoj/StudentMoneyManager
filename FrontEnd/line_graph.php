<?php
session_start();
?>
<!DOCTYPE html>
<html>
    <head>
        <title>Line graph</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="css/bootstrap.min.css">
        <script src="js/jquery.min.js"></script>
        <script src="js/bootstrap.min.js"></script>
        <script type = "text/javascript" src = "https://www.gstatic.com/charts/loader.js"></script>
      <script type = "text/javascript">
         google.charts.load('current', {packages: ['corechart','line']});  
      </script>

    </head>
    <body onload="getLine()">
    <div class="row">
      <nav class="navbar navbar-inverse">
        <div class="container-fluid">
          <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="home.php">StudentMoneyManager</a>
          </div> <!-- div navbar header ends here -->
          <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
            <ul class="nav navbar-nav">
                <li><a href="home.php">Home</a></li>
                <li><a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">My Profile <span class="caret"></span></a>
                <ul class="dropdown-menu">
                    <li> Logout </li>

                </ul>
                </li>
            </ul>
            <ul class="nav navbar-nav navbar-right">
              <li><a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Transactions<span class="caret"></span></a>
                <ul class="dropdown-menu">
                    <li><a href="add.php"> Add </a></li>
                    <li role="separator" class="divider"></li>
                    <li><a href="edit.php"> Edit </a></li>
                    <li role="separator" class="divider"></li>
                    <li><a href="delete.php"> Delete </a></li>
                    <li role="separator" class="divider"></li>
                    <li><a href="pie_chart.php"> View Pie Chart </a></li>
                    <li role="separator" class="divider"></li>
                    <li><a href="line_graph.php"> View Line Graph </a></li>
                </ul>
              </li>
              <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Contact Us <span class="caret"></span></a>
              <ul class="dropdown-menu">
                <li> Ahaan Rajesh </li>
                <li role="separator" class="divider"></li>
                <li> Karthik Ravi </li>
                <li role="separator" class="divider"></li>
                <li> Manshi Sanghai </li>
                <li role="separator" class="divider"></li>
                <li> Manjunath </li>
                <li role="separator" class="divider"></li>
                <li> Manoj Vignesh </li>
                <li role="separator" class="divider"></li>
                <li> Arpitha R </li>
                <li role="separator" class="divider"></li>
                <li> Anusha </li>
                <li role="separator" class="divider"></li>
                <li> Dilip </li>
              </ul>
              </li> <!--Dropdown li ends here -->
            </ul> <!--right nav bar ends here -->
          </div><!-- navbar-collapse ends here -->
        </div><!-- ends container-fluid -->
      </nav>
    </div> <!-- nav bar ends here -->    
    <div class="container">
        <ul class="nav nav-tabs nav-fill">
            <li class="nav-item active"><a href="#1" aria-controls="1" role="tab" data-toggle="tab">Credit Chart</a></li>
            <li class="nav-item"><a href="#2" aria-controls="2" role="tab" data-toggle="tab">Debit Chart</a></li>  
            <li class="nav-item"><a href="#3" aria-controls="3" role="tab" data-toggle="tab">Savings Chart</a></li>  
        </ul>
        
        <div class="tab-content">
           
                <div role="tabpanel" class="tab-pane active" id="1">
                    <div id="chart1"></div>
                </div>
            <div role="tabpanel" class="tab-pane active" id="2">
                <div id="chart2"></div>
            </div>
            <div role="tabpanel" class="tab-pane active" id="3">
                <div id="chart3"></div>
            </div>
        </div>
    </div>
   
    <script type="text/javascript" src="js/line.js"></script>
    </body>
</html>