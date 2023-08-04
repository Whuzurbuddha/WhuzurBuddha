pub fn IPs() -> Vec<String>{
    let mut r_ips: Vec<String> = Vec::new();
    let start_ip: Vec<i32> = vec![80, 99, 161, 10];
    let end_ip: Vec<i32> = vec! [80, 99, 165, 254];
    for a in start_ip[0]..end_ip[0] + 1{
        for b in start_ip[1]..end_ip[1] + 1{
            for c in start_ip[2]..end_ip[2] + 1{
                for d in start_ip[3]..end_ip[3] + 1{
                    let ips= format!("{a}.{b}.{c}.{d}");
                    r_ips.push(ips);
                }
            }
        }
    }
    return r_ips;
}

pub fn IDs(num : usize) -> String{
    let mut num = num as i32;
    let mut vec: Vec<i32> = Vec::new();
    let mut unsolved_digits: Vec<i32> = Vec::new();
    let mut i = 1;
    while i < num {
        if i / 1 == 1{
            vec.push(1);
            vec.push(i * 16)
        }else{
            vec.push(i * 16);
        }
        i *= 16;
    }

    for j in (0..vec.len()).rev(){
        let mut counter = 0;
        while num - vec[j] + 1 > 0{
            num -= vec[j];
            counter += 1;
        }
        unsolved_digits.push(counter);
    }
    let mut hex: Vec<String> = Vec::new();
    for digits in unsolved_digits{
        if digits < 10{
            hex.push(digits.to_string());
        }else{
            match digits{
                10 => hex.push("A".to_string()),
                11 => hex.push("B".to_string()),
                12 => hex.push("C".to_string()),
                13 => hex.push("D".to_string()),
                14 => hex.push("E".to_string()),
                15 => hex.push("F".to_string()),
                _=> print!("")
            }
        }
    }
    hex.remove(0);
    let out =  hex.join("");
    return out;
}

pub fn ID_to_dec(hex: String) -> usize{

    let mut dec = 0;
    for (i, c) in hex.chars().rev().enumerate() {
        let digit = c.to_digit(16).expect("Invalid hexadecimal digit");
        let power = 16u32.pow(i as u32);
        dec += digit * power;
    }
    return dec as usize;
}





