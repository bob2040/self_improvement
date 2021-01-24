package cn.itcast.demo.demo110220;

import java.util.ArrayList;
import java.util.stream.Stream;

public class DemoStream {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("邢恩宝");
        list.add("bbbbb");
        list.add("ccc");
        list.add("d");
        list.add("eee");
        list.add("fffff");
        list.add("ggg");
        list.add("kkkkkkkk");

        list.stream().filter(name -> name.length() == 3).limit(3).forEach(name-> System.out.println(name));
    }
}
