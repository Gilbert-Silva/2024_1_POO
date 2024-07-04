#include <iostream>
#include <stdexcept>

using namespace std;

class Triangulo {
    private:
        double b = 0;
        double h = 0;
    public:
        void set_base(double v) {
            if (v >= 0) b = v;
            else throw invalid_argument("");
        }    
        void set_altura(double v) {
            if (v >= 0) h = v;
            else throw invalid_argument("");
        }    
        double get_base() {
            return b;
        }
        double get_altura() {
            return h;
        }
        double calc_area() {
            return b * h / 2;
        }
};

int main()
{
    Triangulo x;
    cout << "Digite o valor da base: " << endl;
    double v;
    cin >> v;
    x.set_base(v);
    cout << "Digite o valor da altura: ";
    cin >> v;
    x.set_altura(v);
    cout << "Um triângulo de base " << x.get_base() << " e altura " << x.get_altura() << endl;
    cout << "tem área = " << x.calc_area() << endl;
    return 0;
}
