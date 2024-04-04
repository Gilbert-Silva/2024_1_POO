namespace Ex02CS;

class Program  // Nome da classe não importa nesse exemplo
{
    static void Main(string[] args) // Método principal é o executado primeiro
    {
        Item a = new Item("Biscoito", 5, 2.5);  // Variáveis locais
        Item b = new Item("Maça", 10, 2);
        Item c = new Item("Laranja", 5, 1);
        Item d = c;                             // Duas referências para um mesmo objeto
        //Console.WriteLine(a.ToString());
        //Console.WriteLine(a.total());
        //Console.WriteLine(b);
        //Console.WriteLine(b.total());
        //Console.WriteLine(c);
        //Console.WriteLine(c.total());

        Carrinho carrinho = new Carrinho("Jorgiano", "03/04/2024");
        carrinho.inserir(a);
        carrinho.inserir(b);
        carrinho.inserir(c);
        carrinho.remover(a);
        Console.WriteLine(carrinho);
        foreach (Item item in carrinho.listar())
             Console.WriteLine(item);
        Console.WriteLine(carrinho.total());
    }
}

class Item : Object {
    private string produto;  // Declaração de atributos
    private int qtd;
    private double preco_unit;
    public Item(string prod, int qtd, double preco) { // Construtor
        this.produto = prod;
        this.qtd = qtd;
        this.preco_unit = preco;
        if (prod == "") throw new ArgumentOutOfRangeException();
        if (qtd <= 0) throw new ArgumentOutOfRangeException();
        if (preco <= 0) throw new ArgumentOutOfRangeException();
    }    
    public void set_produto(string prod) {
        this.produto = prod;
        if (prod == "") throw new ArgumentOutOfRangeException();
    }
    public void set_qtd(int qtd) {
        this.qtd = qtd;
        if (qtd <= 0) throw new ArgumentOutOfRangeException();
    }
    public void set_preco(double preco) {
        this.preco_unit = preco;
        if (preco <= 0) throw new ArgumentOutOfRangeException();
    }    
    public string get_produto() {
        return this.produto;
    }
    public int get_qtd() {
        return this.qtd;
    }
    public double get_preco() {
        return this.preco_unit;
    }
    public double total() {
        return this.qtd * this.preco_unit;
    }
    public override string ToString() {  // ToString herdado é modificado -> Polimorfismo
        return $"{this.produto} {this.qtd} {this.preco_unit}";
    }
}

class Carrinho {
    private string cliente;
    private string data;
    private List<Item> itens = new List<Item>();
    public Carrinho(string c, string d) { 
        this.cliente = c;
        this.data = d;
        if (c == "") throw new ArgumentOutOfRangeException();
    }
    public void inserir(Item item) {
        this.itens.Add(item);
    }
    public void remover(Item item) {
        this.itens.Remove(item);
    }
    public List<Item> listar() {
        return this.itens;
    }
    public double total() {
        double t = 0;
        foreach (Item item in this.itens)
            t += item.total();    
        return t;
    }
    public override string ToString() {
        return $"{this.cliente} {this.data} {this.itens.Count} item(s)";
    }
}
                                          // len(self.__itens)


