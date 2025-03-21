# IDENTIFICAÇÃO DO ESTUDANTE:
# Preencha seus dados e leia a declaração de honestidade abaixo. NÃO APAGUE
# nenhuma linha deste comentário de seu código!
#
#    Nome completo: Pedro Henrique Novelli Soares
#    Matrícula: 202306364
#    Turma: CC3MB
#    Email: pedronovelli14@gmail.com
#
# DECLARAÇÃO DE HONESTIDADE ACADÊMICA:
# Eu afirmo que o código abaixo foi de minha autoria. Também afirmo que não
# pratiquei nenhuma forma de "cola" ou "plágio" na elaboração do programa,
# e que não violei nenhuma das normas de integridade acadêmica da disciplina.
# Estou ciente de que todo código enviado será verificado automaticamente
# contra plágio e que caso eu tenha praticado qualquer atividade proibida
# conforme as normas da disciplina, estou sujeito à penalidades conforme
# definidas pelo professor da disciplina e/ou instituição.


# Imports permitidos (não utilize nenhum outro import!):
import sys
import math
import base64
import tkinter
from io import BytesIO
from PIL import Image as PILImage


# Classe Imagem:
class Imagem:
    def __init__(self, largura, altura, pixels):                              # Função disponibilizada pelo professor.

        self.largura = largura
        self.altura = altura
        self.pixels = pixels

    def correlacao(self, valorkernel):
        resultCorr = Imagem.nova(self.largura, self.altura)                   # Ao invés de alterar a imagem existente, criaremos uma imagem nova.
        for x in range(0, resultCorr.largura):                                # É acessado o eixo x de Pixels da Imagem Oferecida, a largura.
            for y in range(0, resultCorr.altura):                             # É acessado o eixo y de Pixels da Imagem Oferecida, a altura.
                volta = self.pegar_em_volta(len(valorkernel), x, y)           # A partir do pixel central, é criado uma matriz auxiliar com o mesmo tamanho do Kernel.
                soma = 0                                                      # É inicializado a variável soma com valor 0.
                for i in range(0, len(valorkernel)):                          # É acessado o Kernel Final de eixo i.
                    for j in range(0, len(valorkernel[0])):                   # É acessado o Kernel Final de eixo j, com o primeiro vetor Kernel, já que valor Kernel é Matriz.
                        soma += volta[i][j] * valorkernel[i][j]               # É realizado o Cáculo Fornecido com a variável soma do Kernel com a Auxiliar.
                resultCorr.set_pixel(x, y, round(soma))                       # É aplicado o Cáculo da Correlação na nova imagem.
        return resultCorr                                                     # É retornado a imagem correlacionada.

    def pegar_em_volta(self, tamanho, x, y):                           # Esta função serve para pegar cada pixel em volta.
        aux = []                                                       # É inicializado uma variável auxiliar iniciado como lista.
        valor = math.floor(tamanho / 2)                                # Aplicado Kernel para Diferentes tamanhos: O tamanho do Kernel é dividido por 2.
        inicio, fim = -valor, valor+1                                  # O valor do Kernel é iniciado por -x e irá até abaixo de x+1.
        for i in range(inicio, fim):                                   # É criado o eixo x para a matriz de mesmo tamanho do Kernel Intermediário.
            aux.append([])                                             # É colocado blocos de memória no eixo x, aplicando outras listas nela inicialmente.
            for j in range(inicio, fim):                               # É criado o eixo y para a matriz de mesmo tamanho do Kernel Intermediário.
                aux[i-inicio].append(self.get_pixel(x+i, y+j))         # É acessado cada linha da matriz, o início sempre será negativo, logo deverá ser tratado, e então é aplicado os pixels.
        return aux                                                     # É retornado a matrix auxiliar para a Correlação.

    def get_pixel(self, x, y):                                         # É feito uma correção para os valores do Kernel não quebrarem ao serem acessados.
        if x < 0:
            x = 0
        elif x >= self.largura:                                        # Se o pixel for maior ou igual que a largura, ele será definido como -1 em relação ao valor de largura.
            x = self.largura - 1
        if y < 0:
            y = 0
        elif y >= self.altura:                                         # Se o pixel for maior ou igual a altura, ele reduzirá em -1 em relação ao valor de altura.
            y = self.altura - 1
        i = y * self.largura + x                                       # Conversão de Matriz para Array.
        return self.pixels[i]                                          # É passado o valor i da Conversão, agora como Array.

    def set_pixel(self, x, y, c):
        i = y * self.largura + x                                       # Conversão de Matriz para Array.
        self.pixels[i] = c                                             # É passado o valor i da Conversão.

    def aplicar_por_pixel(self, func):                                 # Função disponibilizada pelo professor, só me preocupei em corrigir ela.
        resultado = Imagem.nova(self.largura, self.altura)             # Alterado o Largura e Altura coforme o acesso do eixo X e Y.
        for x in range(resultado.largura):
                                                                       # Removidos o y e o nova cor ao colocar o resultado.set_pixel no loop for
            for y in range(resultado.altura):
                cor = self.get_pixel(x, y)
                nova_cor = func(cor)
                resultado.set_pixel(x, y, nova_cor)                    # X e Y estavam invertidos e a linha estava fora do loop for.
        return resultado

    def invertida(self):                                               # Função disponibilizada pelo professor, só me preocupei em corrigir ela.
        return self.aplicar_por_pixel(lambda c: 255 - c)               # É corrigido a função de 256 para 255

    def borrada(self, n):
        matrizBorrada = []                                             # A matrizBorrada é inicializada como lista.
        numeroFinal = 1 / pow(n, 2)                                    # O cálculo do número final é aplicado, de acordo com a fórmula.
        for x in range(0, n):                                          # É acessado o eixo X da matriz.
            matrizBorrada.append([])                                   # O eixo X da matriz é preenchido com uma lista.
            for y in range(0, n):                                      # É acessado o eixo Y da matriz.
                matrizBorrada[x].append(numeroFinal)                   # A matriz é preenchida a partir do eixo X com o resultado do número final.
        return self.correlacao(matrizBorrada)                          # É retornado a imagem alterada, não nova, mas borrada.

    def focada(self, n):
        resultado = Imagem.nova(self.largura, self.altura)                                                     # O retorno da matriz é inicializado, uma imagem de mesma altura e largura.
        imagem_borrada = self.borrada(n)                                                                       # É inicializado uma variável de correlação, com base no Kernel da Matriz Borrada.
        for x in range(0, self.largura):                                                                       # É acessado o eixo X da matriz.
            for y in range(0, self.altura):                                                                    # É acessado o eixo Y da matriz.
                calculo = (2 * self.get_pixel(x, y) - imagem_borrada.get_pixel(x, y))                          # É feito o cálculo da imagem focada, de acordo com a fórmula.
                calculo = self.tratarnumero(calculo)                                                           # Há a chance do número quebrar, então é feito um tratamento de erro para isso.
                resultado.set_pixel(x, y, calculo)                                                             # O resultado é aplicado no eixo X e Y dos pixels da imagem.
        return resultado                                                                                       # É retornado uma imagem nova focada.

    def tratarnumero(self, numero):                                    # Um simples tratamento de erro.
        numerotratado = min(max(numero, 0), 255)                       # O número deve ser no máximo 255 e no mínimo 0
        return numerotratado                                           # O número tratado é retornado.

    def bordas(self):
        resultado = Imagem.nova(self.largura, self.altura)             # É criado uma imagem nova, que será o resultado.
        kx = [                                                         # O Kernel x oferecido é criado.
            [-1, 0, 1],
            [-2, 0, 2],
            [-1, 0, 1],
         ]
        ky = [                                                         # O Kernel y oferecido é criado.
            [-1, -2, -1],
            [0, 0, 0],
            [1, 2, 1],
        ]
        ox = self.correlacao(kx)                                                                                    # É feito a correlação da imagem com o Kernel X.
        ox.mostrar()                                                                                                # Conforme a atividade 6, é exibido o kernel OX.
        oy = self.correlacao(ky)                                                                                    # É feito a correlação da imagem com o Kernel Y.
        oy.mostrar()                                                                                                # Conforme a atividade 6, é exibido o kernel OY.
        for x in range(0, self.largura):                                                                            # É acessado o eixo x da imagem;
            for y in range(0, self.altura):                                                                         # É acessado o eixo y da imagem;
                correlacionar = round(math.sqrt(pow(ox.get_pixel(x, y), 2) + pow(oy.get_pixel(x, y), 2)))           # É feito uma correlação, de acordo com o cálculo oferecido.
                correlacionar = self.tratarnumero(correlacionar)                                                    # O resultado é tratado.
                resultado.set_pixel(x, y, correlacionar)                                                            # O pixel é colocado na nova imagem.
        return resultado                                                                                            # É retornado uma imagem nova com detecção de bordas.

    # Abaixo deste ponto estão utilitários para carregar, salvar e mostrar
    # as imagens, bem como para a realização de testes. Você deve ler as funções
    # abaixo para entendê-las e verificar como funcionam, mas você não deve
    # alterar nada abaixo deste comentário.
    #
    # ATENÇÃO: NÃO ALTERE NADA A PARTIR DESTE PONTO!!! Você pode, no final
    # deste arquivo, acrescentar códigos dentro da condicional
    #
    #                 if __name__ == '__main__'
    #
    # para executar testes e experiências enquanto você estiver executando o
    # arquivo diretamente, mas que não serão executados quando este arquivo
    # for importado pela suíte de teste e avaliação.
    def __eq__(self, other):
        return all(getattr(self, i) == getattr(other, i)
                   for i in ('altura', 'largura', 'pixels'))

    def __repr__(self):
        return "Imagem(%s, %s, %s)" % (self.largura, self.altura, self.pixels)

    @classmethod
    def carregar(cls, nome_arquivo):
        """
        Carrega uma imagem do arquivo fornecido e retorna uma instância dessa
        classe representando essa imagem. Também realiza a conversão para tons
        de cinza.

        Invocado como, por exemplo:
           i = Imagem.carregar('test_images/cat.png')
        """
        with open(nome_arquivo, 'rb') as guia_para_imagem:
            img = PILImage.open(guia_para_imagem)
            img_data = img.getdata()
            if img.mode.startswith('RGB'):
                pixels = [round(.299 * p[0] + .587 * p[1] + .114 * p[2]) for p in img_data]
            elif img.mode == 'LA':
                pixels = [p[0] for p in img_data]
            elif img.mode == 'L':
                pixels = list(img_data)
            else:
                raise ValueError('Modo de imagem não suportado: %r' % img.mode)
            l, a = img.size
            return cls(l, a, pixels)

    @classmethod
    def nova(cls, largura, altura):
        """
        Cria imagens em branco (tudo 0) com a altura e largura fornecidas.

        Invocado como, por exemplo:
            i = Imagem.nova(640, 480)
        """
        return cls(largura, altura, [0 for i in range(largura * altura)])

    def salvar(self, nome_arquivo, modo='PNG'):
        """
        Salva a imagem fornecida no disco ou em um objeto semelhante a um arquivo.
        Se o nome_arquivo for fornecido como uma string, o tipo de arquivo será
        inferido a partir do nome fornecido. Se nome_arquivo for fornecido como
        um objeto semelhante a um arquivo, o tipo de arquivo será determinado
        pelo parâmetro 'modo'.
        """
        saida = PILImage.new(mode='L', size=(self.largura, self.altura))
        saida.putdata(self.pixels)
        if isinstance(nome_arquivo, str):
            saida.save(nome_arquivo)
        else:
            saida.save(nome_arquivo, modo)
        saida.close()

    def gif_data(self):
        """
        Retorna uma string codificada em base 64, contendo a imagem
        fornecida, como uma imagem GIF.

        Função utilitária para tornar show_image um pouco mais limpo.
        """
        buffer = BytesIO()
        self.salvar(buffer, modo='GIF')
        return base64.b64encode(buffer.getvalue())

    def mostrar(self):
        """
        Mostra uma imagem em uma nova janela Tk.
        """
        global WINDOWS_OPENED
        if tk_root is None:
            # Se Tk não foi inicializado corretamente, não faz mais nada.
            return
        WINDOWS_OPENED = True
        toplevel = tkinter.Toplevel()
        # O highlightthickness=0 é um hack para evitar que o redimensionamento da janela
        # dispare outro evento de redimensionamento (causando um loop infinito de
        # redimensionamento). Para maiores informações, ver:
        # https://stackoverflow.com/questions/22838255/tkinter-canvas-resizing-automatically
        tela = tkinter.Canvas(toplevel, height=self.altura,
                              width=self.largura, highlightthickness=0)
        tela.pack()
        tela.img = tkinter.PhotoImage(data=self.gif_data())
        tela.create_image(0, 0, image=tela.img, anchor=tkinter.NW)

        def ao_redimensionar(event):
            # Lida com o redimensionamento da imagem quando a tela é redimensionada.
            # O procedimento é:
            #  * converter para uma imagem PIL
            #  * redimensionar aquela imagem
            #  * obter os dados GIF codificados em base 64 (base64-encoded GIF data)
            #    a partir da imagem redimensionada
            #  * colocar isso em um label tkinter
            #  * mostrar a imagem na tela
            nova_imagem = PILImage.new(mode='L', size=(self.largura, self.altura))
            nova_imagem.putdata(self.pixels)
            nova_imagem = nova_imagem.resize((event.width, event.height), PILImage.NEAREST)
            buffer = BytesIO()
            nova_imagem.save(buffer, 'GIF')
            tela.img = tkinter.PhotoImage(data=base64.b64encode(buffer.getvalue()))
            tela.configure(height=event.height, width=event.width)
            tela.create_image(0, 0, image=tela.img, anchor=tkinter.NW)

        # Por fim, faz o bind da função para que ela seja chamada quando a tela
        # for redimensionada:
        tela.bind('<Configure>', ao_redimensionar)
        toplevel.bind('<Configure>', lambda e: tela.configure(height=e.height, width=e.width))

        # Quando a tela é fechada, o programa deve parar
        toplevel.protocol('WM_DELETE_WINDOW', tk_root.destroy)


# Não altere o comentário abaixo:
# noinspection PyBroadException
try:
    tk_root = tkinter.Tk()
    tk_root.withdraw()
    tcl = tkinter.Tcl()


    def refaz_apos():
        tcl.after(500, refaz_apos)


    tcl.after(500, refaz_apos)
except:
    tk_root = None

WINDOWS_OPENED = False

if __name__ == '__main__':
    # O código neste bloco só será executado quando você executar
    # explicitamente seu script e não quando os testes estiverem
    # sendo executados. Este é um bom lugar para gerar imagens, etc.
    pass
    # A partir deste ponto, o código é iniciado.

    # Questão 2:

    # imagem = Imagem.carregar('test_images/bluegill.png')          # É carregado a imagem solicitada.
    # imagem.invertida().salvar('resultados/bluegill.png')          # É salvo a imagem solicitada.
    # imagem.mostrar()                                              # É mostrado a imagem solicitada.

    # Questão 4:

    # kernel = [                                                    # É criado o Kernel, conforme solicitado.
    #    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    #    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    # ]
    # imagem = Imagem.carregar('test_images/pigbird.png')           # É carregado a imagem solicitada.
    # imagem.correlacao(kernel).salvar('resultados/pigbird.png')    # É salvo a imagem solicitada com o kernel criado.

    # Desfoque 5.1

    # imagem = Imagem.carregar('test_images/cat.png')               # É carregado a imagem solicitada.
    # imagem.borrada(5).salvar('resultados/cat.png')                # É salvo a imagem solicitada, borrada com kernel 5.

    # Questão 05

    # imagemFocada = Imagem.carregar('test_images/python.png')      # É carregado a imagem solicitada.
    # imagemFocada.focada(11).salvar('resultados/python.png')       # É salvo a imagem solicidade, focada com kernel 5.

    # Questão 06

    # imagemBorda = Imagem.carregar('test_images/construct.png')    # É carregado a imagem solicitada.
    # imagemBorda.mostrar()                                         # É mostrado a imagem original.
    # imagemBorda.bordas().salvar('resultados/construct.png')       # É salvo a imagem com deteção de borda.

    # O código a seguir fará com que as janelas de Imagem.mostrar
    # sejam exibidas corretamente, quer estejamos a executar
    # interativamente ou não:

    if WINDOWS_OPENED and not sys.flags.interactive:
        tk_root.mainloop()