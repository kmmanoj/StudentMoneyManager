<?php
session_start();
?>

<!DOCTYPE html>
<html>
    <head>
        <title>
            Select Transactions to Delete
        </title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="css/bootstrap.min.css">
        <script src="js/jquery.min.js"></script>
        <script src="js/bootstrap.min.js"></script>
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
        <h1>Delete transactions</h1>
        <form class="form" action="deleteThese.php">
            <div class="table-responsive">
                <table class="table table-bordered table-striped" id="tab1">
                    <th>Select</th>
                    <th>Date</th>
                    <th>Type</th>
                    <th>Category</th>
                    <th>Dealer</th>
                    <th>Paid Status</th>
                    <th>Amount</th>
                </table>
            </div>
             <button class="btn btn-primary" type="submit" >Delete transaction(s)</button>
        </form>
        <script type="text/javascript" src="js/delete.js"></script>
        <script type="text/javascript" src="js/getAll.js"></script>
    </body>
</html>