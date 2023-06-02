# https://leetcode.com/problems/combine-two-tables
Select p.firstName,p.lastName,a.city,a.state from Person p
left join Address a
on p.personId =a.personId