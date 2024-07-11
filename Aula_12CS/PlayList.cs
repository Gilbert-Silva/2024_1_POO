class PlayList {
    private string nome;
    private List<Musica> musicas = new List<Musica>(); 
    public void SetNome(string nome) {
        this.nome = nome;
    }
    public string GetNome() {
        return this.nome;
    }
    public void Inserir(Musica musica) {
        this.musicas.Add(musica);
    }
    public List<Musica> Listar() {
        return this.musicas;
    }
}