<%@ page import="java.util.List" %>
<%@ page import="java.util.ArrayList" %>
<%@ page import="jstl.domain.User" %>
<%@ page import="java.text.SimpleDateFormat" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<head>
    <title>JSTL_EL_Practice</title>
</head>
<body>

    <%
        SimpleDateFormat sdf = new SimpleDateFormat("MM-dd-yyyy");
        List list = new ArrayList();
        list.add(new User("Joe",18,sdf.parse("09-24-1999")));
        list.add(new User("Tom",20,sdf.parse("10-01-1997")));
        list.add(new User("Lily",23,sdf.parse("03-08-1990")));

        request.setAttribute("list",list);
    %>
    <table border="1" width="500" align="center">
        <tr>
            <th>No.</th>
            <th>Name</th>
            <th>Age</th>
            <th>Birthday</th>
        </tr>
        <c:forEach items="${list}" var="user" varStatus="s">

                <tr>
                    <td>${s.count}</td>
                    <td>${user.name}</td>
                    <td>${user.age}</td>
                    <td>${user.birStr}</td>
                </tr>

        </c:forEach>
    </table>

</body>
</html>
