Use `awesome chocolates`;
#Show me all the shipmetns of Orange Choco

Select * from products where Product = 'Orange Choco';

Select * from sales where PID = 'P09';

Select * from sales S left join Products P
ON S.PID = P.PID
Where P.Product = 'Orange Choco';

#Shipment with sales person name and team

Select * from Sales;

Select * from people;

Select * from people P left join Sales S
ON P.SPID = S.SPID;

#Bar shipments alone

Select * from sales S left join Products P
ON S.PID = P.PID
Where P.Category = 'Bars';

# Bars and person name is Barr shipments
Select * from Sales S left join people P
ON S.SPID = P.SPID
LEFT JOIN products Pr
ON S.PID = Pr.PID
Where P.Salesperson like '%Barr%' AND Pr.Category = 'Bars';

# Bars and person name is Barr shipments BY group month
Select DATE_FORMAT(S.SaleDate, '%M %Y') AS 'Month Year',SUM(Amount),SUM(Boxes)  from Sales S left join people P
ON S.SPID = P.SPID
LEFT JOIN products Pr
ON S.PID = Pr.PID
Where P.Salesperson like '%Barr%' AND Pr.Category = 'Bars'
group by DATE_FORMAT(S.SaleDate, '%M %Y');

#Which products are not sold at all
Select * from Products P  left join
Sales S  on S.PID = P.PID
Where S.PID is null;

Select * from Sales where PID is null;

# Did we ship all products on feb 2022
Select * from products P left join Sales S
on P.PID =S.PID AND S.SaleDate = '2021-2-1'
Where SPID is null