use std::fs;

fn main() {
    let data = fs::read_to_string("input.txt").expect("Unable to read file");
    let n: i32 = data.trim().parse().expect("Please enter a number");
    let mut output = String::new();

    for i in 0..n {
        output.push_str(&format!("{:width$}{}\n", "", "*".repeat((2 * i + 1) as usize), width = (n - i - 1) as usize));
    }
    for i in (0..n - 1).rev() {
        output.push_str(&format!("{:width$}{}\n", "", "*".repeat((2 * i + 1) as usize), width = (n - i - 1) as usize));
    }

    fs::write("output.txt", output).expect("Unable to write file");
}
