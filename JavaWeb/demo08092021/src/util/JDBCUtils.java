package util;

import com.alibaba.druid.pool.DruidDataSourceFactory;

import javax.sql.DataSource;
import java.io.IOException;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Properties;

/**
 * Druid连接池的工具类
 *      定义工具类
 *              1.定义一个类 JDBCUtils
 *              2.提供静态代码块加载配置文件，初始化连接池对象
 *              3.提供方法
 *                  1.获取连接的方法：通过数据库连接池来获取连接
 *                  2.释放资源
 *                  3.获取连接池的方法
 */
public class JDBCUtils {
    //1.定义成员变量 DataSource
    private static DataSource ds;

    //在静态代码块中对定义的成员变量进行初始化赋值
    static {
        try {
            //1.加载配置文件
            Properties pro = new Properties();
            pro.load(JDBCUtils.class.getClassLoader().getResourceAsStream("druid.properties"));
            //2.获取获取数据库连接池DataSource对象
            ds = DruidDataSourceFactory.createDataSource(pro);
        } catch (IOException e) {
            e.printStackTrace();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    /**
     * 定义获取连接对象的方法
     */
    public static Connection getConnection() throws SQLException {//此处异常抛出，是为了警告别人
        return ds.getConnection();
    }

    /**
     * 释放资源
     */
    public static void close(Statement stmt,Connection conn){
        /*if (stmt != null){
            try {
                stmt.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
        if (conn != null){//归还连接对象到连接池
            try {
                conn.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }*/
        close(null,stmt,conn);
    }
    public static void close(ResultSet rs, Statement stmt, Connection conn){
        if (rs != null){
            try {
                rs.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
        if (stmt != null){
            try {
                stmt.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
        if (conn != null){//归还连接对象到连接池
            try {
                conn.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
    /**
     * 获取连接池的方法
     */
    public static DataSource getDataSource(){
        return ds;
    }
}
