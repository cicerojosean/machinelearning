//#include <boost/assign/std/vector.hpp>
#include <iostream>
#include <set>
#include <queue>
#include <vector>
#include <hash_set>

#include <list>
#include <vector>

using namespace std;
using __gnu_cxx::hash_set;
//necessário para inicialização de vectors

//using namespace boost::assign;
using namespace std;
class State {

   public:
    /*
     * o estado fornece a posição de cada veículo, utilizando a seguinte convenção :
     * para um veículo horizontal é a coluna da casa mais à esquerda
     * para um veículo vertical é a coluna da casa mais acima
     * (lembrete: a coluna mais à esquerda é 0, e a linha mais alta é 0)
     */
    vector<int> pos;  //posicao de cada veiculo

    /* nós guardamos qual o deslocamento levou a este estado */

    int c;  //c é o veículo
    int d;   //d é o deslocamento
    //d=-1 indica um deslocamento para a esquerda ou para cima,
    //d=+1 indica um deslocamento para a direita ou para baixo)
    State* prev;

    /* constrói um estado inicial (c e d recebem qualquer valor = lixo) */
    State(vector<int>& p) {
        //pos = new int[p.size()];
        int tam = p.size();
        for (int i = 0; i < tam; i++)
            pos.push_back(p[i]);
        prev = NULL;
    }

    /* constrói um estado obtido a partir de s deslocando-se o veículo c de d (-1 ou +1)  */
    State(State* s, int c, int d) {
        // A SER COMPLETADO
        this->prev=s;
        this->c=c;
        this->d=d;
        this->pos=s->pos;
        this->pos[c]=this->pos[c]+d;

    }

    // nós ganhamos?
    bool success() {
        // A SER COMPLETADO
        if(this->pos[0]==4){
        return true;
        }
        return false;

    }

    bool equals(State* s) {
        if (s->pos.size() != pos.size()){
            cerr << "Estados de comprimento diferentes" << endl;
            exit(1);
        }
        int tamanho = pos.size();

        for (int i = 0; i < tamanho; i++)
            if (pos[i] != s->pos[i]) return false;
        return true;
    }


};

//necessário para uso de hash_set

//função hash
struct hash_state
{
   size_t operator()(const State* t) const
   {
     int h = 0;

     for (int i = 0; i < t->pos.size(); i++)
            h = 37 * h + t->pos[i];

     return h;
   }
};

//função igualdade para hash_set
struct eq_state
{
   bool operator()(const State* t1, const State* t2) const {

       if(t1->pos.size() != t2->pos.size()) return false;
       for(int i=0; i < t1->pos.size(); i++){
               if(t1->pos[i] != t2->pos[i]) return false;

       }
      return true;
   }
};

class RushHour {
      public:
    /*
     * a representação do problema é :
     * a grade tem 6 colunas, numeradas 0 a 5 de esquerda para direita
     * e 6 linhas, numeradas de 0 a  5 de cima para baixo
     *
     * existem nbcars carros, numerados de 0 a  nbcars-1
     * para cada veículo i :
     * - color[i] fornece sua cor
     * - horiz[i] indica se temos um carro na horizontal
     * - len[i] fornece o seu comprimento (2 ou 3)
     * - moveon[i] indica em qual linha o carro se desloca para um carro horizontal
     *   e em qual coluna para um carro vertical
     *
     * o veiculo de indice 0 é o que tem que sair, temos então
     * horiz[0]==true, len[0]==2, moveon[0]==2
     */

    int nbcars;
    vector<string> color;
    vector<bool> horiz;
    vector<int> len;
    vector<int> moveon;
    int nbMoves;

    /* a matriz free é utilizada em moves para determinar rapidamente se a casa (i,j) está livre */
    bool free[6][6];

    void initFree(State* s) {   //preenche a matriz das posições dos carros na pista
        // A SER COMPLETADA
        for(int i = 0;i<6; i++){   //diz que as posições iniciais estão vazias
            for(int j=0;j<6;j++){
                free[i][j]=1;
            }
        }
        for (int i = 0; i<nbcars;i++){   //verifica se tem carro ocupando a posição
            if(horiz[i]==0){  //carros na vertical
                for(int j=0;j<len[i];j++){
                    free[s->pos[i]+j][moveon[i]]=0;
                }
            }
            else{  //carros na horizontal
                for(int j=0;j<len[i];j++){
                    free[moveon[i]][s->pos[i]+j]=0;
                }

            }
        }
    }

    /* retorna a lista de deslocamentos possíveis a partir de s */

    list<State*> moves(State* s) {
        initFree(s);
        list<State*> l;
        // A SER COMPLETADA
        for (int i = 0; i<nbcars;i++){
            if(horiz[i]==0){ //carro na vertical
                if(free[(s->pos[i])-1][moveon[i]] == 1 && (s->pos[i] >0)){
                    l.push_back(new State(s,i,-1));
                }
                if(free[(s->pos[i])+len[i]][moveon[i]] == 1 && ((s->pos[i] + len[i]) <=5)){
                    l.push_back(new State(s,i,+1));
                }
            }
            else{ //carro na horizontal
                if(free[moveon[i]][(s->pos[i])-1] == 1 && (s->pos[i] >0)){
                    l.push_back(new State(s,i,-1));
                }
                if(free[moveon[i]][(s->pos[i])+len[i]] == 1 && ((s->pos[i] + len[i]) <=5)){
                    l.push_back(new State(s,i,+1));
                }
            }
        }

        return l;
    }

    /* procura uma solução a partir de s */
    State* solve(State* s) {
        hash_set<State*,hash_state,eq_state> visited; //hash para memorizar os estados que já encontramos
        visited.insert(s);  //insere o estado atual analisado
        queue<State*> Q;  //Fila que contem os estados possíveis a partir do estado atual 's'
        Q.push(s);  //Adiciona a 'cabeça' da fila
        while (!Q.empty()) {
             // A SER COMPLETADO
            State* estadoAtual = Q.front();   //estadoAtual recebe a cabeça da fila
            Q.pop();  //remove a cabeça
            list<State*>vizinhos= moves(estadoAtual);  //fila que armazenará todos os movimentos possíveis a partir do estado 's'
            list<State*>::iterator it;   //iterador de 'vizinhos'
            for(it = vizinhos.begin();it != vizinhos.end();it ++){  //percorre todos movimentos possíveis
                if((*it)->success()){  //verifica se o movimento é possível
                    cout<<"Achou a solução!"<<endl;
                    return *it;  //achou a solução
                }
                else{  //movimento atual ainda não é solução
                    if( (visited.find(*it)) == (visited.end()) ){
                        //verifica se o movimento atual não está já na fila, para evitar redundâncias
                        Q.push(*it);  //caso ainda não exista o movimento na fila, insira-o.
                        visited.insert(*it);
                    }
                }

            }
        }
        cerr << "sem solução" << endl;
        exit(1);
    }

    /*
     * imprime uma solução
     */

    void printSolution(State* s) {
        // A SER COMPLETADO
        string direcao;
        vector<State*> lista_ordenada; //vetor com a ordem crescente de movimentos
        nbMoves=0;
        int i=0;

        while(s->prev !=NULL){
            lista_ordenada.push_back(s);
            s=s->prev;
            i++;
        }
        nbMoves=i;
        cout<<"tamanho da lista "<<lista_ordenada.size()<<endl;
        cout<<endl<<nbMoves<<" deslocamentos"<<endl;
        cout<<"lixo"<<endl;
        for(i=nbMoves;i>0;i--){

            if(horiz[(lista_ordenada[i])->c]==0){  //carro vertical
                if((lista_ordenada[i])->d==1){
                    direcao=" para baixo";
                }
                else{
                    direcao=" para cima";
                }
            }
            else{  //carro horizontal
                if((lista_ordenada[i])->d==1){
                    direcao=" para a direita";
                }
                else{
                    direcao=" para a esquerda";
                }

            }
            cout<<"veiculo "<<color[((lista_ordenada[i]))->c]<<direcao<<endl;


        }

    }

    void test2() {
        nbcars = 8;
        bool horiz1[] = {true, true, false, false, true, true, false, false};
        horiz.assign(horiz1, horiz1+8);
        int len1[] = {2,2,3,2,3,2,3,3};
        len.assign(len1,len1+8);
        int moveon1[] = {2,0,0,0,5,4,5,3};
        moveon.assign(moveon1,moveon1+8);
        int start1[] = {1,0,1,4,2,4,0,1};
        vector<int> start(start1,start1+8);
        State* s = new State(start);
        initFree(s);
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 6; j++)
                cout << free[i][j] << "\t";
            cout << endl;
        }
    }

    void test3(){
        nbcars = 12;
        bool horiz1[] = {true, false, true, false, false, true, false, true,
                         false, true, false, true};
        horiz.assign(horiz1, horiz1+nbcars);
        int len1[] = {2,2,3,2,3,2,2,2,2,2,2,3};
        len.assign(len1,len1+12);
        int moveon1[] = {2,2,0,0,3,1,1,3,0,4,5,5};
        moveon.assign(moveon1,moveon1+nbcars);
        int start1[] = {1,0,3,1,1,4,3,4,4,2,4,1};
        vector<int> start(start1,start1+nbcars);
        State* s = new State(start);
        int start02[] = {1,0,3,1,1,4,3,4,4,2,4,2};
        vector<int> start2(start02,start02+nbcars);
        State* s2 = new State(start2);
        int n = 0;
        for (list<State*> L = moves(s); !L.empty(); n++) L.pop_front();
        cout << n << endl;
        n = 0;
        for (list<State*> L = moves(s2); !L.empty(); n++) L.pop_front();
        cout << n << endl;
    }

    void test4() {
        nbcars = 12;
        string color1[] = {"vermelho","verde claro","amarelo","laranja",
                           "violeta claro","azul ceu","rosa","violeta","verde","preto","bege","azul"};
        color.assign(color1, color1+nbcars);
        bool horiz1[] = {true, false, true, false, false, true, false,
                         true, false, true, false, true};
        horiz.assign(horiz1, horiz1+nbcars);
        int len1[] = {2,2,3,2,3,2,2,2,2,2,2,3};
        len.assign(len1,len1+nbcars);
        int moveon1[] = {2,2,0,0,3,1,1,3,0,4,5,5};
        moveon.assign(moveon1,moveon1+nbcars);
        int start1[] = {1,0,3,1,1,4,3,4,4,2,4,1};
        vector<int> start(start1,start1+nbcars);
        State* s = new State(start);
        int n = 0;
        for (s = solve(s); s->prev != NULL; s = s->prev){
            n++;
        }
        cout << n << endl;
    }

    void solve22() {
    nbcars = 12;
    string color1[] = {"vermelho","verde claro","amarelo","laranja",
    "violeta claro","azul ceu","rosa","violeta","verde","preto","bege","azul"};
    color.assign(color1, color1+nbcars);
    bool horiz1[] = {true, false, true, false, false, true, false,
    true, false, true, false, true};
    horiz.assign(horiz1, horiz1+nbcars);
    int len1[] = {2,2,3,2,3,2,2,2,2,2,2,3};
    len.assign(len1,len1+nbcars);
    int moveon1[] = {2,2,0,0,3,1,1,3,0,4,5,5};
    moveon.assign(moveon1,moveon1+nbcars);
    int start1[] = {1,0,3,1,1,4,3,4,4,2,4,1};
    vector<int> start(start1,start1+nbcars);
    State* s = new State(start);
    s = solve(s);
    printSolution(s);
    }

    void solve1() {
    nbcars = 8;
    string color1[] = {"vermelho","verde claro","violeta",
    "laranja","verde","azul ceu","amarelo","azul"};
    color.assign(color1, color1+nbcars);
    bool horiz1[] = {true, true, false, false, true,
    true, false, false};
    horiz.assign(horiz1, horiz1+nbcars);
    int len1[] = {2,2,3,2,3,2,3,3};
    len.assign(len1,len1+nbcars);
    int moveon1[] = {2,0,0,0,5,4,5,3};
    moveon.assign(moveon1,moveon1+nbcars);
    int start1[] = {1,0,1,4,2,4,0,1};
    vector<int> start(start1,start1+nbcars);
    State* s = new State(start);
    s = solve(s);
    printSolution(s);
    }

    void solve40() {
    nbcars = 13;
    string color1[] = {"vermelho","amarelo","verde claro","laranja","azul claro",
    "rosa","violeta claro","azul","violeta","verde","preto","bege","amarelo claro"};
    color.assign(color1, color1+nbcars);
    bool horiz1[] = {true, false, true, false, false, false, false,
    true, false, false, true, true, true};
    horiz.assign(horiz1, horiz1+nbcars);
    int len1[] = {2,3,2,2,2,2,3,3,2,2,2,2,2};
    len.assign(len1,len1+nbcars);
    int moveon1[] = {2,0,0,4,1,2,5,3,3,2,4,5,5};
    moveon.assign(moveon1,moveon1+nbcars);
    int start1[] = {3,0,1,0,1,1,1,0,3,4,4,0,3};
    vector<int> start(start1,start1+nbcars);
    State* s = new State(start);
    s = solve(s);
    printSolution(s);
    }

};

void test1() {

    int positioning[] = {1,0,1,4,2,4,0,1};
    vector<int> start(positioning, positioning+8);
    State* s0 = new State(start);
    cout << (!s0->success()) << endl;
    State* s = new State(s0, 1, 1);

    cout << (s->prev == s0) << endl;
    cout << s0->pos[1] << " " << s->pos[1] << endl;

    s = new State(s,6,1);
    s = new State(s,1,-1);
    s = new State(s,6,-1);

    cout << s->equals(s0) << endl;

    s = new State(s0,1,1);
    s = new State(s,2,-1);
    s = new State(s,3,-1);
    s = new State(s,4,-1); s = new State(s, 4, -1);
    s = new State(s,5,-1); s = new State(s,5,-1); s = new State(s,5,-1);
    s = new State(s,6,1); s = new State(s, 6, 1); s = new State(s, 6, 1);
    s = new State(s,7,1); s = new State(s, 7, 1);
    s = new State(s,0,1); s = new State(s,0,1); s = new State(s,0,1);

    cout << (s->success()) << endl;
}


int main(){
    RushHour r;
    cout<<"\nResultado do Teste 01:"<<endl;
    //test1();

    cout<<"\nResultado do Teste 02:"<<endl;
    //r.test2();

    cout<<"\nResultado do Teste 03:"<<endl;
    //r.test3();

    cout<<"\nResultado do Teste 04:"<<endl;
    //r.test4();

    cout<<"\nResultado do Teste solve22:"<<endl;
    r.solve22();

    cout<<"\nResultado do Teste solve1:"<<endl;
    r.solve1();

    cout<<"\nResultado do Teste solve40:"<<endl;
    r.solve40();

    cout<<"_____________________________________________"<<endl;
    return 0;
    }
