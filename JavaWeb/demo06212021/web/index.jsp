<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
  <head>
    <title>TextFilter</title>
  </head>
  <body>
    <input type="text" value="${msg}" height="500" width="500" readonly>

    <form action="${pageContext.request.contextPath}/wordsServlet" method="post">
      <input type="text" name="text" width="500" height="500">
      <input type="submit" value="submit">
    </form>

  </body>
</html>
