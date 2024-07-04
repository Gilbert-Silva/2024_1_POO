namespace Aula_10CS;

class Program
{
    static void Main(string[] args)
    {
        Triangulo x = new Triangulo();
        Console.WriteLine("Digite o valor da base: ");
        x.set_base(double.Parse(Console.ReadLine()));
        Console.WriteLine("Digite o valor da altura: ");
        x.set_altura(double.Parse(Console.ReadLine()));
        Console.WriteLine($"Um triângulo de base {x.get_base()} e altura {x.get_altura()}");
        Console.WriteLine($"tem área = {x.calc_area()}");
    }
}

