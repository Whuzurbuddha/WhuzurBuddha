import express, { urlencoded, json } from 'express';
import { compare, genSalt, hash } from 'bcrypt';
import { readFile, writeFile } from 'fs';
const app = express();
const port = 5000;
import cors from 'cors';


app.use(cors());
app.use(urlencoded({ extended: true }));
app.use(json());

app.post('/login', (req, res) => {
    const username = req.body.username;
    const password = req.body.passwd;

    readFile('user_data.json', 'utf8', (err, data) => {
        if (err) {
            console.error('An error occurred during reading data:', err);
            return res.status(500).send('An error occurred during reading data.');
        }

        let userData;
        try {
            userData = JSON.parse(data);
        } catch (err) {
            console.error('An error occurred durring analysing JSON-Data:', err);
            return res.status(500).send('Analysation error.');
        }

        if (userData && userData.username && userData.username === username) {

            compare(password, userData.password, (err, result) => {
                if (err) {
                    console.error('Error while checking password:', err);
                    return res.status(500).send('Error while checking password.');
                }

                if (result) {
                    return res.status(200).send('Successfuly logged in.');
                } else {
                    return res.status(401).send('Wrong password.');
                }
            });
        } else {
            return res.status(404).send("Couldn't find such user  .");
        }
    });
});

app.post('/addUser', (req, res) => {
    const username = req.body.username;
    const password = req.body.passwd;

    genSalt(10, (err, salt) => {
        if (err) {
            console.error('An error occurred while creating the salt:', err);
            return res.status(500).send('An error occurred while saving user data.');
        }


        hash(password, salt, (err, hashedPassword) => {
            if (err) {
                console.error('Password hashing error:', err);
                return res.status(500).send('An error occurred while saving user data.');
            }

            const userData = {
                username: username,
                password: hashedPassword
            };

            writeFile('user_data.json', JSON.stringify(userData, null, 2), (err) => {
                if (err) {
                    console.error(':', err);
                    res.status(500).send('An error occurred while writing the file.');
                } else {
                    console.log('User data has been successfully saved.');
                    res.status(200).send('User data has been successfully saved.');
                }
            });
        });
    });
});

app.listen(port, () => {
    console.log(`Server läuft auf http://192.168.178.29:${port}`);
});
