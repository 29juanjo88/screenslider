import json
ang={a:b for a,b in json.load(open('scripts/angles.json'))}
ideas=json.load(open('ideas_600.json'))
top20=[x['id'] for x in json.load(open('top20.json'))]
fin=[]
for i in top20:
    j=json.load(open(f'e4/{i}/juez.json')); idea=next(x for x in ideas if x['id']==i)
    roles={}
    for P in ['P1','P2']:
        for r in ['atacante','defensor']:
            r1=json.load(open(f'e4/{i}/{P}_{r}_r1.json')); r2=json.load(open(f'e4/{i}/{P}_{r}_r2.json'))
            roles[f'{P}_{r}']=dict(r1=r1.get('argumento_principal',''),concede=r2.get('concesion_mas_importante',''),sigue=r2.get('punto_que_sigue_en_pie',''))
    fin.append(dict(id=i,nombre=idea['nombre'],cliente=idea['cliente_que_paga'],problema=idea['problema'],solucion=idea['solucion'],precio=idea['precio_usd_mes'],canal=idea['canal_primeros_100'],tema=idea['tema_norm'],variantes=idea.get('variantes'),e2=idea['e2_total'],e3=idea['e3_total'],juez=j,roles=roles))
def short(x):
    if x.get('duplicado_de'): st='duplicado'
    elif x.get('variante_de'): st='variante'
    elif x['top20']: st='finalista'
    elif x['top100']: st='top100'
    else: st='fuera'
    return dict(id=x['id'],n=x['nombre'],c=x['cliente_que_paga'],p=x['problema'],s=x['solucion'],pr=x['precio_usd_mes'],ch=x['canal_primeros_100'],t=x['tema_norm'],a=ang.get(x['angulo'],x['angulo']).split(' (')[0],e2=x['e2_total'],r2=x.get('e2_razon') or '',f2=x.get('e2_filtro'),e3=x.get('e3_total'),r3=x.get('e3_razon') or '',st=st,dup=x.get('duplicado_de') or x.get('variante_de'))
data=dict(fin=fin,ideas=[short(x) for x in ideas])
json.dump(data,open('entrega/datos_entrega.json','w'),ensure_ascii=False)
s=json.dumps(data,ensure_ascii=False).replace('</','<\\/')
open('entrega/data.js','w').write('const DATA='+s+';')
print(len(s), sum(1 for x in data['ideas'] if x['st']=='top100'))
