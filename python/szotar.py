szotar={}
szotar["nagy"]="big"
szotar["kicsi"]="small"
print(szotar)
print(szotar["kicsi"])

autok={}
autok["ABC-123"]=13400
autok["BEF-456"]=35612
print(autok)
if("ABC-123" in autok.keys()):
    autok["ABC-123"]=autok["ABC-123"]+100
for i in range(11):
    if("GHI-789" in autok.keys()):
        autok["GHI-789"]=autok["GHI-789"]+200
    else:
     autok["GHI-789"]=75434
print(autok)