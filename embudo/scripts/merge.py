import json,glob,collections
K=["id","nombre","cliente_que_paga","problema","solucion","precio_usd_mes","canal_primeros_100","competidores","por_que_ahora","ventaja_juan","riesgo_principal","evidencia_url","angulo","tema"]
allid=[];out=[];errs=[]
for f in sorted(glob.glob('e1_ideas/gen_*.json')):
    d=json.load(open(f))
    if len(d)!=20: errs.append((f,len(d)))
    for x in d:
        miss=[k for k in K if k not in x]
        if miss: errs.append((x.get('id'),miss))
        if not isinstance(x.get('precio_usd_mes'),(int,float)):
            try: x['precio_usd_mes']=float(str(x['precio_usd_mes']).split()[0].strip('$'))
            except: errs.append((x['id'],'precio',x.get('precio_usd_mes')))
        if isinstance(x.get('competidores'),str): x['competidores']=[x['competidores']]
        out.append({k:x.get(k) for k in K})
ids=[x['id'] for x in out]
print(len(out),len(set(ids)),errs[:10])
json.dump(out,open('ideas_600.json','w'),ensure_ascii=False,indent=1)
urls=sum(1 for x in out if str(x['evidencia_url']).startswith('http'))
print('con url',urls)
print(collections.Counter(int(x['precio_usd_mes']>=20) for x in out))
