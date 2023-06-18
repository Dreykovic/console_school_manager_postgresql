\c template1

DROP DATABASE IF EXISTS gestion_note ;
CREATE DATABASE  gestion_note;

\c gestion_note

CREATE TABLE niveau_serie(
							niveau varchar,
							serie varchar
						);


CREATE TABLE classe (
						nom varchar PRIMARY KEY ,
						effectif integer
					);

CREATE TABLE personne (
						matricule serial PRIMARY KEY,
						nom varchar,
						prenoms varchar,
						date_naissance date,
						contact varchar,
						genre varchar,
						adresse varchar 		
						);
CREATE TABLE tuteur(
					matricule serial PRIMARY KEY ,
					profession varchar
					) INHERITS (personne);

CREATE TABLE eleve (
					matricule serial PRIMARY KEY ,
					tuteur serial REFERENCES tuteur(matricule),
					classe varchar REFERENCES classe(nom)
					) INHERITS (personne);
CREATE TABLE enseignant (
							matricule serial PRIMARY KEY ,
							statut varchar
						) INHERITS (personne);
CREATE TABLE matiere (
						id_matiere serial PRIMARY KEY ,
						libelle varchar
						);

CREATE TABLE programme (
							matiere serial REFERENCES matiere(id_matiere),
							prof serial REFERENCES enseignant(matricule),
							classe varchar REFERENCES classe(nom)
						);

INSERT INTO classe VALUES ('2nde A4', 20),
						  ('1ere A4', 20),
						  ('Tle A4', 20),
						  ('2nde D', 20),
						  ('1ere D', 20),
						  ('Tle D', 20);

INSERT INTO tuteur VALUES (0, 'Admin', 'Admin', NULL, NULL, NULL, NULL, NULL );
