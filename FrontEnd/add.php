<?php
session_start();
?>

<!DOCTYPE html>
<html>
    <head>
        <title>Add Transaction</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1"> 
        <link rel="stylesheet" href="css/bootstrap.min.css">
        <script src="js/jquery.min.js"></script>
        <script src="js/bootstrap.min.js"></script>
        <style>
            .set-width{
                width:200px;
            }
              body{

            background-color: #bebebe;
            background-image: url('css/img/black4.jpg');
            background-position: center;*/
            background-size: 100%;
            background-repeat: no-repeat;
            
        }
        </style>
    </head>
    <body>

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
        <div class="jumbotron">

        <center><h2><b>Add Transaction</b></h2></center>
        <hr style="color:black;"/>
        <center>
      
        <input class="form-control set-width" id="date" type="text" placeholder="Enter date in dd-mm-yyyy" required/>
        <label>Type :
            <select class="form-control set-width" id="type">
                <option id="credit">Credit</option>
                <option id="debit">Debit</option>
                <option id="save">Savings</option>
            </select>
        </label>
        <label>Category:
            <select class="form-control set-width" id="category">
                <option class="form-control set-width" id="Food">Food</option>
                <option class="form-control set-width" id="Misc">Misc</option>
                <option class="form-control set-width" id="Study">Study</option>
                <option class="form-control set-width" id="Cosmetics">Cosmetics</option>
                <option class="form-control set-width" id="Entertainment">Entertainment</option>
                <option class="form-control set-width" id="personal">Personal</option>
                <option class="form-control set-width" id="travel">Travel</option>


            </select>
        </label>
        <input class="form-control set-width" id="dealer" type="text" placeholder="Enter Dealer name" required/>
       
        <label>Paid Status : <input class="form-control set-width" id="paid_status" style="width:20px; height:20px;" type="checkbox"/></label><br/>
        <input id="amount" class="form-control set-width" type="number" placeholder="Enter amount" required/> </label><br/>

        <button class="btn btn-primary" onclick="add()">Add new Transaction</button>

        <div id="result"></div>
        </center>
    </div>
    </div>
      <script type="text/javascript" src="js/add.js"></script>
    </body>
</html>