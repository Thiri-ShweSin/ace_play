show databases;
create database ace_play;
use ace_play;

CREATE TABLE card_images (
    id INT AUTO_INCREMENT PRIMARY KEY,
    card_rank VARCHAR(10),
    suit VARCHAR(10),
    image_path VARCHAR(255)
);

INSERT INTO card_images (card_rank, suit, image_path) VALUES 
('1', 'Spades', 'cards/ace_of_spades.png'),
('1', 'Hearts', 'cards/ace_of_hearts.png'),
('1', 'Diamonds', 'cards/ace_of_diamonds.png'),
('1', 'Clubs', 'cards/ace_of_clubs.png'),
('2', 'Spades', 'cards/2_of_spades.png'),
('2', 'Hearts', 'cards/2_of_hearts.png'),
('2', 'Diamonds', 'cards/2_of_diamonds.png'),
('2', 'Clubs', 'cards/2_of_clubs.png'),
('3', 'Spades', 'cards/3_of_spades.png'),
('3', 'Hearts', 'cards/3_of_hearts.png'),
('3', 'Diamonds', 'cards/3_of_diamonds.png'),
('3', 'Clubs', 'cards/3_of_clubs.png'),
('4', 'Spades', 'cards/4_of_spades.png'),
('4', 'Hearts', 'cards/4_of_hearts.png'),
('4', 'Diamonds', 'cards/4_of_diamonds.png'),
('4', 'Clubs', 'cards/4_of_clubs.png'),
('5', 'Spades', 'cards/5_of_spades.png'),
('5', 'Hearts', 'cards/5_of_hearts.png'),
('5', 'Diamonds', 'cards/5_of_diamonds.png'),
('5', 'Clubs', 'cards/5_of_clubs.png'),
('6', 'Spades', 'cards/6_of_spades.png'),
('6', 'Hearts', 'cards/6_of_hearts.png'),
('6', 'Diamonds', 'cards/6_of_diamonds.png'),
('6', 'Clubs', 'cards/6_of_clubs.png'),
('7', 'Spades', 'cards/7_of_spades.png'),
('7', 'Hearts', 'cards/7_of_hearts.png'),
('7', 'Diamonds', 'cards/7_of_diamonds.png'),
('7', 'Clubs', 'cards/7_of_clubs.png'),
('8', 'Spades', 'cards/8_of_spades.png'),
('8', 'Hearts', 'cards/8_of_hearts.png'),
('8', 'Diamonds', 'cards/8_of_diamonds.png'),
('8', 'Clubs', 'cards/8_of_clubs.png'),
('9', 'Spades', 'cards/9_of_spades.png'),
('9', 'Hearts', 'cards/9_of_hearts.png'),
('9', 'Diamonds', 'cards/9_of_diamonds.png'),
('9', 'Clubs', 'cards/9_of_clubs.png'),
('10', 'Spades', 'cards/10_of_spades.png'),
('10', 'Hearts', 'cards/10_of_hearts.png'),
('10', 'Diamonds', 'cards/10_of_diamonds.png'),
('10', 'Clubs', 'cards/10_of_clubs.png'),
('11', 'Spades', 'cards/jack_of_spades.png'),
('11', 'Hearts', 'cards/jack_of_hearts.png'),
('11', 'Diamonds', 'cards/jack_of_diamonds.png'),
('11', 'Clubs', 'cards/jack_of_clubs.png'),
('12', 'Spades', 'cards/queen_of_spades.png'),
('12', 'Hearts', 'cards/queen_of_hearts.png'),
('12', 'Diamonds', 'cards/queen_of_diamonds.png'),
('12', 'Clubs', 'cards/queen_of_clubs.png'),
('13', 'Spades', 'cards/king_of_spades.png'),
('13', 'Hearts', 'cards/king_of_hearts.png'),
('13', 'Diamonds', 'cards/king_of_diamonds.png'),
('13', 'Clubs', 'cards/king_of_clubs.png');

describe table card_images;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(30),
    email VARCHAR(50),
    password VARCHAR(50)
);
INSERT INTO users (username, email, password) VALUES 
('Hein Htet Kyaw', 'heinhtetkyaw@gmail.com', 'hhk@123'),
('Sithu Aung', 'sithuaung@gmail.com', 'sta@123'),
('Su Htet Thinzar', 'suhtetthinzar@gmail.com', 'shtz@123'),
('Phyo Than Thar Kyaw', 'phyothantharkyaw@gmail.com', 'pttk@123');

select * from cards;
select * from users;