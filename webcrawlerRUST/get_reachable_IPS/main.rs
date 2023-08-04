mod reachable;
mod generate;
mod data;

use tokio::runtime::Runtime;

fn main() {
   let generated_IPs = generate::IPs();

    let runtime = Runtime::new().unwrap();
    let reached_IPs = runtime.block_on(reachable::IP_addresses(generated_IPs.clone()));

    let mut generated_IDs = Vec::new();

    let lastID_option =  data::lastID();
  
    // fetch last ID from database
    if let Some(last_ID) = lastID_option{
        let last_ID = last_ID.ID;

        let last = generate::ID_to_dec(last_ID) + 1;

        for i in last..(last + reached_IPs.len()){
            generated_IDs.push(generate::IDs(i));
        }
    }
    // insert new data in Database
    let _ = data::controller(generated_IDs, reached_IPs);
}
