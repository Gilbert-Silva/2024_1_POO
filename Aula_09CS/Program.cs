// See https://aka.ms/new-console-template for more information
// Console.WriteLine("Hello, World!");            // print("Hello, World!")

Triangulo x = new Triangulo();                     // x = Triangulo()
Console.WriteLine(x);                              // print(x)
Console.WriteLine(x.CalcArea());                   // print(x.calc_area())
Console.WriteLine("Informe o valor da base: ");
x.b = double.Parse(Console.ReadLine());            // x.b = float(input())
Console.WriteLine("Informe o valor da altura: ");
x.h = double.Parse(Console.ReadLine());
Console.WriteLine(x.CalcArea());
