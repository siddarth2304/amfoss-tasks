#include <fstream>
#include <string>

int main() {
    std::ifstream infile("input.txt");
    std::ofstream outfile("output.txt");
    std::string data;
    std::getline(infile, data);
    outfile << data;
    infile.close();
    outfile.close();
    return 0;
}
