<?php
session_start();
?>

<!DOCTYPE html>
<html>
    <head>
        <title>Add Transaction</title>
    </head>
    <body>
        <h1>Add Transaction</h1>
        <label>Date : <input id="date" type="date"/></label><br/>
        <label>type :
            <select id="type">
                <option id="credit">Credit</option>
                <option id="debit">Debit</option>
                <option id="save">Savings</option>
            </select>
        </label><br/>
        <label>Category:
            <select id="category">
                <option id="category1">Category 1</option>
                <option id="category2">Category 2</option>
            </select>
        </label>
        <label>
            Dealer : <input id="dealer" type="text" placeholder="Dealer"/><br/>
        </label>
        <label>Paid Status : <input id="paid_status" type="checkbox"/></label><br/>
        <label>Amount <input id="amount" type="number"/> </label><br/>
        <button onclick="add()">Add new transaction</button>
        <div id="result"></div>

      <script type="text/javascript" src="js/add.js"></script>
    </body>
</html>