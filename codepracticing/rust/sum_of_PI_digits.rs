extern crate rust_mpfr;
extern crate core;

use std::io;


fn compute_pi(index: i32) -> Result<String, String> {

    let mut upi: f64 = 0.0;
    for index in 1..index + 1 {
        let c = index.to_string();
        let n = match c.trim().parse::<f64>() {
            Ok(value) => value,
            Err(_) => {
                return Err(String::from("ERROR"));
            }
        };
        let f = 1.0/n.powf(2.0);
        upi += f;
    }
    //let upi: f64 = vec.iter().sum();
    let pi = (upi * 6.0).sqrt();
    let binding = pi.to_string();
    Ok(binding)
}

fn main() {
/////////////calculating PI///////////////////////////////////////////
/**/    println!("Enter index for calculating PI: ");
/**/    let mut index = String::new();
/**/        io::stdin()
/**/            .read_line(&mut index)
/**/            .unwrap();
/**/    let index = match index
/**/            .trim()
/**/            .parse::<i32>() {
/**/    Ok(value) => value,
/**/    Err(_) => {
/**/    println!("Invalid input. Please enter a valid integer.");
/**/    return;
/**/        }
/**/    };
/**/    let mut pi_vec: Vec<String> = Vec::new();
/**/        match compute_pi(index){
/**/            Ok(value) => pi_vec.push(value),
/**/            Err(error) => println!("Error {}", error),
/**/       };
//////////////////sum of the digits of PI //////////////////////////////////////
/**/
/**/    println!("Pi was calculated and it's: {} \n Now enter the number of decimal places you want to calculate.", pi_vec[0]);
/**/    let mut input = String::new();
/**/    io::stdin().read_line(&mut input).unwrap();
/**/    let error = String::from("Invalid input. Please enter valid number.");
/**/
/**/    let decimal_places = match input.trim().parse::<usize>(){
/**/        Ok(value) => value,
/**/        Err(_) => {
/**/            println!("{}", error);
/**/            return;
/**/        }
/**/    };
///////         deleting the dot from PI                ////////////////////////
/**/    let pi_digits_cleaned: Vec<&str> = pi_vec[0].split(".").collect();
/**/    let mut pi_digits: Vec<i32> = Vec::new();
/**/    let mut final_pi_vec: Vec<i32> = Vec::new();
/**/    for i in 0..pi_digits_cleaned.len(){
/**/         for digit in pi_digits_cleaned[i].chars(){
/**/            pi_digits
/**/               .push(digit
/**/                .to_string()
/**/                .parse::<i32>()
/**/                .unwrap());
/**/        }
/**/     }
/**/        let joined_digits = pi_digits
/**/                .iter()
/**/                .map(|num| num.to_string())
/**/                .collect::<String>();
/**/
/**/        let final_pi: String = joined_digits
/**/                .chars()
/**/                .take(decimal_places)
/**/                .collect();
/**/
/**/        for k in final_pi.chars(){
/**/            final_pi_vec.push(k.to_string().parse::<i32>().unwrap());
/**/       }
/**/        let sum = final_pi_vec.iter().fold(0, |acc, &x|acc + x);
/**/
/**/        println!("sum of digits of pi is: {}", sum);
/**/
/**/    }
/**/
///////////////////////////////////////////////////////////////////////}
