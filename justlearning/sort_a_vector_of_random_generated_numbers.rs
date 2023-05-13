use std::io;
use rand::Rng;

fn main() {
    //input
    println!("How many numbers would you like to generate");
    let mut input_number = String::new();
    io::stdin()
        .read_line(&mut input_number)
        .expect("");

    println!("Enter the range for generating numbers");
    let mut input_range = String::new();
    io::stdin()
        .read_line(&mut input_range)
        .expect("");
    //put generated numbers in vector
    let mut vec: Vec<i32> = Vec::new();
    for _i in 0..input_number.trim().parse::<usize>().unwrap() {
        let index = input_range
            .trim()
            .parse::<i32>()
            .unwrap();
        let mut _digits = rand::thread_rng().gen_range(1..index);
        vec.push(_digits);
    }
    //unsorted vector
    println!("
    **************************************************************
    *                                                            *
    *    unsorted vector:                                        *
    *                                                            *
    **************************************************************");
    for (i, num) in vec.iter().enumerate() {
        print!("{} ", num);
        if (i + 1) % 25 == 0 {
            println!();
        }
    }println!("\n");
    println!("
    **************************************************************
    *                                                            *
    *    sorted vector:                                          *
    *                                                            *
    **************************************************************");
    //bubblesort
    let n = vec.len();
    let mut last_swapped = n - 1;
    let mut sorted = false;
    while !sorted {
        sorted = true;
        for i in 0..last_swapped {
            if vec[i] > vec[i+1] {
                vec.swap(i, i+1);
                sorted = false;
                last_swapped = i;
            }
        }
    }for (k, num) in vec.iter().enumerate() {
        print!("{} ", num);
        if (k + 1) % 25 == 0 {
            println!();
        }
    }
}





