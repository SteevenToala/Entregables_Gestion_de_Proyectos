const fs = require('fs');
const cards = require('./cards_manifest.json');

const mapping = cards.map(c => {
  let cleanTitle = c.title
    .normalize("NFD").replace(/[\u0300-\u036f]/g, "") // remove accents
    .replace(/[^a-zA-Z0-9\s]/g, "") // remove punctuation
    .trim()
    .split(/\s+/)
    .join('_');
  
  let filename = `${c.code}_${cleanTitle}.tex`;
  return {
    code: c.code,
    phase: c.phase,
    folder: c.phase.replace('fase', 'Fase_'),
    title: c.title,
    filename: filename,
    dates: c.dates,
    hours: c.durationHours,
    assigneeName: c.assigneeName,
    deliverable: c.deliverable,
    desc: c.description,
    subtasks: c.subtasks ? c.subtasks.map(s => s.text || s.title || s) : []
  };
});

fs.writeFileSync('Entregables_Latex/full_deliverables_manifest.json', JSON.stringify(mapping, null, 2), 'utf8');
console.log(`Saved ${mapping.length} deliverables in full_deliverables_manifest.json (UTF-8)`);
