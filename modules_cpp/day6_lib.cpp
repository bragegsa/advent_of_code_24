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
std::pair<std::vector<std::vector<char>>, bool> calculate_path(std::vector<std::vector<char>> guard_matrix) {

    std::vector<std::vector<char>> new_guard_matrix = guard_matrix;
    bool patrol_ended = false;

    std::vector<int> position = guard_position(guard_matrix); 
    new_guard_matrix[position[0]][position[1]] = 'X';
    std::vector<int> stop_position;
    
    if (position[2] == 0) { // Retning Oppover
        for (int i = position[0]; i >= 0; i--) {

            if (guard_matrix[i][position[1]] == '#') {

                new_guard_matrix[i + 1][position[1]] = '>';
                break;
            } else if (i == 0) {

                new_guard_matrix[i][position[1]] = '>';
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
                break;
            } else if (i == guard_matrix[0].size() - 1) {

                new_guard_matrix[position[0]][i] = 'v';
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
                break;
            } else if (i == guard_matrix[0].size() - 1) {

                new_guard_matrix[i][position[1]] = '<';
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
                break;
            } else if (i == 0) {

                new_guard_matrix[position[0]][i] = '^';
                patrol_ended = true;
                break;
            } else if (guard_matrix[position[0]][i] == '.' || guard_matrix[position[0]][i] == 'X') {

                new_guard_matrix[position[0]][i] = 'X';
            } 
            
        }
    }
    
    return {new_guard_matrix, patrol_ended};
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
 * @brief calculates the path and prints the number of positions visited by the guard.
 * 
 * @param guard_matrix the matrix of data.
 */
void guard_patrol(std::vector<std::vector<char>> guard_matrix) {

    std::vector<std::vector<char>> new_guard_matrix = guard_matrix;
    bool patrol_ended = false;

    while (patrol_ended == false) {
        auto calculated_path = calculate_path(new_guard_matrix);
        new_guard_matrix = calculated_path.first;
        patrol_ended = calculated_path.second;
    } 

    std::vector<int> position = guard_position(new_guard_matrix); 
    new_guard_matrix[position[0]][position[1]] = 'X';

    int number_of_positions = count_positions(new_guard_matrix);
    std::cout << "Number of distinct positions: " << number_of_positions << std::endl;

}