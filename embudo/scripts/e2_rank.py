import json,collections,statistics
W=dict(dolor=2,pago=2,canal=3,mercado=1,diferenciacion=1,ventaja_juan=1,mvp=1,riesgo=1)
ideas={x['id']:x for x in json.load(open('ideas_600.json'))}
rows=[]
for i in range(1,21):
    L=f'{i:02d}'
    for j in json.load(open(f'e2/juez_{L}.json')):
        p=j['puntajes'] or {}
        t=0 if j.get('filtro_fallado') else sum(W[k]*p.get(k,0) for k in W)
        rows.append(dict(id=j['id'],lote=L,total=t,filtro=j.get('filtro_fallado'),razon=j['razon'],puntajes=p,tema=ideas[j['id']]['tema_norm']))
print(len(rows))
means={L:statistics.mean(r['total'] for r in rows if r['lote']==L and r['total']>0) for L in sorted({r['lote'] for r in rows})}
print('medias por lote (sin descartadas):',{k:round(v,1) for k,v in means.items()})
rows.sort(key=lambda r:-r['total'])
print([r['total'] for r in rows[:5]], [r['total'] for r in rows[95:110]])
json.dump(rows,open('e2/ranking_e2.json','w'),ensure_ascii=False,indent=1)
