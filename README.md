## Editor de Imagem em Python
Este trabalho, realizado em meados de Março de 2024 é basicamente um programa que aplica diversos filtros em imagens a partir do Kernel que informamos para ele, filtros estes como inversão, desfoque, correlação, nitidez e detecção de borda, este trabalho foi aplicado pelo professor Abrantes Araújo que deu toda a base para nós fazermos o mesmo, cada linha do código está comentada para o seu entendimento, e na main nós temos alguns exemplos, além de algumas questões sobre o trabalho, partes das questões estas que dissertarei aqui:

Gostaria também de, antes mostrar as questões e desafios do código, eu não poderia ter concluído graças a uma mulher trans que serviu como monitora em todo meu trabalho, esta é a Sarah Visconsini, uma grande amiga minha que, gostaria, e vou, dedicar esse código a ela.
## QUESTÃO: Execute seu filtro de inversão na imagem test_images/bluegill.png, salve o resultado como uma imagem PNG e salve a imagem
imagem = Imagem.carregar('test_images/bluegill.png')          - Aqui é carregado a imagem solicitada.
imagem.invertida().salvar('resultados/bluegill.png')          - Aqui é salvo a imagem solicitada.
imagem.mostrar()  
## QUESTÃO: Qual será o valor do pixel na imagem de saída no local indicado pelo destaque vermelho? Observe que neste ponto ainda não arredondamos ou recortamos o valor, informe exatamente como você calculou.
O valor indicado pelo destaque será 32.76, o cálculo feito será:
0.00 × 80 + 53 × (-0.07) + 99 × 0.00 + 129 × (-0.45) + 127 x 1.20 + 148 × (-0.25) + 175 × 0.00 + 174 × (-0.12) + 193 × 0.00 = 0-3.710-58.05+152.4 - 37+0-20.88 +0 = 
32.76
## QUESTÃO: Quando você tiver implementado seu código, tente executá-lo em test_images/pigbird.png com o seguinte kernel 9×9:
O Kernel resultante é: 
kernel = [                                                 
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
]
## QUESTÃO: Se quisermos usar uma versão desfocada B que foi feita com um kernel de desfoque de caixa de 3 × 3, que kernel k poderíamos usar para calcular toda a imagem nítida com uma única correlação? Justifique sua resposta mostrando os cálculos.
Ao utilizar um Kernel de Desfoque 3x3 poderíamos utilizar a seguinte formula:
X+X+X
X+X+X
x+x+x=1
9x=1
x=1/9
x = 0.1
Com uma única correlação, o cálculo será:
x = 1/n^2
Sendo N o tamanho do Kernel e
X o valor que somado resultaria em 1.
## QUESTÃO: Implemente uma máscara de não nitidez como o método focada da classe Imagem, onde n denota o tamanho do kernel de desfoque que deve ser usado para gerar a cópia desfocada da imagem.
imagem = Imagem.carregar('test_images/cat.png')               # É carregado a imagem solicitada.
imagem.borrada(5).salvar('resultados/cat.png')                # É salvo a imagem solicitada, borrada com kernel 5.
