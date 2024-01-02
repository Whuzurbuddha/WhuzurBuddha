fn hexademical(mut num: i32) -> String{
    let mut vec: Vec<i32> = Vec::new();
    let mut unsolved_digits: Vec<i32> = Vec::new();
    let mut i = 1;
    while i < num && (i * 16) < num{
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
    let out =  hex.join(" ");
    return out;
}
