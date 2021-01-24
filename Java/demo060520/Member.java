package cn.itcast.demo.demo060520;

import java.util.ArrayList;
import java.util.Random;

public class Member extends User{
    public Member() {
    }

    public Member(String name, int money) {
        super(name, money);
    }
    public void receive(ArrayList<Integer> list){
        int index=new Random().nextInt(list.size());
        int money=super.getMoney();
        int delta=list.remove(index);
        super.setMoney(money+delta);

    }
}
