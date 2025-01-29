#include "main.h"
#include "modules_cpp/day6_lib.h" 

/**
 * @brief This function solves the task for day 6.
**/
int main() {

    std::cout << std::endl;
    std::cout << "--- Day 6 ---" << std::endl;

    std::string filepath = "inputs/day6.txt";
    // std::string filepath = "inputs/inputs_test/day6_test.txt";
    
    std::vector<std::vector<char>> guard_matrix = read_file(filepath);

    std::vector<int> start_position = guard_position(guard_matrix);

    auto start = std::chrono::high_resolution_clock::now();
    guard_patrol(guard_matrix);
    auto end = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double> duration = end - start;
    std::cout << "Execution time: " << duration.count() << " seconds" << std::endl;

    return 0;
}
