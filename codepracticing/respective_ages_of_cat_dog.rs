//inspired by "codewars" :)

use std::io;

fn dinglemouse(past_years: i32){

    let mut cat: Vec<i32> = Vec::new();
    let mut dog: Vec<i32> = Vec::new();
    for i in 1..past_years{
        if i == 1{
            cat.push(15);
            dog.push(15);
        }else if i == 2{
            cat.push(9);
            dog.push(9);
        }else if i > 2{
            cat.push(4);
            dog.push(5);
        }
    }
    let dog_age = dog.iter().sum::<i32>();
    let cat_age = cat.iter().sum::<i32>();
    println!("You got your pets {} years ago, then your dog is now {} and \
      your cat is {} years old.", past_years, dog_age, cat_age);
}

fn main() {
    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("error");
    let past_years = input.trim().parse::<i32>().unwrap();
    dinglemouse(past_years);
}

