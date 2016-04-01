#ifndef GRAFO_H
#define GRAFO_H


#include <iostream>
#include <list>
#include <algorithm> // fun��o find
#include <stack> // pilha para usar na buscaProfundidade
#include <queue> // fila para usar na busLargura
#include "No.h"
#include <GL/glut.h>


using namespace std;

class Grafo
{
	int V; // n�mero de v�rtices
	list<No> *adj; // ponteiro para um array contendo as listas de adjac�ncias
public:
    int tamanho;
    No n[1000];
	Grafo(int V); // construtor
	void adicionarAresta(No v1, No v2); // adiciona uma aresta no grafo
	void buscaProfundidade(No v);// faz uma buscaProfundidade a partir de um v�rtice
	void buscaLargura(No v);// faz uma buscaLargura a partir de um v�rtice
	void buscaAndOr(No v, GLfloat coordena[281]);// faz uma buscaAndOr com a condi��o de par nos Ors
    void copiaArestas(No *v1);
    No buscaId(No v, int i);
};

#endif // GRAFO_H
