DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS author;
DROP TABLE IF EXISTS rental;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  lastName TEXT NOT NULL,
  firstNameTEXT NOT NULL,
  email TEXT NOT NULL
);
CREATE TABLE book(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    salutation TEXT NOT NULL
);
CREATE TABLE author(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    nationalité TEXT NOT NULL,
    dateDeNaissance DATE
);
CREATE TABLE rental(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dateDebut DATE NOT NULL,
    dateFin DATE NOT NULL,
    restitution DATE
);
--password ADMIN = AZERTY, toto = tototo
INSERT INTO user VALUES (1,'admin', 'pbkdf2:sha256:260000$LrwVRHktlDoQhAgV$55ae758fe6f952700cd62d239200e2dc2513a23fee2f9bd2e394d25c22a521ab','nom1','prenom1','email@email.com');
INSERT INTO user VALUES (2,'toto', 'pbkdf2:sha256:260000$RnniOUVDAxs8Ti6j$24a7372b84bfa64b03cfc6daa7370f0671a96981c01b397bba8ebf3f517fd8f7','nom2','prenom2','email2@email.com');

