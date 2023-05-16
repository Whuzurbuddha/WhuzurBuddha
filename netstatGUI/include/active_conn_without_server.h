//
// Created by alexander on 14.05.23.
//

#ifndef NETSTATGUI_ACTIVE_CONN_WITHOUT_SERVER_H
#define NETSTATGUI_ACTIVE_CONN_WITHOUT_SERVER_H

#include <iostream>
#include <cstdlib>
#include <sstream>
#include <cstring>
#include <csignal>
std::vector<std::string> active_conn_without_server(){
    const std::string& command = "netstat -o";
    FILE* pipe = popen(command.c_str(), "r");
    if (!pipe) {
        std::cerr << "Unknown error while running the program" << std::endl;
    }
    const char* targetLine = "Aktive Sockets in der UNIX-Domäne (ohne Server)";
    char buffer[256];
    bool print = true;
    std::vector<std::string> out_vec;
    while (fgets(buffer, sizeof(buffer), pipe) != nullptr) {
        if (std::strncmp(buffer, targetLine, std::strlen(targetLine)) == 0) {
            print = false;
        }

        if (print) {
            out_vec.push_back(buffer);
            std::cout << buffer;
        }
    }
    pclose(pipe);
    return out_vec;
}


#endif //NETSTATGUI_ACTIVE_CONN_WITHOUT_SERVER_H
