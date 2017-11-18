<?php
session_start();
?>
<!DOCTYPE html>
<html>
    <head>
        <title>Edit Transaction</title>
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
        <div class="container">
        <div class="panel-group">

            <div class="panel panel-info">
                <div class="panel-heading">Edit Transaction</div>
                <div class="panel-body">
                <form class="form" action="update.php" method="POST">
                    <label>Id : <input name="id" id="id" type="text" disabled/></label><br/>
                   <label>Date : <input name="date" id="date" type="text" placeholder="dd-mm-yyyy" /></label><br/>
                    <label>Type :
                        <select id="type" name="type">
                            <option value="credit" id="credit">Credit</option>
                            <option value="debit" id="debit">Debit</option>
                            <option value="save" id="save">Savings</option>
                        </select>
                    </label><br/>
                    <label>Category:
                        <select name="category" id="category">
                            <option id="Food" value="food">Food</option>
                            <option id="Misc" value="misc">Misc</option>
                            <option id="Study" value="study">Study</option>
                            <option id="Cosmetics" value="cosmetics">Cosmetics</option>
                            <option id="Entertainment" value="entertainment">Entertainment</option>
                            <option id="personal" id="personal"="personal">Personal</option>
                            <option id="travel" value="travel">Travel</option>
                        </select>
                    </label>
                   <label>
                        Dealer : <input id="dealer" name="dealer" type="text" placeholder="Dealer"/><br/>
                    </label>
                     <label>Paid Status : <input name="paid_status" id="paid_status" value="paid_status"type="checkbox"/></label><br/>
                    <label>Amount <input name="amount" id="amount" type="number"/> </label><br/>
                    <button class="btn btn-success" name="update" type="submit">Update transaction</button>
                    <div id="result"></div>
                    </form>
                </div> <!--body 1 ends here -->
            </div> <!--panel default -->
            <div class="panel panel-primary">
            <div class="panel-heading"> Select Transaction To Edit </div>
            <div class="panel-body">
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
            </div>
         </div>
        </div> <!--panel group -->
        </div> <!-- container -->

        <script type="text/javascript" src="js/edit.js"></script>
        <script type="text/javascript" src="js/getAll.js"></script>
    </body>
</html>