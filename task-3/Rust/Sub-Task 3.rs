use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read input");
    let n: i32 = input.trim().parse().expect("Please enter a number");

    for i in 0..n {
        println!("{:width$}{}", "", "*".repeat((2 * i + 1) as usize), width = (n - i - 1) as usize);
    }
    for i in (0..n - 1).rev() {
        println!("{:width$}{}", "", "*".repeat((2 * i + 1) as usize), width = (n - i - 1) as usize);
    }
}
