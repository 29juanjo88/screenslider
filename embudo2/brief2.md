# Brief v2 — embudo corto de MERCADO GRANDE (reemplaza a embudo/brief.md)

## Perfil del fundador (Juan)
Ingeniero de SOFTWARE senior (backend) en Guadalajara, México. Stack: Node.js, TypeScript, PHP/Laravel, React/Next.js, GraphQL, Python.
Su ventaja: puede construir y mantener un SaaS él solo, casi a costo cero. NO es ingeniero industrial; NO hay que orientar ideas a PLC/CAD/manufactura ni darles bono.
Cuello de botella: distribución y venta. Empieza a tiempo parcial.

## Criterios (fijados por Juan)
- Mercado: GLOBAL EN INGLÉS.
- MERCADO GRANDE: ≥100,000 compradores posibles en el mundo (empresas, equipos o personas que podrían pagar). Es requisito duro.
- Cliente: empresas medianas y grandes (solo autoservicio), desarrolladores y equipos técnicos, profesionales y creadores, consumidores finales. NO pymes mexicanas.
- Meta: US$10–50k MRR, negocio rentable, sin levantar capital.
- Ventas: casi nada; se vende solo (product-led, SEO, marketplaces, comunidad, contenido, viralidad del producto).
- Aceptamos competencia: en mercados grandes siempre hay incumbentes. La idea debe tener una CUÑA: un segmento, una función o un modelo de precio que los incumbentes atienden mal, por la que un producto de una persona puede ganar a sus primeros 500 clientes.

## Filtros de descarte
F1. Incumbente GRATIS y suficientemente bueno PARA LA CUÑA elegida (no basta que exista competencia de pago).
F2. No hay comprador concreto que pague.
F3. Requiere capital, hardware, licencias reguladas o equipo de ventas.
F4. No hay canal nombrado para los primeros 100 clientes de pago.
F5. Precio tan bajo que la meta exige volumen irreal.
F6. Mercado < 100,000 compradores posibles (nicho chico) → descartada.
Depender de una plataforma se permite, marcado como riesgo.

## Rúbrica v2 (1–5 cada criterio; máximo 60)
| Criterio | Peso | 1 = | 5 = |
|---|---|---|---|
| Dolor y urgencia | ×2 | "estaría bien" | pierde dinero/tiempo cada semana y lo busca |
| Disposición de pago | ×2 | espera gratis | ya paga por algo peor o caro |
| Canal y distribución | ×2 | depende de ventas/ads caros | demanda que busca sola o producto que se difunde solo |
| Tamaño de mercado | ×3 | < 100k compradores (falla F6) | > 2 millones de compradores |
| Cuña frente a incumbentes | ×2 | clon sin ángulo | segmento/función/precio claramente mal atendido |
| Ejecución por 1 persona a tiempo parcial | ×1 | requiere equipo | MVP ≤ 6 semanas y operable por 1 persona |
Escala de mercado: 2 = 100k–250k · 3 = 250k–700k · 4 = 700k–2M · 5 = >2M.
Bandas: ALTA ≥ 44 · MEDIA 32–43 · BAJA < 32. Falla F1–F6 → 0.

## Anclas de calibración (no son candidatas; no verificadas)
1) ALTA — "Analítica web simple y respetuosa de la privacidad para sitios pequeños y medianos" (patrón conocido de SaaS bootstrapped).
   Dolor 3 · Pago 4 · Canal 3 · Mercado 5 · Cuña 4 · Ejecución 4 = 6+8+6+15+8+4 = **47**.
2) MEDIA — "Respaldo automático de espacios de trabajo de Notion para equipos".
   Dolor 3 · Pago 3 · Canal 3 · Mercado 4 · Cuña 2 · Ejecución 4 = 6+6+6+12+4+4 = **38**.
3) BAJA — "Otro gestor de tareas genérico para equipos".
   Dolor 2 · Pago 2 · Canal 1 · Mercado 5 · Cuña 1 · Ejecución 2 = 4+4+2+15+2+2 = **29**.

## Presupuesto de búsqueda web (límite real: 200 por turno, compartido)
Generación ≤3/agente · B (selección) 0 · C ≤4/agente · D ronda 1 ≤2, ronda 2 ≤2, juez ≤4.
WebSearch es diferida: cárgala con ToolSearch query "select:WebSearch".
Si no se verifica → "sin verificar". NUNCA inventar cifras, competidores, precios ni URLs.

## Esquema de idea (JSON)
id, nombre, cliente_que_paga, problema, solucion, precio_usd_mes (número), canal_primeros_100, competidores (lista),
cuña (por qué un producto de una persona gana a sus primeros 500 clientes frente a esos competidores),
tamaño_mercado (estimación de compradores posibles + razonamiento o fuente; "sin verificar" si no hay),
por_que_ahora, riesgo_principal, evidencia_url ("sin verificar" si no hay), angulo, tema (2–4 palabras).

## Lecciones (no repetir)
- El embudo anterior favoreció nichos chicos: pedía "nichos específicos", el mercado pesaba ×1 y daba bono industrial. Aquí el mercado pesa ×3 y no hay bono industrial.
- Roles no deciden: el juez ignora probabilidades declaradas; el atacante no tiene veto.
