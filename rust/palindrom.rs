use std::io;

fn main(){
    println!("Enter a word: ");
    let mut word= String::new();
    io::stdin()
        .read_line(&mut word)
        .expect("");
    let fw= word.trim().chars().collect::<String>();
    let bw= word.trim().chars().rev().collect::<String>();
    if fw==bw{
        println!("{fw} is a palindrom");
    }else{
        println!("{fw} is not a palindrom");
    }
}
