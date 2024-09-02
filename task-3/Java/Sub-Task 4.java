import java.nio.file.*;
import java.io.IOException;

public class Subtask4 {
    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(Files.readString(Paths.get("input.txt")).trim());
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < n; i++) {
            output.append(" ".repeat(n - i - 1)).append("*".repeat(2 * i + 1)).append("\n");
        }
        for (int i = n - 2; i >= 0; i--) {
            output.append(" ".repeat(n - i - 1)).append("*".repeat(2 * i + 1)).append("\n");
        }
        Files.writeString(Paths.get("output.txt"), output.toString());
    }
}
