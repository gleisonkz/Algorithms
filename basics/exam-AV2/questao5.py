class Produto:
    produtoID = None
    descricao = None
    custo = None

    def __init__(self, produtoID, descricao, custo):
        self.produtoID = produtoID
        self.descricao = descricao
        self.custo = custo


class AlbumMusica(Produto):
    artista = None
    nomeAlbum = None
    faixaExecucao = None

    def __init__(self, produtoID, descricao, custo, artista, nomeAlbum, faixaExecucao):
        super().__init__(produtoID, descricao, custo)
        self.artista = artista
        self.nomeAlbum = nomeAlbum
        self.faixaExecucao = faixaExecucao


class Livro(Produto):
    autor = None
    titulo = None
    isbn = None

    def __init__(self, produtoID, descricao, custo, autor, titulo, isbn):
        super().__init__(produtoID, descricao, custo)
        self.autor = autor
        self.titulo = titulo
        self.isbn = isbn
