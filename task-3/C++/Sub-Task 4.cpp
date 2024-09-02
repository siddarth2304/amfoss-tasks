#include <fstream>
#include <string>

int main() {
    std::ifstream infile("input.txt");
    std::ofstream outfile("output.txt");
    int n;
    infile >> n;
    for (int i = 0; i < n; i++) {
        outfile << std::string(n - i - 1, ' ') << std::string(2 * i + 1, '*') << std::endl;
    }
    for (int i = n - 2; i >= 0; i--) {
        outfile << std::string(n - i - 1, ' ') << std::string(2 * i + 1, '*') << std::endl;
    }
    infile.close();
    outfile.close();
    return 0;
}
