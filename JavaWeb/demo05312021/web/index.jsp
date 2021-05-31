<%@ page import="java.util.Date" %>
<%@ page import="java.text.SimpleDateFormat" %>
<%@ page import="java.net.URLEncoder" %>
<%@ page import="java.net.URLDecoder" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
  <head>
    <title>JSP_and_Cookie</title>
    <style>
      span{
        color: red;
      }
    </style>
  </head>
  <body>

    <%
      Cookie[] cookies = request.getCookies();
      boolean flag = false;

      if(cookies != null && cookies.length >0){
        for (Cookie cookie : cookies) {
          String name = cookie.getName();
          if("lastTime".equals(name)){
            flag = true;
            Date date = new Date();
            SimpleDateFormat sdf = new SimpleDateFormat("HH:mm:ss MM-dd-yyyy");
            String str_date = sdf.format(date);
            str_date = URLEncoder.encode(str_date,"utf-8");

            String value = cookie.getValue();
            value = URLDecoder.decode(value,"utf-8");
    %>
            <h1>Welcome back!<br>Last time you opened this page: <span><%= value %></span></h1>
    <%
            cookie.setMaxAge(60 * 60 * 24);
            //cookie.setMaxAge(0);
            cookie.setValue(str_date);
            response.addCookie(cookie);

            break;
          }
        }
      }

      if(cookies == null || cookies.length == 0 || flag == false){
        Date date = new Date();
        SimpleDateFormat sdf = new SimpleDateFormat("HH:mm:ss MM-dd-yyyy");
        String str_date = sdf.format(date);
        str_date = URLEncoder.encode(str_date,"utf-8");
    %>
        <h1>This is your first visit,Welcome!</h1>
    <%
        Cookie cookie = new Cookie("lastTime",str_date);
        cookie.setMaxAge(60 * 60 * 24);
        //cookie.setMaxAge(0);
        response.addCookie(cookie);
      }
    %>

    <%
      Date date_realTime = new Date();
      SimpleDateFormat sdf_realTime = new SimpleDateFormat("HH:mm:ss MM-dd-yyyy");
      String str_date_realTime = sdf_realTime.format(date_realTime);
    %>
    <h1>This time you opened this page: <span><%=str_date_realTime%></span></h1>

  </body>
</html>
