package service.impl;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import dao.ProvinceDao;
import dao.impl.ProvinceDaoImpl;
import domain.Province;
import jedis.util.JedisPoolUtils;
import redis.clients.jedis.Jedis;
import service.ProvinceService;

import java.util.List;

public class ProvinceServiceImpl implements ProvinceService {

    private ProvinceDao dao = new ProvinceDaoImpl();
    @Override
    public List<Province> findAll() {
        return dao.findAll();
    }


    @Override
    public String findAllJson() {

        Jedis jedis = JedisPoolUtils.getJedis();

        String province_json = jedis.get("province");

        if(province_json == null || province_json.length() == 0){

            System.out.println("There are no province data in Redis，querying MySQL database......");

            List<Province> ps = dao.findAll();

            ObjectMapper mapper = new ObjectMapper();
            try {
                province_json = mapper.writeValueAsString(ps);
            } catch (JsonProcessingException e) {
                e.printStackTrace();
            }

            jedis.set("province",province_json);

            jedis.close();
        }else {

            System.out.println("The province data are in Redis already，querying cache......");
        }
        return province_json;
    }
}
