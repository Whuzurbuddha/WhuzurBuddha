use reqwest::Client;
use serde::Deserialize;
use std::io;

#[derive(Deserialize)]
struct TranslationResponse {
    translations: Vec<Translation>,
}

#[derive(Deserialize)]
struct Translation {
    text: String,
}

async fn translate_text(text: &str) -> Result<String, Box<dyn std::error::Error>> {
    let client = Client::new();
    let response = client
        .post("https://api-free.deepl.com/v2/translate")
        .form(&[
            ("auth_key", "YOUR-API-KEY"),
            ("text", text),
            ("target_lang", "DE"), //TODO add more languages choices
        ])
        .send()
        .await?; 
    let response_text = response.text().await?;
    let response_json: TranslationResponse = serde_json::from_str(&response_text)
        .map_err(|err| Box::new(err) as Box<dyn std::error::Error>)?;
    if let Some(translation) = response_json.translations.first() {
        Ok(translation.text.clone())
    } else {
        Err("Translation not available".into())
    }
}

#[tokio::main]
async fn main() {
    println!("Enter the text you would like to translate \n");
    let mut input_text = String::new();
    io::stdin()
        .read_line(&mut input_text)
        .unwrap();
    match translate_text(&input_text).await {
        Ok(german_text) => println!("Translated text: {}", german_text),
        Err(err) => eprintln!("Translation error: {}", err),
    }
}

//TODO put more flexibility to the whole project
