class Triangulo {
    private double b = 0; // Atributo ou campo
    private double h = 0;
    public Triangulo() {  // Construtor 1
    }
    public Triangulo(double b, double h) {  // Construtor 2 - Sobrecarga
        //this.b = b;
        //this.h = h;
        set_base(b);
        set_altura(h);
    }
    public void set_base(double v) {
        if (v >= 0) b = v;
        else throw new ArgumentOutOfRangeException();
    }    
    public void set_altura(double v) {
        if (v >= 0) h = v;
        else throw new ArgumentOutOfRangeException();
    }    
    public double get_base() {
        return b;
    }
    public double get_altura() {
        return h;
    }
    public double calc_area() {
        double area;       // Variável local
        area = b * h / 2;
        return area;
    }
    public override string ToString() {  // Polimorfismo
      return $"Triângulo com Base = {b}, Altura = {h}";
    }
}        