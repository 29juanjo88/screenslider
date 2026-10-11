import json,re,itertools
d=json.load(open('ideas_600.json'))
stop=set("de la el en para y a los las un una con que por del se al su sus o es como sin más to the for and of".split())
def tok(x): return {w for w in re.findall(r'[a-záéíóúñ0-9]+',(x['nombre']+' '+x['solucion']+' '+x['tema']).lower()) if w not in stop and len(w)>3}
T={x['id']:tok(x) for x in d}
pairs=[]
for a,b in itertools.combinations(d,2):
    A,B=T[a['id']],T[b['id']]
    j=len(A&B)/max(1,len(A|B))
    if j>=0.25: pairs.append([a['id'],b['id'],round(j,2)])
pairs.sort(key=lambda p:-p[2])
json.dump(pairs,open('e1_ideas/candidatos_duplicados.json','w'))
print(len(pairs)); print(pairs[:5])
with open('e1_ideas/compacto.txt','w') as f:
    for x in d: f.write(f"{x['id']} | {x['nombre']} | {x['cliente_que_paga'][:80]} | {x['solucion'][:140]} | tema:{x['tema']}\n")
