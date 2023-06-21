CREATE OR REPLACE FUNCTION recup_id_tuteur(varchar, varchar, date, varchar,varchar, varchar,varchar) RETURNS text
    LANGUAGE plpgsql 
    AS $_$
/*  Function:     recup_id_tuteur(table tutor columns)
    Description:  Return the id of the tutor inserted
    Affects:      
    Arguments:    
    Returns:      text
*/
DECLARE
        --adresse ALIAS FOR $1;
        --contact ALIAS FOR $2;
        --date_naissance ALIAS FOR $3;
        --genre ALIAS FOR $4;
        --nom ALIAS FOR $5;
        --prenom ALIAS FOR $6;
        --profession ALIAS FOR $7;
        id record;          
BEGIN
    INSERT INTO tuteur(matricule, adresse, contact, date_naissance, genre, nom, prenoms, profession) 
    VALUES ($1,$2,$3,$4,$5,$6,$7)
    RETURNING tuteur.matricule, tuteur.nom, tuteur.prenoms INTO id;
    RETURN id;
END;
$_$;

SELECT recup_id_tuteur(500, 'Sok', '70478925', '2001-02-01','Masculin','SEDO', 'Eric', 'Marchand');
