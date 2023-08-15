use reqwest;
use select::document::Document;
use select::node::Node;
use select::predicate::{Name, Predicate, Attr};


pub async fn content(url: &str) -> Result<(Vec<String>, Vec<String>), Box<dyn std::error::Error>> {

    let mut headings: Vec<String> = Vec::new();
    let mut links: Vec<String> = Vec::new();

    let response = reqwest::get(url).await?;
    let body = response.text().await?;

    let document = Document::from(body.as_str());

    for node in document.find(Name("h1").or(Name("h2")).or(Name("h3"))) {
        headings.push(node.text());
    }

    for node in document.find(Name("a")) {
        if let Some(link) = node.attr("href") {
            links.push(link.to_string());
        }
    }
    Ok((headings, links))
}
