#ifndef DAY6_LIB
#define DAY6_LIB

#pragma once

#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <vector> 
#include <utility>
#include <tuple>

std::vector<std::vector<char>> read_file(std::string file_path);
std::vector<int> guard_position(std::vector<std::vector<char>> guard_matrix);
void print_matrix(std::vector<std::vector<char>> guard_matrix);
std::tuple<std::vector<std::vector<char>>, bool, std::vector<int>> calculate_path(std::vector<std::vector<char>> guard_matrix, std::vector<int> current_position);
int count_positions(std::vector<std::vector<char>> guard_matrix);
void guard_patrol(std::vector<std::vector<char>> guard_matrix);
std::vector<std::vector<char>> remove_guard(std::vector<std::vector<char>> guard_matrix);
// void place_obstacle(std::vector<std::vector<char>>  guard_matrix);

#endif