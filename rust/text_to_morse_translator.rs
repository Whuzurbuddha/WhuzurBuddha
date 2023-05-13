use std::io;

pub fn morse_output() {
        println!("Enter text: ");
    loop{
        println!();
        let mut input = String::new();
        io::stdin()
            .read_line(&mut input)
            .expect("error");
        for input in input.chars() {
            let input_char_list = vec![input];
            for input in input_char_list {
                match input {
                    //text to morse
                    'a' | 'A' => print!(".-|"),
                    'ä' | 'Ä' => print!(".-|.|"),
                    'b' | 'B' => print!("-...|"),
                    'c' | 'C' => print!("-.-.|"),
                    'd' | 'D' => print!("-..|"),
                    'e' | 'E' => print!(".|"),
                    'f' | 'F' => print!("..-.|"),
                    'g' | 'G' => print!("--.|"),
                    'h' | 'H' => print!("....|"),
                    'i' | 'I' => print!("..|"),
                    'j' | 'J' => print!(".---|"),
                    'k' | 'K' => print!("-.-|"),
                    'l' | 'L' => print!(".-..|"),
                    'm' | 'M' => print!("--|"),
                    'n' | 'N' => print!("-.|"),
                    'o' | 'O' => print!("---|"),
                    'ö' | 'Ö' => print!("---|.|"),
                    'p' | 'P' => print!(".--.|"),
                    'q' | 'Q' => print!("--.-|"),
                    'r' | 'R' => print!(".-.|"),
                    's' | 'S' => print!("...|"),
                    't' | 'T' => print!("-|"),
                    'u' | 'U' => print!("..-|"),
                    'ü' | 'Ü' => print!("..-|.|"),
                    'v' | 'V' => print!("...-|"),
                    'w' | 'W' => print!(".-- |"),
                    'x' | 'X' => print!("-..-|"),
                    'y' | 'Y' => print!("-.--|"),
                    'z' | 'Z' => print!("--..|"),
                    ' ' => print!("    "),
                    _ => print!(""),
                }
            }
        }
    }
}
