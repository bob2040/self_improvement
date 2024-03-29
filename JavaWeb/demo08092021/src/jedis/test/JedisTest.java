package jedis.test;

import jedis.util.JedisPoolUtils;
import org.junit.Test;
import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;

import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * Jedis测试类
 */
public class JedisTest {
/**
 * 快速入门
 */
    @Test
    public void test1(){
        //1.获取连接
        Jedis jedis = new Jedis("localhost",6379);
        //2.操作
        jedis.set("username","zhangsan");
        //3.关闭连接
        jedis.close();
    }

    /**
     * string 数据结构操作
     */
    @Test
    public void test2(){
        //1.获取连接
        Jedis jedis = new Jedis();//如果使用空参构造，默认值 "localhost",6379端口
        //2.操作
        //存储
        jedis.set("username","zhangsan");
        //获取
        String username = jedis.get("username");
        System.out.println(username);

        //可以使用setex()方法存储可以指定过期时间的key value键值对
        jedis.setex("activecode",20,"hehe");//将activecode:hehe键值对存入redis，并且20秒后自动删除该键值对

        //3.关闭连接
        jedis.close();
    }

    /**
     * hash 数据结构操作
     */
    @Test
    public void test3(){
        //1.获取连接
        Jedis jedis = new Jedis();//如果使用空参构造，默认值 "localhost",6379端口
        //2.操作
        //存储hash
        jedis.hset("user","name","lisi");
        jedis.hset("user","age","24");
        jedis.hset("user","gender","male");
        //获取hash
        String name = jedis.hget("user", "name");
        System.out.println(name);

        //获取hash的所有map中的数据
        Map<String, String> user = jedis.hgetAll("user");
        //keySet()方法遍历
        Set<String> set = user.keySet();
        for (String key : set) {
            //获取value
            String value = user.get(key);
            System.out.println(key + ":" + value);
        }
        //3.关闭连接
        jedis.close();
    }

    /**
     * list 数据结构操作
     */
    @Test
    public void test4(){
        //1.获取连接
        Jedis jedis = new Jedis();//如果使用空参构造，默认值 "localhost",6379端口
        //2.操作
        //list 存储
        jedis.lpush("mylist","a","b","c");//从左边存
        jedis.rpush("mylist","a","b","c");//从右边存
        //list 范围获取
        List<String> mylist = jedis.lrange("mylist", 0, -1);
        System.out.println(mylist);//[c, b, a, a, b, c]

        //list弹出
        String element1 = jedis.lpop("mylist");
        System.out.println(element1);//c
        String element2 = jedis.rpop("mylist");
        System.out.println(element2);//c

        List<String> mylist2 = jedis.lrange("mylist", 0, -1);
        System.out.println(mylist2);//[b, a, a, b]

        //3.关闭连接
        jedis.close();
    }

    /**
     * set 数据结构操作
     */
    @Test
    public void test5(){
        //1.获取连接
        Jedis jedis = new Jedis();//如果使用空参构造，默认值 "localhost",6379端口
        //2.操作
        //set 存储
        jedis.sadd("myset","java","php","c++");
        //set 获取
        Set<String> myset = jedis.smembers("myset");
        System.out.println(myset);//[c++, java, php]

        //3.关闭连接
        jedis.close();
    }

    /**
     * sortedset 数据结构操作
     */
    @Test
    public void test6(){
        //1.获取连接
        Jedis jedis = new Jedis();//如果使用空参构造，默认值 "localhost",6379端口
        //2.操作
        //sortedset 存储
        jedis.zadd("mysortedset",3,"亚瑟");
        jedis.zadd("mysortedset",30,"后羿");
        jedis.zadd("mysortedset",25,"孙悟空");
        //sortedset 获取
        Set<String> mysortedset = jedis.zrange("mysortedset", 0, -1);
        System.out.println(mysortedset);//[亚瑟, 孙悟空, 后羿]

        //3.关闭连接
        jedis.close();
    }

    /**
     * Jedis连接池
     */
    @Test
    public void test7(){
        //0.创建配置对象
        JedisPoolConfig config = new JedisPoolConfig();
        config.setMaxTotal(50);
        config.setMaxIdle(10);

        //1.创建Jedis连接池对象
        JedisPool jedisPool = new JedisPool(config,"localhost",6379);
        //2.获取连接
        Jedis jedis = jedisPool.getResource();
        //3.使用
        jedis.set("hehe","hihi");

        //4.关闭 归还到连接池中
        jedis.close();
    }

    /**
     * Jedis连接池工具类使用
     */
    @Test
    public void test8(){
        //通过Jedis连接池工具类获取连接
        Jedis jedis = JedisPoolUtils.getJedis();
        //3.使用
        jedis.set("hello","world!");

        //4.关闭 归还到连接池中
        jedis.close();
    }

}
