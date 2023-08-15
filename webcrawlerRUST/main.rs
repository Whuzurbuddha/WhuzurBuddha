#![allow(unused_imports)]
mod get;
mod insert;
mod select;
use url::Url;
use std::fs::File;
use std::io::{self, BufRead};

fn is_valid_url(s: &str) -> bool {
    match Url::parse(s) {
        Ok(url) => url.scheme() == "http" || url.scheme() == "https",
        Err(_) => false,
    }
}

fn read_urls_from_file(filename: &str) -> io::Result<Vec<String>> {
    let file = File::open(filename)?;
    let lines = io::BufReader::new(file).lines();
    let urls: Vec<String> = lines.map(|line| line.unwrap()).collect();
    Ok(urls)
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let urls: Vec<String> = read_urls_from_file("urls.txt")?;

    for url in urls.iter().enumerate() {
        let content: (Vec<String>, Vec<String>) = get::content(url.1).await.unwrap();
        let headings = content.0;
        let links = content.1;
        let names = url.1.to_string();
        let keys = insert::last_id()?;

        let valid_links: Vec<String> = links.into_iter()
            .filter(|link| is_valid_url(link))
            .collect();

        let cleaned_headings: Vec<String> = headings.iter()
            .map(|s| s.trim().to_string())
            .filter(|s| !s.is_empty())
            .collect();

        insert::urls(names)?;
        insert::headings(keys, cleaned_headings)?;
        insert::links(keys, valid_links)?;
    }

    Ok(())
}
