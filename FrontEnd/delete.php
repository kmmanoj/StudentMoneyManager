<!DOCTYPE html>
<html>
    <head>
        <title>
            select to delete
        </title>
    </head>
    <body>
        <h1>Delete transactions</h1>
        <div>
                <table border="1">
                    <th></th>
                    <th>transaction id</th>
                    <th>dealer</th>
                    <th>..</th>
                    <th>amount</th>
                    <tr>
                        <td><input type="checkbox" name="transaction1"/></td>
                        <td>1</td>
                        <td>dealer1</td>
                        <td>..</td>
                        <td>100</td>
                    </tr>
                    <tr>
                        <td><input type="checkbox" name="transaction2"/></td>
                        <td>2</td>
                        <td>dealer2</td>
                        <td>..</td>
                        <td>120</td>
                    </tr>
                </table>
            </div>
            <button onclick="edit()">Delete transaction</button>
    </body>
</html>