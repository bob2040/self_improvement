package jedis.test;

import jedis.util.JedisPoolUtils;
import org.junit.Test;
import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;

import java.util.List;
import java.util.Map;
import java.util.Set;



public class JedisTest {

    @Test
    public void test1(){

        Jedis jedis = new Jedis("localhost",6379);

        jedis.set("username","zhangsan");

        String username = jedis.get("username");
        System.out.println(username);

        jedis.close();
    }


    @Test
    public void test2(){

        Jedis jedis = new Jedis();

        jedis.setex("activecode",10,"hehe");

        jedis.close();
    }


}
