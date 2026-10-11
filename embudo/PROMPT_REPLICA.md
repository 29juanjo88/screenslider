Eres mi asistente para encontrar una idea de software con oportunidades reales de éxito. Responde en español. Vas a orquestar agentes en un embudo de varias etapas con evaluación adversarial y evidencia web.

## Quién soy
- Juan, ingeniero de SOFTWARE senior (backend) en Guadalajara, México. Stack: Node.js, TypeScript, PHP/Laravel, React/Next.js, GraphQL, Python.
- Mi ventaja: puedo construir y operar un SaaS yo solo, casi a costo cero. Mi cuello de botella es la distribución y la venta. Empiezo a tiempo parcial.
- Tengo experiencia previa con PLC y CAD, pero NO quiero que pese en la evaluación ni que oriente las ideas hacia manufactura.

## Lo que ya probamos (no repetir)
1. Ecocard (tarjetas NFC): mercado comoditizado, sin product fit.
2. Embudo 1 (600 ideas): terminó en nichos chicos sin ninguna idea alta, porque los generadores tenían instrucciones de "preferir nichos", el mercado pesaba ×1 y había bono por experiencia industrial.
3. Embudo 2 (238 ideas, solo mercados de 100 mil compradores o más): tampoco salió ninguna alta. En mercados grandes, cada cuña de "más barato" o "más simple" ya la ocupaba alguien. La mejor fue Amazon FBA Claims Auditor (media, 37/60).
4. Conclusión: las ideas que un agente genera con investigación de escritorio casi siempre ya existen. Este embudo debe buscar ventajas difíciles de copiar, no solo precio.

## Paso 0: pregúntame antes de lanzar agentes (preguntas de opción múltiple)
1. Mercado: global en inglés / inglés y español / México y LatAm.
2. Cliente (varias): empresas medianas y grandes con autoservicio / desarrolladores / profesionales y creadores / consumidores.
3. Meta: US$10–50k al mes rentable / startup con capital / ingreso lateral de US$2–10k.
4. Ventas: casi nada / algo de venta directa / venta directa fuerte.
5. Tamaño mínimo de mercado: ≥20 mil / ≥100 mil / ≥1 millón de compradores posibles.
6. Fuente de ideas: generadas por canal y tendencia / partir de mi experiencia (hazme 10 preguntas sobre problemas que he visto como desarrollador) / ambas.
Con mis respuestas escribe brief.md con criterios, filtros, rúbrica y anclas. Muéstramelo en 10 líneas y arranca.

## Reglas de operación (aprendidas)
- **Agentes con esfuerzo medio:** las definiciones en `.claude/agents/*.md` (frontmatter `model: sonnet`, `effort: medium`) solo se cargan si existen al iniciar la sesión. Revisa si ya existen `generador`, `atacante`, `defensor` y `juez`. Si no, créalas y usa general-purpose con model "sonnet" hasta que aparezcan; avísame en una línea.
- **Máximo 20 agentes simultáneos**, en tandas de hasta 20 en un mismo mensaje.
- Todo se guarda en archivos JSON validados con Python dentro de una carpeta de trabajo. Los agentes responden solo "OK" y una línea. Escribe cada instrucción de agente en un archivo `.prompt` y pásale al agente solo la ruta.
- **Búsqueda web:** WebSearch es una herramienta diferida; cada agente debe cargarla con ToolSearch `select:WebSearch` (si ToolSearch no existe, puede llamarla directo). **Límite real: 200 búsquedas por turno, compartidas por todos los agentes.** El presupuesto se reinicia con cada mensaje mío. Planea las etapas por turnos y nunca lances una tanda que pueda pasar de unas 180 búsquedas en el turno. Cuando haga falta, detente y pídeme "sigue".
- Si una búsqueda falla o no confirma algo, se marca "sin verificar". Nunca inventes cifras, competidores, precios ni URLs.
- Mantén una lista de tareas visible y avísame en una línea al terminar cada etapa. Guarda el avance con commit y push en una rama propia después de cada etapa.

## Filtros de descarte (desde la generación)
F1. Incumbente gratis y suficientemente bueno **para la cuña elegida** (incluye funciones nativas de plataformas y de ChatGPT).
F2. No hay comprador concreto que pague.
F3. Requiere capital, hardware, licencias reguladas o equipo de ventas (según el paso 0).
F4. No hay canal nombrado para los primeros 100 clientes de pago.
F5. Precio tan bajo que la meta exige volumen irreal.
F6. Mercado por debajo del mínimo elegido en el paso 0.
Depender de una plataforma se permite, marcado como riesgo.

## Rúbrica (1–5 por criterio, máximo 60)
Dolor ×2 · Pago ×2 · Canal ×2 · Mercado ×3 · Cuña difícil de copiar ×2 · Ejecución por una persona a tiempo parcial ×1.
- Escala de mercado: 2 = 100k–250k, 3 = 250k–700k, 4 = 700k–2M, 5 = más de 2M (ajústala al mínimo del paso 0).
- **Cuña 4–5 solo si no se resuelve con precio:** datos propios, integración difícil, flujo de trabajo profundo, efecto de red o acceso a una comunidad. "Más barato" o "más simple" vale 2 como máximo.
- Bandas: ALTA ≥44 · MEDIA 32–43 · BAJA <32. Si falla un filtro, 0.
- En brief.md incluye 3 anclas calificadas (alta, media y baja) que no sean candidatas, y avisa a los jueces que no premien el parecido con un ancla.

## Etapa A: generación (~200 ideas)
- 10 agentes × 20 ideas, con ángulos de mercado amplio (tiendas generalistas, desarrolladores, creadores, freelancers y agencias, complementos de Workspace/M365/Slack/Notion, usuarios de IA, consumidores, marketing, unbundling de incumbentes caros, contrarias) más los que salgan de mis respuestas del paso 0.
- **No pidas "nichos específicos".** Pide un mercado grande con una cuña concreta frente a incumbentes con nombre.
- Máximo 3 búsquedas por agente; que usen al menos 2 para buscar quejas sobre incumbentes.
- Campos: id, nombre, cliente_que_paga, problema, solucion, precio_usd_mes, canal_primeros_100, competidores, cuña, tamaño_mercado, por_que_ahora, riesgo_principal, evidencia_url, angulo, tema.
- Al terminar: unir, validar y agrupar duplicados con un script de similitud más una revisión manual.

## Etapa B: ~200 → 40 (sin búsquedas)
- Lotes aleatorios de unas 30 ideas, con 3 agentes por lote: atacante, defensor (rescata solo las que valen la pena) y juez neutral con puntaje absoluto contra las anclas.
- Corte global por puntaje, máximo 3 por tema, fusionando casi duplicados. Si hay empate en el corte, un segundo juez independiente.
- Verifica que la media por lote sea comparable (dentro de ±2 puntos).

## Etapa C: 40 → 10 (con búsquedas)
- 8 lotes de 5 ideas; atacante, defensor y juez con máximo 4 búsquedas cada uno.
- **El juez debe buscar al menos una vez, el nombre de la idea más "app"**, para detectar competidores con el mismo nombre o el mismo ángulo. En el embudo 1 se descartó tarde una finalista porque existía un plugin idéntico.
- Corte a 10, máximo 2 por tema.

## Etapa D: 10 finalistas (máximo rigor)
- Por idea, 2 pares independientes de atacante y defensor, en 2 rondas:
  - Ronda 1: caso con evidencia (máximo 2 búsquedas).
  - Ronda 2: réplica al rival, concediendo lo cierto (máximo 2 búsquedas).
- Dimensiones obligatorias: dolor, pago, alternativas actuales, canal y costo de adquisición, retención, mercado (tamaño con fuente), defensa frente a copias, ejecución por una persona a tiempo parcial.
- Un juez neutral por idea (máximo 4 búsquedas) lee los 4 agentes y decide AVANZA / CONDICIONAL / DESCARTADA. Da también probabilidad (alta, media o baja), el hecho decisivo con URL, la condición y el experimento más barato con umbral.
- Contra el sesgo de rol: el juez ignora las probabilidades que declare cada rol, pondera la evidencia con URL, trata las concesiones de la ronda 2 como evidencia fuerte, y el atacante no tiene veto.
- Reparto por turnos: turno 1 = A + B + C (~130 búsquedas); turno 2 = D ronda 1 (~80) más la mitad de la ronda 2; turno 3 = resto de la ronda 2, jueces y entrega.

## Verificación antes de entregar
Para las 3 mejores, un agente prepara un kit de validación con máximo 8 búsquedas. Si encuentra un competidor que ocupa exactamente la cuña, márcala como "DESCARTADA tras verificar", sube la siguiente y avísame.

## Entrega final
- Una página HTML publicada como artifact: finalistas ordenadas por veredicto, fichas con los argumentos de ambos pares y el razonamiento del juez, y todas las ideas filtrables.
- Para las 3 mejores, un plan de validación de 2 semanas sin escribir producto: landing con lista de espera o preventa, 10 conversaciones con compradores (dónde encontrarlos y qué preguntar) y la métrica que decide si seguir.
- Kit por idea: textos de la landing en inglés, lugares donde están los compradores con URL, competidores con precio, guion de entrevista tipo Mom Test, mensajes de contacto, calendario de 14 días a unas 2 horas diarias.
- Un resumen de máximo 300 palabras con qué cambió frente a los embudos anteriores y sus limitaciones.
