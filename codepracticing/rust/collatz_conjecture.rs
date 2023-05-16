use std::io;

fn main() {
    println!("Enter a number: ");
    let mut input = String::new();
    let mut output: Vec<usize> = Vec::new();
    io::stdin()
        .read_line(&mut input)
        .unwrap();
    let parsed_input = input.trim().parse::<usize>().unwrap();
    output.push(parsed_input);
    loop {
        let last = output.last().cloned();
        match last {
            Some(num) => {
                if num == 1 {
                    break;
                } else if num % 2 != 0 {
                    output.push((num * 3) + 1);
                }else if num % 2 == 0{
                    output.push(num / 2);
                }
            }
            None => {
                output.push(1);
            }
        }
    }
    for (i, num) in output.iter().enumerate() {
        print!("{} ", num);
        if (i + 1) % 10 == 0 {
            println!();
        }
    }println!("\n");
}
