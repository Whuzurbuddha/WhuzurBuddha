use std::io;

fn main() {
    println!("Enter text you want to encrypt: ");
    loop{
        let mut input = String::new();
        io::stdin()
            .read_line(&mut input)
            .expect("error");
        for input_char in input.chars() {
            let input_char_list = vec![input_char];
            for i in input_char_list {
               let char_to_ascii= i as u32;
                let encrypting_input= char_to_ascii + 1;
                 if encrypting_input == 33 {
                         print!(" ");
                     }else if encrypting_input == 45{
                        print!(", ");
                     }else{
                     let encrypted_passwd= char::from_u32(encrypting_input);
                     if let Some(i) = encrypted_passwd{
                         print!("{}", i);
                     }
                 }
            }
        }
    }
}
