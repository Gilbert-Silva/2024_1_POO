import java.util.Scanner;

public class Program
{
    public static void main(String[] args)
    {
        Triangulo x = new Triangulo();
        System.out.println("Digite o valor da base: ");
        Scanner sc = new Scanner(System.in);
        x.set_base(sc.nextDouble());
        System.out.println("Digite o valor da altura: ");
        x.set_altura(sc.nextDouble());
        System.out.println(String.format("Um triângulo de base %f e altura %f", x.get_base(), x.get_altura()));
        System.out.println(String.format("tem área = %f", x.calc_area()));
        sc.close();
    }
}

class Triangulo {
    private double b = 0;
    private double h = 0;
    public void set_base(double v) {
        if (v >= 0) b = v;
        else throw new IllegalArgumentException();
    }    
    public void set_altura(double v) {
        if (v >= 0) h = v;
        else throw new IllegalArgumentException();
    }    
    public double get_base() {
        return b;
    }
    public double get_altura() {
        return h;
    }
    public double calc_area() {
        return b * h / 2;
    }
}
