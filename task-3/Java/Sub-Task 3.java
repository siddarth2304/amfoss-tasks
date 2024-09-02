import java.util.Scanner;

public class Subtask3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        for (int i = 0; i < n; i++) {
            System.out.println(" ".repeat(n - i - 1) + "*".repeat(2 * i + 1));
        }
        for (int i = n - 2; i >= 0; i--) {
            System.out.println(" ".repeat(n - i - 1) + "*".repeat(2 * i + 1));
        }
    }
}
