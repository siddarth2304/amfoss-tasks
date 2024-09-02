import java.nio.file.*;
import java.io.IOException;

public class Subtask2 {
    public static void main(String[] args) throws IOException {
        String data = Files.readString(Paths.get("input.txt"));
        Files.writeString(Paths.get("output.txt"), data);
    }
}
