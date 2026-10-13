const cards = require('./cards_manifest.json');

cards.forEach(c => {
  console.log(`================================================================`);
  console.log(`[${c.code}] ${c.title.toUpperCase()}`);
  console.log(`Fase: ${c.phase} | Fechas: ${c.dates} (${c.durationHours}h) | Resp: ${c.assigneeName}`);
  console.log(`Entregable Oficial: ${c.deliverable}`);
  console.log(`Descripcion: ${c.description}`);
  if (c.subtasks && c.subtasks.length > 0) {
    console.log(`Subtareas:`);
    c.subtasks.forEach(st => console.log(`   - ${st.text || st.title || JSON.stringify(st)}`));
  }
});
