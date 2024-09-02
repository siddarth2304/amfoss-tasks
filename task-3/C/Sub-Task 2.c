#include <stdio.h>

int main() {
    FILE *infile = fopen("input.txt", "r");
    FILE *outfile = fopen("output.txt", "w");
    char data[100];
    fgets(data, 100, infile);
    fputs(data, outfile);
    fclose(infile);
    fclose(outfile);
    return 0;
}
