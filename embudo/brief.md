# Brief del embudo 600 → 100 → 20 → finalistas

## Perfil del fundador (Juan)
Ingeniero backend senior (Guadalajara, MX). Stack: Node.js, TypeScript, PHP/Laravel, React/Next.js, GraphQL, Python.
Experiencia industrial: PLC (Siemens TIA Portal, Rockwell Studio 5000), CAD/CAM (SolidWorks, AutoCAD), firmware de impresoras 3D.
Construye software casi a costo cero. Cuello de botella: distribución y venta. Empieza a tiempo parcial.

## Criterios definidos AL INICIO (Paso 0)
- Mercado: GLOBAL EN INGLÉS. El producto, el canal y los clientes son internacionales/anglosajones.
- Cliente: cualquiera de: empresas medianas y grandes (solo autoservicio, sin ciclos de compra con ventas), desarrolladores y equipos técnicos, profesionales y creadores, consumidores finales. NO orientar a pymes mexicanas.
- Meta: negocio rentable de US$10–50k MRR. Ejemplos de volumen razonable: 500 clientes × $40, 200 × $100, 50 × $500.
- Ventas: CASI NADA. Debe venderse solo: marketplaces, app stores, SEO, product-led, comunidad, contenido. Sin equipo de ventas, sin demos obligatorias, sin outbound como canal principal.
- Probabilidad objetivo: buscamos ideas con probabilidad ALTA bajo estos criterios.

## Filtros de descarte (eliminan la idea, sin importar la rúbrica)
F1. Existe un incumbente GRATIS y suficientemente bueno (incluye funciones nativas de la plataforma).
F2. No hay un comprador concreto (rol/persona) que pague.
F3. Requiere capital relevante, hardware propio, licencias reguladas (banca, salud con certificación, seguros, legal ejercido) o equipo de ventas.
F4. No hay un canal NOMBRADO y concreto para los primeros 100 clientes de pago (ej.: "búsqueda 'customs forms' en Shopify App Store", no "marketing digital").
F5. Precio tan bajo que la meta exige un volumen irreal (ej.: $3/mes requiere >3,000 pagadores para $10k).
Depender de UNA plataforma (Shopify, Chrome, Atlassian…) se permite, pero se marca como riesgo.

## Rúbrica (cada criterio 1–5; total ponderado máximo 60)
| Criterio | Peso | 1 = | 5 = |
|---|---|---|---|
| Dolor y urgencia | ×2 | "estaría bien" | pierde dinero/tiempo cada semana, lo busca activamente |
| Disposición de pago | ×2 | espera gratis | ya paga por algo peor o caro; presupuesto existente |
| Distribución propia y canal | ×3 | depende de ventas/ads caros | demanda que busca sola en un canal nombrado (marketplace/SEO/comunidad) con intención de compra |
| Tamaño de mercado | ×1 | < 2,000 compradores posibles | > 100,000 compradores posibles |
| Diferenciación | ×1 | clon sin ángulo | ángulo claro que los incumbentes no cubren |
| Ventaja de Juan | ×1 | ninguna | software casi gratis + conocimiento industrial/CAD/PLC/3D que pocos tienen |
| MVP en 6 semanas (tiempo parcial) | ×1 | > 6 meses | ≤ 6 semanas |
| Riesgo bajo | ×1 | plataforma/regulación/IA lo puede matar | riesgos menores y diversificables |

Bandas: ALTA ≥ 44 · MEDIA 32–43 · BAJA < 32. Si falla un filtro F1–F5 → puntaje 0 y "descartada".
Reglas de juez: califica la idea, no la redacción. Una afirmación sin evidencia vale menos que una con URL. Sin cuotas.

## Anclas de calibración (todos los jueces califican contra estas)
1) ALTA — "API de conversión y vista previa de archivos CAD (STEP/IGES/DXF → glTF/PNG/SVG) para desarrolladores de SaaS de manufactura".
   Dolor 3 · Pago 4 · Canal 4 (SEO "step to gltf api", directorios de APIs, docs) · Mercado 3 · Dif 4 · Ventaja 5 · MVP 4 · Riesgo 4
   = 6+8+12+3+4+5+4+4 = **46**. (Ancla de calibración; no está verificada.)
2) MEDIA — "Cotizador instantáneo de piezas DXF para talleres de corte láser (widget web + WhatsApp)" (CotizaMaquila globalizado).
   Dolor 4 · Pago 3 · Canal 2 (no hay marketplace; llegar a talleres exige outreach) · Mercado 2 · Dif 3 · Ventaja 5 · MVP 4 · Riesgo 3
   = 8+6+6+2+3+5+4+3 = **37**.
3) BAJA — "Tarjetas de presentación NFC con perfil digital" (Ecocard).
   Dolor 1 · Pago 1 · Canal 2 · Mercado 3 · Dif 1 · Ventaja 1 · MVP 4 · Riesgo 2 = 2+2+6+3+1+1+4+2 = **21** (además falla F1: perfiles digitales gratis).

## Presupuesto de búsqueda web
Generación ≤3/agente · 600→100: 0 · 100→20: ≤5/agente · Finalistas: ≤8 ronda 1, ≤4 ronda 2.
Si una búsqueda falla o no confirma algo → escribir "sin verificar". NUNCA inventar cifras, competidores, precios ni URLs.

## Esquema de idea (JSON)
id, nombre, cliente_que_paga, problema, solucion, precio_usd_mes (número), canal_primeros_100, competidores (lista),
por_que_ahora, ventaja_juan, riesgo_principal, evidencia_url ("" o "sin verificar" si no hay), angulo, tema (2–4 palabras).

## Lecciones del embudo anterior (no repetir)
- Ideas genéricas para pymes (WhatsApp, contador, cobranza) → evitar.
- No premiar redacción; premiar evidencia y canal.
- Los roles no deciden: el juez ignora probabilidades declaradas por atacante/defensor; el atacante no tiene veto.
