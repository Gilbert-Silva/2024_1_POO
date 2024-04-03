using System.Globalization;

Console.WriteLine("Hello, World!");   // print("Hello, World!")
int x = 10;                           // x = 10
double y = 5.5;                       // y = 5.5
char c = 'A';                         // Python não tem char
string s = "POO";                     // s = "POO"
bool b = true;                        // b = True
Console.WriteLine(x); 
Console.WriteLine(y);
Console.WriteLine(c);
Console.WriteLine(s);
Console.WriteLine(b);

Console.WriteLine("Digite seu nome");              // print("Digite seu nome")
string? nome = Console.ReadLine();                 // nome = input()
Console.WriteLine($"Bem-vindo(a) ao C#, {nome}");  // print(f"Bem-vindo(a) ao C#, {nome}")  

Console.WriteLine("Digite um inteiro");            // print("Digite um inteiro")
int k = int.Parse(Console.ReadLine());             // k = int(input())
if (k >= 0 && k <= 10) {                           // if k >= 0 and k <= 10:
    Console.WriteLine("Valor está entre 0 e 10");
} 
else {
    Console.WriteLine("Valor não está entre 0 e 10");
}

for (int j = 1; j <= 10; j++) {                    // for j in range(1, 11):
    Console.WriteLine(j);
}

int l = 1;                                        // l = 1
while (l <= 10) {                                 // while l <= 10:
    Console.WriteLine(l);
    l++;
}

s = "Programação em C#";                          // s = "Programação em C#" 
foreach (char letra in s)                         // for letra in s:
    Console.WriteLine(letra);                     //     print(letra)

// Parâmetro de tipo 
List<int> lista = new List<int>();                // lista = []
lista.Add(10);                                    // lista.append(10)
lista.Add(20);
lista.Add(30);
foreach (int i in lista)                          // for i in lista:
  Console.WriteLine(i);                           //     print(i)

  



  


