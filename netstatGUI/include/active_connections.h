//
// Created by alexander on 14.05.23.
//

#ifndef NETSTATGUI_ACTIVE_CONNECTIONS_H
#define NETSTATGUI_ACTIVE_CONNECTIONS_H

#include <iostream>
#include <cstdlib>
#include <sstream>
#include <cstring>
#include <csignal>

[[maybe_unused]] std::string active_connections(){
    const std::string& command = "netstat -l";
    FILE* pipe = popen(command.c_str(), "r");
    if (!pipe) {
        std::cerr << "Unknown error while running the program" << std::endl;
    }
    const char* targetLine = "Aktive Sockets in der UNIX-Domäne (Nur Server)";
    char buffer[256];
    bool print = true;
    std::string out_vec;
    while (fgets(buffer, sizeof(buffer), pipe) != nullptr) {
        if (std::strncmp(buffer, targetLine, std::strlen(targetLine)) == 0) {
            print = false;
        }

        if (print) {
            out_vec.append(buffer);
            std::cout << buffer;
        }
    }
    pclose(pipe);
    return out_vec;
}
#endif //NETSTATGUI_ACTIVE_CONNECTIONS_H
