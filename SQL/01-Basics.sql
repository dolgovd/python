/* Create a simple table for book store:
------------+-----------------------------------
Field       |           Description
------------+-----------------------------------
book_id	    |   INT PRIMARY KEY AUTO_INCREMENT
title	    |   VARCHAR(50)
author      |	VARCHAR(30)
price	    |   DECIMAL(8, 2)
amount      |	INT
------------+-----------------------------------
*/
CREATE TABLE book(
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(50),
    author VARCHAR(30),
    price DECIMAL(8,2),
    amount INT
);

================================================

/* Insert a record into the table
title: Мастер и Маргарита
author: Булгаков М.А.
price: 670.99
amount: 3
*/

INSERT INTO book(title, author, price, amount)
VALUES ('Мастер и Маргарита', 'Булгаков М.А.', 670.99, 3)

SELECT * FROM book