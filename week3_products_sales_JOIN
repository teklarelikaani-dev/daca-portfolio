
-- LEFT JOIN: kõik tooted, ka need mis pole müüdud 
SELECT
p.product_name,
p.category,
p.subcategory,
p.retail_price,
s.sale_id
FROM products p LEFT JOIN sales s
ON p.product_id = s.product_id
WHERE s.sale_id IS NULL;    -- Kui sale_id on NULL, siis toodet pole kunagi müüdud!  

 --Loe müümata tooted kokku:
SELECT COUNT(*) AS müümata_tooteid
FROM products p LEFT JOIN sales s 
ON p.product_id = s.product_id
WHERE s.sale_id IS NULL;   

--Leia enim müüdud tooted
SELECT
p.product_name,
p.category,
p.subcategory,
COUNT(s.sale_id) AS müüdud_kordi, 
SUM(s.total_price) AS kogumüük
FROM products p INNER JOIN sales s
ON p.product_id = s.product_id
GROUP BY p.product_id, p.product_name, p.category, p.subcategory
ORDER BY kogumüük desc
LIMIT 10;

 --Analüüsi kategooriate kaupa
SELECT
p.category,
COUNT(DISTINCT p.product_id) AS tooteid,
COUNT(s.sale_id) AS müüke,
SUM(s.total_price) AS kogumüük
FROM products p LEFT JOIN sales s 
ON p.product_id = s.product_id
GROUP BY p.category
ORDER BY kogumüük DESC; 

--Ühenda inventuuriga — millised tooted on laos?
SELECT distinct
p.product_name,
p.category,
i.location,
i.quantity_available,
i.reorder_point,
CASE WHEN i.quantity_available <= i.reorder_point THEN 'TELLI JUURDE' ELSE 'OK' END AS staatus
FROM products p LEFT JOIN inventory i
ON p.product_id = i.product_id
ORDER BY i.quantity_available asc;

--Ühenda kolm tabelit: leia tooted, mis on laos, aga pole kunagi müüdud — topelt kahju (laoseis + müümata):
SELECT
p.product_name,
p.category,
p.retail_price,
i.quantity_available,
(p.retail_price * i.quantity_available) AS kinni_olev_raha
FROM products p
LEFT JOIN sales s ON p.product_id = s.product_id
LEFT JOIN inventory i ON p.product_id = i.product_id
WHERE s.sale_id IS NULL AND i.quantity_available > 0
ORDER BY kinni_olev_raha DESC;

--Palju laos ja palju müüdud
SELECT 
    p.product_name,
    p.category,
    p.retail_price,
    COALESCE(i.quantity_available, 0) AS laos_olemas,
    COUNT(s.sale_id) AS müüdud_kordi
FROM products p
LEFT JOIN inventory i ON p.product_id = i.product_id
LEFT JOIN sales s ON p.product_id = s.product_id
GROUP BY 
    p.product_id, 
    p.product_name, 
    p.category, 
    p.retail_price, 
    i.quantity_available
ORDER BY laos_olemas DESC, müüdud_kordi ASC;


--Laoseis ja müük kategooria kaupa 2
SELECT
p.category,
COUNT(DISTINCT p.product_id) AS tooteid,
COUNT(s.sale_id) AS müüke,
SUM(s.total_price) AS kogumüük
FROM products p LEFT JOIN sales s
ON p.product_id = s.product_id
GROUP BY p.category
ORDER BY kogumüük DESC; 


SELECT
    p.category,
    COUNT(DISTINCT p.product_id) AS erinevaid_tooteid,
    COALESCE(SUM(inv.laos_kokku), 0) AS laoseis_kokku,
    COALESCE(SUM(inv.lao_väärtus_kokku), 0) AS laoseis_omahinnas_kokku,
    COUNT(s.sale_id) AS müüke,
    SUM(s.total_price) AS kogumüük
FROM products p
-- Alampäring arvutab laoseisud tootepõhiselt:
LEFT JOIN (
    SELECT 
        i.product_id, 
        SUM(i.quantity_available) AS laos_kokku,
        SUM(i.quantity_available * prod.cost_price) AS lao_väärtus_kokku
    FROM inventory i
    JOIN products prod ON i.product_id = prod.product_id
    GROUP BY i.product_id
) inv ON p.product_id = inv.product_id
-- Liidame müügid:
LEFT JOIN sales s ON p.product_id = s.product_id
GROUP BY p.category
ORDER BY kogumüük DESC;

SELECT SUM(i.quantity_available * p.cost_price) AS lao_väärtus_omahinnas_kokku
FROM inventory i
JOIN products p ON i.product_id = p.product_id;

SELECT SUM(total_price) AS kogumüük_kokku 
FROM sales;

SELECT
    product_name, 
    COUNT(*) AS korduste_arv,
    -- See rida liidab kokku kõigi duplikaatsete ridade arvud üle terve tabeli:
    SUM(COUNT(*)) OVER() AS kõiki_duplikaatseid_tooteid_kokku
FROM products
GROUP BY product_name
HAVING COUNT(*) > 1
ORDER BY korduste_arv DESC;
