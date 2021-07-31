#include <iostream>
#include <iterator>
#include <list>
#include <cmath>

constexpr int GRID_SIZE = 50;

struct Pos{
    int i;
    int j;
};

enum MOVE
{
    Up,
    Left,
    Dwon,
    Right,
    LAST
};

char move_char(MOVE move){
    if (move == Up)
    {
        return 'U';
    }
    else if (move == Dwon)
    {
        return 'D';
    }
    else if (move == Right)
    {
        return 'R';
    }
    else if (move == Left)
    {
        return 'L';
    }
    return 'O';
}

struct ListItem
{
    Pos pos;
    int label;
    MOVE move;
};

bool legal(
    Pos pos,
    int pos_label,
    int grid_label[GRID_SIZE][GRID_SIZE],
    std::list<ListItem> lst,
    MOVE move)
{
    if(move == Dwon){
        pos.i += 1;
        if (GRID_SIZE <= pos.i)
            return true;
    }else if(move == Up){
        pos.i -= 1;
        if(pos.i<0)
            return true;
    }else if(move == Right){
        pos.j += 1;
        if (GRID_SIZE <= pos.j)
            return true;
    }else if(move == Left){
        pos.j -= 1;
        if (pos.j < 0)
            return true;
    }

    int label = grid_label[pos.i][pos.j];
    if(label == pos_label){
        return true;
    }
    for (auto itr = lst.rbegin(); itr != lst.rend(); itr++){
        if ((*itr).label == label)
            return true;
    }
    return false;
}

int main()
{
    Pos start;
    int grid_label[GRID_SIZE][GRID_SIZE];
    int grid_score[GRID_SIZE][GRID_SIZE];

    std::cin >> start.i >> start.j;
    for (int x = 0; x < GRID_SIZE; x++)
    {
        for (int y = 0; y < GRID_SIZE; y++)
        {
            std::cin >> grid_label[x][y];
        }
    }
    for (int x = 0; x < GRID_SIZE; x++)
    {
        for (int y = 0; y < GRID_SIZE; y++)
        {
            std::cin >> grid_score[x][y];
        }
    }
    
    std::list<ListItem> lst;
    Pos pos = start;
    MOVE search_order[4] = {Up,Left,Dwon,Right};
    int di = pos.i - GRID_SIZE / 2, dj = pos.j - GRID_SIZE / 2;
    int i_bias, j_bias;
    if(std::abs(di) > std::abs(dj)){
        i_bias = 0;
        j_bias = 1;
    }else{
        i_bias = 1;
        j_bias = 0;
    }

    search_order[i_bias + (0 < di ? 0 : 2)] = Up;
    search_order[i_bias + (0 < di ? 2 : 0)] = Dwon;
    search_order[j_bias + (0 < dj ? 0 : 2)] = Right;
    search_order[j_bias + (0 < dj ? 2 : 0)] = Left;

    while(true)
    {
        int pos_label = grid_label[pos.i][pos.j];
        MOVE illegal_move = LAST;
        for (int move_index = 0; move_index < 4; move_index++)
        {
            MOVE move = search_order[move_index];
            if(!legal(pos, pos_label, grid_label, lst, move)){
                illegal_move = move;
                break;
            }
        }
        
        if(illegal_move == LAST){
            for (auto itr = lst.begin(); itr != lst.end(); itr++)
            {
                MOVE move = (*itr).move;
                std::cout << move_char(move);
            }
            std::cout << std::endl;
            break;
        }else{
            lst.push_back({pos, pos_label, illegal_move});
            if (illegal_move == Dwon)
            {
                pos.i += 1;
            }
            else if (illegal_move == Up)
            {
                pos.i -= 1;
            }
            else if (illegal_move == Right)
            {
                pos.j += 1;
            }
            else if (illegal_move == Left)
            {
                pos.j -= 1;
            }
        }
    }
    return 0;
}