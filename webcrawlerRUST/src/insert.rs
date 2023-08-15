use lazy_static::lazy_static;
use mysql::*;
use mysql::prelude::*;

#[derive(Debug, PartialEq, Eq)]
struct Users {
    hostname: String,
    username: String,
    password: String,
    db: String,
    port: String,
}

#[derive(Debug, PartialEq, Eq, FromRow)]
pub struct IPs {
    pub(crate) ips: String,
}

lazy_static!{
    static ref USER: Users = Users{
        hostname: "localhost".parse().unwrap(),
        username: "username".parse().unwrap(),
        password: "DB password".parse().unwrap(),
        db: "DB".parse().unwrap(),
        port: "port".parse().unwrap(),
    };
}

pub fn last_id() -> std::result::Result<usize, Box<dyn std::error::Error>> {
    let url = format!(
        "mysql://{}:{}@{}:{}/{}",
        USER.username, USER.password, USER.hostname, USER.port, USER.db
    );

    let pool = Pool::new(&*url)?;
    let mut conn = pool.get_conn()?;
    let last_id: Option<usize> = conn.query_first("SELECT ID FROM url ORDER BY ID DESC LIMIT 1")?;
    Ok(last_id.unwrap_or(0) + 1)
}

pub fn urls(name: String) -> std::result::Result<(), Box<dyn std::error::Error>>{
    let url = format!(
        "mysql://{}:{}@{}:{}/{}",
        USER.username, USER.password, USER.hostname, USER.port, USER.db
    );

    let pool = Pool::new(&*url)?;
    let mut conn = pool.get_conn()?;

    let sql = r"INSERT INTO url (WNAME) VALUES (?)";
    let param: Vec<(String,)> = vec![(name.to_string(),)];

    conn.exec_batch(
        sql,
        param
    )?;
    Ok(())
}
pub fn headings(key: usize, heading: Vec<String>) -> std::result::Result<(), Box<dyn std::error::Error>>{
    let url = format!(
        "mysql://{}:{}@{}:{}/{}",
        USER.username, USER.password, USER.hostname, USER.port, USER.db
    );

    let pool = Pool::new(&*url)?;
    let mut conn = pool.get_conn()?;

    let sql = r"INSERT INTO headings (HEADING, HEADINGS_KEY) VALUES (?, ?)";
    for i in 0..heading.len() {
        conn.exec_batch(
            sql,
            std::iter::once((heading[i].clone(), key))
        )?;
    };
    Ok(())
}

pub fn links(key: usize, link: Vec<String>) -> std::result::Result<(), Box<dyn std::error::Error>>{
    let url = format!(
        "mysql://{}:{}@{}:{}/{}",
        USER.username, USER.password, USER.hostname, USER.port, USER.db
    );

    let pool = Pool::new(&*url)?;
    let mut conn = pool.get_conn()?;

    let sql = r"INSERT INTO links (LINK, LINKS_KEY) VALUES (?, ?)";

    for i in 0..link.len() {
        conn.exec_batch(
            sql,
            std::iter::once((link[i].clone(), key))
        )?;
    }
    Ok(())
}
