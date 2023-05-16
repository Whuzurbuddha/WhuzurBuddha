//
// Created by alexander on 14.05.23.
//

#ifndef NETSTATGUI_ROUTING_TABLE_H
#define NETSTATGUI_ROUTING_TABLE_H

#include <iostream>
#include <cstdlib>
#include <sstream>
#include <cstring>
#include <csignal>
std::string routing_table(){
    const std::string& command = "netstat -r";
    FILE* pipe = popen(command.c_str(), "r");
    if (!pipe) {
        std::string err = "Error while running programm";
        return err;
    }
    std::ostringstream output_stream;
    char buffer[128];
    while (fgets(buffer, sizeof(buffer), pipe) != nullptr) {
        output_stream << buffer;
    }
    pclose(pipe);
    std::string output = output_stream.str();
    std::istringstream line_stream(output);
    std::cout << output << std::endl;
    return output;
}

#endif //NETSTATGUI_ROUTING_TABLE_H
