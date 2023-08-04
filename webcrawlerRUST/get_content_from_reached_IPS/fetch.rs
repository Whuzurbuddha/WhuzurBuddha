#![allow(unused_mut)]
use reqwest;
use std::time::Duration;
use lazy_static::lazy_static;
use tokio::time::{timeout, timeout_at};

pub struct Url {
    url: String,
}
lazy_static! {
    static ref URL: Url = Url {
        url: "http://".to_string(),
    };
}
pub async fn WebContent(IPs: Vec<String>) -> Vec<String> {
    let mut result = Vec::new();
    for IP in IPs {
        let url = format!("{}{}", URL.url, IP);

        match reqwest::get(&url).await{
            Ok(resp) => {
                if resp.status().is_success() {
                    let body = resp.text().await;
                    if let Ok(body) = body {
                        result.push(body);
                    }
                } else {
                    println!("Request to {} failed with status code: {:?}", url, resp.status());
                }
            }
            Err(err) => {
                println!("Request to {} failed: {}", url, err);
            }
        }
    }
    return result;
}
