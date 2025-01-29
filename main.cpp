#include "main.h"
#include "modules_cpp/day6_lib.h" 

/**
 * @brief This function solves the task for day 6.
**/
int main() {

    std::cout << std::endl;
    std::cout << "--- Day 6 ---" << std::endl;

    std::string filepath = "inputs/day6.txt";
    std::vector<std::vector<char>> guard_matrix = read_file(filepath);

    std::vector<int> start_position = guard_position(guard_matrix);

    guard_patrol(guard_matrix);

    return 0;
}
