SELECT addresses.*, content.*
FROM addresses
JOIN content ON addresses.ID = content.content_KEY
WHERE content.content_KEY = 1;
