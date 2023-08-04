mod get;
mod fetch;
mod data;
use tokio::runtime::Runtime;

fn main() {
    print!("FETCHING IPs FROM DATABASE");
    let ips_result = get::IPs();
    let mut IPs_vec: Vec<String> = Vec::new();
    if ips_result.is_empty() {
        println!("No IP addresses found in the database.");
    } else {
        for content in ips_result {
            IPs_vec.push(content.ips);
        }
    }
    print!("GET WEBCONTENT");
    let runtime = Runtime::new().unwrap();
    let web_content = runtime.block_on(fetch::WebContent(IPs_vec.clone()));
    print!("INSERT CONTENT IN DATABASE");
    data::controller(IPs_vec.clone(), web_content).unwrap();
}
