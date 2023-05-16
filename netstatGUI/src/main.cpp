#include <fstream>
#include <vector>
#include "../include/active_connections.h"
#include "../include/active_conn_without_server.h"
#include "../include/routing_table.h"
#include "../include/interfaces.h"


void generateRouting() {
    std::string output = routing_table();
    std::ofstream outputFile("output/outrouting.txt", std::ofstream::trunc);
    if (outputFile.is_open()) {
        outputFile << output << std::endl;
        outputFile.close();
    } else {
        std::cerr << "Failed to open output file." << std::endl;
    }
}

void generateInterfaces() {
    std::string output = interfaces();
    std::ofstream outputFile("output/interout.txt", std::ofstream::trunc);
    if (outputFile.is_open()) {
        outputFile << output << std::endl;
        outputFile.close();
    } else {
        std::cerr << "Failed to open output file." << std::endl;
    }
}

void generateConnectionServer() {
    std::vector<std::string> out = active_connections();
    std::ofstream outputFile("output/acs.txt", std::ofstream::trunc);
    if (outputFile.is_open()) {
        for(const auto & i : out){
            outputFile << i;
        }
        outputFile.close();
    } else {
        std::cerr << "Failed to open output file." << std::endl;
    }
}

void generateConnWServer() {
    std::vector<std::string> out = active_conn_without_server();
    std::ofstream outputFile("output/acws.txt", std::ofstream::trunc);
    if (outputFile.is_open()) {
        for(const auto & i : out){
            outputFile << i;
        }
        outputFile.close();
    } else {
        std::cerr << "Failed to open output file." << std::endl;
    }
}

int main() {
    generateRouting();
    generateInterfaces();
    generateConnectionServer();
    generateConnWServer();
    return 0;
}

