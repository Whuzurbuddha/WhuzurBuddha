use std::io;

fn main() {
    println!("Enter a date: (DD.MM.YYYY)");
    let mut date=String::new();
    io::stdin()
        .read_line(&mut date)
        .expect("");
    let split_string: Vec<&str> = date.split('.').collect();
    let day = split_string[0].trim().parse::<usize>().unwrap();
    let month = split_string[1].trim().parse::<usize>().unwrap();
    let year = split_string[2].trim().parse::<usize>().unwrap();
    if ((month==2) && ((year%4==0) && (day>0 && day<=29)) || (year%100!=0) && (day>0 && day <=28)) ||
        (((month == 4 || month == 6 || month == 9 || month == 11) && (day > 0 && day <= 30)) ||
            ((month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) &&
                (day > 0 && day <= 31))) {
        let date= format!("{day}.{month}.{year}");
        println!("{date}");
    }else{
        println!("Date does not exist!");
    }
}
