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
    pub(crate) ID: String,
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

pub fn controller(IDs: Vec<String>, IPs: Vec<String>) -> std::result::Result<(), Box<dyn std::error::Error>> {

    let url = format!(
        "mysql://{}:{}@{}:{}/{}",
        USER.username, USER.password, USER.hostname, USER.port, USER.db
    );

    let pool = Pool::new(&*url)?;
    let mut conn = pool.get_conn()?;

    let sql = r"INSERT INTO reachable_IPs (ID, IP) VALUES (?, ?)";

    for i in 0..IDs.len() {
        conn.exec_batch(
            sql,
            std::iter::once((IDs[i].clone(), IPs[i].clone()))
        )?;
    }
    Ok(())
}

pub fn lastID() -> Option<LastID> {
    let url = format!(
        "mysql://{}:{}@{}:{}/{}",
        USER.username, USER.password, USER.hostname, USER.port, USER.db
    );

    let pool = Pool::new(&*url).expect("Failed to create pool");
    let mut conn = pool.get_conn().expect("Failed to get connection");

    let sql = r"SELECT ID FROM reachable_IPs ORDER BY ID DESC LIMIT 1;";

    let last_entry: Option<LastID> = conn.query_map(sql, |ID| LastID { ID })
        .expect("Failed to execute query")
        .pop();

    last_entry
}
