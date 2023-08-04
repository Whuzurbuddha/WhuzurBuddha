use lazy_static::lazy_static;
use mysql::*;
use mysql::prelude::*;

#[derive(Debug, PartialEq, Eq)]
struct Users {
    hostname: String,
    username: String,
    password: String,
    db: String,
    port: String
}

#[derive(Debug, PartialEq, Eq, FromRow)]
pub struct LastID {
    pub(crate) ID: i32,
}

lazy_static!{
    static ref USER: Users = Users{
        hostname: "localhost".parse().unwrap(),
        username: "user".parse().unwrap(),
        password: "password".parse().unwrap(),
        db: "database name".parse().unwrap(),
        port: " ".parse().unwrap()
    };
}

pub fn controller(IPs: Vec<String>, Content: Vec<String>) -> std::result::Result<(), Box<dyn std::error::Error>> {

    let url = format!(
        "mysql://{}:{}@{}:{}/{}",
        USER.username, USER.password, USER.hostname, USER.port, USER.db
    );

    let pool = Pool::new(&*url)?;
    let mut conn = pool.get_conn()?;

    let sqlIP = r"INSERT INTO addresses (address) VALUES (?)";
    let sqlCont = r"INSERT INTO content (content_key, content_data) VALUES (?, ?)";

    for i in 0..IPs.len() {
        conn.exec_batch(
            sqlIP,
            std::iter::once((IPs[i].clone(),))
        )?;

        let last_id: Option<LastID> = conn.query_first("SELECT ID FROM addresses ORDER BY ID DESC LIMIT 1")?;
        if let Some(last_id) = last_id {
            let content_key = last_id.ID;

            for j in 0..Content.len() {
                conn.exec_batch(
                    sqlCont,
                    std::iter::once((content_key, Content[j].clone()))
                )?;
            }
        }
    }

    Ok(())
}
