SELECT COUNT(*) AS ridade_arv FROM sales; --Mitu rida on Sales tabelis
SELECT * FROM sales LIMIT 10; --Millised veerud ja andmed tabelis on
SELECT * FROM sales WHERE store_location = 'Tallinn' ORDER BY sale_date DESC LIMIT 15; --Tallinna kaupluse müügid kuupäeva järgi kahanevalt
SELECT * FROM sales ORDER BY total_price DESC LIMIT 10; --10 suurimat tehingut kahanevalt 
SELECT * FROM sales ORDER BY total_price ASC LIMIT 10; --10 väiksemat tehingut kasvavalt
SELECT COUNT(*) - COUNT(customer_id) AS puuduv_klient FROM sales; --Mitmel real on kliendi info puudu
SELECT COUNT(*) AS kokku_emaile, COUNT(DISTINCT email) AS unikaalseid_emaile FROM customers; --Emailid topelt
SELECT channel, store_location, payment_method FROM sales LIMIT 10;  -- Millised kanalid, asukohad ja makseviisid on
SELECT DISTINCT channel FROM sales; --Unikaalsed müügikanalid
SELECT DISTINCT store_location FROM sales; --Unikaalsed kauplused
SELECT DISTINCT payment_method FROM sales; --Unikaalsed makseviisid
SELECT * FROM sales WHERE channel = 'online' ORDER BY total_price DESC LIMIT 15; --Online müügid
SELECT COUNT(*) AS puuduv_asukoht FROM sales WHERE store_location IS NULL; --Tehingud kus asukoht puudu 
SELECT store_location, COUNT(*) AS tehinguid FROM sales WHERE store_location IS NOT NULL GROUP BY store_location ORDER BY tehinguid DESC; --Tehingute arv kaupluse kohta
SELECT COUNT(*) AS online_tehinguid FROM sales WHERE channel = 'online'; --Online tehingute arv
SELECT COUNT(*) AS poe_tehinguid FROM sales WHERE channel = 'pood'; --Kaupluste tehingute arv
SELECT COUNT(*) AS klientide_arv FROM customers; --Mitu klienti on kokku
SELECT * FROM customers LIMIT 10; --Millised veerud ja andmed on tabelis
SELECT DISTINCT city FROM customers; --Millistest linnadest kliendid tulevad
SELECT * FROM customers WHERE city = 'Tallinn' ORDER by last_name ASC LIMIT 15; --Tallinna kliendid perekonnanime järgi kasvavalt
SELECT MIN(registration_date) AS vanim, MAX(registration_date) AS uusim FROM customers; --Vanim ja uusim registreerimine
SELECT COUNT(*) - COUNT(first_name) AS puuduvad_eesnimed FROM customers; --Mitmel kliendil on eesnimi puudu
SELECT COUNT(*) - COUNT(email) AS puuduvad_emailid FROM customers; --Mitmel kliendil on e-mail puudu
