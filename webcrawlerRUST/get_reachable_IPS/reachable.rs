use reqwest::Client;
use std::time::Instant;
use futures::future::join_all;
use std::time::Duration;

pub async fn IP_addresses(IPs: Vec<String>) -> Vec<String> {
    let mut result = Vec::new();
    for IP in IPs{
        let url = format!("http://{}", IP);

        let timeout_duration = Duration::from_secs(1/2);

        let client = Client::new();
        let start_time = Instant::now();
        let response = client.get(&url).timeout(timeout_duration).send().await;
        let duration = start_time.elapsed();

        match response {
            Ok(resp) => {
                println!("Found source at {IP}");
                result.push(IP);
            }
            Err(err) => {
                eprintln!("{}: {}", IP, err);
            }
        }
    }
    return result;
