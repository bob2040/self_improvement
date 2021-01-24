package demo12072020;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;


public class DemoJDBC {
    public static void main(String[] args) {
        Statement stmt = null;
        Connection conn = null;
        try {
            Class.forName("com.mysql.jdbc.Driver");
            conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/db3", "root", "root");
            String sql = "insert into student values(null,'Lily',18)";
            stmt = conn.createStatement();
            int count = stmt.executeUpdate(sql);
            System.out.println(count);
            if(count > 0){
                System.out.println("Add data successfully!");
            }else{
                System.out.println("Add data unsuccessfully!");
            }
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {

            if (stmt != null){
                try {
                    stmt.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
            if (conn != null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
