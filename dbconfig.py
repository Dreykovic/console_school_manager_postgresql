
from modeles.migration import *
from modeles.database import tables
from modeles.linker import Linker

trig="""
CREATE SEQUENCE seconded MINVALUE 65 MAXVALUE 91;
CREATE SEQUENCE secondec MINVALUE 65 MAXVALUE 91;
CREATE SEQUENCE secondea MINVALUE 65 MAXVALUE 91;
CREATE SEQUENCE premiered MINVALUE 65 MAXVALUE 91;
CREATE SEQUENCE premierec MINVALUE 65 MAXVALUE 91;
CREATE SEQUENCE premierea MINVALUE 65 MAXVALUE 91;
CREATE SEQUENCE terminalc MINVALUE 65 MAXVALUE 91;
CREATE SEQUENCE terminald MINVALUE 65 MAXVALUE 91;
CREATE SEQUENCE terminala MINVALUE 65 MAXVALUE 91;
-- Création de la fonction PL/pgSQL
CREATE OR REPLACE FUNCTION inserer_valeur_auto()
RETURNS TRIGGER AS $$
DECLARE
    val integer;
BEGIN    
    IF NEW.nom = '2nde D' THEN
        val := nextval('seconded')::int;
        
        NEW.nom := NEW.nom || ' ' || CHR(val);
    ELSIF NEW.nom = '2nde C4' THEN
        val := nextval('secondec')::int;
        
        NEW.nom := NEW.nom || ' ' || CHR(val);
    ELSIF NEW.nom = '2nde A4' THEN
        val := nextval('secondea')::int;
        
        NEW.nom := NEW.nom || ' ' || CHR(val);
    ELSIF NEW.nom = '1ere C4' THEN
        val := nextval('premierec')::int;
        
        NEW.nom := NEW.nom || ' ' || CHR(val);
    ELSIF NEW.nom = '1ere A4' THEN
        val := nextval('premierea')::int;
        
        NEW.nom := NEW.nom || ' ' || CHR(val);
    ELSIF NEW.nom = '1ere D' THEN
        val := nextval('premiered')::int;
        
        NEW.nom := NEW.nom || ' ' || CHR(val);
    ELSIF NEW.nom = 'Tle C4' THEN
        val := nextval('terminalc')::int;
        
        NEW.nom := NEW.nom || ' ' || CHR(val);
    ELSIF NEW.nom = 'Tle A4' THEN
        val := nextval('terminala')::int;
        
        NEW.nom := NEW.nom || ' ' || CHR(val);
    ELSIF NEW.nom = 'Tle D' THEN
        val := nextval('terminald')::int;
        
        NEW.nom := NEW.nom || ' ' || CHR(val);
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


-- Création du déclencheur (trigger)
CREATE TRIGGER inserer_valeur_auto_trigger
BEFORE INSERT ON Classe
FOR EACH ROW
EXECUTE FUNCTION inserer_valeur_auto();


"""


    
for relation in tables:
    create_tables(relation, tables[relation])

lk = Linker()
lk.executerReq(trig)
lk.commit()
lk.close()