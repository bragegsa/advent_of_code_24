#include "day6_lib.h"


/**
 * @brief reads a file and returns a matrix of data.
 * 
 * @param file_path the path to the file.
 * @return guard_matrix The matrix of data retrived from the file.
 */
std::vector<std::vector<char>> read_file(std::string file_path) {

    std::ifstream inputFile(file_path);

    std::vector<std::vector<char>> guard_matrix;
    std::vector<char> row;

    std::string line;
    while (std::getline(inputFile, line)) {

        for (int i = 0; i < line.size(); i++) {
            if (line[i] != ' ') {
                row.push_back(line[i]);
            }
        }

        guard_matrix.push_back(row);
        row.clear();
    }

    inputFile.close();

    return guard_matrix;
}

/**
 * @brief prints a matrix of data.
 * 
 * @param guard_matrix the matrix of data.
 */
void print_matrix(std::vector<std::vector<char>> guard_matrix) {

    for (int i = 0; i < guard_matrix.size(); i++) {

        for (int j = 0; j < guard_matrix[0].size(); j++) {

            std::cout << guard_matrix[i][j];

        }

        std::cout << std::endl;
    }
}

/**
 * @brief returns the position of the guard in the given matrix.
 * 
 * @param guard_matrix the matrix of data.
 * @return position the position of the guard.
 */
std::vector<int> guard_position(std::vector<std::vector<char>> guard_matrix) {

    std::vector<int> position;
    std::vector<char> rotation = {'^', '>', 'v', '<'};

    for (int i = 0; i < guard_matrix.size(); i++) {

        for (int j = 0; j < guard_matrix[0].size(); j++) {

            for (int k = 0; k < rotation.size(); k++) {
                if (guard_matrix[i][j] == rotation[k]) {
                    position.push_back(i);
                    position.push_back(j);
                    position.push_back(k);

                    return position; 
                }
            }
            

        }
    }

    std::cout << "--- No position found! ---" << std::endl;
    return position;
}

/**
 * @brief returns a matrix showing the path of the guard
 * 
 * @param guard_matrix the matrix of data.
 * @return new_guard_matrix the matrix showing the path of the guard.
 */
std::tuple<std::vector<std::vector<char>>, bool, std::vector<int>> calculate_path(std::vector<std::vector<char>> guard_matrix, std::vector<int> current_position) {

    std::vector<std::vector<char>> new_guard_matrix = guard_matrix;
    bool patrol_ended = false;

    std::vector<int> position; 

    if (current_position[2] == 4) {
        position = guard_position(guard_matrix); 
    } else {
        position = current_position;
    }


    new_guard_matrix[position[0]][position[1]] = 'X';
    std::vector<int> stop_position;
    
    if (position[2] == 0) { // Retning Oppover
        for (int i = position[0]; i >= 0; i--) {

            if (guard_matrix[i][position[1]] == '#') {

                new_guard_matrix[i + 1][position[1]] = '>';
                position = {i + 1, position[1], 1};
                break;
            } else if (i == 0) {

                new_guard_matrix[i][position[1]] = '>';
                position = {i, position[1], 1};
                patrol_ended = true;
                break;
            } else if (guard_matrix[i][position[1]] == '.' || guard_matrix[i][position[1]] == 'X') {

                new_guard_matrix[i][position[1]] = 'X';
            }              
        }
    } else if (position[2] == 1) { // Reting Høyre
        for (int i = position[1]; i < guard_matrix[0].size(); i++) {

            if (guard_matrix[position[0]][i] == '#') {

                new_guard_matrix[position[0]][i-1] = 'v';
                position = {position[0], i-1, 2};
                break;
            } else if (i == guard_matrix[0].size() - 1) {

                new_guard_matrix[position[0]][i] = 'v';
                position = {position[0], i, 2};
                patrol_ended = true;
                break;
            } else if (guard_matrix[position[0]][i] == '.' || guard_matrix[position[0]][i] == 'X') {

                new_guard_matrix[position[0]][i] = 'X';
            } 
            
        }
    } else if (position[2] == 2) { // Retning Nedover
        for (int i = position[0] + 1; i < guard_matrix[0].size(); i++) {

            if (guard_matrix[i][position[1]] == '#') {

                new_guard_matrix[i - 1][position[1]] = '<';
                position = {i-1, position[1], 3};
                break;
            } else if (i == guard_matrix[0].size() - 1) {

                new_guard_matrix[i][position[1]] = '<';
                position = {i, position[1], 3};
                patrol_ended = true;
                break;
            } else if (guard_matrix[i][position[1]] == '.' || guard_matrix[i][position[1]] == 'X') {

                new_guard_matrix[i][position[1]] = 'X';
            }              
        }
    } else if (position[2] == 3) { // Reting Venstre
        for (int i = position[1]; i >= 0; i--) {

            if (guard_matrix[position[0]][i] == '#') {

                new_guard_matrix[position[0]][i+1] = '^';
                position = {position[0], i+1, 0};
                break;
            } else if (i == 0) {

                new_guard_matrix[position[0]][i] = '^';
                position = {position[0], i, 0};
                patrol_ended = true;
                break;
            } else if (guard_matrix[position[0]][i] == '.' || guard_matrix[position[0]][i] == 'X') {

                new_guard_matrix[position[0]][i] = 'X';
            } 
            
        }
    }
    
    return {new_guard_matrix, patrol_ended, position};

}

/**
 * @brief returns an int of the number of positions the guard has visited
 * 
 * @param guard_matrix the matrix of data.
 * @return number_of_positions the number of positions the guard has visited.
 */
int count_positions(std::vector<std::vector<char>> guard_matrix) {

    int number_of_positions = 0;

    for (int i = 0; i < guard_matrix.size(); i++) {

        for (int j = 0; j < guard_matrix[0].size(); j++) {

            if (guard_matrix[i][j] == 'X') {
                number_of_positions += 1;
            }
        }
    }


    return number_of_positions;
}

/**
 * @brief returns the guard_matrix where the guard has been replaced by a path
 * 
 * @param guard_matrix the matrix of data without path.
 */
std::vector<std::vector<char>> remove_guard(std::vector<std::vector<char>> guard_matrix) {

    std::vector<int> position = guard_position(guard_matrix); 
    guard_matrix[position[0]][position[1]] = 'X';

    return guard_matrix;
}

// /**
//  * @brief returns the number of loops by placing obstacle
//  * 
//  * @param guard_matrix the matrix of data without path.
//  * @return guard_matrix_with_path the matrix of data with path
//  */
// int place_obstacle(std::vector<std::vector<char>> guard_matrix, std::vector<std::vector<char>> guard_matrix_with_path) {

//     std::vector<std::vector<char>> guard_matrix_test = guard_matrix;
//     std::vector<int> start_position = guard_position(guard_matrix);
    
//     bool patrol_ended = false;
//     int number_of_loops = 0;

//     int loop_checker = 0;

//     for (int i = 0; i < guard_matrix_with_path.size(); i++) {

//         for (int j = 0; j < guard_matrix[0].size(); j++) {

//             if (guard_matrix_with_path[i][j] == 'X' && guard_matrix[i][j] == '.') {

//                 loop_checker = 0;
//                 guard_matrix_test[i][j] = '#';

//                 while (patrol_ended == false) {
//                     auto calculated_path = calculate_path(guard_matrix_test);
//                     patrol_ended = calculated_path.second;
                    
                    
//                     if (remove_guard(calculated_path.first) == remove_guard(guard_matrix_test) && patrol_ended == false) {                        
//                         if(loop_checker == 4) {
//                             patrol_ended = true;
//                             number_of_loops = number_of_loops + 1;
//                         } else {
//                             loop_checker = loop_checker + 1;
//                         }
                        
//                     }

//                     guard_matrix_test = calculated_path.first;
                    
//                 } 

//                 guard_matrix_test = guard_matrix;
//                 patrol_ended = false;

//             }
//         }
//     }

//     return number_of_loops;

// }

/**
 * @brief calculates the path and prints the number of positions visited by the guard.
 * 
 * @param guard_matrix the matrix of data.
 */
void guard_patrol(std::vector<std::vector<char>> guard_matrix) {

    std::vector<std::vector<char>> new_guard_matrix = guard_matrix;
    bool patrol_ended = false;

    std::vector<int> current_position = {0, 0, 4};

    while (patrol_ended == false) {
        auto [new_guard_matrix_temp, patrol_ended_temp, current_position_temp] = calculate_path(new_guard_matrix, current_position);
        new_guard_matrix = new_guard_matrix_temp;
        patrol_ended = patrol_ended_temp;
        current_position = current_position_temp;
    } 

    std::vector<int> position = guard_position(new_guard_matrix); 
    new_guard_matrix[position[0]][position[1]] = 'X';

    int number_of_positions = count_positions(new_guard_matrix);
    std::cout << "Number of distinct positions: " << number_of_positions << std::endl;

    // int number_of_loops = place_obstacle(guard_matrix, new_guard_matrix);
    // std::cout << "The number of positions that create a loop is: " << number_of_loops << std::endl;

}