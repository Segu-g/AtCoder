#include <cstdint>
#include <vector>

class Graph
{
public:
    Graph();
    Graph(std::int64_t n);
    ~Graph();

    void add_edges(std::int64_t from, std::int64_t to);
    std::int64_t get_vertices_num();

private:
    std::int64_t vertices_num;
    std::vector<int64_t> *edges;
};