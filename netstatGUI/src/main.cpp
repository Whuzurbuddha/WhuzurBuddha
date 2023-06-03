#include <fstream>
#include <vector>
#include "../include/active_connections.h"
#include "../include/active_conn_without_server.h"
#include "../include/routing_table.h"
#include "../include/interfaces.h"


void generateContent() {
    std::vector<std::string> functions = {"routing_table()", "interfaces()", "active_connections()", "active_conn_without_server()"};
    std::vector<std::string> output_files = {"outrouting.txt", "interout.txt", "acs.txt", "acws.txt"};
    for(int i = 0; i < functions.size(); ++i){
        std::string output = functions[i];
        std::ofstream outputFile("/NETstetGUI/output/" + output_files[i], std::ofstream::trunc);
        if (outputFile.is_open()) {
            outputFile << output << std::endl;
            outputFile.close();
        } else {
            std::cerr << "Failed to open output file." << std::endl;
        }
    }
}

int main() {
    generateContent();
    return 0;
}


