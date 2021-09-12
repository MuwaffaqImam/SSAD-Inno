package com.moofiyTv.mossapp.LSP_IS.wrong;


// liskov princible the parent and the child can be relacable
public class Duck implements Birds {
    @Override
    public void fly() {
        System.out.println("Flying...");
    }

    @Override
    public void eat() {
        System.out.println("eating");
    }

    @Override
    public void layEggs() {
        System.out.println("laying eggs");
    }

    @Override
    public void swim() {
        throw new AssertionError("I Can swim");
    }
}
