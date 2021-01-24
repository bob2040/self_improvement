package cn.itcast.demo.demo060520;

import cn.itcast.demo.demo060520.Manager;
import cn.itcast.demo.demo060520.Member;

import java.util.ArrayList;

/*
Practice title:
A manager in a wechat group send a redpacket to their members
 */
public class DemoRedPacket {
    public static void main(String[] args) {
        Manager manager =new Manager("Manager",100);
        Member one=new Member("M-A",0);
        Member two=new Member("M-B",0);
        Member three=new Member("M-C",0);

        manager.show();
        one.show();
        two.show();
        three.show();
        System.out.println("=============");

        ArrayList<Integer> redList=manager.send(20,3);
        one.receive(redList);
        two.receive(redList);
        three.receive(redList);

        manager.show();
        one.show();
        two.show();
        three.show();

    }
}
