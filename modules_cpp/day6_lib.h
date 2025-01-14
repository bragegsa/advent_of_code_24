#ifndef DAY6_LIB
#define DAY6_LIB

#pragma once

#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <vector> 
#include <utility>

std::vector<std::vector<char>> read_file(std::string file_path);
std::vector<int> guard_position(std::vector<std::vector<char>> guard_matrix);
void print_matrix(std::vector<std::vector<char>> guard_matrix);
std::pair<std::vector<std::vector<char>>, bool> calculate_path(std::vector<std::vector<char>> guard_matrix);
int count_positions(std::vector<std::vector<char>> guard_matrix);
void guard_patrol(std::vector<std::vector<char>> guard_matrix);


#endif