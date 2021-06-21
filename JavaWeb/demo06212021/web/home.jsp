<%@ page contentType="text/html;charset=UTF-8" language="java" %>


<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>FilterWords</title>
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <script src="js/jquery-3.2.1.min.js"></script>
    <script src="js/bootstrap.min.js"></script>

    <style>
        .form-control{
            width: 800px;
            font-size: 20px;
        }
        .btn{
            margin-left: 730px;
        }
        div{
            width: 800px;
            height: 200px;
            margin: auto;
        }
    </style>

</head>
<body>
<div>
<h3>Output:</h3>
<textarea class="form-control" rows="5" readonly>${filtered_text}</textarea>
</div>
<br>
<form action="${pageContext.request.contextPath}/wordsServlet" method="post">
    <div>
    <h3>Input:</h3>
    <textarea class="form-control"  name="text" rows="5">${original_text}</textarea>
    </div>
    <br>
    <div>
    <input class="btn btn-warning" type="submit" value="submit">
    </div>
</form>

</body>
</html>