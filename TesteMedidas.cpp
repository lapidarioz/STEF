#include "MedidasBase.h"

/*------------------ Derived class TesteMedidas from MedidasBase ------------------*/
class TesteMedidas: public MedidasBase{
    public:
        void imprimeAlpha(){
        for(int i2=0;i2<46;i2++){
                cout << alphas[i2] << "\n";
            }
        }
        void lerAlphas(int emotion){

            ifstream infilestream;
            string line;
            string line2;
            float n;
            int i=0;
            if (emotion==1) infilestream.open("1_Alfas_Neutra_Satisfa��o.txt");
            if (emotion==2) infilestream.open("2_Alfas_Neutra_Tristeza.txt");
            if (emotion==3) infilestream.open("3_Alfas_Neutra_Surpresa.txt");
            if (emotion==4) infilestream.open("4_Alfas_Neutra_Medo.txt");
            if (emotion==5) infilestream.open("5_Alfas_Neutra_Raiva.txt");
            if (emotion==6) infilestream.open("6_Alfas_Neutra_Aversao.txt");
            for(int x=0;x<5;x++){
                infilestream >> line;
            }
            //SEsquerda
            for(int x=0;x<3;x++){
                infilestream >> line;
            }
            for(int x=0;x<6;x++){
                infilestream >> line;
                infilestream >> line;
                infilestream >> n;
                alphas[i++]=n;
            }
            //SDireita
            for(int x=0;x<3;x++){
                infilestream >> line;
            }
            for(int x=0;x<6;x++){
                infilestream >> line;
                infilestream >> line;
                infilestream >> n;
                alphas[i++]=n;
            }
            //Oesquerdo
            for(int x=0;x<3;x++){
                infilestream >> line;
            }
            for(int x=0;x<8;x++){
                infilestream >> line;
                infilestream >> line;
                infilestream >> n;
                alphas[i++]=n;
            }
             //Odireito
            for(int x=0;x<3;x++){
                infilestream >> line;
            }
            for(int x=0;x<8;x++){
                infilestream >> line;
                infilestream >> line;
                infilestream >> n;
                alphas[i++]=n;
            }
            //Nariz
            for(int x=0;x<2;x++){
                infilestream >> line;
            }
            for(int x=0;x<10;x++){
                infilestream >> line;
                infilestream >> line;
                infilestream >> n;
                alphas[i++]=n;
            }

            //Boca
            for(int x=0;x<2;x++){
                infilestream >> line;
            }
            for(int x=0;x<8;x++){
                infilestream >> line;
                infilestream >> line;
                infilestream >> n;
                alphas[i++]=n;
            }
            infilestream.close();
        }
/*----------------------------------------------------*/

        Grafo lerGrafo(){
            Grafo grafo(1000);
            ifstream infilestream;
            string line;
            //N
            int tipo;
            string id;
            //R
            int no1;
            int no2;
            int i=0;
            infilestream.open("grafo2.txt");
            while (infilestream) {
                infilestream >> line;
                if(line=="N") {
                        infilestream >> tipo;
                        infilestream >> id;
                        criaNo(tipo,id, &grafo);
                }
                if(line=="R") {
                        infilestream >> no1;
                        infilestream >> no2;
                        criaRelacaoBin(no1, no2, &grafo);
                }
            }
            cont=0;
            infilestream.close();
            return grafo;
            //grafo.buscaAndOr(grafo.n[0]);
        }
/*----------------------------------------------------*/

        void criaNo(int tipo,string valor, Grafo *g){
            //printf("[[criando no %i]]\n", cont);
            No n0(tipo,cont,valor,0);
            g->n[cont]=n0;
            cont++;
        }

        void criaRelacaoBin(int pai,int filho,Grafo * g){
            //printf("[[criando aresta]]\n");
            g->adicionarAresta(g->n[pai],g->n[filho]);
            g->copiaArestas(&g->n[pai]);
        }
};

