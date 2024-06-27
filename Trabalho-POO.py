class Jogo:
    def __init__(self, id, titulo, preco):
        self.id = id
        self.titulo = titulo
        self.preco = preco

    def __str__(self):
        return f"{self.titulo} - R${self.preco}"


class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def __str__(self):
        return self.nome


class ItemPedido:
    def __init__(self, jogo, quantidade):
        self.jogo = jogo
        self.quantidade = quantidade

    def obter_preco_total(self):
        return self.jogo.preco * self.quantidade

    def __str__(self):
        return f"{self.quantidade} x {self.jogo.titulo} - R${self.obter_preco_total()}"


class Pedido:
    def __init__(self, id, cliente):
        self.id = id
        self.cliente = cliente
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def obter_valor_total(self):
        total = sum(item.obter_preco_total() for item in self.itens)
        return total

    def __str__(self):
        itens_str = "\n".join(str(item) for item in self.itens)
        return f"Pedido #{self.id} para {self.cliente.nome}:\n{itens_str}\nTotal: R${self.obter_valor_total()}"


class Loja:
    def __init__(self, nome):
        self.nome = nome
        self.jogos = []
        self.clientes = []
        self.pedidos = []

    def adicionar_jogo(self, jogo):
        self.jogos.append(jogo)

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def criar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def __str__(self):
        jogos_str = "\n".join(str(jogo) for jogo in self.jogos)
        clientes_str = "\n".join(str(cliente) for cliente in self.clientes)
        return f"Loja: {self.nome}\nJogos:\n{jogos_str}\nClientes:\n{clientes_str}"


# Criar uma loja
loja = Loja("Jogos Incríveis")

# Adicionar jogos à loja
jogo1 = Jogo(1, "The Legend of Zelda", 59.99)
jogo2 = Jogo(2, "Super Mario Odyssey", 49.99)
jogo3 = Jogo(3, "Minecraft", 19.99)

loja.adicionar_jogo(jogo1)
loja.adicionar_jogo(jogo2)
loja.adicionar_jogo(jogo3)

# Adicionar clientes à loja
cliente1 = Cliente(1, "João Silva")
cliente2 = Cliente(2, "Maria Souza")

loja.adicionar_cliente(cliente1)
loja.adicionar_cliente(cliente2)

# Criar um pedido
pedido1 = Pedido(1, cliente1)
item_pedido1 = ItemPedido(jogo1, 2)  # 2 unidades de The Legend of Zelda
item_pedido2 = ItemPedido(jogo3, 1)  # 1 unidade de Minecraft

pedido1.adicionar_item(item_pedido1)
pedido1.adicionar_item(item_pedido2)

loja.criar_pedido(pedido1)

# Exibir o estado atual da loja
print(loja)

# Exibir o pedido
print(pedido1)