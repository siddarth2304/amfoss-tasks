#include <stdio.h>

int main() {
    FILE *infile = fopen("input.txt", "r");
    FILE *outfile = fopen("output.txt", "w");
    int n;
    fscanf(infile, "%d", &n);
    for (int i = 0; i < n; i++) {
        fprintf(outfile, "%*s", n - i - 1, "");
        for (int j = 0; j < 2 * i + 1; j++) {
            fprintf(outfile, "*");
        }
        fprintf(outfile, "\n");
    }
    for (int i = n - 2; i >= 0; i--) {
        fprintf(outfile, "%*s", n - i - 1, "");
        for (int j = 0; j < 2 * i + 1; j++) {
            fprintf(outfile, "*");
        }
        fprintf(outfile, "\n");
    }
    fclose(infile);
    fclose(outfile);
    return 0;
}
