A Linguagem A é definida a partir da Linguagem C, as características da
A são:
▪ Possui apenas os tipos de dados int e string;
▪ Não possui laços de repetição;
▪ Possui a instrução if-else, tal qual a Linguagem C;
▪ Cada função da A tem no máximo dois parâmetros;
▪ As demais características são idênticas ao C, inclusive a sintaxe;


analisador semântico para a Linguagem A. O analisador semântico deve verificar:
I. Se as operações usam tipos compatíveis;
II. Se as variáveis (e funções) estão sendo usadas dentro de seu escopo; e
III. Se as variáveis (e funções) estão sendo usadas sem serem declaradas.

Entrada
A entrada é composta por um código fonte de um programa qualquer escrito em A
Saída
Para cada entrada, seu programa deve produzir uma mensagem de “Sucesso” ou um
erro semântico.
Exemplo
Entrada
int fun ( int a , int b ) {
return a + b ;
}
int main ( ) {
	int a = 3 ;
	int b = 5 ;
	int c = a + b ;
	return c + fun ( a , b ) ;
}
Saída
Sucesso
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
				EXECUTANDO COM PYTHON
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
								No terminal digite python3 e logo depois

from analisador_semantico.py import *
Em seguida teste o Analisador com Analisador()
								Ou digite python3 analisador_semantico.py **nota: para mudar o arquivo que vai execultar troque o nome em 
								lc = arquivoPraLinha('saida.txt') por lc = arquivoPraLinha('minhaENTRADA.txt') 

_____________________________________________________________________________
para executar com o jupyter notebook basta ir no terminal na pasta TRABALHO3 e digitar jupyter notebook:
no menu vá em Cell e clique em: Run All
nota: *** uma vez mudado o arquivo de entrada, repita o processo:
no menu vá em Cell e clique em: Run All
 
_____________________________________________________________________________

SITES:

Jupyter Notebook:
					http://jupyter.readthedocs.io/en/latest/install.html

Anaconda ou Miniconda:
					https://www.continuum.io/downloads

------------------------------------------------------------------------------

instalações ubuntu
					Jupyter Notebook
					pip3 install --upgrade pip
					pip3 install jupyter

Pacotes a serem instalados- 
					Pandas: pip3 install pandas
					Numpy: pip3 install numpy

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
				EXECUTANDO COM JUPYTER NOTEBOOK
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
								Rodar a célula
Vá no Menu - Cell e selecione Run cells.

	ou
Segure Ctrl e aperte ENTER na célula selecionada(Com o ícone do mouse dentro)

'irá aparecer * para indicar que está rodando, logo depois irá aparecer um número(número de controle de execução) que indicará que deu certo.'


------------------------------------------------------------------------------

								Alguns comandos úteis:

** Caso dê erro ao exportar para PDF no Jupyter, olhe o link abaixo:
http://stackoverflow.com/questions/29156653/ipython-jupyter-problems-saving-notebook-as-pdf

Ou coloque os comandos abaixo:

converter para PDF:

Exporte para PDF

jupyter nbconvert --to pdf filename.ipynb
	Ou
ipython nbconvert --to latex --post PDF MyNotebook.ipynb 


Caso aconteça algum erro instale o pacote:
sudo apt-get install texlive texlive-latex-extra pandoc

converter para .tex
ipython nbconvert --to latex MyNotebook.ipynb 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
