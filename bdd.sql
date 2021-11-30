DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS book;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  nom TEXT NOT NULL,
  prenom TEXT NOT NULL,
  dateDeNaissance DATE,
  email TEXT NOT NULL
);
CREATE TABLE book(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titre TEXT NOT NULL,
    auteur TEXT NOT NULL,
    quantite INTEGER NOT NULL,
    dateDeParution DATE,
    genre TEXT NOT NULL
);
CREATE TABLE auteur(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    nationalité TEXT NOT NULL,
    dateDeNaissance DATE
);
CREATE TABLE location(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dateDebut DATE NOT NULL,
    dateFin DATE NOT NULL,
    restitution DATE
);

INSERT INTO user VALUES ('1','1','nom1','prenom1','01/01/1999','email@email.com');

