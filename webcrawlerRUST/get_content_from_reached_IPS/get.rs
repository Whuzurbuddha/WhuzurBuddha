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
        username: "user".parse().unwrap(),
        password: "password".parse().unwrap(),
        db: "database name".parse().unwrap(),
        port: " ".parse().unwrap(),
    };
}

pub fn IPs() -> Vec<IPs> {
    let url = format!(
        "mysql://{}:{}@{}:{}/{}",
        USER.username, USER.password, USER.hostname, USER.port, USER.db
    );

    let pool = Pool::new(&*url).expect("Failed to create pool");
    let mut conn = pool.get_conn().expect("Failed to get connection");

    let sql = r"SELECT IP FROM reachable_IPs";

    let ips: Vec<IPs> = conn.query_map(sql, |ip| IPs { ips: ip })
        .expect("Failed to execute query");

    return ips;
}
