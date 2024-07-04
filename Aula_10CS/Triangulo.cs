class Triangulo {
    private double b = 0;
    private double h = 0;
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
        return b * h / 2;
    }
}        