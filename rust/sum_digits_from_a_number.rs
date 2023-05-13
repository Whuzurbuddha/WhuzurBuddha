use std::io;
fn main(){
    println!("Enter a (3digits)number");
    let mut number= String::new();
    io::stdin()
        .read_line(&mut number)
        .expect("");
    let a= number.chars().nth(0).unwrap();
    let a= format!("{a}");
    let a= a.trim().parse::<usize>().expect("");
    let b= number.chars().nth(1).unwrap();
    let b= format!("{b}");
    let b= b.trim().parse::<usize>().expect("");
    let c= number.chars().nth(2).unwrap();
    let c= format!("{c}");
    let c= c.trim().parse::<usize>().expect("");
    let subtract_sum= a+b+c;
    if subtract_sum>=10 && subtract_sum <=100{
        let check_list=["","kiwi","pear","kiwi","banana","melon","banana","melon",
            "pineapple","apple","pineapple","cucumber","pineapple","cucumber",
            "orange","grape","orange","grape","apple","grape","cherry",
            "pear","cherry","pear","kiwi","banana","kiwi","apple",
            "melon","banana","melon","pineapple","melon","pineapple",
            "cucumber","orange","apple","orange","grape","orange",
            "grape","cherry","pear","cherry","pear","apple","pear",
            "kiwi","banana","kiwi","banana","melon","pineapple","melon",
            "apple","cucumber","pineapple","cucumber","orange","cucumber",
            "orange","grape","cherry","apple","cherry","pear","cherry",
            "pear","kiwi","pear","kiwi","banana","apple","banana",
            "melon","pineapple","melon","pineapple","cucumber","pineapple",
            "cucumber","apple","grape","orange","grape","cherry","grape",
            "cherry","pear","cherry","apple","kiwi","banana","kiwi",
            "banana","melon","banana","melon","pineapple","apple","pineapple"];
        println!("{}", check_list[subtract_sum]);
        println!("{}", subtract_sum);
    }else{
        println!("Not in the list");
    }
}
