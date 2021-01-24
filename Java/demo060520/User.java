package cn.itcast.demo.demo060520;

public class User {
    private String name;//users' name
    private int money;//how much money you have

    public User() {
    }

    public User(String name, int money) {
        this.name = name;
        this.money = money;
    }
    public void show(){
        System.out.println("My name is:"+name+",How much money i have:"+money);
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getMoney() {
        return money;
    }

    public void setMoney(int money) {
        this.money = money;
    }
}
