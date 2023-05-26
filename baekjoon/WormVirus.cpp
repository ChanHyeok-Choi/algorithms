#include <iostream>
#include <vector>

using namespace std;

enum LABEL { UNEXPLORED, VISITED, DISCOVERY, CROSS };

class Edge {
private:
    LABEL label;
    Vertice *src, *dst;
public:
    void setLabel(LABEL l) { label = l; }
    LABEL getLabel() { return label; }
    Vertice* getSrc() { return src; }
    Vertice* getDst() { return dst; }
    Vertice* opposite(Vertice* v) { return (v == dst) ? src : dst; }
};

class Vertice {
private:
    int elem;
    LABEL label;
    vector<Edge> *incidentEdges;
public:
    void setVertice(int e) { elem = e; }
    void setLabel(LABEL l) { label = l; }
    LABEL getLabel() { return label; }
    vector<Edge>* getIncidentEdges() { return incidentEdges; }
};

class Graph {
private:
    Vertice *root;
public:
    
};

int main() {
    int num_comp, num_link;
    cin >> num_comp >> num_link;


    return 0;
}