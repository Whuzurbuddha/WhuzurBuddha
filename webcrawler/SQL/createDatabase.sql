CREATE TABLE addresses (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    address VARCHAR(100)
);

CREATE TABLE content (
    content_id INT AUTO_INCREMENT PRIMARY KEY,
    content_data VARCHAR(800),
    content_KEY INT,
    FOREIGN KEY (content_KEY) REFERENCES addresses(ID)
);
