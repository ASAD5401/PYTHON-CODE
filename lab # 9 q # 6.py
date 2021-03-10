d=83
c=101
f=22
dc=31
df=8
cf=10
dcf=6
o=34
onlydog=d-(dc-dcf)-(df-dcf)-dcf
onlycat=c-(dc-dcf)-(cf-dcf)-dcf
print("How many purchases were for a dog product only?",onlydog)
print("How many purchases were for cat product only?",onlycat)
print("How many purchases for a dog or a fish product?",onlydog+dc-dcf+df-dcf+cf-dcf+dcf)
print("How many purchases were there in total?",d+c+f+o-dc-dcf-cf-df)