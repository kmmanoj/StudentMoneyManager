<?php
session_start();
?>
<!DOCTYPE html>
<html>
    <head>
        <title>Home page</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="css/bootstrap.min.css">
        <script src="js/jquery.min.js"></script>
        <script src="js/bootstrap.min.js"></script>
        <style type="text/css">
            .btnLink{
                text-decoration: none !important;
                color: black;
                font-weight: 10;
            }
            body{

            background-color: #bebebe;
            background-image: url('css/img/black4.jpg');
            background-position: center;*/
            background-size: 100%;
            background-repeat: no-repeat;
            
        }
            .allTransac{
                height:400px;
                overflow-x: scroll;
                width:100%;

            }
        </style>
    </head>
    <body onload="getAll()">

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
                    <li><a href="debts.php"> Debts </a></li>
                    <li role="separator" class="divider"></li>
                    <li><a href="owes.php"> Owes </a></li>
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
            <div class="row">
                <h3 style="color:white; font-weight: 10px;">
                Hi, <?php 
                        if ($_SESSION['uname'])
                            echo $_SESSION['uname'];
                        else
                            echo "Guest";?>!
                </h3>
            </div>
            <div class="row">
                <div class="col-sm-1"></div>
                <div class="col-sm-2">
                    <button class="btn btn-primary"><a class="btnLink" href="add.php"> Add transaction </a></button>
                </div>
                <div class="col-sm-2">
                    <button class="btn btn-success"><a class="btnLink" href="delete.php">Delete transaction</a></button>
                </div>
                <div class="col-sm-2">
                    <button class="btn btn-info"><a class="btnLink" href="edit.php">Edit transaction</a></button>
                </div>
            
                <div class="col-sm-2">
                    <button class="btn btn-warning"><a class="btnLink" href="pie_chart.php">Pie chart</a></button>
                </div>
                <div class="col-sm-2">
                    <button class="btn btn-default"><a class="btnLink" href="line_graph.php">Line graph</a></button>
                </div>
                <div class="col-sm-1"></div>
            </div>
           
        </div>
        <br />
        <div class="container">
            <div class="panel panel-primary allTransac">
            <div class="panel-heading">All Your Transactions</div>
            <div class="panel-body">
                <div class="table-responsive">
                    <table class="table table-bordered table-striped" id="tab1">
                        <th>Date</th>
                        <th>Type</th>
                        <th>Category</th>
                        <th>Dealer</th>
                        <th>Paid Status</th>
                        <th>Amount</th>
                    </table>
                </div>
            </div>
            </div>
        </div>
        <script type="text/javascript" src="js/home.js"></script>
        <script type="text/javascript" src="js/getAll.js"></script>
    </body>
</html>