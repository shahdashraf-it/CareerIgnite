// Online Java Compiler
// Use this editor to write, compile and run your Java code online
import java.util.Scanner;
class Car {
    private String maker;
    private int model;
    public void setmaker(String m) {
    maker=m;
    }
    public void setmodel(int year ){
        model=year;
    }
     public String getmaker( ){
        return maker;
    }
      public int getmodel( ){
        return model;
    }
class Main {
    public static void main(String[] args) {
     Scanner input = new Scanner(System.in);
    Car c1=new Car();
    
           c1.setmaker("hondaa");
           c1.setmodel(2017);


    }

    
}

