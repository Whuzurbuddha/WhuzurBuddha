fn main(){
    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("error");
    let mut vec: Vec<&str> = input.trim().split(',').collect();
    for i in 1..vec.len(){
        for j in 0..vec.len(){
            if vec[i] < vec[j] {
                vec.swap(i,j);
            }
        }
    } println!("{:?}", vec);
}
